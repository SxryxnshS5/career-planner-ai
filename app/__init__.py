from flask import Flask

app = Flask(__name__)

# Ensure configuration values are set here if necessary
# Example: app.config['MODEL'] = MODEL

# Import routes to register them with the app
from app import routes
