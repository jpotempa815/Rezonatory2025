import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# wpisz ścieżkę do katalogu z danymi
my_path = r'C:\Users\mkowa\Desktop\Julia\Rezonatory2025\pomiary\pomiary_040825'
# wpisz nazwę pliku
# file = r'grafen_m1_1_time=2_040825.csv'
# file2 = r'grafen_m1_1_time=5_040825.csv'
# file3 = r'grafen_m1_1_time=10_040825.csv'
# nazwa katalogu zapisu
save_path = r'C:\Users\mkowa\Desktop\Julia\Rezonatory2025\wyniki\wyniki_040825'
# wpisz nazwę pliku do zapisu wykresus
file_save = r'laser_vs_probka_040825.png'

# laser vs probka
for i in range(1,92):
    file = f"laser_vs_probka_{i}_040825.csv"
    data = pd.read_csv(os.path.join(my_path, file))
    df = pd.DataFrame(data)
    P2 = df['Power2 [W]']
    z = df['Position [mm]']
    if i % 10 == 0:
        plt.plot(z, P2, label=f'Pomiar {i}')
# data = pd.read_csv(os.path.join(my_path, file))
# data2 = pd.read_csv(os.path.join(my_path, file2))
# data3 = pd.read_csv(os.path.join(my_path, file3))
# df = pd.DataFrame(data)
# df2= pd.DataFrame(data2)
# df3 = pd.DataFrame(data3)

# P1 = df['Power [W]']
# P2 = df2['Power [W]']
# P3 = df3['Power [W]']

# z1 = df['Position [mm]']
# z2 = df2['Position [mm]']
# z3 = df3['Position [mm]']

'''PLOT'''

# plt.plot(z1, P1, color='darkorange', label='Czas: 2s')
# plt.plot(z2, P2, color='blue', label='Czas: 5s')
# plt.plot(z3, P3, color='green', label='Czas: 10s')
plt.xlabel('Pozycja [mm]')
plt.ylabel('Moc [W]')
plt.xlim(0,25)
plt.legend()
plt.grid(linestyle='--')
plt.savefig(os.path.join(save_path, file_save))
plt.show()