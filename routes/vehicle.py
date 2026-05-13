from flask import jsonify,request,Blueprint
from psycopg2.extras import RealDictCursor
from database import get_connection
vehicle=Blueprint("vehicle",__name__)
# Get crud opperations below
@vehicle.route("/")
def get_vehicle():
    try:
        conn=get_connection()
        cur=conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("""
        select * from vehicle
        
                    """)
        rows=cur.fetchall()
        cur.close()
        conn.close()
    except Exception as e:
        return jsonify({"message":f"an error occurred {e}"})  
    else:
        return jsonify(rows)
    
 # post crud opperations  
# letting the program know this is a post method you have to say post method

@vehicle.route("/",methods=["POST"])

def create_vehicle():
    try:
        conn=get_connection()
        cur=conn.cursor()
        data=request.get_json()
    
        cur.execute("""
        insert into vehicle
        (model,license_plate,driver_id)
         values
                    (%s,%s,%s)


                    """,(data["model"],data["license_plate"],data["driver_id"]))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
            return jsonify({"message":f"an error occurred {e}"})  
    else:
            return jsonify({"message":"object created"}),201
    # the Put (upate, or change a record, row)
@vehicle.route("/<int:id>",methods=["PUT"]) 
def update_vehicle(id):
     try:
        conn=get_connection()
        cur=conn.cursor()
        data=request.get_json()
        cur.execute("""
            update vehicle
                      set model=%s,
                      license_plate=%s,
                    driver_id=%s
                      where vehicle_id=%s
                     
""",(data["model"],data["license_plate"],data["driver_id"],id))
        conn.commit()
        cur.close()
        conn.close()
     except Exception as e:
        return jsonify({"message":f"an error occurred {e}"})  
     else:
            return jsonify({"message":"object updated"}),201
    #  delete opperation
@vehicle.route("/<int:id>",methods=["DELETE"])
def delete_vehicle(id):
    try:
        conn=get_connection()
        cur=conn.cursor()
        cur.execute("""
        delete from vehicle
         where vehicle_id=%s
                    """,(id,))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
     return jsonify({"message":f"an error occurred {e}"})  
    else:
     return jsonify({"message":"object updated"}),201
     #  delete opperation
