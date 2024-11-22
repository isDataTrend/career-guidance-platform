from flask import Blueprint, request, jsonify
from services.career_mapper import map_skills_to_careers

career_bp = Blueprint("career_bp", __name__)

@career_bp.route("/", methods=["POST"])
def recommend_careers():
    data = request.json
    skills = data.get("skills")

    if not skills:
        return jsonify({"error": "Skills are missing"}), 400

    try:
        careers = map_skills_to_careers(skills)
        return jsonify({"careers": careers}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

