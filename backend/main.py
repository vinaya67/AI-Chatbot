from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from ollama import analyze_log
from rally import create_rally_ticket

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze/")
async def analyze(file: UploadFile = File(None), text: str = Form(None)):
    content = ""
    if file:
        content = (await file.read()).decode('utf-8', errors='ignore')
    elif text:
        content = text
    else:
        return {"error": "No input provided"}

    solution = analyze_log(content)

    if solution and "no issue" not in solution.lower():
        return {"result": solution}

    # fallback → create Rally ticket
    ticket_url = create_rally_ticket(content)
    return {
        "result": "No automated solution found. Ticket created for DevOps engineer.",
        "ticket_url": ticket_url
    }
