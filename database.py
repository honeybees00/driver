
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
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
                    
    
        create table if not exists driver
            (
                driver_id    serial Primary Key,
                name         varchar(50) not null,
                license_type varchar(50) not null
            );

            create table if not exists route
            (
                route_id     serial Primary key,
                service_zone Varchar(50) not null,
                date         date,
                driver_id    int references driver (driver_id)
            );

            create table if not exists vehicle
            (
                vehicle_id    serial Primary key,
                license_plate varchar(50) not null,
                model         varchar(50) not null,
                driver_id     int references driver (driver_id) unique
            );


            create table if not exists package
            (
                package_id  serial Primary Key,
                description varchar(75) not null,
                weight      int         not null,
                route_id    int references route (route_id)
            );

        """)

        cur.execute("""
            GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO christina;
            GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO christina;
        """)

        conn.commit()
        cur.close()
        conn.close()
        print(' database ready!')
    except Exception as e:
        print(f"Problem: {e}")