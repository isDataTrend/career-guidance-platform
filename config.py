import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key')
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', './uploads')
    ALLOWED_EXTENSIONS = {'pdf', 'csv'}
    AI_MODEL_PATH = os.getenv('AI_MODEL_PATH', './models/')







