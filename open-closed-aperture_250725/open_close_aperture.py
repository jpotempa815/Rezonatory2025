from zaber_motion import Units, Library
from zaber_motion.ascii import Connection
from datetime import datetime
from ctypes import *
from TLPMX import TLPMX, TLPM_DEFAULT_CHANNEL
import time
import csv

Library.enable_device_db_store()

# ZMIEN NAZWE PLIKU !!!!!
with Connection.open_serial_port("COM3") as connection:
    connection.enable_alerts()
    device_list = connection.detect_devices()

    device = device_list[0]
    axis = device.get_axis(1)

    if not axis.is_homed():
        print("Homing axis...")
        axis.home()
        axis.wait_until_idle()

    # parametry ruchu
    min_pos = 0
    max_pos = 47
    step_size_norm = 0.5
    step_size_peak = 0.1
    delay = 0.5
    measure_delay = 2

    # pozycja początkowa
    print(f"Starting position: {min_pos:.2f} mm")
    axis.move_absolute(min_pos, Units.LENGTH_MILLIMETRES)
    axis.wait_until_idle()

    pos = min_pos

    # inicjalizacja miernikow
    deviceCount = c_uint32()
    tlpm = TLPMX()
    tlpm.findRsrc(byref(deviceCount))


    if deviceCount.value < 2:
        print(f"Only {deviceCount.value} device(s) found. Two required.")
        exit(1)

    print("Number of found devices:", deviceCount.value)


    resource_names = []
    for i in range(deviceCount.value):
        buf = create_string_buffer(1024)
        tlpm.getRsrcName(c_int(i), buf)
        resource_name = c_char_p(buf.raw).value
        print(f"Resource name of device {i}: {resource_name.decode()}")
        resource_names.append(resource_name)

    # koniec szukania
    tlpm.close()

    # nowe polaczenie
    tlpm1 = TLPMX()
    tlpm2 = TLPMX()
    tlpm1.open(resource_names[0], c_bool(True), c_bool(True))
    tlpm2.open(resource_names[1], c_bool(True), c_bool(True))

    for idx, tl in enumerate([tlpm1, tlpm2], start=1):
        msg = create_string_buffer(1024)
        tl.getCalibrationMsg(msg, TLPM_DEFAULT_CHANNEL)
        print(f"Device {idx} calibration date: {msg.value.decode()}")
        tl.setWavelength(c_double(532.5), TLPM_DEFAULT_CHANNEL)
        tl.setPowerAutoRange(c_int16(1), TLPM_DEFAULT_CHANNEL)
        tl.setPowerUnit(c_int16(0), TLPM_DEFAULT_CHANNEL)

    time.sleep(2)

    out = "open_close_aperture_250725.csv"

    power1_measurements = []
    power2_measurements = []
    time_relative = []
    positions = []

    print("\nStarting measurement...\n")
    start_time = time.time()

    power1 = c_double()
    power2 = c_double()
    tlpm1.measPower(byref(power1), TLPM_DEFAULT_CHANNEL)
    tlpm2.measPower(byref(power2), TLPM_DEFAULT_CHANNEL)

    t_rel = time.time() - start_time
    power1_measurements.append(power1.value)
    power2_measurements.append(power2.value)
    time_relative.append(t_rel)
    positions.append(pos)
    print(f"{t_rel:.2f} s: Power1 = {power1.value:.6f} W, Power2 = {power2.value:.6f} W")

    step_size = step_size_norm

    while pos + step_size <= max_pos:
        # if 20 < pos < 28:
        #     step_size = step_size_peak
        # else:
        #     step_size = step_size_norm
        pos += step_size
        print(f"Position: {pos:.2f} mm")
        axis.move_absolute(pos, Units.LENGTH_MILLIMETRES)
        axis.wait_until_idle()
        time.sleep(measure_delay)

        power1 = c_double()
        power2 = c_double()
        tlpm1.measPower(byref(power1), TLPM_DEFAULT_CHANNEL)
        tlpm2.measPower(byref(power2), TLPM_DEFAULT_CHANNEL)

        t_rel = time.time() - start_time
        power1_measurements.append(power1.value)
        power2_measurements.append(power2.value)
        time_relative.append(t_rel)
        positions.append(pos)
        print(f"{t_rel:.2f} s: Power1 = {power1.value:.6f} W, Power2 = {power2.value:.6f} W")
        time.sleep(delay)

    # Powrót
    axis.move_absolute(min_pos, Units.LENGTH_MILLIMETRES)
    axis.wait_until_idle()

# Zapis danych
with open(out, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Time [s]", "Position [mm]", "Power1 [W]", "Power2 [W]"])
    for t, p, pow1, pow2 in zip(time_relative, positions, power1_measurements, power2_measurements):
        writer.writerow([f"{t:.3f}", p, pow1, pow2])

tlpm1.close()
tlpm2.close()

print("\nDone")
