import RPi.GPIO as GPIO
import time
import sys
import Adafruit_DHT


sensor_args={'11':Adafruit_DHT.DHT11,
             '22':Adafruit_DHT.DHT22,
             '2302':Adafruit_DHT.AM2302}
if len(sys.argv)==3 and sys.argv[1] in sensor_args:
    sensor = sensor_args[sys.argv[1]]
    pin = sys.argv[2]
else:
    print('error')
    sys.exit(1)

LED_PIN = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN,GPIO.OUT)

try:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(sensor,pin)
        print(temperature)
        if temperature >= 25:
            GPIO.output(LED_PIN,GPIO.HIGH)
            print("LED is on")
        else:
            GPIO.output(LED_PIN,GPIO.LOW)
            print("LED is off")
except KeyboardInterrupt:
    print "Exception: KeyboardInterrupt"
finally:
    GPIO.clean()
