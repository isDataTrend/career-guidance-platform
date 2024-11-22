import os

class Config:
    UPLOAD_FOLDER = "uploads/"
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB upload limit
    SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")

