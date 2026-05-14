from flask import jsonify, request, Blueprint
from psycopg2.extras import RealDictCursor
from database import get_connection

packages = Blueprint("packages", __name__)

@packages.route("/")
def get_packages():
    conn = cur = None
    try:
        conn = get_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT * FROM package")
        rows = cur.fetchall()
        return jsonify(rows)
    except Exception as e:
        return jsonify({"message": f"an error occurred {e}"}), 500
    finally:
        if cur: cur.close()
        if conn: conn.close()

@packages.route("/", methods=["POST"])
def create_packages():
    conn = cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        data = request.get_json()
        cur.execute(
            "INSERT INTO package (weight, description, route_id) VALUES (%s, %s, %s)",
            (data["weight"], data["description"], data["route_id"])
        )
        conn.commit()
        return jsonify({"message": "object created"}), 201
    except Exception as e:
        if conn: conn.rollback()
        return jsonify({"message": f"an error occurred {e}"}), 500
    finally:
        if cur: cur.close()
        if conn: conn.close()

@packages.route("/<int:id>", methods=["PUT"])
def update_packages(id):
    conn = cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        data = request.get_json()
        cur.execute(
            "UPDATE package SET weight=%s, description=%s, route_id=%s WHERE package_id=%s",
            (data["weight"], data["description"], data["route_id"], id)
        )
        conn.commit()
        return jsonify({"message": "object updated"}), 200
    except Exception as e:
        if conn: conn.rollback()
        return jsonify({"message": f"an error occurred {e}"}), 500
    finally:
        if cur: cur.close()
        if conn: conn.close()

@packages.route("/<int:id>", methods=["DELETE"])
def delete_package(id):
    conn = cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM package WHERE package_id=%s", (id,))
        conn.commit()
        return jsonify({"message": "object deleted"}), 200
    except Exception as e:
        if conn: conn.rollback()
        return jsonify({"message": f"an error occurred {e}"}), 500
    finally:
        if cur: cur.close()
        if conn: conn.close()
