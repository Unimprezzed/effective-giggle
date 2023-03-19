# effective-giggle
A simple script that tests your Astro-Pi setup and OpenCV. This script was written with the 32-bit OS in mind, but I'm going to rewrite it to support 64-bit Raspberry Pi OS, which should make it backwards compatible with the older version.

The AstroPi Setup: 
This was based off of an archived project detailed at https://projects.raspberrypi.org/en/projects/astro-pi-flight-case. The script was made to test this version. 
There is a new version detailed at https://projects.raspberrypi.org/en/projects/astro-pi-flight-case-mk2, but this script should be compatible with both versions of the flight case + hardware set up, since it's only testing the SenseHat and camera. 

Differences between v1 and v2 of the AstroPi flight case: 
 - v2 has 2 buttons instead of 4
 - v2 has a PIR sensor for detecting movement 

Hardware Requirements: 
- Raspberry Pi 4 or 3, Model B or Model B+
- Raspberry Pi Camera Module
- Raspberry Pi SenseHat

Package Requirements: 
- Numpy
- OpenCV
- sense-hat

Recommended: 
-virtualenv (for running in a virtual environment)

How to use: 
This script can be run "python App.py". That's all there is to it! 

Description: 
When run, this program will use the camera to produce a live video feed thresholded to 15 frames per second (any faster results in a really dark image). The script then uses OpenCV to reduce the size of the image so that it can be output to the SenseHat's 8x8 LED display and display the current output of the SenseHat's sensors. 
