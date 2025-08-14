import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# wpisz ścieżkę do katalogu z danymi
my_path = r'C:\Users\mkowa\Desktop\Julia\Rezonatory2025\pomiary\pomiary_140825'
file1 = r'swcnt_sa-3(2)_1_140825.csv'
file2 = r'swcnt_sa-3(2)_2_140825.csv' 
file3 = r'swcnt_sa-3(2)_4_140825.csv'
file4 = r'grafen_b2_szklo_140825.csv'
file5 = r'C:\Users\mkowa\Desktop\Julia\Rezonatory2025\pomiary\pomiary_130825\1_grafen_m1_szklo_130825.csv'
# nazwa katalogu zapisu
save_path = r'C:\Users\mkowa\Desktop\Julia\Rezonatory2025\wyniki\wyniki_140825'
# wpisz nazwę pliku do zapisu wykresus
file_save = r'swcnt_sa-3(2)_plot.png'

plt.figure(figsize=(8,6))

data1 = pd.read_csv(os.path.join(my_path, file1))
data2 = pd.read_csv(os.path.join(my_path, file2))
data3 = pd.read_csv(os.path.join(my_path, file3))
data4 = pd.read_csv(os.path.join(my_path, file4))

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
df3 = pd.DataFrame(data3)
df4 = pd.DataFrame(data4)

# P_soczewka = 0.481 #W moc za pierwszą soczewką
P0 = 0.5 #W moc lasera

P_wsp = 0.962
P_ref = P0 * P_wsp #W moc padająca na próbkę

#straty
# P_bez_probki = 0.44 #W moc tracona na przejściu przez drugą soczewkę i szkiełko
# P_wsp2 = 0.91476
P2 = df4['Power [W]']
P2_wsp = P2/P_ref

P_strat = 1 + (1 - P2_wsp) #czynnik strat (czyli ile więcej transmitancji ostatecznie jest)

# P1_1 = df1['Power [W]']/P_ref *P_strat * 100
# P1_2 = df2['Power [W]']/P_ref * P_strat * 100
# P1_3 = df3['Power [W]']/P_ref * P_strat * 100
P1_1 = df1['Power [W]']/P_ref * 100
P1_2 = df2['Power [W]']/P_ref * 100
P1_3 = df3['Power [W]']/P_ref * 100
P2 = df4['Power [W]']/P_ref * 100
# P2 = P2 / P_ref *100

z1 = df1['Position [mm]']

'''PLOT'''

plt.plot(z1, P1_1, color='darkorange', label = 'Punkt 1')
plt.plot(z1, P1_2, color='red', label = 'Punkt 2')
plt.plot(z1, P1_3, color='green', label = 'Punkt 3')
plt.plot(z1, P2, color='blue', label = 'Szkło')
plt.xlabel('Pozycja [mm]')
# plt.ylabel('Moc [W]')
plt.ylabel('Transmitancja [%]')
# plt.ylabel("Intensywność [arb. units]")
plt.xlim(0,13)
plt.legend()
plt.grid(linestyle='--')
# plt.savefig(os.path.join(save_path, file_save))
plt.show()