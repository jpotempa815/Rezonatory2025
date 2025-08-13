import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# wpisz ścieżkę do katalogu z danymi
my_path = r'C:\Users\mkowa\Desktop\Julia\Rezonatory2025\pomiary\pomiary_130825'
file = r'1_grafen_m1_probka_130825.csv'
file2 = r'1_grafen_m1_szklo_130825.csv' 
# nazwa katalogu zapisu
save_path = r'C:\Users\mkowa\Desktop\Julia\Rezonatory2025\wyniki\wyniki_130825'
# wpisz nazwę pliku do zapisu wykresus
file_save = r'grafen_m1_1_130825_plot.png'

plt.figure(figsize=(8,6))

data = pd.read_csv(os.path.join(my_path, file))
data1 = pd.read_csv(os.path.join(my_path, file2))

df = pd.DataFrame(data)
df1 = pd.DataFrame(data1)

# P_soczewka = 0.481 #W moc za pierwszą soczewką
P0 = 0.5 #W moc lasera

P_wsp = 0.962
P_ref = P0 * P_wsp #W moc padająca na próbkę

#straty
# P_bez_probki = 0.44 #W moc tracona na przejściu przez drugą soczewkę i szkiełko
# P_wsp2 = 0.91476
P2 = df1['Power [W]']
P2_wsp = P2/P_ref

P_strat = 1 + (1 - P2_wsp) #czynnik strat (czyli ile więcej transmitancji ostatecznie jest)

P1 = df['Power [W]']/P_ref * P_strat * 100
# P2 = P2 / P_ref *100

z1 = df['Position [mm]']

'''PLOT'''

plt.plot(z1, P1, color='darkorange', label = 'Próbka')
# plt.plot(z1, P2, color='blue', label = 'Szkło')
plt.xlabel('Pozycja [mm]')
# plt.ylabel('Moc [W]')
plt.ylabel('Transmitancja [%]')
# plt.ylabel("Intensywność [arb. units]")
plt.xlim(0,13)
plt.legend()
plt.grid(linestyle='--')
plt.savefig(os.path.join(save_path, file_save))
plt.show()