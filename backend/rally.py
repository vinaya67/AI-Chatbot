import os
import requests

RALLY_API_URL = "https://rally1.rallydev.com/slm/webservice/v2.0/defect"

def create_rally_ticket(log_content: str) -> str:
    api_key = os.getenv("RALLY_API_KEY")
    project_ref = os.getenv("RALLY_PROJECT")

    headers = {
        "ZSESSIONID": api_key,
        "Content-Type": "application/json"
    }

    payload = {
        "Defect": {
            "Name": "Auto-generated Jenkins Log Issue",
            "Description": log_content[:5000],  # Rally desc limit is ~5000 chars
            "Project": project_ref,
            "Severity": "Major Problem",
            "Priority": "High"
        }
    }

    response = requests.post(RALLY_API_URL, headers=headers, json=payload)
    response.raise_for_status()

    ticket_ref = response.json()['CreateResult']['Object']['_ref']
    return ticket_ref
