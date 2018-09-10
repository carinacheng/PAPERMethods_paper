#! /usr/bin/env python

import numpy as n
import pylab as p

"""
Error bars are errors of each PS half added in quadrature 
(equivalent script: ~/capo/ctc/code/plot_jackknives_v2.py)
"""

# New jackknives (differencing of 2 PS)
file_lst_diff = n.load('plot_jackknives_lst.npz')
file_lst_1 = n.load('plot_jackknives_lst1.npz')
file_lst_2 = n.load('plot_jackknives_lst2.npz')
file_bls_diff = n.load('plot_jackknives_bls.npz')
file_bls_1 = n.load('plot_jackknives_bls1.npz')
file_bls_2 = n.load('plot_jackknives_bls2.npz')
file_eo_diff = n.load('plot_jackknives_evenodd.npz')
file_eo_1 = n.load('plot_jackknives_eo1.npz')
file_eo_2 = n.load('plot_jackknives_eo2.npz')

# Mask for masking out inner horizon points
mask = n.ones_like(file_lst_diff['kpl'])
mask[9:12] = 0
mask = n.ma.masked_where(mask==0, mask)

# Horizon limit
horizon = 0.06272882578029243 # computed using hera_pspec.conversions.Cosmo_Conversions.tau_to_kpara

# Plot range
ymin=-1e9
ymax=1e9

#------------------------

# LST null test
noise_lst = n.sqrt(12126854.2805**2 + 26470884.0693**2) # 1-sigma noise added in quadrature (the noise differs for lst_1 and lst_2)
p.figure()
p.errorbar(file_lst_diff['kpl']*mask,file_lst_diff['pIv_old']*mask,n.sqrt(file_lst_1['pIv_err_old']**2 + file_lst_2['pIv_err_old']**2)*2*mask,linestyle='',marker='.',color='k',linewidth=2)#,label='LST Null Test')
#p.errorbar(file_lst_1['kpl']-0.005,file_lst_1['pIv_old'],file_lst_1['pIv_err_old']*2,linestyle='',marker='.',color='k',label='LST1')
#p.errorbar(file_lst_2['kpl']+0.005,file_lst_2['pIv_old'],file_lst_2['pIv_err_old']*2,linestyle='',marker='.',color='0.5',label='LST2')
p.axvline(x=horizon,color='k',linestyle='--')
p.axvline(x=-horizon,color='k',linestyle='--')
p.axhline(0,color='k',linestyle='--')
p.axhspan(-noise_lst*2,noise_lst*2,facecolor='0.5',edgecolor="none",alpha=0.5,label='Estimated $2\sigma$ Error')
#p.legend(numpoints=1,prop={'size':16})
p.ylabel('$P(k)$ [mK$^{2}$($h^{-1}$ Mpc)$^{3}$]',fontsize=18)
p.xlabel('$k_{\\parallel}$ [$h$ Mpc$^{-1}$]',fontsize=18)
p.tick_params(axis='both', which='major', labelsize=16)
p.ylim(ymin,ymax)
p.grid()
p.title('Null Test: LST',fontsize=18)

# Baselines null test
noise_bl = n.sqrt(2*28839565.8058**2) # 1-sigma noise added in quadrature (sqrt(x^2 + x^2)) where the noise is the same for each half
p.figure()
p.errorbar(file_bls_diff['kpl']*mask,file_bls_diff['pIv_old']*mask,n.sqrt(file_bls_1['pIv_err_old']**2 + file_bls_2['pIv_err_old']**2)*2*mask,linestyle='',marker='.',color='k',linewidth=2)#,label='Baselines Null Test')
#p.errorbar(file_bls_1['kpl']-0.005,file_bls_1['pIv_old'],file_bls_1['pIv_err_old']*2,linestyle='',marker='.',color='k',label='BL1')
#p.errorbar(file_bls_2['kpl']+0.005,file_bls_2['pIv_old'],file_bls_2['pIv_err_old']*2,linestyle='',marker='.',color='0.5',label='BL2')
p.axvline(x=horizon,color='k',linestyle='--')
p.axvline(x=-horizon,color='k',linestyle='--')
p.axhline(0,color='k',linestyle='--')
p.axhspan(-noise_bl*2,noise_bl*2,facecolor='0.5',edgecolor="none",alpha=0.5,label='Estimated $2\sigma$ Error')
#p.legend(numpoints=1,prop={'size':16})
p.ylabel('$P(k)$ [mK$^{2}$($h^{-1}$ Mpc)$^{3}$]',fontsize=18)
p.xlabel('$k_{\\parallel}$ [$h$ Mpc$^{-1}$]',fontsize=18)
p.tick_params(axis='both', which='major', labelsize=16)
p.ylim(ymin,ymax)
p.grid()
p.title('Null Test: Baselines',fontsize=18)

# Even/Odd null test
noise_eo = n.sqrt(2*(14419782.9029*2)**2) # sensitivity of usual even/odd multiplied by 2, since now we're only doing one quadrant of the grid instead of 2
p.figure()
p.errorbar(file_eo_diff['kpl']*mask,file_eo_diff['pIv_old']*mask,n.sqrt(file_eo_1['pIv_err_old']**2 + file_eo_2['pIv_err_old']**2)*2*mask,linestyle='',marker='.',color='k',linewidth=2)#,label='Even/Odd Null Test')
#p.errorbar(file_eo_1['kpl']-0.005,file_eo_1['pIv_old'],file_eo_1['pIv_err_old']*2,linestyle='',marker='.',color='k',label='Even')
#p.errorbar(file_eo_2['kpl']+0.005,file_eo_2['pIv_old'],file_eo_2['pIv_err_old']*2,linestyle='',marker='.',color='0.5',label='Odd')
p.axvline(x=horizon,color='k',linestyle='--')
p.axvline(x=-horizon,color='k',linestyle='--')
p.axhline(0,color='k',linestyle='--')
p.axhspan(-noise_eo*2,noise_eo*2,facecolor='0.5',edgecolor="none",alpha=0.5,label='Estimated $2\sigma$ Error')
#p.legend(numpoints=1,prop={'size':16})
p.ylabel('$P(k)$ [mK$^{2}$($h^{-1}$ Mpc)$^{3}$]',fontsize=18)
p.xlabel('$k_{\\parallel}$ [$h$ Mpc$^{-1}$]',fontsize=18)
p.tick_params(axis='both', which='major', labelsize=16)
p.ylim(ymin,ymax)
#p.yscale('symlog',linthreshy=1e7)
p.grid()
p.title('Null Test: Even/Odd',fontsize=18)

p.show()

