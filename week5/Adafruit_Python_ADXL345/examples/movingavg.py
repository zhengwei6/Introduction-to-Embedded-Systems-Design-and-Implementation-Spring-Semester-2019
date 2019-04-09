import time
import Adafruit_ADXL345
import numpy
accel = Adafruit_ADXL345.ADXL345()
movingAvg= [0,0,0,0,0]
while True:
    x, y, z = accel.read()
    real_x = x * 0.004
    real_y = y * 0.004
    real_z = z * 0.004
    norm = numpy.sqrt(pow(real_x,2)+pow(real_y,2)+pow(real_z,2))
    movingAvg.pop(0)
    movingAvg.append(norm)
    ans = sum(movingAvg) / len(movingAvg)
    print(ans) 
    time.sleep(1)
