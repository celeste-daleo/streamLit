# Imports
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib as plt
import numpy as np


#  Data
link = 'https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv'
cars =  pd.read_csv(link)

# Format continent column
cars['continent'] = cars['continent'].str.strip().replace('.', '')
cars['continent'] = cars['continent'].str.replace('.', '')


# Selectors
butons = cars['continent'].unique()
selected_country = st.selectbox("Select please", butons)

cars_selected = cars[cars['continent'] == selected_country]

# Heatmap
viz_heatmap = sns.heatmap(cars_selected.corr())
st.pyplot(viz_heatmap.figure)

# Distribution plot
viz_distribution = sns.displot(cars_selected, x="mpg")
st.pyplot(viz_distribution.figure)




# To run the app type the following in the terminal:
# streamlit run cars.py

'''
import streamlit as st 
import pandas as pd

data = {'name':['Tom', 'nick', 'krish', 'jack'],
        'nickname':['jack','krish','karim','joe'],
        'age':[20, 18, 19, 18]}
 
df = pd.DataFrame(data)
df_result_search = pd.DataFrame() 


searchcheckbox_name_nickname = st.checkbox("Name or Nickname ",value = False,key=1)
searchcheckbox_age = st.checkbox("age",value = False,key=2)

if searchcheckbox_name_nickname:
    name_search = st.text_input("name")
    nickname_search = st.text_input("nickname")
if searchcheckbox_age:   
    age_search = st.number_input("age",min_value=0)
if st.button("search"):
    if not searchcheckbox_name_nickname or not searchcheckbox_age:
        st.error('Please enter both name **and** age.')
    else:
        df_result_search = df[df['name'].str.contains(name_search,case=False, na=False)]
        df_result_search = df[df['nickname'].str.contains(nickname_search,case=False, na=False)]
        
        df_result_search = df[df['age']==(age_search)]
                        
        st.write("{} Records ".format(str(df_result_search.shape[0])))
        st.dataframe(df_result_search)

'''