import os
import json
import re
import requests
from dotenv import load_dotenv
import google.genai as genai

load_dotenv()

def extract_json_from_text(text):
    """
    Safely extracts the JSON block from text, dealing with potential markdown wrappers
    or conversational text returned by the LLM.
    """
    # Try to find a code block containing JSON
    match = re.search(r'```(?:json)?\s*(\[.*?\]|\{.*?\})\s*```', text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(1))
        except json.JSONDecodeError:
            pass
            
    # Try just parsing the whole text
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
        
    # Final robust attempt: search for bounding brackets
    try:
        start_idx = text.find('[')
        end_idx = text.rfind(']') + 1
        if 0 <= start_idx < end_idx:
            return json.loads(text[start_idx:end_idx])
    except Exception:
        pass
        
    return None

def build_prompt(skills, repos):
    """
    Constructs the exact strict prompt format requested by the user.
    Uses only necessary repo details to avoid blowing up context window.
    """
    # Serialize repos string efficiently
    repo_list_str = ""
    for r in repos:
        name = r.get('repo', r.get('title', 'Unknown'))
        desc = r.get('description', '')[:200] # trim long descriptions
        repo_list_str += f"- {name}: {desc}\n"

    prompt = f"""
You are an expert open-source mentor.

User Skills:
{skills}

Repositories:
{repo_list_str}

Task:
Recommend the top 3 most suitable repositories for this user.

For each repository, provide:

1. Repository Name
2. Why it matches the user’s skills
3. Specific contribution ideas (real tasks)
4. Difficulty Level (Beginner / Intermediate / Advanced)
5. Learning Outcome (what user will gain)

Return the response in clean JSON format like:

[
{{
"name": "",
"reason": "",
"contributions": "",
"difficulty": "",
"learning": ""
}}
]
"""
    return prompt.strip()

def call_gemini(api_key, prompt):
    print(f"DEBUG: Initializing GenAI Client with Key (len={len(api_key)})")
    client = genai.Client(api_key=api_key)
    print(f"DEBUG: Calling generate_content for model 'gemini-2.5-flash'...")
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash", contents=prompt
        )
        print("DEBUG: Generation complete.")
        return response.text
    except Exception as e:
        print(f"DEBUG: GenAI Generation Error: {e}")
        return None

def call_ollama(ollama_url, prompt, model="llama3"):
    url = f"{ollama_url.rstrip('/')}/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    
    response = requests.post(url, json=payload, timeout=30)
    response.raise_for_status()
    data = response.json()
    return data.get('response', '')

def generate_ai_recommendations(skills, repos):
    """
    Entrypoint to get recommendations for a user.
    Attempts Gemini if key is present, falls back to Ollama.
    Matches returned LLM JSON to original repo URLs.
    """
    if not repos or not isinstance(repos, list):
        return None
        
    prompt = build_prompt(skills, repos)
    
    gemini_key = os.environ.get('GEMINI_API_KEY')
    ollama_url = os.environ.get('OLLAMA_URL', 'http://localhost:11434')
    
    response_text = ""
    
    try:
        if gemini_key and gemini_key.strip():
            print("Using Gemini API for recommendations...")
            response_text = call_gemini(gemini_key, prompt)
        else:
            print(f"Using Ollama local API ({ollama_url}) for recommendations...")
            response_text = call_ollama(ollama_url, prompt)
            
    except Exception as e:
        print(f"LLM API Error: {e}")
        return None
        
    # Attempt parsing
    parsed_json = extract_json_from_text(response_text)
    if not parsed_json or not isinstance(parsed_json, list):
        print("Failed to parse valid JSON from LLM.")
        return None
        
    # Enrich the JSON with the original URL so the frontend can link out
    # Create lookup map ignoring case
    repo_map = {}
    for r in repos:
        name = r.get('repo', r.get('title', 'Unknown')).lower()
        url = r.get('url', r.get('html_url', '#'))
        repo_map[name] = url
        
    enriched_results = []
    for item in parsed_json:
        if not isinstance(item, dict):
            continue
            
        target_name = item.get('name', '').lower()
        
        # Fuzzy matching key from LLM to original list
        matched_url = "#"
        for repo in repos:
            original_name = repo.get('repo', repo.get('title', 'Unknown'))
            if target_name in original_name.lower() or original_name.lower() in target_name:
                matched_url = repo.get('url', repo.get('html_url', '#'))
                item['name'] = original_name # restore original casing
                break
                
        item['url'] = matched_url
        item['is_ai_recommended'] = True
        enriched_results.append(item)
        
    # Limit to top 3 as requested
    return enriched_results[:3]
