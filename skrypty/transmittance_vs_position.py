import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# wpisz ścieżkę do katalogu z danymi
my_path = r'C:\Users\mkowa\Desktop\Julia\Rezonatory2025\pomiary\pomiary_120825'
# wpisz nazwę pliku
file = r'6_probka_120825.csv'
file2 = r'6_szklo_120825.csv' 
# file3 = r'7_krawedz_120825.csv'
# file4 = r'fin_4_110825.csv'
# nazwa katalogu zapisu
save_path = r'C:\Users\mkowa\Desktop\Julia\Rezonatory2025\wyniki\wyniki_120825'
# wpisz nazwę pliku do zapisu wykresus
file_save = r'6_merge_120825_plot.png'

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
data1 = pd.read_csv(os.path.join(my_path, file2))
# data2 = pd.read_csv(os.path.join(my_path, file3))
# data3 = pd.read_csv(os.path.join(my_path, file4))
df = pd.DataFrame(data)
df1 = pd.DataFrame(data1)
# df2 = pd.DataFrame(data2)
# df3 = pd.DataFrame(data3)
# P_soczewka = 0.481 #W moc za pierwszą soczewką
P0 = 0.5 #W moc lasera
# P0 = 0.383 #W
# P01 = 0.384 #z filtrem
# P02 = 0.405
P0 = 0.412
P_wsp = 0.962
P_ref = P0 * P_wsp #W moc padająca na próbkę
# P_ref1 = P01 * P_wsp #W moc padająca na próbkę
# P_ref2 = P02 * P_wsp #W moc padająca na próbkę
#straty
P_bez_probki = 0.44 #W moc tracona na przejściu przez drugą soczewkę i szkiełko
P_wsp2 = 0.91476
P_strat = 1 + (1 - P_wsp2) #czynnik strat (czyli ile więcej transmitancji ostatecznie jest)

# P1 = df['Power [W]']/P_ref * P_strat * 100
# P2 = df1['Power [W]']/P_ref*100
P1 = df['Power [W]']/P_ref * 100
P2 = df1['Power [W]']/P_ref * 100
# P1 = P1 - P2
# P3 = df2['Power [W]']/P_ref*100
# P4 = df3['Power [W]']/P_ref*P_strat*100

z1 = df['Position [mm]']
z2 = df1['Position [mm]']
# z3 = df2['Position [mm]']
# z4 = df3['Position [mm]']

'''PLOT'''

plt.plot(z1, P1, color='darkorange', label = 'Próbka')
plt.plot(z2, P2, color='blue', label = 'Szkło')
# plt.plot(z3, P3, color='green', label = 'Krawedz')
# plt.plot(z4, P4, color='red', label = '30 minut naświetlania')
plt.xlabel('Pozycja [mm]')
# plt.ylabel('Moc [W]')
plt.ylabel('Transmitancja [%]')
# plt.ylabel("Intensywność [arb. units]")
plt.xlim(0,13)
plt.legend()
plt.grid(linestyle='--')
plt.savefig(os.path.join(save_path, file_save))
plt.show()