from flask import Flask
from routes.upload_routes import upload_bp
from routes.analysis_routes import analysis_bp
from routes.career_routes import career_bp

app = Flask(__name__)

# Configuration
app.config.from_object("config.Config")

# Register blueprints
app.register_blueprint(upload_bp, url_prefix="/upload")
app.register_blueprint(analysis_bp, url_prefix="/analysis")
app.register_blueprint(career_bp, url_prefix="/career")

@app.route("/")
def home():
    return "Welcome to the AI Career Guidance Platform!"

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask
from services.transcript_parser import parse_transcript

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Welcome to the Career Guidance Platform!"}

@app.route("/upload", methods=["POST"])
def upload_transcript():
    # Logic for handling transcript uploads
    return parse_transcript("example.pdf")

if __name__ == "__main__":
    app.run(debug=True)

