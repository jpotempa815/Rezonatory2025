import time
from zaber_motion import Units, Library
from zaber_motion.ascii import Connection

Library.enable_device_db_store()


with Connection.open_serial_port("COM3") as connection:
    connection.enable_alerts()
    device_list = connection.detect_devices()

    device = device_list[0]
    axis = device.get_axis(1)

    if not axis.is_homed():
        print("Homing axis...")
        axis.home()
        axis.wait_until_idle()

    #pozycja początkowa
    # start_pos = axis.get_position(Units.LENGTH_MILLIMETRES)
    # print(f"Pozycja początkowa: {start_pos:.2f} mm")

    #parametry ruchu
    # num_steps = 5
    start = 31 #mm
    stop = 38 #mm
    step_size = 0.5 #mm
    delay = 1 #s    

    #start
    axis.move_absolute(start, Units.LENGTH_MILLIMETRES)
    start_pos = axis.get_position(Units.LENGTH_MILLIMETRES)
    print(f"Pozycja początkowa: {start_pos:.2f} mm")
    pos = start_pos
    
    while pos <= stop:
        pos += step_size
        print(f"Przesuwam do {pos:.2f} mm")
        axis.move_absolute(pos, Units.LENGTH_MILLIMETRES)
        axis.wait_until_idle()
        time.sleep(delay)

    #pozycja początkowa
    axis.move_absolute(start_pos, Units.LENGTH_MILLIMETRES)
    axis.wait_until_idle()

