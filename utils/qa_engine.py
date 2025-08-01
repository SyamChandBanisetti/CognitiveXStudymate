import requests
import os

API_KEY = os.getenv("WATSONX_API_KEY")  # Store in Streamlit secrets
ENDPOINT = "https://us-south.ml.cloud.ibm.com"  # Adjust based on region

def ask_question(context_chunks, question):
    prompt = f"""Use the below context to answer the question:
Context:
{'\n'.join(context_chunks)}

Question: {question}
Answer:"""

    payload = {
        "input": prompt,
        "parameters": {
            "max_new_tokens": 300,
            "temperature": 0.3
        }
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    response = requests.post(
        f"{ENDPOINT}/v2/inference",
        headers=headers,
        json=payload
    )

    if response.ok:
        return response.json().get("generated_text", "No answer generated.")
    else:
        return f"Error: {response.status_code} {response.text}"
