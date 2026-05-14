from flask import jsonify, request, Blueprint
from psycopg2.extras import RealDictCursor
from database import get_connection

vehicle = Blueprint("vehicle", __name__)

@vehicle.route("/")
def get_vehicle():
    conn = cur = None
    try:
        conn = get_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT * FROM vehicle")
        rows = cur.fetchall()
        return jsonify(rows)
    except Exception as e:
        return jsonify({"message": f"an error occurred {e}"}), 500
    finally:
        if cur: cur.close()
        if conn: conn.close()

@vehicle.route("/", methods=["POST"])
def create_vehicle():
    conn = cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        data = request.get_json()
        cur.execute(
            "INSERT INTO vehicle (model, license_plate, driver_id) VALUES (%s, %s, %s)",
            (data["model"], data["license_plate"], data["driver_id"])
        )
        conn.commit()
        return jsonify({"message": "object created"}), 201
    except Exception as e:
        if conn: conn.rollback()
        return jsonify({"message": f"an error occurred {e}"}), 500
    finally:
        if cur: cur.close()
        if conn: conn.close()

@vehicle.route("/<int:id>", methods=["PUT"])
def update_vehicle(id):
    conn = cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        data = request.get_json()
        cur.execute(
            "UPDATE vehicle SET model=%s, license_plate=%s, driver_id=%s WHERE vehicle_id=%s",
            (data["model"], data["license_plate"], data["driver_id"], id)
        )
        conn.commit()
        return jsonify({"message": "object updated"}), 200
    except Exception as e:
        if conn: conn.rollback()
        return jsonify({"message": f"an error occurred {e}"}), 500
    finally:
        if cur: cur.close()
        if conn: conn.close()

@vehicle.route("/<int:id>", methods=["DELETE"])
def delete_vehicle(id):
    conn = cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM vehicle WHERE vehicle_id=%s", (id,))
        conn.commit()
        return jsonify({"message": "object deleted"}), 200
    except Exception as e:
        if conn: conn.rollback()
        return jsonify({"message": f"an error occurred {e}"}), 500
    finally:
        if cur: cur.close()
        if conn: conn.close()
