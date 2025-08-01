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

'''POWER REFLECTED PERCENTAGE'''
P_ref = 0.0086 # 0.86%
# ile razy P_ini jest większe od P_ref
P_ref_ini = 1/P_ref

'''LOSS THROUGH LENS PERCENTAGE'''
P_trans = 0.058 # 5.8%

'''LOSS THROUGH GLASS PERCENTAGE'''
P_glass = 0.0738 # 7.38%

'''MEASURED POWER PERCENTAGE'''
meas_perc = (1-P_ref)* (1-P_trans)*(1-P_glass)* P_ref_ini

'''FINAL POWER PERCENTAGE ON SECOND POWER METER'''
P_ref_v = 1/(P * meas_perc)


'''PLOT'''

plt.plot(z, P_ref_v, color='darkorange', label='Moc')
# plt.plot(z, P, color='darkorange', label='Moc')
# plt.plot(z, P1, color='chocolate')
# plt.plot(z, P2, color='darkblue')
plt.xlabel('Pozycja [mm]')
plt.ylabel('Moc [W]')
plt.xlim(0,25)
plt.grid(linestyle='--')
plt.savefig(os.path.join(my_path, file_save))
plt.show()