import csv
import os
import math
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import optimize
from matplotlib.ticker import MultipleLocator
from collections import namedtuple

def d4Sig(z,w0,m2,z0,lam=2300e-9):
	return np.sqrt(w0**2 + m2**2 * (lam/(np.pi*w0))**2 * (z-z0)**2)

'''CALIBRATION DATA'''

filename_cal = r"c:\Users\gosc\Desktop\stolik\wyniki_230725\kalibracja.txt"
data_cal = np.array(np.genfromtxt(filename_cal))
z_cal = data_cal[:, 0]*1e-3
d_cal_X = data_cal[:, 1]*1e-6 #um -> m
d_cal_Y = data_cal[:, 2]*1e-6 #um -> m

zx_min = z_cal[np.argmin(d_cal_X)]
zy_min = z_cal[np.argmin(d_cal_Y)]
z_min = zx_min

'''GRAPH SHIFT'''

filename_zscan = r"c:\Users\gosc\Desktop\stolik\wyniki_230725\nanorurki_230725.txt"
data_zscan = np.array(np.genfromtxt(filename_zscan))
z_sample = data_zscan[:, 0] * 1e-3         # mm -> m
P_measured = data_zscan[:, 1]              # moc [W]
P_ref = 0.484	#W

T_measured = P_measured / P_ref * 100 #transmitancja [%]

z_maxT = z_sample[np.argmax(T_measured)]

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

plt.scatter(z_cal, d_cal_X)
plt.plot(z_cal, d4Sig(z_cal, fitParams_X[0], fitParams_X[1], fitParams_X[2]))
plt.savefig("fitowanie.png")
plt.show()

'''FLUENCE CALCULATION'''



new_d_X = d4Sig(z_sample, fitParams_X[0], fitParams_X[1], fitParams_X[2])
new_d_Y = d4Sig(z_sample, fitParams_Y[0], fitParams_Y[1], fitParams_Y[2])

rx = new_d_X/2*1e2 #cm
ry = new_d_Y/2*1e2 #cm
Ax = np.pi * rx**2 #cm2
Ay = np.pi * ry**2 #cm2

f_rep = 100 #MHz

E = P_measured/f_rep #uJ

Fx = E/Ax #uJ/cm2
Fy = E/Ay #uJ/cm2

'''PLOTTING'''

sns.set(style="whitegrid")

plt.figure(figsize=(10,8))
plt.plot(Fx, T_measured, color='cornflowerblue', linewidth=2, label='Pomiar w osi X')
plt.plot(Fy, T_measured, color='coral', linewidth=2, label='Pomiar w osi Y')

plt.xlabel(r"Fluence $\left[\frac{ μ\text{J}}{\text{cm}^2}\right]$", fontsize=14)
plt.ylabel("Transmittance [%]", fontsize=14)

plt.grid(linestyle='--')
plt.legend()
plt.show()
