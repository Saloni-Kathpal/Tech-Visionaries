import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

def call_gemini_rest(prompt: str, model: str = "gemini-2.5-flash"):
    """
    Direct REST call to Gemini API to avoid SDK-specific model/version issues.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return {"error": "Missing GEMINI_API_KEY"}

    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ],
        "generationConfig": {
            "temperature": 0.7,
            "topP": 0.95,
            "topK": 40,
            "maxOutputTokens": 4096,
        }
    }

    try:
        print(f"DEBUG: Calling Gemini REST API ({model})...")
        response = requests.post(url, headers=headers, json=payload, timeout=60)
        
        if response.status_code != 200:
            print(f"DEBUG: REST API Error: {response.status_code} - {response.text}")
            return {"error": f"API Error {response.status_code}: {response.text}"}
            
        data = response.json()
        if "candidates" in data and data["candidates"]:
            # Extract text from the response
            parts = data["candidates"][0].get("content", {}).get("parts", [])
            if parts:
                return {"text": parts[0].get("text", "")}
                
        return {"error": "Invalid API response format"}

    except Exception as e:
        print(f"DEBUG: REST Exception: {str(e)}")
        return {"error": str(e)}
