import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# wpisz ścieżkę do katalogu z danymi
my_path = r'C:\Users\mkowa\Desktop\Julia\Rezonatory2025\!wyniki\230725_ini'
# wpisz nazwę pliku
file = r'power_vs_position_mwcnt1_1_23072025.csv'
# wpisz nazwę pliku do zapisu wykresu
file_save = r'szkiełko.png'

data = pd.read_csv(os.path.join(my_path, file))
df = pd.DataFrame(data)

P1 = df['Power1 [W]']
P2 = df['Power2 [W]']
z = df['Position [mm]']

'''POWER BEFORE'''
P_norm = 0.484 #W

'''NORMALIZATION'''
P1 = P1 / P1.max()
P2 = P2 / P2.max()


plt.plot(z, P1, color='chocolate')
plt.plot(z, P2, color='darkblue')
plt.xlabel('Pozycja [mm]')
plt.ylabel('Moc [W]')
plt.xlim(10,30)
plt.grid(linestyle='--')
plt.savefig(os.path.join(my_path, file_save))
plt.show()