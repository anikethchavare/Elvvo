# Elvvo - run-steps.py

''' This is the 'run-steps.py' file. '''

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

''' Run this program if you're setting up Elvvo. '''

''' STEP 1 - Download the latest version of Python. The system should be 64-bit. '''
''' STEP 2 - Enter your MySQL password when it asks you. '''
''' STEP 3 - Let this file install and upgrade the necessary packages and tools required for Elvvo. '''

# Imports
import os
from configparser import ConfigParser

# Initializing the "ConfigParser" Class
config_parser_object = ConfigParser()

# Setting the Data in the "config_parser_object" Variable
config_parser_object["MYSQL"] = {
    "password": str(input("\nEnter the MySQL password: "))
}

# Writing "config_parser_object" to the "config.ini" File
with open("MySQL/config.ini", "w") as config_file:
    config_parser_object.write(config_file)

# Start Text
print("\nInstalling and upgrading the necessary packages and tools required for Elvvo.\n")

# Installing and Updgrading the Python Packages and Libraries
os.system("python -m pip install --upgrade pip")

os.system("pip install --upgrade fastapi")
os.system("pip install --upgrade uvicorn")
os.system("pip install --upgrade jinja2")
os.system("pip install --upgrade opencv-python")
os.system("pip install --upgrade imutils")
os.system("pip install --upgrade pytesseract")
os.system("pip install --upgrade numpy")
os.system("pip install --upgrade Pillow")
os.system("pip install --upgrade mysql-connector-python")