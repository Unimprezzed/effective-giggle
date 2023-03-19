import cv2
from sense_hat import SenseHat

if __name__ == "__main__":
    print("Application has started running.")
    
    sense = SenseHat()
    messages = []
    
    def pushed_up(event):
        messages.append("Pushed Up!")

    def pushed_down(event):
        messages.append("Pushed Down!")

    def pushed_left(event):
        messages.append("Pushed Left!")

    def pushed_right(event):
        messages.append("Pushed Right!")

    #Setup Sense-Hat with functions defined above
    sense.stick.direction_up = pushed_up
    sense.stick.direction_down = pushed_down
    sense.stick.direction_left = pushed_left
    sense.stick.direction_right = pushed_right
    font = cv2.FONT_HERSHEY_SIMPLEX

    #Set up the camera
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 608)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 608)
    cap.set(cv2.CAP_PROP_FPS, 15)
    if not cap.isOpened():
        print("Fatal Error: Cannot open camera")
        exit()
    else:
        while True:
            #Read the camera
            ret, frame = cap.read()
            if not ret:
                print("Cannot receive frame! Exiting...")
                break
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_sense_hat = cv2.resize(rgb_frame, (8,8), interpolation=cv2.INTER_AREA).reshape(64,3)
            #Get the sensor readouts
            humidity = sense.get_humidity() #Percentage relative humidity
            temperature_from_humidity = sense.get_temperature_from_humidity() #Celcius
            temperature_from_pressure = sense.get_temperature_from_pressure() #Celcius
            pressure = sense.get_pressure() #Millibar
            orientation_radians = sense.get_orientation_radians() #Radians pitch-roll-yaw
            orientation_degrees = sense.get_orientation() #Degrees for pitch-roll-yaw
            compass = sense.get_compass() #Degrees from North?
            raw_compass = sense.get_compass_raw() #Magnetic intensity MicroTeslas
            gyro = sense.get_gyroscope() #Pitch, Roll, Yaw 
            raw_gyro = sense.get_gyroscope_raw() #X,Y,Z in radians / second
            accelerometer = sense.get_accelerometer() #Pitch Roll Yaw in degrees
            raw_accelerometer = sense.get_accelerometer_raw() #Accelerating intensity in Gs. 
            #Show the sensor readouts and put them in the image
            messages.clear()
            #Populate the messages 
            messages.append("Humidity: {}% rH".format(humidity))
            messages.append("Temperature (Humidity Sensor): {}".format(temperature_from_humidity))
            messages.append("Temperature (Pressure Sensor): {}".format(temperature_from_pressure))
            messages.append("Pressure: {} millibars".format(pressure))
            messages.append("Orientation (radians): p: {pitch}, r: {roll}, y: {yaw}".format(**orientation_radians))
            messages.append("Orientation (degrees): p: {pitch}, r: {roll}, y: {yaw}".format(**orientation_degrees))
            messages.append("Compass: {} degrees from north".format(compass))
            messages.append("Compass data: x: {x} µT, y: {y} µT, z: {z} µT".format(**raw_compass))
            messages.append("Gyro (Degrees): p: {pitch}, r: {roll}, y: {yaw}".format(**gyro))
            messages.append("Gyro (rad/s): x: {x}, y: {y}, z: {z}".format(**raw_gyro))
            messages.append("Accelerometer (degrees): p: {pitch}, r: {roll}, y: {yaw}".format(**accelerometer))
            messages.append("Accelerometer (G): x: {x}, y: {y}, z: {z}".format(**raw_accelerometer))
            
            for i in range(len(messages)):
                cv2.putText(rgb_frame, messages[i], (5, 10*i), font, 0.3, (255,255,255),1,cv2.LINE_AA)

            sense.set_pixels(frame_sense_hat)

            cv2.imshow('Camera', rgb_frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                sense.clear()
                break