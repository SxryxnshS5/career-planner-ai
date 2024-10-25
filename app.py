from flask import Flask
from app import routes  # Import routes from app.routes

# Flask app initialization
app = Flask(__name__)

# Register routes
app.add_url_rule('/', 'index', routes.index)
app.add_url_rule('/analyze', 'analyze', routes.analyze, methods=['POST'])

if __name__ == "__main__":
    app.run(debug=True)
