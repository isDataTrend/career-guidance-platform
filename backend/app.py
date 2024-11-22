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

