from flask import jsonify,request,Blueprint
from psycopg2.extras import RealDictCursor
from database import get_connection
drivers=Blueprint("packsges",__name__)
# Get crud opperations below
@drivers.route("/")
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
    (packages_id,weight,description)
        values
     (%s,%s,%s)           
    
        """,(data["package_id"],data["weight"],data["description"]))
     conn.commit()
     cur.close()
     conn.close()
     except Exception as e:
     return jsonify({"message":f"an error occurred {e}"})  
else:
     return jsonify({"message":"object created"}),201
    # the Put (upate, or change a record, row)
@package.route("/<int:id>",methods=["PUT"]) 
def update_package(id):
     try:
        conn=get_connection()
        cur=conn.cursor()
        data=request.get_json()
        cur.execute("""
            update driver
                      set weight=%s,
                      description=%s
                      where package_id=%s
""",(data["package_id"],data["weight"],data["description"],id))
        conn.commit()
        cur.close()
        conn.close()
     except Exception as e:
        return jsonify({"message":f"an error occurred {e}"})  
     else:
            return jsonify({"message":"object updated"}),201
    #  delete opperation
@package.route("/<int:id>",methods=["Delete"])
def delete_package(id):
     try:
        conn=get_connection()
        cur=conn.cursor()
        cur.execute("""
        delete from package
         where package_id=%s
    conn.commit()
    cur.close()
    conn.close()
       except Exception as e:
        return jsonify({"message":f"an error occurred {e}"})  
    else:
        return jsonify({"message":"object updated"}),201
     #  delete opperation
@package.route("/<int:id>",methods=["Delete"])
    def delete_package(id):
                    """)


        

  




