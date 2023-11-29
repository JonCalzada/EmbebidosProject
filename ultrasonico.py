import RPi.GPIO as GPIO
import time

# ESTA EN CM
MIN_DISTANCIA=10

#GPIO.setwarnings(False)
def medir():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    TRIG = 24
    ECHO = 25

    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)

    GPIO.output(TRIG, False)
    #print("Waiting For Sensor To Settle")
    time.sleep(2)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150
    distance = round(distance, 2)
    
    print(distance)
    #return (distance<MIN_DISTANCIA)
    return int(distance)
