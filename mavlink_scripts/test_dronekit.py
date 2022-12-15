from dronekit import connect, VehicleMode
import time
import sys

vehicle = connect('tcp:127.0.0.1:5762', wait_ready = False, timeout = 60)

try:
    vehicle.wait_for_armable()
    vehicle.wait_for_mode('GUIDED')
    vehicle.arm()
    time.sleep(1)
    vehicle.wait_simple_takeoff(10, timeout=20)

except TimeoutError as takeoffError:
    sys.eixt(0)
