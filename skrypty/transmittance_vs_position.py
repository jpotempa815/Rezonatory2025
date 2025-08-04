import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# wpisz ścieżkę do katalogu z danymi
my_path = r'C:\Users\gosc\Desktop\Rezonatory2025\Rezonatory2025\pomiary\pomiary_010825'
# wpisz nazwę pliku
file = r'grafen_m1_8_010825.csv'
# nazwa katalogu zapisu
save_path = r'C:\Users\gosc\Desktop\Rezonatory2025\Rezonatory2025\wyniki\010825'
# wpisz nazwę pliku do zapisu wykresus
file_save = r'grafen_m1_8_010825_plot.png'

data = pd.read_csv(os.path.join(my_path, file))
df = pd.DataFrame(data)

P = df['Power [W]']
z = df['Position [mm]']

'''PLOT'''

plt.plot(z, P, color='darkorange', label='Moc')
plt.xlabel('Pozycja [mm]')
plt.ylabel('Moc [W]')
plt.xlim(0,25)
plt.grid(linestyle='--')
plt.savefig(os.path.join(my_path, file_save))
plt.show()