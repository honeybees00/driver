from flask import jsonify, request, Blueprint
from psycopg2.extras import RealDictCursor
from database import get_connection

driver = Blueprint("driver", __name__)

@driver.route("/")
def get_driver():
    conn = cur = None
    try:
        conn = get_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT * FROM driver")
        rows = cur.fetchall()
        return jsonify(rows)
    except Exception as e:
        return jsonify({"message": f"an error occurred {e}"}), 500
    finally:
        if cur: cur.close()
        if conn: conn.close()

@driver.route("/", methods=["POST"])
def create_driver():
    conn = cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        data = request.get_json()
        cur.execute(
            "INSERT INTO driver (name, license_type) VALUES (%s, %s)",
            (data["name"], data["license_type"])
        )
        conn.commit()
        return jsonify({"message": "object created"}), 201
    except Exception as e:
        if conn: conn.rollback()
        return jsonify({"message": f"an error occurred {e}"}), 500
    finally:
        if cur: cur.close()
        if conn: conn.close()

@driver.route("/<int:id>", methods=["PUT"])
def update_driver(id):
    conn = cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        data = request.get_json()
        cur.execute(
            "UPDATE driver SET name=%s, license_type=%s WHERE driver_id=%s",
            (data["name"], data["license_type"], id)
        )
        conn.commit()
        return jsonify({"message": "object updated"}), 200
    except Exception as e:
        if conn: conn.rollback()
        return jsonify({"message": f"an error occurred {e}"}), 500
    finally:
        if cur: cur.close()
        if conn: conn.close()

@driver.route("/<int:id>", methods=["DELETE"])
def delete_driver(id):
    conn = cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM driver WHERE driver_id=%s", (id,))
        conn.commit()
        return jsonify({"message": "object deleted"}), 200
    except Exception as e:
        if conn: conn.rollback()
        return jsonify({"message": f"an error occurred {e}"}), 500
    finally:
        if cur: cur.close()
        if conn: conn.close()
