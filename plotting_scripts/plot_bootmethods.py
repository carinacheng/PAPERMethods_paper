#! /usr/bin/env python

import numpy as n
import matplotlib.pyplot as plt

# Files to read
boot_bl = n.load('plot_bootmethods.npz')
boot_time = n.load('plot_bootmethods_time.npz')

noise = 2827408.41233 #4436767.36822 # XXX

# Plot
plt.plot(boot_bl['kpl'], boot_bl['pIn_err_old']*2, color='black', linewidth=2, label='Bootstrap baselines only')
plt.plot(boot_time['kpl'], boot_time['pIn_err_old']*2, color='0.5', linewidth=2, label='Bootstrap baselines and times')
plt.axhline(y=noise*2, color='green', linestyle='-', linewidth=2, label='Analytic')
plt.legend(numpoints=1,prop={'size':14},loc='best')
plt.grid()
plt.yscale('log')
#plt.title('2$\sigma$ errors for PAPER-64 using different bootstrapping methods')
plt.xlabel('$k_{\\parallel}$ [$h$ Mpc$^{-1}$]',fontsize=18)
plt.ylabel('$P(k)$ [mK$^{2}$($h^{-1}$ Mpc)$^{3}$]',fontsize=18)
plt.tick_params(axis='both', which='major', labelsize=14)
#plt.ylim(1e6,7e9) # for data
plt.ylim(5e5,1e8)
plt.show()


