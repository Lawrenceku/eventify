from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from events import events_bp
from tickets import tickets_bp
from auth import auth_bp, jwt
from models import db
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure JWT
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy and Flask-Migrate
db.init_app(app)
migrate = Migrate(app, db)

# Initialize JWT with flask app
jwt.init_app(app)

# Register blueprints
app.register_blueprint(events_bp)
app.register_blueprint(tickets_bp)
app.register_blueprint(auth_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)