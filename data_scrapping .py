#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd 
import numpy as np  
import  requests as rq 
from bs4 import BeautifulSoup 

url = 'https://www.worldometers.info/coronavirus' 
html_content = rq.get(url).text 
soup=BeautifulSoup(html_content , "html.parser")  
table = soup.find('table',attrs={'id':"main_table_countries_today"})
table_data = table.find_all("tr")  
data_list=[]
for rows in table_data :  
  data_list.append(rows.text.strip().split('\n')[1:5]) 

df= pd.DataFrame(data_list[9:]  , columns=data_list[0])   
df.to_csv("covid.csv")  

df

df_plot = df[["Country,Other"  , "TotalCases"]]  

df_plot["TotalCases"] = df_plot["TotalCases"].apply(lambda x : x.replace(',' , '' ))
df_plot["TotalCases"] = pd.to_numeric(df_plot["TotalCases"])   
df_plot['TotalCases'] = pd.to_numeric(df_plot['TotalCases'])  
df.dropna() 
df_plot[:20].plot(kind="bar" , x =	'Country,Other' , y='TotalCases' )

