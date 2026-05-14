import os
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from database import init_db
from routes.driver import driver
from routes.packages import packages
from routes.vehicle import vehicle
from routes.routes import route

init_db()
app = Flask(__name__)
CORS(app)

# API blueprints
app.register_blueprint(driver,   url_prefix="/driver")
app.register_blueprint(packages, url_prefix="/packages")
app.register_blueprint(route,    url_prefix="/routes")
app.register_blueprint(vehicle,  url_prefix="/vehicle")

@app.route("/api")
def home():
    return jsonify({"message": "server online"})

# Serve the React build for all non-API routes
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve_react(path):
    dist = os.path.join(os.path.dirname(__file__), "driver-frontend", "dist")
    if path and os.path.exists(os.path.join(dist, path)):
        return send_from_directory(dist, path)
    return send_from_directory(dist, "index.html")

if __name__ == "__main__":
    app.run(debug=False)

