import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# wpisz ścieżkę do katalogu z danymi
my_path = r'C:\Users\mkowa\Desktop\Julia\Rezonatory2025\pomiary\pomiary_070825'
# wpisz nazwę pliku
file = r'dwie_soczewki_070825.csv'
# file2 = r'2PA_2_070825.csv' 
# file3 = r'2PA_3_070825.csv'
# file4 = r'2PA_4_070825.csv'
# nazwa katalogu zapisu
save_path = r'C:\Users\mkowa\Desktop\Julia\Rezonatory2025\wyniki\wyniki_070825'
# wpisz nazwę pliku do zapisu wykresus
file_save = r'dwie_soczewki_070825_plot.png'

plt.figure(figsize=(8,6))

# laser vs probka
# for i in [2,4,8,12,16]:
#     file = f"laser_vs_probka_{i}_040825.csv"
#     data = pd.read_csv(os.path.join(my_path, file))
#     df = pd.DataFrame(data)
#     P1 = df['Power2 [W]']
#     z = df['Position [mm]']
#     plt.plot(z, P1, label=f'Pomiar {i}')
data = pd.read_csv(os.path.join(my_path, file))
# data1 = pd.read_csv(os.path.join(my_path, file2))
# data2 = pd.read_csv(os.path.join(my_path, file3))
# data3 = pd.read_csv(os.path.join(my_path, file4))
df = pd.DataFrame(data)
# df1 = pd.DataFrame(data1)
# df2 = pd.DataFrame(data2)
# df3 = pd.DataFrame(data3)
P_ref = 0.501 #W

P1 = df['Power [W]']/P_ref *100
# P2 = df1['Power [W]']/P_ref*100
# P3 = df2['Power [W]']/P_ref*100
# P4 = df3['Power [W]']/P_ref*100

z1 = df['Position [mm]']
# z2 = df1['Position [mm]']
# z3 = df2['Position [mm]']
# z4 = df3['Position [mm]']

'''PLOT'''

plt.plot(z1, P1, color='darkorange', label = 'Pomiar 1 - zaraz po odsłonięciu')
# plt.plot(z2, P2, color='blue', label = 'Pomiar 2 - po 10 minutach naświetlania')
# plt.plot(z3, P3, color='green', label = 'Pomiar 3 - ponownie odsłonięta')
# plt.plot(z4, P4, color='red', label = 'Pomiar 4 - po 20 minutach naświetlania')
plt.xlabel('Pozycja [mm]')
# plt.ylabel('Moc [W]')
plt.ylabel('Transmitancja [%]')
plt.xlim(0,15)
# plt.legend()
plt.grid(linestyle='--')
plt.savefig(os.path.join(save_path, file_save))
plt.show()