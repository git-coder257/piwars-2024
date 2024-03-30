import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO_TRIGGER =14
GPIO_ECHO =4

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
def distance():
    # 10us is the trigger signal
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001) #10us
    GPIO.output(GPIO_TRIGGER, False)
    start_time = time.time() # Log the time the program runs to this point
    stop_time = time.time() # Log the time the program runs to this point
    while GPIO.input(GPIO_ECHO) == 0: #Indicates that the ultrasonic wave has been emitted
        start_time = time.time() #Record launch time
    while GPIO.input(GPIO_ECHO) == 1: #Indicates that the returned ultrasound has been received
        stop_time = time.time() #Record receiving time
    time_elapsed = stop_time

    start_time #Time difference from transmit to receive
    distance = (time_elapsed * 34000) / 2 #Calculate the distance
    return distance #Return to calculated distance
