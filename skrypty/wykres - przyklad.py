'''Imports and Functions'''
import csv
import os
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import optimize
from matplotlib.ticker import MultipleLocator
from collections import namedtuple

def d4Sig(z,w0,m2,z0,lam=2300e-9):
	return np.sqrt(w0**2 + m2**2 * (lam/(np.pi*w0))**2 * (z-z0)**2)

""" define global variables """

lam=2300e-9   																				#central wavelength

''' Pathnames'''
filename	=	r"c:\Users\gosc\Desktop\stolik\wyniki_230725\test.txt"

''' Import and rearrange data'''

data = np.array(np.genfromtxt(filename))
d4sig_sag = data[:, 1]/2 *1E-6																# Input need to be of form: Beam diameter (D4Sig, Second order moments)	[µm]
d4sig_tang = data[:, 2]/2 *1E-6																# Input need to be of form: Beam diameter (D4Sig, Second order moments)	[µm]
z = data[:, 0]*1E-3																			# Input need to be of form: Position of measurement	[mm]
z_plot=np.linspace(np.amin(z),np.amax(z),int(1e3))

werr = 1

yerr1 = [x*werr/100.0 for x in d4sig_sag]
yerr2 = [x*werr/100.00 for x in d4sig_tang]

''' Beam caustic fit '''
fitParams_sag, fitCovariances_sag = optimize.curve_fit(d4Sig, z, d4sig_sag, p0=(140e-6/2,1.2,0.0355), sigma=None)					# p0: initial guess for the parameters in SI units
fitParams_tang, fitCovariances_tang = optimize.curve_fit(d4Sig, z, d4sig_tang, p0=(140e-6/2,1.2,0.0355), sigma=None)

'''Parameters for data fitting'''

z0_sag = round(fitParams_sag[2]*1e2,4)
w0_sag = round(fitParams_sag[0]*1e6,4)
M2_sag = round(fitParams_sag[1],4)

z0_tang = round(fitParams_tang[2]*1e2,4)
w0_tang = round(fitParams_tang[0]*1e6,4)
M2_tang = round(fitParams_tang[1],4)

''' Print section '''

print("central wavelength = ", lam*1e9, "nm")
print("________________________________________________________")
print("z0_sag = ", z0_sag, "cm")
print("w0_sag = ", w0_sag, "um")
print("M2_sag = ", M2_sag)
print("________________________________________________________")
print("z0_tang = ", z0_tang, "cm")
print("w0_tang = ", w0_tang, "um")
print("M2_tang = ", M2_tang)

''' Plot section'''

#---General plot settings---#

fs		=	14
lw		=	1.5
mks 	= 	5 

#---Control Figure dimension---#

fig1 	= plt.figure(figsize= (26.3/2.54, 8/2.54),frameon=True)
ax1		= plt.subplot(1,1,1)

#---ax1	= beam caustic---#

plt1a	=	ax1.plot(z, d4sig_tang*1e6, ls = 'None', marker = 'o', color = '#009440', label = 'tangential', markersize=mks)
plt1b	=	ax1.plot(z_plot, d4Sig(z_plot, fitParams_tang[0], fitParams_tang[1], fitParams_tang[2])*1e6, color='#009440',linewidth=lw)#, label='fit')
plt1c	=	ax1.plot(z, d4sig_sag*1e6, ls = 'None', marker = 'o', color = '#000000', label = 'sagittal', markersize=mks)
plt1d	=	ax1.plot(z_plot,d4Sig(z_plot, fitParams_sag[0], fitParams_sag[1], fitParams_sag[2])*1e6, color='#000000',linewidth=lw)#, label ='fit')


ax1.set_xlim(np.amin(z_plot),np.amax(z_plot))
ax1.set_ylim(0.8*np.amin(d4sig_sag)*1e6, 1.1*np.amax(d4sig_sag)*1e6)
ax1.set_ylabel("Beam radius [µm]")
ax1.set_xlabel("Position z [m]")  
ax1.text(0.99*fitParams_sag[2], np.amax(d4sig_sag)*1e6, '$\mathregular{{M^{{2}}_{{tangentialY}}}}= {:.2f}$'.format(fitParams_tang[1]), verticalalignment='top', horizontalalignment='left', color='#009440',fontsize=fs)
ax1.text(0.99*fitParams_sag[2], 0.95*np.amax(d4sig_sag)*1e6, '\n$\mathregular{{M^{{2}}_{{sagittalX}}}}= {:.2f}$'.format(fitParams_sag[1]), verticalalignment='top', horizontalalignment='left', color='#000000',fontsize=fs)

#--- Save figure---# 

fig1.tight_layout(rect = (0, 0, 1, .92))

plt.savefig(filename + '_FitResult.png',dpi=1200)

plt.show()


