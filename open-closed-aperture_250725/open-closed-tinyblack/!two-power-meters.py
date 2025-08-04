from zaber_motion import Units, Library
from zaber_motion.ascii import Connection
from datetime import datetime
import os
import pathlib
import sys
import glob
import csv

sys.path.insert(0, os.path.abspath('.'))
sys.path.extend(glob.glob(f'{pathlib.Path(__file__).parents[0].resolve()}/*/**/', recursive=True))

from ThorlabsPowerMeter import ThorlabsPowerMeter
import time

for i in range(6, 100):
    if __name__=='__main__':
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
            max_pos = 25
            step_size_norm = 0.5
            step_size_peak = 0.1
            delay = 0.5
            measure_delay = 2

            # pozycja początkowa
            print(f"Starting position: {min_pos:.2f} mm")
            axis.move_absolute(min_pos, Units.LENGTH_MILLIMETRES)
            axis.wait_until_idle()

            pos = min_pos

            _deviceList = ThorlabsPowerMeter.listDevices()
            logger=_deviceList.logger
            # deviceA=_deviceList.connect(_deviceList.resourceName[0])
            # deviceB=_deviceList.connect(_deviceList.resourceName[1])
            deviceA = _deviceList.connect(_deviceList.resourceName[0])
            if deviceA is None:
                logger.error(f"Failed to connect to device: {_deviceList.resourceName[0]}")
                sys.exit(1)
            deviceB = _deviceList.connect(_deviceList.resourceName[1])
            if deviceB is None:
                logger.error(f"Failed to connect to device: {_deviceList.resourceName[1]}")
                sys.exit(1)
            deviceA.getSensorInfo()
            deviceB.getSensorInfo()
            deviceA.setWaveLength(2300) 
            deviceB.setWaveLength(2300)                            
            deviceA.setDispBrightness(0.7) 
            deviceB.setDispBrightness(0.7)                          
            deviceA.setAttenuation(0)      
            deviceB.setAttenuation(0)                          
            deviceA.setPowerAutoRange(True)
            deviceB.setPowerAutoRange(True)                             
            time.sleep(5)                                                    
            deviceA.setAverageTime(0.01)
            deviceB.setAverageTime(0.01)                           
            # deviceA.setTimeoutValue(1000)                             
            # deviceB.setTimeoutValue(1000)                                                   

            #katalog
            my_path = r'C:\Users\mkowa\Desktop\Julia\Rezonatory2025\pomiary\pomiary_040825'
            #nazwa pliku
            out = f"laser_vs_probka_{i}_040825.csv"
            #sciezka do pliku
            out = os.path.join(my_path, out)

            power1_measurements = []
            power2_measurements = []
            time_relative = []
            positions = []

            print("\nStarting measurement...\n")
            start_time = time.time()

            t_rel = time.time() - start_time
            deviceA.updatePowerReading(0.1)
            power1_measurements.append(deviceA.meterPowerReading)
            deviceB.updatePowerReading(0.1)
            power2_measurements.append(deviceB.meterPowerReading)
            time_relative.append(t_rel)
            positions.append(pos)
            logger.info(f'|{__name__}| A: {deviceA.meterPowerReading} {deviceA.meterPowerUnit}, B: {deviceB.meterPowerReading} {deviceB.meterPowerUnit}')

            step_size = step_size_peak

            while pos + step_size <= max_pos:
                # if 5 < pos < 7:
                #     step_size = step_size_peak
                # else:
                #     step_size = step_size_norm
                pos += step_size
                logger.info(f"Position: {pos:.2f} mm")
                axis.move_absolute(pos, Units.LENGTH_MILLIMETRES)
                axis.wait_until_idle()
                time.sleep(measure_delay)

                t_rel = time.time() - start_time
                deviceA.updatePowerReading(0.1)
                power1_measurements.append(deviceA.meterPowerReading)
                deviceB.updatePowerReading(0.1)
                power2_measurements.append(deviceB.meterPowerReading)
                time_relative.append(t_rel)
                positions.append(pos)
                logger.info(f'|{__name__}| A: {deviceA.meterPowerReading} {deviceA.meterPowerUnit}, B: {deviceB.meterPowerReading} {deviceB.meterPowerUnit}')
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
        deviceA.disconnect()
        deviceB.disconnect()
        logger.info(f'|{__name__}| Done')  

