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
my_path = r'/workspaces/Rezonatory2025/!wyniki/290725_open_closed_aperture'
filename_cal = os.path.join(my_path, 'kalibracja.txt')
data_cal = np.array(np.genfromtxt(filename_cal))
z_cal = data_cal[:, 0]*1e-3
d_cal_X = data_cal[:, 1]*1e-6 #um -> m
d_cal_Y = data_cal[:, 2]*1e-6 #um -> m

zx_min = z_cal[np.argmin(d_cal_X)]
zy_min = z_cal[np.argmin(d_cal_Y)]
z_min = zx_min

'''GRAPH SHIFT'''

file_zscan = 'open_close_aperture_mwcnt1_290725.csv'
data = pd.read_csv(os.path.join(my_path, file_zscan))
df = pd.DataFrame(data)

P1_measured = df['Power1 [W]']
P2_measured = df['Power2 [W]']
z = df['Position [mm]']
z_sample = z * 1e-3  # mm -> m
# 230725
# P_ref = 0.484
# 290725
# P_ref = 0.456	#W
# 010825
P_ref = 0.522 #W

T1 = P1_measured / P_ref * 100 #transmitancja [%]
T2 = P2_measured / P_ref * 100

z1_maxT = z_sample[np.argmax(T1)]
z2_maxT = z_sample[np.argmax(T2)]

z1_shift = z_min - z1_maxT
z2_shift = z_min - z2_maxT

z1_cal = z_cal + z1_shift
z2_cal = z_cal + z2_shift

'''FITTING'''

fitParams_X1, fitCovariances_X1 = optimize.curve_fit(d4Sig, z1_cal, d_cal_X, p0=(140e-6,1.2,0.0355), sigma=None)					# p0: initial guess for the parameters in SI units
fitParams_Y1, fitCovariances_Y1 = optimize.curve_fit(d4Sig, z1_cal, d_cal_Y, p0=(140e-6,1.2,0.0355), sigma=None)

fitParams_X2, fitCovariances_X2 = optimize.curve_fit(d4Sig, z2_cal, d_cal_X, p0=(140e-6,1.2,0.0355), sigma=None)					# p0: initial guess for the parameters in SI units
fitParams_Y2, fitCovariances_Y2 = optimize.curve_fit(d4Sig, z2_cal, d_cal_Y, p0=(140e-6,1.2,0.0355), sigma=None)

# z0_X -> fitParams_X[2]
# w0_X -> fitParams_X[0]
# M2_X -> fitParams_X[1]

# z0_Y -> fitParams_Y[2]
# w0_Y -> fitParams_Y[0]
# M2_Y -> fitParams_Y[1]

plt.scatter(z_cal, d_cal_X)
plt.plot(z1_cal, d4Sig(z1_cal, fitParams_X1[0], fitParams_X1[1], fitParams_X1[2]), label='z1')
plt.plot(z2_cal, d4Sig(z2_cal, fitParams_X2[0], fitParams_X2[1], fitParams_X2[2]), label='z2')
file_save = 'fit.png'
plt.legend()
plt.savefig(os.path.join(my_path, file_save))
plt.show()

'''FLUENCE CALCULATION'''



new_d_X1 = d4Sig(z_sample, fitParams_X1[0], fitParams_X1[1], fitParams_X1[2])
new_d_Y1 = d4Sig(z_sample, fitParams_Y1[0], fitParams_Y1[1], fitParams_Y1[2])
new_d_X2 = d4Sig(z_sample, fitParams_X2[0], fitParams_X2[1], fitParams_X2[2])
new_d_Y2 = d4Sig(z_sample, fitParams_Y2[0], fitParams_Y2[1], fitParams_Y2[2])

rx1 = new_d_X1/2*1e2 #cm
ry1 = new_d_Y1/2*1e2 #cm
Ax1 = np.pi * rx1**2 #cm2
Ay1 = np.pi * ry1**2 #cm2

rx2 = new_d_X2/2*1e2 #cm
ry2 = new_d_Y2/2*1e2 #cm
Ax2 = np.pi * rx2**2 #cm2
Ay2 = np.pi * ry2**2 #cm2

f_rep = 100 #MHz

E1 = P1_measured/f_rep #uJ
E2 = P2_measured/f_rep #uJ

Fx1 = E1/Ax1 #uJ/cm2
Fy1 = E1/Ay1 #uJ/cm2
Fx2 = E2/Ax2 #uJ/cm2
Fy2 = E2/Ay2 #uJ/cm2

# '''PLOTTING'''

sns.set(style="whitegrid")

plt.figure(figsize=(10,8))
plt.plot(Fx1, T1, color='cornflowerblue', linewidth=2, label='Pomiar w osi X')
plt.plot(Fy1, T1, color='coral', linewidth=2, label='Pomiar w osi Y')
plt.plot(Fy2, T1, color='cornflowerblue', linewidth=2, label='Miernik 1')
plt.plot(Fx2, T2, color='coral', linewidth=2, label='Miernik 2')

plt.xlabel(r"Fluence $\left[\frac{ μ\text{J}}{\text{cm}^2}\right]$", fontsize=14)
plt.ylabel("Transmittance [%]", fontsize=14)

plt.grid(linestyle='--')
plt.legend()
file_save2 = 'transmittance_vs_fluence_plot1.png'
plt.savefig(os.path.join(my_path, file_save2))
plt.show()
