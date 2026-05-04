from flask import jsonify,request,Blueprint
from psycopg2.extras import RealDictCursor
from database import get_connection
drivers=Blueprint("drivers",__name__)
# Get crud opperations below
@drivers.route("/")
def get_drivers():
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

@drivers.route("/",methods=["POST"])

def create_driver():
    try:
        conn=get_connection()
        cur=conn.cursor()
        data=request.get_json()
    
        cur.execute("""
        insert into driver
        (driver_id,name,license_type)
         values
                    (%s,%s,%s)           
    
        
                    """,(data["driver_id"],data["name"],data["license_type"]))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
            return jsonify({"message":f"an error occurred {e}"})  
    else:
            return jsonify({"message":"object created"}),201
    # the Put (upate, or change a record, row)
@drivers.route("/<int:id>",methods=["PUT"]) 
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
@drivers.route("/<int:id>",methods=["Delete"])
def delete_driver(id):
try:
        conn=get_connection()
        cur=conn.cursor()
        cur.execute("""
        delete from driver
         where driver_id=%s
conn.commit()
cur.close()
conn.close()
    except Exception as e:
    return jsonify({"message":f"an error occurred {e}"})  
 else:
        return jsonify({"message":"object updated"}),201
     #  delete opperation
@drivers.route("/<int:id>",methods=["Delete"])
    def delete_driver(id):
                    """)


        

  

