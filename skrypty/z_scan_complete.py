from zaber_motion import Units, Library
from zaber_motion.ascii import Connection
from datetime import datetime
from ctypes import *
from TLPMX import TLPMX, TLPM_DEFAULT_CHANNEL
import time
import os
import csv


Library.enable_device_db_store()

# ZMIEN NAZWE PLIKU !!!!!
# katalog zapisu
my_path = r'C:\Users\mkowa\Desktop\Julia\Rezonatory2025\pomiary\pomiary_130825'
# nazwa pliku
out_file = "1_probka_130825.csv"
# sciezka do pliku
out = os.path.join(my_path, out_file)

with Connection.open_serial_port("COM3") as connection: #tu trzeba dać odpowiednią nazwę portu usb
    connection.enable_alerts()
    device_list = connection.detect_devices()

    device = device_list[0]
    axis = device.get_axis(1)

    if not axis.is_homed():
        print("Homing axis...")
        axis.home()
        axis.wait_until_idle()


    #parametry ruchu stolika
    min_pos = 0  # mm
    max_pos = 13 # mm
    step_size_norm = 0.5 # mm
    step_size_peak = 0.1 # mm
    # step_size_peak = 0.04 #mm
    delay = 0.5 #s
    measure_delay = 2 #s

    #pozycja początkowa
    print(f"Starting position: {min_pos:.2f} mm")
    axis.move_absolute(min_pos, Units.LENGTH_MILLIMETRES)
    axis.wait_until_idle()

    pos = min_pos

    tlPM = TLPMX()
    deviceCount = c_uint32()
    tlPM.findRsrc(byref(deviceCount))

    if deviceCount.value == 0:
        print("No devices found.")
        exit(1)

    print("Number of found devices:", deviceCount.value)

    resourceName = create_string_buffer(1024)
    for i in range(deviceCount.value):
        tlPM.getRsrcName(c_int(i), resourceName)
        print("Resource name of device", i, ":", c_char_p(resourceName.raw).value)
    tlPM.close()

    tlPM = TLPMX()
    tlPM.open(resourceName, c_bool(True), c_bool(True))

    message = create_string_buffer(1024)
    tlPM.getCalibrationMsg(message, TLPM_DEFAULT_CHANNEL)
    print("Connected to device", i)
    print("Last calibration date:", c_char_p(message.raw).value.decode())

    #konfiguracja
    tlPM.setWavelength(c_double(2300), TLPM_DEFAULT_CHANNEL)
    tlPM.setPowerAutoRange(c_int16(1), TLPM_DEFAULT_CHANNEL)
    tlPM.setPowerUnit(c_int16(0), TLPM_DEFAULT_CHANNEL)
    time.sleep(2)   

    #tablice do zapisu
    power_measurements = []
    time_relative = []
    positions = []
    print("\nStarting measurement...\n")
    start_time = time.time()

    power = c_double()
    tlPM.measPower(byref(power), TLPM_DEFAULT_CHANNEL)
    t_rel = time.time() - start_time
    power_measurements.append(power.value)
    time_relative.append(t_rel)
    positions.append(pos)
    print(f"{t_rel:.2f} s: {power.value:.6f} W")

    step_size = step_size_peak
    
    while pos + step_size <= max_pos:
        # if 6 < pos < 10:
        #     step_size = step_size_peak
        # else: 
        #     step_size = step_size_norm
        pos += step_size
        print(f"Position: {pos:.2f} mm")
        axis.move_absolute(pos, Units.LENGTH_MILLIMETRES)
        axis.wait_until_idle()
        time.sleep(measure_delay)
        power = c_double()
        tlPM.measPower(byref(power), TLPM_DEFAULT_CHANNEL)
        t_rel = time.time() - start_time
        power_measurements.append(power.value)
        time_relative.append(t_rel)
        positions.append(pos)
        print(f"{t_rel:.2f} s: {power.value:.6f} W")
        time.sleep(delay)

    #powrot do pozycji początkowej
    axis.move_absolute(min_pos, Units.LENGTH_MILLIMETRES)
    axis.wait_until_idle()


with open(out, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Time [s]", "Position [mm]", "Power [W]"])
    for t, p, pow in zip(time_relative, positions, power_measurements):
        writer.writerow([f"{t:.3f}", p, pow])
        
tlPM.close()
print("\nDone")