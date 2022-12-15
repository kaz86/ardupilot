from pymavlink import mavutil
import time
import sys

# Connection to the aircraft
master = mavutil.mavlink_connection('tcp:127.0.0.1:5762')
master.wait_heartbeat() 

master.mav.param_request_list_send(
    master.target_system, master.target_component
)

while True:
    time.sleep(0.01)
    try:
        message = master.recv_match(type='PARAM_VALUE', blocking = True).to_dict()
        print('name: %s\tvalue: %d' %
            (message['param_id'],message['param_value']))
    except Exception as error:
        sys.exit(0)

