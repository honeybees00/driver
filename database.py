import psycopg2
import os 
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    conn = psycopg2.connect(
        host = os.getenv("DB_HOST"), 
        port = os.getenv("DB_PORT"), 
        dbname = os.getenv("DB_NAME"), 
        user= os.getenv("DB_USER"), 
        password= os.getenv("DB_PASSWORD"),
        sslmode= os.getenv("DB_SSLMODE")
    )
    return conn

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
 create table if not exists driver(
    driver_id serial Primary Key,
    name varchar (50) not null,
   license_type varchar (50) not null
 
                             );
 create table if not exists route(
   route_id serial Primary key,
   service_zone Varchar (50) not null,
    date date
 foreign key (driver_id) references driver(driver_id)
                );
 create table if not exists vehicle(
    vehicle_id serial Primary key,
      license_plate varchar (50) not null,
       model varchar (50) not nul,
       driver_id int unique,
          foreign key (driver_id) refernces driver(driver_id)                                       
      );
create table if not exists package(
   package_id serial Primary Key,
    description varchar (75) not null,
    weight int (50) not null,
    route_id int  
     foreign key (route_id) refernces route(route_id)                        
                            );

                                                                                                                                       )                                                     

   """)
    conn.commit()
    cur.close()
    conn.close()
    print(' database ready!')