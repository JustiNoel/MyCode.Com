# safe_bazaar_ai/verification.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()  # Load your .env file with secrets

GROK_API_KEY = os.getenv("GROK_API_KEY")
if not GROK_API_KEY:
    raise ValueError("No Grok API key found! Add GROK_API_KEY=your_key_here to .env file.")

def verify_seller(id_text: str, doc_text: str, selfie_description: str, language: str = "English") -> dict:
    """
    Verifies seller docs using Grok AI for Safe Bazaar AI.
    Supports English/Swahili prompts for Kenyan users.
    Inputs: Text simulations of ID, doc, selfie (later: real images).
    Returns: {'score': 95, 'reason': 'Looks legit!', 'language': 'English'}
    """
    # Prompt in chosen language
    if language.lower() == "swahili":
        prompt = f"""
        Chunguza udanganyifu:
        - Kitambulisho: {id_text}
        - Hati ya Biashara: {doc_text}
        - Picha ya Selfie: {selfie_description}
        
        Toa alama 0-100% halali. Chini ya 80 = bandia. Toa sababu.
        """
    else:
        prompt = f"""
        Analyze for fraud:
        - ID: {id_text}
        - Business Doc: {doc_text}
        - Selfie: {selfie_description}
        
        Score 0-100% legit. Below 80 = fake. Give reason. Check Kenyan formats (e.g., KRA PIN like A123456789B).
        """
    
    # Call Grok API
    response = requests.post(
        "https://api.x.ai/v1/chat/completions",
        headers={"Authorization": f"Bearer {GROK_API_KEY}"},
        json={
            "model": "grok-beta",  # Use grok-4 if your access allows
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.3  # Slightly higher for nuanced reasons
        }
    )
    
    if response.status_code != 200:
        return {"score": 0, "reason": f"API error: {response.text}", "language": language}
    
    result = response.json()["choices"][0]["message"]["content"]
    
    # Parse the result (robust – handles variations)
    try:
        # Find score: Look for number before '%'
        score_str = result.split("%")[0].split()[-1]
        score = int(score_str) if score_str.isdigit() else 50
        # Reason: Everything after first sentence
        reason = ".".join(result.split(".")[1:]).strip()
    except Exception:
        score = 50
        reason = "Failed to parse Grok's response – raw: " + result
    
    return {"score": score, "reason": reason, "language": language}

# Test run – try both languages!
if __name__ == "__main__":
    # Good test data
    test_id = "Kenyan National ID: 12345678, Name: Noel Omondi, DOB: 2003-01-01"
    test_doc = "KRA PIN: A123456789B, Business: Safe Bazaar Traders, Registered 2025"
    test_selfie = "Young man in Kisumu, smiling, matches ID photo exactly"
    
    # English test
    result_en = verify_seller(test_id, test_doc, test_selfie, "English")
    print(f"English Score: {result_en['score']}% - Reason: {result_en['reason']}")
    
    # Swahili test (simulates Kenyan user)
    result_sw = verify_seller(test_id, test_doc, test_selfie, "Swahili")
    print(f"Swahili Score: {result_sw['score']}% - Reason: {result_sw['reason']}")
    
    # Scam test (should low score)
    scam_id = "Fake ID: 999, Name: Scammer, DOB: Yesterday"
    scam_result = verify_seller(scam_id, test_doc, "Mismatched old photo", "English")
    print(f"Scam Score: {scam_result['score']}% - Reason: {scam_result['reason']}")