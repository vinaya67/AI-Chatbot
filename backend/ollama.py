import requests

OLLAMA_URL = "http://ollama:11434/api/generate"
MODEL_NAME = "llama3"  # or another installed Ollama model

PROMPT_TEMPLATE = """
You are a DevOps expert. Analyze the following Jenkins log and suggest a solution.
If it is not clear or cannot be solved automatically, just say "No issue detected".

Log:
{log}
"""

def analyze_log(log_content: str) -> str:
    prompt = PROMPT_TEMPLATE.format(log=log_content)

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    response.raise_for_status()

    return response.json().get("response", "").strip()
