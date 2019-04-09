import time
import Adafruit_ADXL345
import numpy
accel = Adafruit_ADXL345.ADXL345()
lowy=0
while True:
    x, y, z = accel.read()
    real_x = x * 0.004
    real_y = y * 0.004
    real_z = z * 0.004
    norm = numpy.sqrt(pow(real_x,2)+pow(real_y,2)+pow(real_z,2))
    if lowy == 0:
        lowy=norm
    else:
        lowy=(0.5*norm)+(0.5 * lowy)
    print(lowy) 
    time.sleep(1)
