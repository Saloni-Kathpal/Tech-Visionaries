import os
import json
import requests
from dotenv import load_dotenv
import google.genai as genai
from services import llm_recommender

load_dotenv()

def analyze_repo(repo_data: dict):
    """
    Calls Gemini 1.5 to analyze the repository content.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return {"error": "Missing GEMINI_API_KEY"}

    owner = repo_data.get("owner")
    repo = repo_data.get("repo")
    readme = repo_data.get("readme", "")
    tree = repo_data.get("file_tree", "")
    tech = ", ".join(repo_data.get("tech_stack", []))

    prompt = f"""
You are a senior full-stack engineer and security researcher.
Analyze this repository: https://github.com/{owner}/{repo}

README Snapshot:
{readme}

File Structure:
{tree}

Tech Stack Manifests Found:
{tech}

Task: Generate actionable insights for this project.
Return the response in a STRICT CLEAN JSON format with the following keys:

{{
  "health_score": (integer 0-100),
  "issues": [string list of potential code/architecture issues],
  "code_smells": [string list of patterns that could be improved],
  "security_risks": [string list of potential security vulnerabilities],
  "improvements": [string list of general project improvements],
  "beginner_friendly_issues": [
    {{
      "title": "...",
      "description": "...",
      "difficulty": "Easy"
    }}
  ]
}}

Ensure ONLY the raw JSON is returned.
"""

    try:
        from services import ai_proxy
        # Using Gemini 2.5 REST call
        result = ai_proxy.call_gemini_rest(prompt, model="gemini-2.5-flash")
        
        if "error" in result:
            return {"error": result["error"]}
            
        parsed = llm_recommender.extract_json_from_text(result["text"])
        if not parsed:
            print(f"DEBUG: Failed to parse LLM response: {result['text']}")
            return {"error": "Failed to parse AI response"}
            
        return parsed

    except Exception as e:
        print(f"Error in Repo Analysis: {e}")
        return {"error": str(e)}
