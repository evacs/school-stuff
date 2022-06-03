#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas 
import matplotlib.pyplot as plt
from matplotlib import rcParams

get_ipython().run_line_magic('matplotlib', 'inline')
data = pandas.read_csv('Downloads\data_pm.csv')

#print(data.keys())
print(len(data)) # number of stars

##gaiaedr3.gaia_source.pm > gaiaedr3.gaia_source.parallax


# # 3a-Gaia Query

# SELECT TOP 500 
# gaia_source.source_id,gaia_source.ra,gaia_source.dec,gaia_source.parallax,gaia_source.parallax_error,gaia_source.pm,
# gaia_source.phot_g_mean_flux,gaia_source.phot_g_mean_flux_error,gaia_source.phot_g_mean_mag,gaia_source.bp_rp,
# gaia_source.dr2_radial_velocity,gaia_source.dr2_radial_velocity_error
# 
# FROM gaiaedr3.gaia_source 
# 
# WHERE (gaiaedr3.gaia_source.parallax>=100 AND gaiaedr3.gaia_source.pm>=100 AND gaiaedr3.gaia_source.phot_g_mean_mag<=10)

# In[2]:


#map for funsies
fig, ax = plt.subplots()
ax.scatter(data['ra'], data['dec'], marker = '.', s=2)
ax.set_xlabel('RA [deg]')
ax.set_ylabel('Dec [deg]')
ax.set_aspect(1)#change
plt.show()


# # 3b Histogram with all data

# In[3]:


#mask my data
high_sn_m = data['phot_g_mean_flux'] / data['phot_g_mean_flux_error'] > 5
high_sn_pm = abs(data['dr2_radial_velocity'] / data['dr2_radial_velocity_error']) > 5

#create masked array with total velocity 
sp_v = 4.74*data['pm'][high_sn_pm][high_sn_m]/data['parallax'][high_sn_pm][high_sn_m]
#v_total = np.sqrt( sp_v ** 2 + raidal_velocity ** 2 ) ## getting 3d motion

fig, ax = plt.subplots()
n, bins, patches = ax.hist(sp_v, bins=20)
ax.set_xlabel('Total Velocity [Km/s]')
ax.set_ylabel('Star Counts')
ax.set_title('Count/Total Velocity Distribution')
plt.show()
                          
print(len(sp_v)) #shows how many stars remain after masking


# In[4]:


max_v = sp_v.max()  #find max velocity in masked array

print(max_v)


# In[5]:


np.where(sp_v==max_v) #find index of max value in masked array


# In[6]:


sp_v.iloc[[34]] #find index in original data array


# In[7]:


data.iloc[[69]] #print all data from this index


# In[8]:


tv = 4.74*7061.731/109.02964 #to check that my index was correct
print(tv)


# # 3c-Fast Star ID

# In[9]:


print("Fastest star's velocity: ", max_v)
print("Fastest star's source ID: ", data['source_id'][69])


# In[ ]:




