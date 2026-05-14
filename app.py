import os
from flask import Flask, jsonify, send_from_directory, request
from flask_cors import CORS
from database import init_db
from routes.driver import driver
from routes.packages import packages
from routes.vehicle import vehicle
from routes.routes import route

init_db()
app = Flask(__name__)
CORS(app, origins="*", supports_credentials=False)

# API blueprints
app.register_blueprint(driver,   url_prefix="/driver")
app.register_blueprint(packages, url_prefix="/packages")
app.register_blueprint(route,    url_prefix="/routes")
app.register_blueprint(vehicle,  url_prefix="/vehicle")

@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"]  = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type,Authorization"
    response.headers["Access-Control-Allow-Methods"] = "GET,POST,PUT,DELETE,OPTIONS"
    return response

@app.route("/driver/", methods=["OPTIONS"])
@app.route("/vehicle/", methods=["OPTIONS"])
@app.route("/routes/", methods=["OPTIONS"])
@app.route("/packages/", methods=["OPTIONS"])
@app.route("/driver/<path:p>", methods=["OPTIONS"])
@app.route("/vehicle/<path:p>", methods=["OPTIONS"])
@app.route("/routes/<path:p>", methods=["OPTIONS"])
@app.route("/packages/<path:p>", methods=["OPTIONS"])
def handle_options(**kwargs):
    return "", 204

@app.route("/api")
def home():
    return jsonify({"message": "server online"})

# Serve the React build for all non-API routes
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve_react(path):
    dist = os.path.join(os.path.abspath(os.path.dirname(__file__)), "driver-frontend", "dist")
    if path and os.path.exists(os.path.join(dist, path)):
        return send_from_directory(dist, path)
    return send_from_directory(dist, "index.html")

if __name__ == "__main__":
    app.run(debug=False)

