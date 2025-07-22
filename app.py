from flask import Flask
from routes.homeroutes import main_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main_bp)  # Register the blueprint with the Flask app

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)