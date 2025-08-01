import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# wpisz ścieżkę do katalogu z danymi
my_path = r'C:\Users\mkowa\Desktop\Julia\Rezonatory2025\pomiary\pomiary_010825'
# wpisz nazwę pliku
file = r'grafen_m1_8_010825.csv'
# wpisz nazwę pliku do zapisu wykresu
file_save = r'grafen_m1_8_010825_plot.png'

data = pd.read_csv(os.path.join(my_path, file))
df = pd.DataFrame(data)

P = df['Power [W]']
# P1 = df['Power1 [W]'] 
# P2 = df['Power2 [W]'] 
z = df['Position [mm]']

'''POWER BEFORE'''
P_norm = 0.456 #W

'''POWER REFLECTED'''
P_ref = 0.006

'''POWER TRANSMITTED'''
P_trans = 0.444

'''NORMALIZATION'''
# P1 = P1 / P1.max()
# P2 = P2 / P2.max()

'''LOSSES THROUGH GLASS'''
P_glass = 0.459
P_bef = 0.499
loss = (1 - P_glass / P_bef)

'''PLOT'''

plt.plot(z, P*(1+loss), color='darkorange', label='Moc')
# plt.plot(z, P, color='darkorange', label='Moc')
# plt.plot(z, P1, color='chocolate')
# plt.plot(z, P2, color='darkblue')
plt.xlabel('Pozycja [mm]')
plt.ylabel('Moc [W]')
plt.xlim(0,25)
plt.grid(linestyle='--')
plt.savefig(os.path.join(my_path, file_save))
plt.show()