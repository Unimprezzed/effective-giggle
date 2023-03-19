# effective-giggle
A simple script that tests your Astro-Pi setup. This script was written with 32-bit in mind, but I'm going to rewrite it to support 64-bit Raspberry Pi OS, which should make it backwards compatible with 32-bit

Hardware Requirements: 
- Raspberry Pi 3, Model B or Model B+
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
