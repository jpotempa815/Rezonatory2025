import csv
import os
import math
import pandas as pd
import seaborn as sns
import numpy as np
import os
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import optimize
from matplotlib.ticker import MultipleLocator
from collections import namedtuple
from scipy.interpolate import UnivariateSpline

'''FITTING FUNCTIONS'''

def d4Sig(z,w0,m2,z0,lam=2300e-9):
	return np.sqrt(w0**2 + m2**2 * (lam/(np.pi*w0))**2 * (z-z0)**2)

def T_fit(F, T_ns, T_delt, F_sat):#, F_2):
	return T_ns - (1 - np.exp(-F/F_sat)) * T_delt/(F/F_sat)# - F/F_2
# T_ns - 

'''CALIBRATION DATA'''
save_path = r'C:\Users\gosc\Desktop\Rezonatory2025\Rezonatory2025\wyniki\wyniki_210825'
my_path = r'C:\Users\gosc\Desktop\Rezonatory2025\Rezonatory2025\pomiary\pomiary_140825'
# dotyczy pomiarow do 010825 do probki grafen_m1_4 -> wtedy nazwa kalibracja.txt
# my_path2 = r'C:\Users\gosc\Desktop\Rezonatory2025\Rezonatory2025\wyniki\wyniki_230725'
# dotyczy pomiarow od 010825 do probki grafen_m1_4 -> wtedy nazwa beam_profile.txt
my_path2 = r'C:\Users\gosc\Desktop\Rezonatory2025\Rezonatory2025\pomiary\pomiary_010825'
# filename_cal = os.path.join(my_path2, 'kalibracja.txt')
filename_cal = os.path.join(my_path2, 'beam_profile.txt')
# nazwa wykresu
file_save2 = 'grafen_b2_fluencja.png'


data_cal = np.array(np.genfromtxt(filename_cal))
z_cal = data_cal[:, 0]*1e-3
d_cal_X = data_cal[:, 1]*1e-6 #um -> m
d_cal_Y = data_cal[:, 2]*1e-6 #um -> m

#szukanie najmniejszej plamki
pola = np.pi * (d_cal_X / 2) * (d_cal_Y / 2)
idx_min = np.argmin(pola)
z_min = z_cal[idx_min]

'''GRAPH SHIFT'''

file_zscan = 'grafen_b2_probka_1_140825.csv'
file_surf = 'grafen_b2_szklo_140825.csv'
data = pd.read_csv(os.path.join(my_path, file_zscan))
data2 = pd.read_csv(os.path.join(my_path, file_surf))

df = pd.DataFrame(data)
df2 = pd.DataFrame(data2)
 
P1 = df['Power [W]']
P2 = df2['Power [W]']
z = df['Position [mm]']
z_sample = z * 1e-3  # mm -> m

# P_soczewka = 0.481 #W moc za pierwszą soczewką
P0 = 0.5 #W moc lasera
P_wsp = 0.962
P_ref = P0 * P_wsp #W moc padająca na próbkę
#straty

P_wsp2 = P2 / P_ref
P_strat = 1 + (1 - P_wsp2) #czynnik strat (czyli ile więcej transmitancji ostatecznie jest)
P1 = P1 * P_strat
T = P1/P_ref * 100

z_maxT = z_sample[np.argmax(T)]

z_shift = z_min - z_maxT

z_cal = z_cal - z_shift

'''FITTING'''

fitParams_X, fitCovariances_X = optimize.curve_fit(d4Sig, z_cal, d_cal_X, p0=(140e-6,1.2,0.0065), sigma=None)					# p0: initial guess for the parameters in SI units
fitParams_Y, fitCovariances_Y = optimize.curve_fit(d4Sig, z_cal, d_cal_Y, p0=(140e-6,1.2,0.0065), sigma=None)

# z0_X -> fitParams_X[2]
# w0_X -> fitParams_X[0]
# M2_X -> fitParams_X[1]

# z0_Y -> fitParams_Y[2]
# w0_Y -> fitParams_Y[0]
# M2_Y -> fitParams_Y[1]

plt.plot(z_cal*1e3, d4Sig(z_cal, fitParams_X[0], fitParams_X[1], fitParams_X[2])*1e6, color = 'orangered', label = 'Dopasowana funkcja')
plt.scatter(z_cal*1e3, d_cal_X*1e6, color = 'orange', label='Pomiar kalibracyjny')
file_save = 'fit.png'
plt.legend()
plt.ylabel(r"Szerokość wiązki [$\mu$m]")
plt.xlabel("Pozycja [mm]")
plt.legend()
plt.grid(ls='--')
# plt.savefig(os.path.join(my_path, file_save))
plt.show()

'''FLUENCE CALCULATION'''

new_d_X = d4Sig(z_sample, fitParams_X[0], fitParams_X[1], fitParams_X[2])
new_d_Y = d4Sig(z_sample, fitParams_Y[0], fitParams_Y[1], fitParams_Y[2])

rx = new_d_X/2*1e2 #cm
ry = new_d_Y/2*1e2 #cm
A_eff = np.pi * rx * ry #cm2

f_rep = 100 #MHz

E = P1/f_rep #uJ

F = E/A_eff #uJ/cm2

'''DOUBLE FLUENCE IS NO MORE'''
# indeks dla ktorego jest max T
maxT_index = np.argmax(T)

F_cut = F[:maxT_index]

T_cut = T[:maxT_index]


'''PLOT FITTING'''
# zgadywane parametry do lepszego dopasowania
T_ns_guess = 100 - max(T_cut)
T_delt_guess = max(T_cut) - min(T_cut)
T_sat_guess = 0.37*T_delt_guess 
# F_sat_guess = T_cut[np.argmin(np.abs(max(T_cut) - T_sat_guess))]
print(T_ns_guess)
print(T_delt_guess)
print(T_sat_guess)
# print(F_sat_guess)

fitParams_T, fitCovariances_T = optimize.curve_fit(T_fit, F_cut, T_cut, p0=[T_ns_guess, T_delt_guess, 10], sigma=None)
T_new = T_fit(F_cut, *fitParams_T)

'''PLOTTING'''

plt.figure(figsize=(10,8))
plt.plot(F_cut, T_cut, 'o', color='coral', linewidth=2, label='Dane eksperymentalne')
plt.plot(F_cut, T_new, '-', color='sandybrown', linewidth=2, label='Dopasowana krzywa')

plt.xlabel(r"Fluence $\left[\frac{ μ\text{J}}{\text{cm}^2}\right]$", fontsize=14)
plt.ylabel("Transmittance [%]", fontsize=14)

plt.xscale('log')
plt.grid(linestyle='--')
plt.legend()
plt.savefig(os.path.join(save_path, file_save2))
plt.show()

