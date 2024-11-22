from flask import Blueprint, jsonify
from services.career_mapper import map_careers

bp = Blueprint('career_routes', __name__)

@bp.route('/recommendations', methods=['POST'])
def recommend_careers():
    data = request.get_json()
    skills = data.get('skills')
    if not skills:
        return jsonify({"error": "Skills are required"}), 400

    careers = map_careers(skills)
    return jsonify({"careers": careers}), 200

