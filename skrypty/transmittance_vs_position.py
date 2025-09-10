import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# wpisz ścieżkę do katalogu z danymi
my_path = r'C:\Users\gosc\Desktop\Rezonatory2025\Rezonatory2025\pomiary\pomiary_130825'
file1 = r'2_grafen_m1_probka_130825.csv'
file2 = r'1_grafen_m1_szklo_130825.csv'

# nazwa katalogu zapisu
save_path = r'C:\Users\gosc\Desktop\Rezonatory2025\Rezonatory2025\wyniki\wyniki_080925'
# wpisz nazwę pliku do zapisu wykresus
file_save = r'grafen_m1_plot.png'

data1 = pd.read_csv(os.path.join(my_path, file1))
data2 = pd.read_csv(os.path.join(my_path, file2))

# zestawienie
grafen_m1 = ['1_grafen_m1_probka_130825.csv', '2_grafen_m1_probka_130825.csv', '3_grafen_m1_probka_130825.csv', '1_grafen_m1_szklo_130825.csv']
grafen_b2 = ['grafen_b2_probka_1_140825.csv', 'grafen_b2_probka_2_140825.csv', 'grafen_b2_szklo_140825.csv']
G_3L_D3863 = ['G_3L_D3863_1warstwa_2_180825.csv', 'G_3L_D3863_2warstwy_2_180825.csv', 'G_3L_D3863_szklo_180825.csv']
G_1030_BM_D4105 = ['G_1030_BM_D4105_1_180825.csv', 'G_1030_BM_D4105_2_180825.csv', 'G_1030_BM_D4105_3_180825.csv']
SixCarbon = ['SixCarbon_probka_1_180825.csv', 'SixCarbon_probka_2_180825.csv', 'SixCarbon_probka_3_180825.csv', 'SixCarbon_szklo_180825.csv']
G_2L_D3861 = ['G_2L_D3861_probka_3_200825.csv', 'G_2L_D3861_probka_4_200825.csv', 'G_2L_D3861_szklo_200825.csv']

# CNT
swcnt_sa_3_1 = ['swcnt_sa-3(1)_probka_180825.csv', 'swcnt_sa-3(1)_szklo_180825.csv']
swcnt_sa_3_2 = ['swcnt_sa-3(2)_1_140825.csv']
swcnt_sa_1_2 = ['swcnt_sa-1(2)_1_180825.csv']
swcnt_sa_2_1 = ['swcnt_sa-2(1)_1_180825.csv']
CNT_25nm = ['CNT_25nm_probka_2_190825.csv', 'CNT_25nm_szklo_190825.csv']
CNT_30nm = ['CNT_30nm_probka_1_190825.csv', 'CNT_30nm_szklo_190825.csv']
CNT_40nm = ['CNT_40nm_probka_1_190825.csv', 'CNT_40nm_szklo_190825.csv']
CNT_50nm = ['CNT_50nm_probka_1_190825.csv', 'CNT_50nm_szklo_190825.csv']
CNT_100nm = ['CNT_100nm_probka_1_190825.csv', 'CNT_100nm_szklo_190825.csv']
CNT_150nm = ['CNT_150nm_probka_1_190825.csv', 'CNT_150nm_szklo_190825.csv']
CNT_200nm = ['CNT_200nm_probka_2_190825.csv', 'CNT_200nm_szklo_190825.csv']
CNT_300nm = ['CNT_300nm_probka_1_200825.csv', 'CNT_300nm_szklo_200825.csv']
CNT_50nm_2 = ['CNT_1_1b_50nm_probka_1_200825.csv', 'CNT_100nm_szklo_190825.csv']


plt.figure(figsize=(10,8))

# #grafen
# data1 = pd.read_csv(os.path.join(my_path, grafen_b2[2]))
# data2 = pd.read_csv(os.path.join(my_path, grafen_b2[0]))
# data3 = pd.read_csv(os.path.join(my_path, grafen_m1[2]))
# data4 = pd.read_csv(os.path.join(my_path, grafen_m1[3]))
# data5 = pd.read_csv(os.path.join(my_path, G_3L_D3863[2]))
# data6 = pd.read_csv(os.path.join(my_path, G_3L_D3863[0]))
# data7 = pd.read_csv(os.path.join(my_path, G_3L_D3863[1]))
# data8 = pd.read_csv(os.path.join(my_path, G_1030_BM_D4105[1]))
# data9 = pd.read_csv(os.path.join(my_path, SixCarbon[0]))
# data10 = pd.read_csv(os.path.join(my_path, SixCarbon[3]))
# data11 = pd.read_csv(os.path.join(my_path, G_2L_D3861[0]))
# data12 = pd.read_csv(os.path.join(my_path, G_2L_D3861[1]))
# data13 = pd.read_csv(os.path.join(my_path, G_2L_D3861[2]))


#nanorurki
# data1 = pd.read_csv(os.path.join(my_path, swcnt_sa_3_1[0]))
# data2 = pd.read_csv(os.path.join(my_path, swcnt_sa_3_1[1]))
# data3 = pd.read_csv(os.path.join(my_path, swcnt_sa_3_2[0]))
# data4 = pd.read_csv(os.path.join(my_path, swcnt_sa_1_2[0]))
# data5 = pd.read_csv(os.path.join(my_path, swcnt_sa_2_1[0]))
# data6 = pd.read_csv(os.path.join(my_path, CNT_25nm[0]))
# data7 = pd.read_csv(os.path.join(my_path, CNT_25nm[1]))
# data8 = pd.read_csv(os.path.join(my_path, CNT_30nm[0]))
# data9 = pd.read_csv(os.path.join(my_path, CNT_30nm[1]))
# data10 = pd.read_csv(os.path.join(my_path, CNT_40nm[0]))
# data11 = pd.read_csv(os.path.join(my_path, CNT_40nm[1]))
# data12 = pd.read_csv(os.path.join(my_path, CNT_50nm[0]))
# data13 = pd.read_csv(os.path.join(my_path, CNT_50nm[1]))
# data14 = pd.read_csv(os.path.join(my_path, CNT_100nm[0]))
# data15 = pd.read_csv(os.path.join(my_path, CNT_100nm[1]))
# data16 = pd.read_csv(os.path.join(my_path, CNT_150nm[0]))
# data17 = pd.read_csv(os.path.join(my_path, CNT_150nm[1]))
# data18 = pd.read_csv(os.path.join(my_path, CNT_200nm[0]))
# data19 = pd.read_csv(os.path.join(my_path, CNT_200nm[1]))
# data20 = pd.read_csv(os.path.join(my_path, CNT_300nm[0]))
# data21 = pd.read_csv(os.path.join(my_path, CNT_300nm[1]))
# data22 = pd.read_csv(os.path.join(my_path, CNT_50nm_2[0]))

# data2 = pd.read_csv(os.path.join(my_path, file2))
# data3 = pd.read_csv(os.path.join(my_path, file3))
# data4 = pd.read_csv(os.path.join(my_path, file4))
# data5 = pd.read_csv(os.path.join(my_path, file5))

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
# df3 = pd.DataFrame(data3)
# df3 = pd.DataFrame(data3)
# df4 = pd.DataFrame(data4)
# df5 = pd.DataFrame(data5)
# df6 = pd.DataFrame(data6)
# df7 = pd.DataFrame(data7)
# df8 = pd.DataFrame(data8)
# df9 = pd.DataFrame(data9)
# df10 = pd.DataFrame(data10)
# df11 = pd.DataFrame(data11)
# df12 = pd.DataFrame(data12)
# df13 = pd.DataFrame(data13)
# df14 = pd.DataFrame(data14)
# df15 = pd.DataFrame(data15)
# df16 = pd.DataFrame(data16)
# df17 = pd.DataFrame(data17)
# df18 = pd.DataFrame(data18)
# df19 = pd.DataFrame(data19)
# df20 = pd.DataFrame(data20)
# df21 = pd.DataFrame(data21)
# df22 = pd.DataFrame(data22)

# P_soczewka = 0.481 #W moc za pierwszą soczewką
P0 = 0.5 #W moc lasera

P_wsp = 0.962
P_ref = P0 * P_wsp #W moc padająca na próbkę

#straty
# P_bez_probki = 0.44 #W moc tracona na przejściu przez drugą soczewkę i szkiełko
# P_wsp2 = 0.91476

P2 = df2['Power [W]']
P2_wsp = P2/P_ref
# #grafen
# P2_grafen_m1 = df4['Power [W]']
# P2_grafen_b2 = df1['Power [W]']
# P2_G_3L = df5['Power [W]']
# P2_SixCarbon = df10['Power [W]']
# P2_G_2L = df13['Power [W]']
# P2_wsp_grafen_m1 = P2_grafen_m1/P_ref
# P2_wsp_grafen_b2 = P2_grafen_b2/P_ref
# P2_wsp_G_3L = P2_G_3L/P_ref
# P2_wsp_SixCarbon = P2_SixCarbon/P_ref
# P2_wsp_G_2L = P2_G_2L/P_ref
# #nanorurki
# P2_wsp_swcnt_sa_3_1 = df2['Power [W]']/P_ref
# P2_wsp_CNT_25nm = df7['Power [W]']/P_ref
# P2_wsp_CNT_30nm = df9['Power [W]']/P_ref
# P2_wsp_CNT_40nm = df11['Power [W]']/P_ref
# P2_wsp_CNT_50nm = df13['Power [W]']/P_ref
# P2_wsp_CNT_100nm = df15['Power [W]']/P_ref
# P2_wsp_CNT_150nm = df17['Power [W]']/P_ref
# P2_wsp_CNT_200nm = df19['Power [W]']/P_ref
# P2_wsp_CNT_300nm = df21['Power [W]']/P_ref

# czynnik strat 
P_strat = 1 + (1 - P2_wsp)
#grafen
# P_strat_grafen_m1 = 1 + (1 - P2_wsp_grafen_m1) 
# P_strat_grafen_b2 = 1 + (1 - P2_wsp_grafen_b2) 
# P_strat_G_3L = 1 + (1 - P2_wsp_G_3L)
# P_strat_SixCarbon = 1 + (1 - P2_wsp_SixCarbon)
# P_strat_G_2L = 1 + (1 - P2_wsp_G_2L)
#nanorurki
# P_strat_swcnt_sa_3_1 = 1 + (1 - P2_wsp_swcnt_sa_3_1)
# P_strat_CNT_25nm = 1 + (1 - P2_wsp_CNT_25nm)
# P_strat_CNT_30nm = 1 + (1 - P2_wsp_CNT_30nm)
# P_strat_CNT_40nm = 1 + (1 - P2_wsp_CNT_40nm)
# P_strat_CNT_50nm = 1 + (1 - P2_wsp_CNT_50nm)
# P_strat_CNT_100nm = 1 + (1 - P2_wsp_CNT_100nm)
# P_strat_CNT_150nm = 1 + (1 - P2_wsp_CNT_150nm)
# P_strat_CNT_200nm = 1 + (1 - P2_wsp_CNT_200nm)
# P_strat_CNT_300nm = 1 + (1 - P2_wsp_CNT_300nm)

P1_1 = df1['Power [W]']/P_ref * P_strat * 100
# P1_2 = df2['Power [W]']/P_ref * P_strat * 100
# P1_3 = df3['Power [W]']/P_ref * P_strat * 100
# P1_4 = df4['Power [W]']/P_ref * P_strat * 100
# #grafen
# P1_grafen_m1 = df3['Power [W]']/P_ref * P_strat_grafen_m1 * 100
# P1_grafen_b2 = df2['Power [W]']/P_ref * P_strat_grafen_b2 * 100
# P1_G_3L_1 = df6['Power [W]']/P_ref * P_strat_G_3L * 100
# P1_G_3L_2 = df7['Power [W]']/P_ref * P_strat_G_3L * 100
# P1_G_1030_BM = df8['Power [W]']/P_ref * P_strat_G_3L * 100
# P1_SixCarbon = df9['Power [W]']/P_ref * P_strat_SixCarbon * 100
# P1_G_2L_1 = df11['Power [W]']/ P_ref * P_strat_G_2L * 100
# P1_G_2L_2 = df12['Power [W]']/P_ref * P_strat_G_2L*100
# #nanorurki
# P1_swcnt_sa_3_1 = df1['Power [W]']/P_ref * P_strat_swcnt_sa_3_1 * 100
# P1_swcnt_sa_3_2 = df3['Power [W]']/P_ref * P_strat_swcnt_sa_3_1 * 100
# P1_swcnt_sa_1_2 = df4['Power [W]']/P_ref * P_strat_swcnt_sa_3_1 * 100
# P1_swcnt_sa_2_1 = df5['Power [W]']/P_ref * P_strat_swcnt_sa_3_1 * 100
# P1_CNT_25nm = df6['Power [W]']/P_ref * P_strat_CNT_25nm * 100
# P1_CNT_30nm = df8['Power [W]']/P_ref * P_strat_CNT_30nm * 100
# P1_CNT_40nm = df10['Power [W]']/P_ref * P_strat_CNT_40nm * 100
# P1_CNT_50nm = df12['Power [W]']/P_ref * P_strat_CNT_50nm * 100
# P1_CNT_100nm = df14['Power [W]']/P_ref * P_strat_CNT_100nm * 100
# P1_CNT_150nm = df16['Power [W]']/P_ref * P_strat_CNT_150nm * 100
# P1_CNT_200nm = df18['Power [W]']/P_ref * P_strat_CNT_200nm * 100
# P1_CNT_300nm = df20['Power [W]']/P_ref * P_strat_CNT_300nm * 100
# P1_CNT_50nm_2 = df22['Power [W]']/P_ref * P_strat_CNT_100nm *100

# P1_1 = df1['Power2 [W]']/P_ref * 100
# P1_2 = df2['Power2 [W]']/P_ref * 100
# P1_3 = df3['Power2 [W]']/P_ref * 100
# P1_4 = df4['Power2 [W]']/P_ref * 100
# P1_5 = df5['Power2 [W]']/P_ref * 100
# P2 = df3['Power [W]']/P_ref * 100

# z = df3['Position [mm]']
z1 = df1['Position [mm]']

'''PLOT'''

# #grafen
# plt.plot(z, P1_grafen_m1, color='darkorange', label = 'graphene m1 KAIST', linewidth=3)
# plt.plot(z1, P1_grafen_b2, color='blue', label = 'grafen b2 KAIST', linewidth=3)
# plt.plot(z1, P1_G_3L_1, color='red', label = 'G_3L: 1 layer', linewidth=3)
# plt.plot(z1, P1_G_3L_2, color='green', label = 'G_3L: 2 layers', linewidth=3)
# plt.plot(z1, P1_G_1030_BM, color='purple', label = 'G_1030_BM', linewidth=3)
# plt.plot(z1, P1_SixCarbon, color='brown', label = 'SixCarbon', linewidth=3)
# plt.plot(z1, P1_G_2L_1, color='magenta', label='G_2L: 1 layer', linewidth=3)
# plt.plot(z1, P1_G_2L_2, color='cyan', label='G_2L: 2 layers', linewidth=3)
#nanorurki
# plt.plot(z1, P1_swcnt_sa_3_1, color='darkorange', label = 'swcnt_sa-3(1)', linewidth=3)
# plt.plot(z1, P1_swcnt_sa_3_2, color='blue', label = 'swcnt_sa-3(2)', linewidth=3)
# plt.plot(z1, P1_swcnt_sa_1_2, color='red', label = 'swcnt_sa-1(2)', linewidth=3)
# plt.plot(z1, P1_swcnt_sa_2_1, color='green', label = 'swcnt_sa-2(1)', linewidth=3)
# plt.plot(z1, P1_CNT_25nm, color='purple', label = 'CNT 25nm', linewidth=3)
# plt.plot(z1, P1_CNT_30nm, color='brown', label = 'CNT 30nm', linewidth=3)
# plt.plot(z1, P1_CNT_40nm, color='pink', label = 'CNT 40nm', linewidth=3)
# plt.plot(z1, P1_CNT_50nm, color='cyan', label = 'CNT 50nm', linewidth=3)
# plt.plot(z1, P1_CNT_100nm, color='magenta', label = 'CNT 100nm', linewidth=3)
# plt.plot(z1, P1_CNT_150nm, color='gray', label = 'CNT 150nm', linewidth=3)
# plt.plot(z1, P1_CNT_200nm, color='olive', label = 'CNT 200nm', linewidth=3)
# plt.plot(z1, P1_CNT_300nm, color='teal', label = 'CNT 300nm', linewidth=3)
# plt.plot(z1, P1_CNT_50nm_2, color='chocolate', label='CNT 50nm (different source)', linewidth=3)

plt.plot(z1, P1_1, color='darkorange', label = 'Measurement 2')#, linewidth=3)
# plt.plot(z1, P1_2, color='chocolate', label = 'Measurement 3', linewidth=3)
# plt.plot(z1, P1_3, color='olive', label = 'Measurement 8', linewidth=3)
# plt.plot(z1, P1_4, color='forestgreen', label = 'Measurement 12', linewidth=3)
# plt.plot(z1, P1_5, color='teal', label = 'Measurement 16', linewidth=3)
# plt.plot(z1, P2, color='brown', label = 'Raw data: glass', linewidth=3)
# plt.plot(z1, P1, color='olive', label='Raw data: sample', linewidth=3)
plt.xlabel('Position [mm]', fontsize=20)
# plt.ylabel('Moc [W]')
plt.ylabel('Transmittance [%]', fontsize=20)
# plt.ylabel("Intensywność [arb. units]")
plt.xlim(0,13)
# plt.ylim(87,90)
# plt.legend(loc='upper left', fontsize =14)
# plt.legend(fontsize=20)
plt.grid(linestyle='--')
plt.savefig(os.path.join(save_path, file_save))
plt.show()