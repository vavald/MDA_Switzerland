#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import folium


# In[3]:


noise = pd.read_csv('final_noise_data.csv')


# In[4]:


weather = pd.read_csv('final_weather_data.csv')


# In[5]:


model =  pd.read_csv('model_input.csv', sep=';', index_col=0)


# In[6]:


TelraamCalva = pd.read_csv('Telraam_Calvariekapel.csv')


# In[7]:


weatherclean = pd.read_csv('Weather_cleaned.csv')


# In[8]:


noise.head()


# In[8]:


weather.head()


# In[9]:


model.head()


# In[85]:


print(model.info())


# In[10]:


model.day_week.unique()


# In[11]:


model.month .unique()


# ### Plots Model data
# 
# import seaborn as sns

# In[12]:


import plotly.express as px


# In[13]:


px.scatter(model, x="day_month", y="avg_cars", animation_frame="day_month", animation_group="lcpeak_avg",
           color="lcpeak_avg", hover_name="lcpeak_avg",
           size_max=55, range_x=[-5,40], range_y=[-5,100])


# In[15]:



px.scatter(model, x="month", y="lcpeak_avg", animation_frame="month", animation_group="lcpeak_avg",
         color="lcpeak_avg", hover_name="lcpeak_avg",
            range_x=[0,13])


# In[131]:


px.scatter(model, x="day_month", y="LC_WINDSPEED", animation_frame="month", animation_group="LC_WINDSPEED",
         color="LC_WINDSPEED", hover_name="LC_WINDSPEED",
            size_max=55, range_x=[0,13])


# In[132]:



fig = px.bar(model, x="month", y="avg_trucks", color="lcpeak_avg",
  animation_frame="month", animation_group="lcpeak_avg",range_x=[-10,15])
fig.show()


# In[125]:


px.scatter(model, x="LC_DWPTEMP", y="lcpeak_avg", animation_frame="month", animation_group="lcpeak_avg",
           color="lcpeak_avg", hover_name="lcpeak_avg",
           size_max=55, range_x=[-20,30], range_y=[25,90])


# In[119]:


fig = px.bar(model, x="LC_DWPTEMP", y="lcpeak_avg", color="lcpeak_avg",
  animation_frame="month", animation_group="LC_DWPTEMP", range_y=[0,137])
fig.show()


# In[ ]:


### bar chart que se mueve


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.animation import FuncAnimation

df = pd.read_csv('city_populations.csv',
				usecols=['name', 'group', 'year', 'value'])

colors = dict(zip(['India','Europe','Asia',
				'Latin America','Middle East',
				'North America','Africa'],
					['#adb0ff', '#ffb3ff', '#90d595',
					'#e48381', '#aafbff', '#f7bb5f',
					'#eafb50']))

group_lk = df.set_index('name')['group'].to_dict()

def draw_barchart(year):
	dff = df[df['year'].eq(year)].sort_values(by='value',
											ascending=True).tail(10)
	ax.clear()
	ax.barh(dff['name'], dff['value'],
			color=[colors[group_lk[x]] for x in dff['name']])
	dx = dff['value'].max() / 200
	
	for i, (value, name) in enumerate(zip(dff['value'],
										dff['name'])):
		ax.text(value-dx, i,	 name,		
				size=14, weight=600,
				ha='right', va='bottom')
		ax.text(value-dx, i-.25, group_lk[name],
				size=10, color='#444444',
				ha='right', va='baseline')
		ax.text(value+dx, i,	 f'{value:,.0f}',
				size=14, ha='left', va='center')
		
	# polished styles
	ax.text(1, 0.4, year, transform=ax.transAxes,
			color='#777777', size=46, ha='right',
			weight=800)
	ax.text(0, 1.06, 'Population (thousands)',
			transform=ax.transAxes, size=12,
			color='#777777')
	
	ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
	ax.xaxis.set_ticks_position('top')
	ax.tick_params(axis='x', colors='#777777', labelsize=12)
	ax.set_yticks([])
	ax.margins(0, 0.01)
	ax.grid(which='major', axis='x', linestyle='-')
	ax.set_axisbelow(True)
	ax.text(0, 1.12, 'The most populous cities in the world from 1500 to 2018',
			transform=ax.transAxes, size=24, weight=600, ha='left')
	
	ax.text(1, 0, 'by @pratapvardhan; credit @jburnmurdoch',
			transform=ax.transAxes, ha='right', color='#777777',
			bbox=dict(facecolor='white', alpha=0.8, edgecolor='white'))
	plt.box(False)
	plt.show()

fig, ax = plt.subplots(figsize=(15, 8))
animator = FuncAnimation(fig, draw_barchart,
						frames = range(1990, 2019))
plt.show()


# In[ ]:




