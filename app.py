from flask import Flask,jsonify
from database import init_db
from routes.driver import drivers
from routes.packages import packages
from routes.vehicle import vehicle
from routes.routes import route
init_db()
app=Flask(__name__)
# establishs the end points for the api your making
app.register_blueprint(drivers,url_prefix="/drivers")
app.register_blueprint(packages,url_prefix="/packages")
app.register_blueprint(route,url_prefix="/routes")
app.register_blueprint(vehicle,url_prefix="/vehicle")

@app.route("/")
# proof of life this prints out server online when you go live
def home():
    return jsonify({"message":"server online"})

if  __name__ == "__main__":
# everytime the app.py __name__ to __main__ 
    app.run(debug=True)

