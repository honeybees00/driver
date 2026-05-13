from flask import jsonify,request,Blueprint
from psycopg2.extras import RealDictCursor
from database import get_connection
route=Blueprint("route",__name__)
# Get crud opperations below
@route.route("/")
def get_route():
    try:
        conn=get_connection()
        cur=conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("""
        select * from route
        
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

@route.route("/",methods=["POST"])

def create_route():
    try:
        conn=get_connection()
        cur=conn.cursor()
        data=request.get_json()
    
        cur.execute("""
        insert into route
        (date,service_zone,driver_id)
         values
                    (%s,%s,%s)


                    """,(data["date"],data["service_zone"],data["driver_id"]))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
            return jsonify({"message":f"an error occurred {e}"})  
    else:
            return jsonify({"message":"object created"}),201
    # the Put (upate, or change a record, row)
@route.route("/<int:id>",methods=["PUT"]) 
def update_route(id):
     try:
        conn=get_connection()
        cur=conn.cursor()
        data=request.get_json()
        cur.execute("""
            update route
                      set date=%s,
                      service_zone=%s,
                    driver_id=%s
                      where route_id=%s
                    
""",(data["date"],data["service_zone"],data["driver_id"],id))
        conn.commit()
        cur.close()
        conn.close()
     except Exception as e:
        return jsonify({"message":f"an error occurred {e}"})  
     else:
            return jsonify({"message":"object updated"}),201
    #  delete opperation
@route.route("/<int:id>",methods=["DELETE"])
def delete_route(id):
    try:
        conn=get_connection()
        cur=conn.cursor()
        cur.execute("""
        delete from route
         where route_id=%s
                    """,(id,))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
     return jsonify({"message":f"an error occurred {e}"})  
    else:
     return jsonify({"message":"object updated"}),201
     #  delete opperation
