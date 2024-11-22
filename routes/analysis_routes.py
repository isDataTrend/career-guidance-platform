from flask import Blueprint, request, jsonify
from services.transcript_parser import parse_transcript
from services.keyword_extractor import extract_keywords

analysis_bp = Blueprint("analysis_bp", __name__)

@analysis_bp.route("/", methods=["POST"])
def analyze_transcript():
    data = request.json
    filepath = data.get("filepath")
    filetype = data.get("filetype")

    if not filepath or not filetype:
        return jsonify({"error": "Filepath or filetype is missing"}), 400

    try:
        text = parse_transcript(filepath, filetype)
        keywords = extract_keywords(text)
        return jsonify({"keywords": keywords}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

