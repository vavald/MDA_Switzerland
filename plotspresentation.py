#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install streamlit_jupyter


# In[2]:


import pandas as pd
import numpy as np
import folium
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time

from streamlit_jupyter import StreamlitPatcher, tqdm


# In[13]:


sp = StreamlitPatcher()
sp.jupyter()  # register patcher with streamlit


# In[40]:


noise = pd.read_csv('final_noise_data.csv')


# In[6]:


model =  pd.read_csv('model_input.csv', sep=';', index_col=0)


# In[41]:


noise.head()


# In[36]:


print(noise.info())


# In[9]:


model.head()


# In[25]:


print(model.info())


# In[10]:


model.day_week.unique()


# In[11]:


model.month .unique()


# ### Plots Model data
# 
# 

# In[14]:


import plotly.express as px


# In[52]:


# |exporti

st.markdown(
    """
    The scatter plot 'Noise level of average cars per day in one month' shows us the noise level produced by
    the average cars per day. 
    The colors represent the noise levels with its correspondent value. 
    Higher level of noise tends to have a yellow color.
    
    For example, in the 14th day we can see a noise level of 73.56 dB with a averge of autos of 80. 
    However it is important to note that higher average of autos does not imply higher noise level 
    we can see for example in the 14th day that a noise level of  80,20dB is obtained when the average autos is 41,69.
"""
)


# In[23]:


px.scatter(model, x="day_month", y="avg_cars", animation_frame="day_month", animation_group="lcpeak_avg",
           color="lcpeak_avg", hover_name="lcpeak_avg",
           size_max=55, range_x=[-2,33], range_y=[-2,100],
          title=" Noise level of average cars per day in one month")


# In[49]:


# |exporti

st.markdown(
    """
    In the scatter plot 'Noise level per month', we see the noise levels per month in one year.
    The colors respresent the noise levels whit its correspondent value. 
    Higher level of noise tends to have a yellow color.
    
    For example,the months with highest level of noise are :
    July  with noise value 93.04dB 
    February with noise level 91.4 dB
    January with noise level 90.48 dB. 
    
"""
)


# In[33]:



px.scatter(model, x="month", y="lcpeak_avg", animation_frame="month", animation_group="lcpeak_avg",
         color="lcpeak_avg", hover_name="lcpeak_avg",range_y=[50,100],
            range_x=[0,13],title=" Noise level per month" )


# In[56]:


# |exporti

st.markdown(
    """
    The scatter plot 'Noise level per day every 10 minutes' shows us the behavior of the noise level every day of the week
    at the same time in intervals of 10 minutes.
    The colors represent the noise levels with its correspondent value. 
    Higher level of noise tends to have a yellow color.
    
    For example:
    
    Monday at 8:20 has the highest noise level of the week with a value of 99.63 dB.
    Tuesday at 9:50 has the highest noise level of the week with a value of 109.68 dB.
    
    Friday at 15:40 the noise level starts to be higher than 99 dB
    
    Sunday at 10:10 has a nose level of approximately 103 dB.
    
    At 7:50, we can see that every day has a noise level higher than 90 dB. So we can assume this hour as a "critical point"
    where we can find "noise contamination"
    
    
"""
)


# In[47]:


px.scatter(noise, x="day_week", y="lcpeak", animation_frame="10_min_interval_start_time", animation_group="lcpeak",
           color="lcpeak", hover_name="lcpeak",
           size_max=55, range_x=[-1,8], range_y=[50,110],
          title=" Noise level per day every 10 minutes")


# In[ ]:





# In[ ]:




