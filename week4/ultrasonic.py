import RPi.GPIO as GPIO
import time

LED_PIN = 12
v = 343
TRIGGER_PIN = 16
ECHO_PIN = 18
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN,GPIO.OUT)
GPIO.setup(TRIGGER_PIN,GPIO.OUT)
GPIO.setup(ECHO_PIN,GPIO.IN)

def measure() :
    GPIO.output(TRIGGER_PIN, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIGGER_PIN, GPIO.LOW)

    while GPIO.input(ECHO_PIN) == GPIO.LOW:
        pulse_start = time.time()
    while GPIO.input(ECHO_PIN) == GPIO.HIGH:
        pulse_end = time.time()
    t = pulse_end - pulse_start
    d = t * v
    d = d/2
    return d*100

try:
    while True:
        if measure() > 100:
            print('safe')
        elif measure() > 30:
            print('be careful')
            GPIO.output(LED_PIN,GPIO.HIGH)
            time.sleep(0.01)
            GPIO.output(LED_PIN,GPIO.LOW)
            time.sleep(0.01)
            GPIO.output(LED_PIN,GPIO.HIGH)
            time.sleep(0.01)
            GPIO.output(LED_PIN,GPIO.LOW)
        elif measure():
            print('dangerous')
            GPIO.output(LED_PIN,GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(LED_PIN,GPIO.LOW)
            time.sleep(0.1)
            GPIO.output(LED_PIN,GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(LED_PIN,GPIO.LOW)
        time.sleep(1)
except KeyboardInterrupt:
    print "Exception"
finally:
    GPIO.cleanup()
