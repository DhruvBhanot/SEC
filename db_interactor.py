import psycopg2
import smtplib
import configparser as cp
import os



def readconfig():

 config = cp.ConfigParser()
 config.read("db.ini")

 db_params = {
    "host": config["database"]["host"],
    "port": config["database"]["port"],
    "user": config["database"]["username"],
    "password": config["database"]["password"],
    "dbname": config["database"]["database_name"]
 }

 return db_params

def selectall():  
 vals = []
 conn = None
 credentials = readconfig()
 try:
   with psycopg2.connect(dbname = credentials["dbname"],user = credentials["user"],password = credentials["password"],host = credentials["host"], port = credentials["port"]) as conn:
 
    with conn.cursor() as cur:
     cur.execute("SELECT * FROM people_room")
     for part in cur.fetchall():
        vals.append(part)
   
 except Exception as error:
    print(error)
 finally:
  
   if conn is not None:
      conn.close()
 return vals

def select( room_num):
 vals = ()
 conn = None
 credentials = readconfig()
 try:
   with psycopg2.connect(dbname = credentials["dbname"],user = credentials["user"],password = credentials["password"],host = credentials["host"], port = credentials["port"]) as conn:
 
    with conn.cursor() as cur:
     cur.execute("SELECT * FROM people_room WHERE room_num = " + "'"+ room_num +"'")
     for part in cur.fetchall():
       vals = part
      
     
 except Exception as error:
    print(error)
 finally:
  
   if conn is not None:
      conn.close()
 return vals
   

def remove(room_num):
 conn = None
 credentials = readconfig()
 try:
   with psycopg2.connect(dbname = credentials["dbname"],user = credentials["user"],password = credentials["password"],host = credentials["host"], port = credentials["port"]) as conn:
 
    with conn.cursor() as cur:
     cur.execute("DELETE FROM people_room WHERE room_num =" + "'"+ room_num +"'")
     
 except Exception as error:
    print(error)
 finally:
   if conn is not None:
      conn.close()
      
 return 'deleted' + room_num



  
  

