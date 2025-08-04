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

def d4Sig(z,w0,m2,z0,lam=2300e-9):
	return np.sqrt(w0**2 + m2**2 * (lam/(np.pi*w0))**2 * (z-z0)**2)

'''CALIBRATION DATA'''
my_path = r'C:\Users\gosc\Desktop\Rezonatory2025\Rezonatory2025\pomiary\pomiary_010825'
# dotyczy pomiarow do 010825 do probki grafen_m1_4 -> wtedy nazwa kalibracja.txt
# my_path2 = r'C:\Users\mkowa\Desktop\Julia\Rezonatory2025\wyniki\290725_open_closed_aperture'
# dotyczy pomiarow od 010825 do probki grafen_m1_4 -> wtedy nazwa beam_profile.txt
my_path2 = r'C:\Users\gosc\Desktop\Rezonatory2025\Rezonatory2025\pomiary\pomiary_010825'
filename_cal = os.path.join(my_path2, 'beam_profile.txt')
#katalo zapisu
save_path = r'C:\Users\gosc\Desktop\Rezonatory2025\Rezonatory2025\wyniki\010825'
# nazwa wykresu
file_save2 = 'power-meter_reference_010825_fluence.png'


data_cal = np.array(np.genfromtxt(filename_cal))
z_cal = data_cal[:, 0]*1e-3
d_cal_X = data_cal[:, 1]*1e-6 #um -> m
d_cal_Y = data_cal[:, 2]*1e-6 #um -> m

zx_min = z_cal[np.argmin(d_cal_X)]
zy_min = z_cal[np.argmin(d_cal_Y)]
z_min = zx_min

'''GRAPH SHIFT'''

file_zscan = 'power-meter_reference_010825.csv'
data = pd.read_csv(os.path.join(my_path, file_zscan))
df = pd.DataFrame(data)

P1 = df['Power1 [W]']
P2 = df['Power2 [W]']
z = df['Position [mm]']
z_sample = z * 1e-3  # mm -> m
P_ref = 0.0086 

T = P2 / P1 * P_ref * 100

z_maxT = z_sample[np.argmax(T)]

z_shift = z_min - z_maxT

z_cal = z_cal - z_shift

'''FITTING'''

fitParams_X, fitCovariances_X = optimize.curve_fit(d4Sig, z_cal, d_cal_X, p0=(140e-6,1.2,0.0355), sigma=None)					# p0: initial guess for the parameters in SI units
fitParams_Y, fitCovariances_Y = optimize.curve_fit(d4Sig, z_cal, d_cal_Y, p0=(140e-6,1.2,0.0355), sigma=None)

# z0_X -> fitParams_X[2]
# w0_X -> fitParams_X[0]
# M2_X -> fitParams_X[1]

# z0_Y -> fitParams_Y[2]
# w0_Y -> fitParams_Y[0]
# M2_Y -> fitParams_Y[1]

# plt.scatter(z_cal, d_cal_X)
# # plt.plot(z1_cal, d4Sig(z1_cal, fitParams_X1[0], fitParams_X1[1], fitParams_X1[2]), label='z1')
# # plt.plot(z2_cal, d4Sig(z2_cal, fitParams_X2[0], fitParams_X2[1], fitParams_X2[2]), label='z2')
# plt.plot(z_cal, d4Sig(z_cal, fitParams_X[0], fitParams_X[1], fitParams_X[2]))
# file_save = 'fit.png'
# plt.legend()
# plt.savefig(os.path.join(my_path, file_save))
# plt.show()

'''FLUENCE CALCULATION'''

new_d_X = d4Sig(z_sample, fitParams_X[0], fitParams_X[1], fitParams_X[2])
new_d_Y = d4Sig(z_sample, fitParams_Y[0], fitParams_Y[1], fitParams_Y[2])

rx = new_d_X/2*1e2 #cm
ry = new_d_Y/2*1e2 #cm
A_eff = np.pi * rx * ry #cm2

f_rep = 100 #MHz

E = P2/f_rep #uJ

F = E/A_eff #uJ/cm2

'''PLOTTING'''

plt.figure(figsize=(10,8))
plt.plot(F, T, color='coral', linewidth=2)

plt.xlabel(r"Fluence $\left[\frac{ μ\text{J}}{\text{cm}^2}\right]$", fontsize=14)
plt.ylabel("Transmittance [%]", fontsize=14)

plt.xscale('log')
plt.grid(linestyle='--')
plt.legend()
plt.savefig(os.path.join(save_path, file_save2))
plt.show()
