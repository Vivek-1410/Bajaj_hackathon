# main.py
from flask import Flask, request, jsonify
from query_parser import parse_query
from pdf_extractor import extract_text_from_pdfs
from decision_engine import get_llm_response
import os

app = Flask(__name__)
PDF_FOLDER = os.path.join(os.path.dirname(__file__), "pdfs")

@app.route('/api/v1/hackrx/run', methods=['POST'])
def hackrx_webhook():
    data = request.get_json()
    pdf_url = data.get("documents")
    questions = data.get("questions")

    if not pdf_url or not questions:
        return jsonify({"error": "Missing documents or questions"}), 400

    # (Optional) download PDF from pdf_url if needed
    pdf_text = extract_text_from_pdfs(PDF_FOLDER)

    answers = []
    for question in questions:
        parsed = parse_query(question)
        answer = get_llm_response(pdf_text, parsed)
        answers.append(answer)

    return jsonify({"answers": answers})

if __name__ == '__main__':
    app.run(debug=True)
