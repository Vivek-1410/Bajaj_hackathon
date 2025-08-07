import google.generativeai as genai
import os

# ✅ Replace with your actual Gemini API key
GOOGLE_API_KEY = "AIzaSyDc47KPKcBpDVFLLmGBcJJ8LZ--55vnU8o"
genai.configure(api_key=GOOGLE_API_KEY)

def get_llm_response(pdf_text, query_dict):
    prompt = f"""
You are an insurance claim assistant. Based on the following documents and user query, decide:

1. Whether the claim is eligible
2. Expected payout (if any)
3. Reason with references to the original content

User Query:
{query_dict}

Insurance Policy Documents Content:
{pdf_text}
"""
    try:
        model = genai.GenerativeModel('models/gemini-1.5-flash')
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Error during LLM call: {e}"