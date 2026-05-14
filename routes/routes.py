from flask import jsonify, request, Blueprint
from psycopg2.extras import RealDictCursor
from database import get_connection

route = Blueprint("route", __name__)

@route.route("/")
def get_route():
    conn = cur = None
    try:
        conn = get_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT * FROM route")
        rows = cur.fetchall()
        return jsonify(rows)
    except Exception as e:
        return jsonify({"message": f"an error occurred {e}"}), 500
    finally:
        if cur: cur.close()
        if conn: conn.close()

@route.route("/", methods=["POST"])
def create_route():
    conn = cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        data = request.get_json()
        cur.execute(
            "INSERT INTO route (date, service_zone, driver_id) VALUES (%s, %s, %s)",
            (data["date"], data["service_zone"], data["driver_id"])
        )
        conn.commit()
        return jsonify({"message": "object created"}), 201
    except Exception as e:
        if conn: conn.rollback()
        return jsonify({"message": f"an error occurred {e}"}), 500
    finally:
        if cur: cur.close()
        if conn: conn.close()

@route.route("/<int:id>", methods=["PUT"])
def update_route(id):
    conn = cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        data = request.get_json()
        cur.execute(
            "UPDATE route SET date=%s, service_zone=%s, driver_id=%s WHERE route_id=%s",
            (data["date"], data["service_zone"], data["driver_id"], id)
        )
        conn.commit()
        return jsonify({"message": "object updated"}), 200
    except Exception as e:
        if conn: conn.rollback()
        return jsonify({"message": f"an error occurred {e}"}), 500
    finally:
        if cur: cur.close()
        if conn: conn.close()

@route.route("/<int:id>", methods=["DELETE"])
def delete_route(id):
    conn = cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM route WHERE route_id=%s", (id,))
        conn.commit()
        return jsonify({"message": "object deleted"}), 200
    except Exception as e:
        if conn: conn.rollback()
        return jsonify({"message": f"an error occurred {e}"}), 500
    finally:
        if cur: cur.close()
        if conn: conn.close()
