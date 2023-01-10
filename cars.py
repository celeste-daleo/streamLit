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