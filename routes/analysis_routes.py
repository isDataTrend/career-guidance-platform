from flask import Blueprint, request, jsonify, current_app
import os

bp = Blueprint('upload_routes', __name__)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']

@bp.route('/transcript', methods=['POST'])
def upload_transcript():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file and allowed_file(file.filename):
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        return jsonify({"message": "File uploaded successfully", "path": filepath}), 200
    return jsonify({"error": "Invalid file type"}), 400

