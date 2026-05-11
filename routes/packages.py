from flask import jsonify,request,Blueprint
from psycopg2.extras import RealDictCursor
from database import get_connection
packages=Blueprint("packsges", __name__)
# Get crud opperations below
@packages.route("/")
def get_packages():
    try:
     conn=get_connection()
     cur=conn.cursor(cursor_factory=RealDictCursor)
     cur.execute("""
        select * from packages
        
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

@packages.route("/",methods=["POST"])
def create_packages():
    try:
      conn=get_connection()
      cur=conn.cursor()
      data=request.get_json()
    
      cur.execute("""
                
    insert into packages
    (packages_id,weight,description,route_id)
        values
     (%s,%s,%s,%s)           
    
        """,(data["package_id"],data["weight"],data["description"],data["route_id"]))
      conn.commit()
      cur.close()
      conn.close()
    except Exception as e:
     return jsonify({"message":f"an error occurred {e}"})  
    else:
     return jsonify({"message":"object created"}),201
    # the Put (upate, or change a record, row)
@packages.route("/<int:id>",methods=["PUT"]) 
def update_packages(id):
     try:
        conn=get_connection()
        cur=conn.cursor()
        data=request.get_json()
        cur.execute("""
            update packages
                      set weight=%s,
                      description=%s,
                    route_id=%s
                      where package_id=%s
""",(data["package_id"],data["weight"],data["description"],data["route_id"],id))
        conn.commit()
        cur.close()
        conn.close()
     except Exception as e:
        return jsonify({"message":f"an error occurred {e}"})  
     else:
            return jsonify({"message":"object updated"}),201
    #  delete opperation
@packages.route("/<int:id>",methods=["DELETE"])
def delete_package(id):
    try:
        conn=get_connection()
        cur=conn.cursor()
        cur.execute("""
    delete from package
    where package_id=%s
                      """,(id))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        return jsonify({"message":f"an error occurred {e}"})  
    else:
        return jsonify({"message":"object delete"}),201
     #  delete opperation




