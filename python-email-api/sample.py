
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
except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")






class EmailResource(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200
        resp.body = 'Email API 2'
    def on_post(self, req, resp):
        """Handles POST requests"""
        try:
            raw_json = req.stream.read().decode('utf-8')
        except Exception as ex:
            raise falcon.HTTPError(falcon.HTTP_400,
                'Error',
                ex.message)
 
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
        server.quit()
        config = {
          'user': os.getenv('MYSQL_USER', 'app_user'),
          'password': os.getenv('MYSQL_PASSWORD', 'password'),
          'host': os.getenv('MYSQL_SERVICE_HOST', 'mysql-2-hblq2'),
          'db': os.getenv('MYSQL_DATABASE', 'microservices'),
          'cursorclass': pymysql.cursors.DictCursor,
        }
    
        
        connection = pymysql.connect(**config)
        try:
            with connection.cursor() as cursor:
                add_email = ("INSERT INTO emails "
                       "(from_add, to_add, subject, body, created_at) "
                       "VALUES (%s, %s, %s, %s, %s)")

                data_email = ('janepelladinesh97@gmail.com', email_req['to'], 'New registration',msg, datetime.now())
                cursor.execute(add_email, data_email)
                connection.commit()
                #create table emails (from_add varchar(40), to_add varchar(40), subject varchar(40), body varchar(200), created_at date);
        finally:
            connection.close()
        resp.body = json.dumps(email_req)

api = falcon.API()
api.add_route('/email', EmailResource())
