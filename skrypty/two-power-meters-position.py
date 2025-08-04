import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# wpisz ścieżkę do katalogu z danymi
my_path = r'C:\Users\mkowa\Desktop\Julia\Rezonatory2025\pomiary\pomiary_040825'
# wpisz nazwę pliku
file = r'power-meter_reference_040825.csv'
#katalog zapisu
save_path = r'C:\Users\mkowa\Desktop\Julia\Rezonatory2025\wyniki\wyniki_040825'
# wpisz nazwę pliku do zapisu wykresu
file_save = r'power-meter_reference_040825_plot.png'

data = pd.read_csv(os.path.join(my_path, file))
df = pd.DataFrame(data)

P1 = df['Power1 [W]'] 
P2 = df['Power2 [W]'] 
z = df['Position [mm]']

'''POWER REFLECTED PERCENTAGE'''
# P_ref = 0.0086 # 0.86%
P_ref = 0.009665 # 0.97%

'''TRANSMITTANCE'''
T = P2/P1 * P_ref *100 #%

'''PLOT'''
# plt.plot(z, P1, color='blue', label='Power1 [W]')
plt.plot(z, P2, color='darkorange', label='Moc')
plt.xlabel('Pozycja [mm]')
plt.ylabel('Transmitancja [%]')
plt.xlim(0,25)
plt.grid(linestyle='--')
plt.savefig(os.path.join(save_path, file_save))
plt.show()