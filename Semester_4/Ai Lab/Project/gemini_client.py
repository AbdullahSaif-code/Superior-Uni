import os
import requests

GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')
GEMINI_MODEL = os.environ.get('GEMINI_MODEL', 'gemini-2.5-pro')


class GeminiError(Exception):
    pass


def query_gemini(prompt_text, temperature=0.7, max_output_tokens=2048):
    """Send a prompt to Google Gemini (Generative Language API) and return text.

    Uses the environment variable `GEMINI_API_KEY` and `GEMINI_MODEL`.
    This module is deliberately isolated from the PDF/RAG logic.
    """
    if not GEMINI_API_KEY:
        raise GeminiError('GEMINI_API_KEY not set in environment')

    # Use the correct Gemini API v1beta endpoint with generateContent
    endpoint = f'https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent'
    
    headers = {
        'Content-Type': 'application/json'
    }
    
    params = {
        'key': GEMINI_API_KEY
    }

    # Correct payload format for Gemini API
    payload = {
        "contents": [{
            "parts": [{
                "text": prompt_text
            }]
        }],
        "generationConfig": {
            "temperature": temperature,
            "maxOutputTokens": max_output_tokens
        }
    }

    try:
        resp = requests.post(endpoint, headers=headers, params=params, json=payload, timeout=30)
    except requests.RequestException as e:
        raise GeminiError(f'Network error: {str(e)}')

    if resp.status_code != 200:
        # Try to surface any returned message
        try:
            detail = resp.json()
        except Exception:
            detail = resp.text
        raise GeminiError(f'Gemini API returned {resp.status_code}: {detail}')

    data = resp.json()

    # Parse the correct response format from Gemini API
    try:
        if 'candidates' in data and len(data['candidates']) > 0:
            candidate = data['candidates'][0]
            
            # Check finish reason
            finish_reason = candidate.get('finishReason', '')
            if finish_reason == 'MAX_TOKENS':
                # If hit max tokens but no content, increase token limit or return partial response
                if 'content' in candidate and 'parts' in candidate['content']:
                    parts = candidate['content']['parts']
                    if len(parts) > 0 and 'text' in parts[0]:
                        return parts[0]['text']
                raise GeminiError('Response exceeded token limit. Try asking a simpler question.')
            
            if 'content' in candidate and 'parts' in candidate['content']:
                parts = candidate['content']['parts']
                if len(parts) > 0 and 'text' in parts[0]:
                    return parts[0]['text']
    except (KeyError, IndexError, TypeError) as e:
        raise GeminiError(f'Unexpected response format: {data}')

    raise GeminiError(f'No text found in response: {data}')
