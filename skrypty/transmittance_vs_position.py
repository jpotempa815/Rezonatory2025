import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# wpisz ścieżkę do katalogu z danymi
my_path = r'C:\Users\gosc\Desktop\Rezonatory2025\Rezonatory2025\pomiary\pomiary_040825'
# wpisz nazwę pliku
# file = r'z_scan_szklo_apertura_310725.csv'
# nazwa katalogu zapisu
save_path = r'C:\Users\gosc\Desktop\Rezonatory2025\Rezonatory2025\wyniki\wyniki_060825'
# wpisz nazwę pliku do zapisu wykresus
file_save = r'laser_vs_probka_wybrane_060825.png'

plt.figure(figsize=(8,6))

# laser vs probka
for i in [2,4,8,12,16]:
    file = f"laser_vs_probka_{i}_040825.csv"
    data = pd.read_csv(os.path.join(my_path, file))
    df = pd.DataFrame(data)
    P1 = df['Power2 [W]']
    z = df['Position [mm]']
    plt.plot(z, P1, label=f'Pomiar {i}')
# data = pd.read_csv(os.path.join(my_path, file))
# df = pd.DataFrame(data)

# P = df['Power [W]']

# z = df['Position [mm]']

'''PLOT'''

# plt.plot(z, P, color='darkorange')
plt.xlabel('Pozycja [mm]')
plt.ylabel('Moc [W]')
plt.xlim(0,25)
plt.legend()
plt.grid(linestyle='--')
plt.savefig(os.path.join(save_path, file_save))
plt.show()