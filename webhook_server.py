from flask import Flask, request, jsonify
from query_parser import parse_query
from pdf_extractor import extract_text_from_pdfs
from decision_engine import get_llm_response
import os

app = Flask(__name__)
PDF_FOLDER = os.path.join(os.path.dirname(__file__), "pdfs")

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.get_json()
        query = data.get("query", "")
        
        if not query:
            return jsonify({"error": "Missing query field"}), 400

        parsed_query = parse_query(query)
        pdf_text = extract_text_from_pdfs(PDF_FOLDER)
        decision = get_llm_response(pdf_text, parsed_query)
        
        return jsonify({"decision": decision})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
