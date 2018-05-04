'''
Author: Trey "Unimprezzed" Blankenship
Date of first commit: 5/4/2018
This program makes a very low resolution real-time camera preview for an Astro Pi (https://astro-pi.org/) replica, in addition to testing all sensors on the SenseHat
'''
from picamera.array import PiRGBArray
from picamera import PiCamera
from sense_hat import SenseHat
import time
import cv2
import sys
#Configuration
resolution = (608,608)
print("Beginning setup...")
sense = SenseHat()
camera = PiCamera()
camera.resolution = resolution
camera.rotation = 90
camera.framerate = 15
camera.awb_mode = 'cloudy'
sense.set_rotation(270)
raw_capture = PiRGBArray(camera, size = resolution)
dim = (8,8)
time.sleep(0.1)
font = cv2.FONT_HERSHEY_SIMPLEX

sensor_header = "Sensor output:"
def main():
    for frame in camera.capture_continuous(raw_capture, format="bgr", use_video_port= True):
        image = frame.array #Get the frame from the camera.
        #Update raw sensor output.
        temperature = sense.temp
        temp_humid = sense.get_temperature_from_humidity()
        temp_pressure = sense.get_temperature_from_pressure()
        pressure = sense.pressure
        humidity = sense.humidity
        orientation = sense.orientation
        gyroscope = sense.gyroscope
        gyroscope_raw = sense.gyroscope_raw
        accelerometer = sense.accelerometer
        accelerometer_raw = sense.accelerometer_raw
        compass_raw = sense.compass_raw
        north = sense.compass
        
        #End stuff. 
        resized = cv2.resize(image,dim,interpolation=cv2.INTER_AREA)
        img = resized[...,::-1]
        sense.set_pixels(img.reshape(64,3))
        #Add Sensor output on the preview screen.
        cv2.putText(image,sensor_header,(5,10),font,0.3,(255,255,255),1,cv2.LINE_AA)
        cv2.putText(image,'Temperature: %.1f C (Thermometer)' % temperature,(5,20),font,0.3,(255,255,255),1,cv2.LINE_AA)
        cv2.putText(image,'Temperature (Barometer): %.1f C' % temp_pressure, (5,30),font,0.3,(255,255,255),1,cv2.LINE_AA)
        cv2.putText(image,'Temperature (Humidity Sensor): %.1f C' % temp_humid, (5,40),font,0.3,(255,255,255),1,cv2.LINE_AA)
        cv2.putText(image,'Pressure: %.1f mbar (Barometer)' % pressure,(5,50),font,0.3,(255,255,255),1,cv2.LINE_AA)
        cv2.putText(image,'Humidity: %.1f %%(Humidity Sensor)' % humidity, (5,60), font, 0.3, (255,255,255),1,cv2.LINE_AA)
        cv2.putText(image,'Orientation: p: {pitch}, r: {roll}, y: {yaw}'.format(**orientation), (5,70), font, 0.3, (255,255,255), 1, cv2.LINE_AA)
        cv2.putText(image,'Magnetic North: %s'%north, (5,80), font, 0.3, (255,255,255), 1, cv2.LINE_AA)
        cv2.putText(image,'Compass (raw): x: {x}µT, y: {y}µT, z: {z}µT'.format(**compass_raw), (5,90), font, 0.3, (255,255,255), 1, cv2.LINE_AA)
        cv2.putText(image,'Gyroscope: p: {pitch}, r: {roll}, y: {yaw}'.format(**gyroscope),(5,100), font, 0.3, (255,255,255), 1, cv2.LINE_AA)
        cv2.putText(image,'Gyroscope (raw): x: {x} rad/s, y: {y} rad/s, z: {z} rad/s'.format(**gyroscope_raw), (5,110), font, 0.3,  (255,255,255), 1, cv2.LINE_AA)
        cv2.putText(image,'Accelerometer: p: {pitch}, r: {roll}, y: {yaw}'.format(**accelerometer), (5,120),font,0.3,(255,255,255),1,cv2.LINE_AA)
        cv2.putText(image,'Accelerometer: x: {x} G, y: {y} G, z: {z} G'.format(**accelerometer_raw),(5,130),font,0.3,(255,255,255),1,cv2.LINE_AA)
        
        cv2.imshow("Camera Preview",image)
        key = cv2.waitKey(1) & 0xFF
        raw_capture.truncate(0)
        if key == ord("q"):
            sense.clear()
            break
        
if __name__ == "__main__":
    main()