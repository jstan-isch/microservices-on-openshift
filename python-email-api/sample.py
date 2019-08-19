
import falcon
import json
import smtplib
import codecs
import pymysql.cursors
import os
from datetime import datetime
from datetime import timedelta
import mysql.connector
from mysql.connector import Error





'''
try:
    connection = mysql.connector.connect(host='mysql',
                                         database='microservices',
                                         user='app_user',
                                         password='password')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Your connected to database: ", record)
    mySql_Create_Table_Query = """CREATE TABLE Laptop ( 
                             Id int(11) NOT NULL,
                             Name varchar(250) NOT NULL,
                             Price float NOT NULL,
                             Purchase_date Date NOT NULL,
                             PRIMARY KEY (Id)) """
    cursor = connection.cursor()
    result = cursor.execute(mySql_Create_Table_Query)
    print("Laptop Table created successfully ")

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

'''




class EmailResource(object):

 
        try:
            email_req = json.loads(raw_json)
        except ValueError:
            raise falcon.HTTPError(falcon.HTTP_400,
                'Malformed JSON',
                'Could not decode the request body. The '
                'JSON was incorrect.')
 
        resp.status = falcon.HTTP_202
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('janepelladinesh97@gmail.com', '9000795104')
        msg = email_req['msg']
        server.sendmail('janepelladinesh97@gmail.com', email_req['to'], msg)
        
        try:
            connection = mysql.connector.connect(host='mysql',
                                         database='microservices',
                                         user='app_user',
                                         password='password')
            mycursor = connection.cursor()
            sql="INSERT INTO emails (from_add, to_add, subject, body, created_at) VALUES (%s, %s, %s, %s, %s)"
            val=('janepelladinesh97@gmail.com',email_req['to'], 'New registration',msg, datetime.now())
            mycursor.execute(sql, val)
            connection.commit()
            print(mycursor.rowcount, "record inserted.")    
                #create table emails (from_add varchar(40), to_add varchar(40), subject varchar(40), body varchar(200), created_at date);
        finally:
            connection.close()
        resp.body = json.dumps(email_req)
        print("message sent")

api = falcon.API()
api.add_route('/email', EmailResource())
