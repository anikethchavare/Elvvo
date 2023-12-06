# Elvvo - An Interactive and Smart Traffic Management App

## What is Elvvo?

Elvvo is an all-in-one traffic solution that changes its traffic lights according to traffic density. Some other features of Elvvo are:
- It determines the speed of vehicles in a given video. A video is loaded and the speed of each vehicle is calculated and the speed (in km/h) will be written in white text right above the vehicle.
- There are many license plate images. So, Elvvo can process that image and return the license number as a String. Then, you can add a crime or fine to that number and it creates separate JSON files in ```data/crime```.
- It changes the lights according to the traffic density as given in the images which are randomly selected by the program. The program randomly selects images, calculates the traffic density, and says whether it has low, high, or very high traffic.

## What is BorderHacks2021?

BorderHacks is a 36-hour online hackathon hosted by Aislyn Laurent and is sponsored by many companies. This is their [link](https://www.borderhacks2021.devpost.com).

One more thing, I couldn't possibly work on this project without the support from my school "Alpine Public School". Their website is [this](https://alpinepublicschool.com). My school is the one that got me the equipment I needed to complete my project, and without them, I don't think I could've participated in this hackathon.

## Inspiration

I just wanted to create something that helps improve traffic flow in major cities. Then, I got the idea of creating Elvvo, an all-in-one traffic solution that helps you to automatically change the lights according to the traffic density.

It also has other features like determining the speed of vehicles or storing criminal data on vehicles using their license number.

## Technologies Used

This application is purely written in Python. For the main GUI, I used PyQt5. For the images and videos, I downloaded those and used them in the programs. For the criminal records, I used JSON to store the license numbers, list of crimes, and the fine.

For the computer vision and OCR (Optical Character Recognition), I used OpenCV and PyTesseract (TesseractOCR) respectively.

The technologies used in making this project are:
* Python (PyQt5, Core)
* Managing JSON Files with Python
* API Requests (GET)
* Raspberry Pi
* Managing External Hardware on Raspberry Pi
* Computer Vision (OpenCV)
* Optical Character Recognition (OCR - PyTesseract)

## All the Libraries Used

I have used many libraries which are:
* RPi.GPIO
* time
* sys
* PyQt5
* atexit
* requests
* json
* cv2
* threading
* dlib
* math
* random
* os
* typing
* imutils
* numpy
* pytesseract

## Challenges I Ran Into

There were a lot of challenges that I ran into. One was to download all the images and videos. Most of the media that I downloaded were either corrupt or not compatible with the program. It at least took me 2 hours to find the proper media that I needed.

When I developed the 'Speed' functionality, it was not quite fetching the speeds of every passing vehicle. So, it took me a lot of time to find correct pre-trained models of these cars and add them to the programs.

The last challenge was to add the data to the JSON files and try to modify/edit the data because, in the beginning, I was planning to put all the data in one JSON file itself, but then I got the idea to create different JSON files for different license numbers. Also, there was something wrong with the configuration of my raspberry pi, so I had to do the whole thing again from scratch (but I had backed up all the code on my laptop).

## Accomplishments I'm Proud Of

I was successfully getting the traffic density data to finish my program. I was also proud when I finally finished extracting the license numbers and trying to get the speed of the vehicles.

## What I Learned

I learned how computer vision works (OpenCV) and OCR (TesseractOCR). I also learned how to manage JSON data and create Python GUI's.

## What's Next for Elvoo

Well, this is just a prototype and I may include more features like catching the speed of the vehicles through a camera or accurately identifying the license number and traffic density on an actual street. One thing I am actually looking forward to is to create a database with license numbers, the vehicle's owner's email, name, address, etc. and try to send reminders/alerts through emails/SMS if that person got a ticket or a fine, or if they paid one already. It's something like getting personalized alerts.

## External Media

I just created a PPT on Elvvo. You can view that [here](https://docs.google.com/presentation/d/1SvfmvYcGw8A6jx_Evs8ZN9_C0nzeWCEY/edit?usp=sharing&ouid=109927448714846827229&rtpof=true&sd=true).

I also uploaded a demo video on YouTube. You can check it out [here](https://youtu.be/38bXPLaae34).

You can view my participation certificate [here](https://drive.google.com/file/d/1PbTYM9aNIBi2kesFaR2R-fnhRxQEcvhk).

## How to Use It?

Yes, you can download the entire repository and store it in one directory itself.

You should download all the necessary Python packages and run the `main.py` program to start the GUI.

## Changelog

Go to the [CHANGELOG.md](https://github.com/anikethchavare/Elvvo/blob/main/CHANGELOG.md) file to see the changelog.

## Credits

Go to the [CREDITS.md](https://github.com/anikethchavare/Elvvo/blob/main/CREDITS.md) file to see the credits.

## License

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

## Conclusion

If you experience any problems or bugs, please go to the 'Issues' section and create an issue. I will look into it and resolve it ASAP.

I hope you liked this project. Thank you!