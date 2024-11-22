
from flask import Flask
from flask_cors import CORS
from routes import upload_routes, analysis_routes, career_routes
from config import Config

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)

# Register blueprints
app.register_blueprint(upload_routes.bp, url_prefix='/upload')
app.register_blueprint(analysis_routes.bp, url_prefix='/analysis')
app.register_blueprint(career_routes.bp, url_prefix='/career')

if __name__ == "__main__":
    app.run(debug=True)





































