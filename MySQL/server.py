# Elvvo - server.py

''' This is the 'server.py' file. '''

'''
Copyright 2023 Aniketh Chavare

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''

# Imports
import os
import shutil
import uvicorn
import mysql.connector as mysql
from configparser import ConfigParser

from python_routers import python_router_mysql
from python_routers import python_router_algorithm

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse, JSONResponse
from fastapi import FastAPI, Request, HTTPException

# Initializing the "ConfigParser" Class
config_parser_object = ConfigParser()

# Checking if "config.ini" File Exists
if (not os.path.exists(os.path.dirname(os.path.realpath(__file__)).replace(os.sep, "/") + "/config.ini")):
    # Raising an Exception
    raise Exception("The 'config.ini' does not exist.")
else:
    # Reading the Values from the "config.ini" File
    config_parser_object.read(os.path.dirname(os.path.realpath(__file__)).replace(os.sep, "/") + "/config.ini")

    # Assigning the Variable
    mysql_password = config_parser_object["MYSQL"]["password"]

# Function 1 - MySQL Prerequisite
def mysql_prerequisite():
    # Variables
    table_names = ["vehicle_detection_data", "license_plate_data", "people_detection_data", "crime_data"]

    # Variables (MySQL - Connector and Cursor - Without Database)
    mysql_connector = mysql.connect(host="localhost", user="root", password=mysql_password)
    mysql_cursor = mysql_connector.cursor()

    # Setting the "autocommit" Attribute to "mysql_connector"
    mysql_connector.autocommit = True

    # Checking if Database "Elvvo" Exists
    mysql_cursor.execute("SHOW DATABASES LIKE '{0}';".format("Elvvo"))

    if (len(mysql_cursor.fetchall()) == 0):
        # Creating the Database "Elvvo"
        mysql_cursor.execute("CREATE DATABASE Elvvo;")

    # Variables (MySQL - Connector and Cursor - With Database)
    mysql_connector_database = mysql.connect(host="localhost", user="root", password=mysql_password, database="Elvvo")
    mysql_cursor_database = mysql_connector_database.cursor()

    # Setting the "autocommit" Attribute to "mysql_connector_database"
    mysql_connector_database.autocommit = True

    # Checking if Tables Exist
    for table in table_names:
        # Checking if Table Exists
        mysql_cursor_database.execute("SHOW TABLES LIKE '{0}';".format(table))

        if (len(mysql_cursor_database.fetchall()) == 0):
            # Creating the Tables
            if (table == "vehicle_detection_data"): mysql_cursor_database.execute("CREATE TABLE vehicle_detection_data(Date VARCHAR(100), Time VARCHAR(100), File_Name VARCHAR(100), File_Type VARCHAR(100), Number_of_Vehicles INT);")
            elif (table == "license_plate_data"): mysql_cursor_database.execute("CREATE TABLE license_plate_data(Date VARCHAR(100), Time VARCHAR(100), File_Name VARCHAR(100), File_Type VARCHAR(100), License_Plate_Number VARCHAR(100));")
            elif (table == "people_detection_data"): mysql_cursor_database.execute("CREATE TABLE people_detection_data(Date VARCHAR(100), Time VARCHAR(100), File_Name VARCHAR(100), File_Type VARCHAR(100), Number_of_People INT);")
            elif (table == "crime_data"): mysql_cursor_database.execute("CREATE TABLE crime_data(License_Plate_Number VARCHAR(100), Date VARCHAR(100), Time VARCHAR(100), Offense VARCHAR(500), Fine INT);")

    # Closing the MySQL Connections
    mysql_connector.close()
    mysql_connector_database.close()

# Initializing the "App" Server
app = FastAPI()

# Mounting the "assets" Folder to the "App" Server
app.mount("/assets", StaticFiles(directory="templates/assets"), name="/assets")

# Index (App)
@app.get("/")
async def app_index(request: Request):
    # MySQL Prerequisite
    mysql_prerequisite()

    # Returning the Template
    return Jinja2Templates(directory="templates").TemplateResponse("index.html", {"request": request})

# Vehicle Detection (App)
@app.get("/vehicle-detection")
async def app_vehicledetection(request: Request):
    # MySQL Prerequisite
    mysql_prerequisite()

    # Returning the Template
    return Jinja2Templates(directory="templates").TemplateResponse("vehicle-detection.html", {"request": request})

# License Plate (App)
@app.get("/license-plate")
async def app_licenseplate(request: Request):
    # MySQL Prerequisite
    mysql_prerequisite()

    # Returning the Template
    return Jinja2Templates(directory="templates").TemplateResponse("license-plate.html", {"request": request})

# People Detection (App)
@app.get("/people-detection")
async def app_peopledetection(request: Request):
    # MySQL Prerequisite
    mysql_prerequisite()

    # Returning the Template
    return Jinja2Templates(directory="templates").TemplateResponse("people-detection.html", {"request": request})

# Crime Data (App)
@app.get("/crime-data")
async def app_crimedata(request: Request):
    # MySQL Prerequisite
    mysql_prerequisite()

    # Returning the Template
    return Jinja2Templates(directory="templates").TemplateResponse("crime-data.html", {"request": request})

# Sample Media (App)
@app.get("/sample-media/{algorithm}/{file_type}/{file}")
async def app_samplemedia(request: Request, algorithm: str, file_type: str, file: str):
    # Returning the File
    return FileResponse(path=os.path.dirname(os.path.realpath(__file__)).replace(os.sep, "/") + "/python_routers/sample_media/{0}/{1}/{2}".format(algorithm, file_type, file))

# Delete Cache (App)
@app.get("/delete-cache")
async def app_deletecache(request: Request):
    # Try/Except - Deleting Cache
    try:
        # Variables
        directory_main = os.path.dirname(os.path.realpath(__file__)).replace(os.sep, "/") + "/__pycache__"
        directory_routers = os.path.dirname(os.path.realpath(__file__)).replace(os.sep, "/") + "/python_routers/__pycache__"

        # Checking if Path Exists (Directory Main)
        if (os.path.exists(directory_main)):
            shutil.rmtree(directory_main)

        # Checking if Path Exists (Directory Routers)
        if (os.path.exists(directory_routers)):
            shutil.rmtree(directory_routers)
    except:
        pass

    # Returning the Message
    return JSONResponse({"Message": "Successfully deleted the cache.", "Status Code": 200}, status_code=200)

# Including "python_router_mysql" in the "App" Server
app.include_router(python_router_mysql.router_mysql)

# Including "python_router_algorithm" in the "App" Server
app.include_router(python_router_algorithm.router_algorithm)

# Error 404 (App)
@app.exception_handler(404)
async def app_error404(request: Request, exec: HTTPException):
    # Returning the Error
    return JSONResponse({"Error": "The requested route does not exist. Please try again.", "Status Code": 404}, status_code=404)

# Starting the Server (Development)
if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=7777, reload=True)