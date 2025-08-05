import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# wpisz ścieżkę do katalogu z danymi
my_path = r'C:\Users\gosc\Desktop\Rezonatory2025\Rezonatory2025\pomiary\pomiary_040825'
# wpisz nazwę pliku
# file = r'z_scan_szklo_apertura_310725.csv'
# nazwa katalogu zapisu
save_path = r'C:\Users\gosc\Desktop\Rezonatory2025\Rezonatory2025\wyniki\wyniki_040825'
# wpisz nazwę pliku do zapisu wykresus
file_save = r'laser_vs_probka_ref_050825.png'

# laser vs probka
for i in range(1,92):
    file = f"laser_vs_probka_{i}_040825.csv"
    data = pd.read_csv(os.path.join(my_path, file))
    df = pd.DataFrame(data)
    P1 = df['Power1 [W]']
    z = df['Position [mm]']
    if i % 10 == 0:
        if i == 17:
            P1 = P1/100
        elif i >= 18:
            P1 = P1/1000
        plt.plot(z, P1, label=f'Pomiar {i}')
# data = pd.read_csv(os.path.join(my_path, file))
# df = pd.DataFrame(data)

# P = df['Power [W]']

# z = df['Position [mm]']

'''PLOT'''

# plt.plot(z, P, color='darkorange')
plt.xlabel('Pozycja [mm]')
plt.ylabel('Moc [W]')
plt.xlim(0,40)
plt.legend()
plt.grid(linestyle='--')
plt.savefig(os.path.join(save_path, file_save))
plt.show()