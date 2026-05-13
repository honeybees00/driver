from flask import jsonify,request,Blueprint
from psycopg2.extras import RealDictCursor
from database import get_connection

driver=Blueprint("driver",__name__)
# Get crud opperations below
@driver.route("/")
def get_driver():
    try:
        conn=get_connection()
        cur=conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("""
        select * from driver
        
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

@driver.route("/",methods=["POST"])

def create_driver():
    try:
        conn=get_connection()
        cur=conn.cursor()
        data=request.get_json()
    
        cur.execute("""
        insert into driver
        (name,license_type)
         values
                    (%s,%s)


                    """,(data["name"],data["license_type"]))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
            return jsonify({"message":f"an error occurred {e}"})  
    else:
            return jsonify({"message":"object created"}),201
    # the Put (upate, or change a record, row)
@driver.route("/<int:id>",methods=["PUT"]) 
def update_driver(id):
     try:
        conn=get_connection()
        cur=conn.cursor()
        data=request.get_json()
        cur.execute("""
            update driver
                      set name=%s,
                      license_type=%s
                      where driver_id=%s
""",(data["name"],data["license_type"],id))
        conn.commit()
        cur.close()
        conn.close()
     except Exception as e:
        return jsonify({"message":f"an error occurred {e}"})  
     else:
            return jsonify({"message":"object updated"}),201
    #  delete opperation
@driver.route("/<int:id>",methods=["DELETE"])
def delete_driver(id):
    try:
        conn=get_connection()
        cur=conn.cursor()
        cur.execute("""
        delete from driver
         where driver_id=%s
                    """ ,(id,))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
     return jsonify({"message":f"an error occurred {e}"})  
    else:
     return jsonify({"message":"object updated"}),201
     #  delete opperation
