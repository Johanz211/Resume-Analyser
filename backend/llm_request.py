import requests
import json


def get_llm_opinion(text):
    url = "http://localhost:11434/api/generate"

    # Prompting for JSON output so we can separate reasoning from search terms
    prompt = f"""
    You are an expert career counsellor. Analyze this resume:
    {text}

    Return a JSON object with exactly these two keys:
    1. "reasoning": A detailed explanation of why they are a good fit for specific roles.
    2. "job_titles": A list of the top 3-4 professional job titles suitable for this candidate.

    Ensure the response is valid JSON.
    """

    payload = {
        "model": "llama3",
        "prompt": prompt,
        "format": "json",  # Llama 3 supports a specific JSON mode
        "stream": False
    }

    try:
        response = requests.post(url, json=payload)
        # Parse the string response from LLM into a Python dict
        result = json.loads(response.json().get("response"))
        return result
    except Exception as e:
        return {"reasoning": f"Error: {str(e)}", "job_titles": []}