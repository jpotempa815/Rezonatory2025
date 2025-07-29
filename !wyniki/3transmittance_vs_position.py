import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# wpisz ścieżkę do katalogu z danymi
my_path = r'/workspaces/Rezonatory2025/!wyniki/290725_open_closed_aperture'
# wpisz nazwę pliku
file = r'open_close_aperture_mwcnt1_290725.csv'
# wpisz nazwę pliku do zapisu wykresu
file_save = r'open_close_aperture_mwcnt1_290725_plot2.png'

data = pd.read_csv(os.path.join(my_path, file))
df = pd.DataFrame(data)

P1 = df['Power1 [W]'] 
P2 = df['Power2 [W]'] 
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

# plt.plot(z, P1, color='chocolate')
plt.plot(z, P2, color='darkblue')
plt.xlabel('Pozycja [mm]')
plt.ylabel('Moc [W]')
plt.xlim(0,46.5)
plt.grid(linestyle='--')
plt.savefig(os.path.join(my_path, file_save))
plt.show()