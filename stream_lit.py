# Imports
import streamlit as st
st.__version__
import pandas as pd
# pd.__version__

import seaborn as sns
sns.__version__

# Streamlit app
st.balloons()

st.title('Hello Wilders, welcome to my application!')

st.write("I enjoy to discover stremalit possibilities")

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/weather2019.csv"
df_weather = pd.read_csv(link)
st.write(df_weather)


# Here we use "magic commands":
# df_weather

# To display graphics, streamlit includes some graphics. So you can use these native graphics, by adding to your script :

st.line_chart(df_weather['MAX_TEMPERATURE_C'])


# To display a seaborn graph, or matplotlib, you can use the dedicated function st.pyplot.
# First you create a variable that will contain your graph. 
# Then, instead of using the traditional plt.show(), 
# you should use st.pyplot() by specifying the name of your variable followed by the figure attribute.


viz_correlation = sns.heatmap(df_weather.corr(), 
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True)
								)

st.pyplot(viz_correlation.figure)



#####

name = st.text_input("Please give me your name:")
name_length = len(name)
st.write("Your name has ",name_length, "characters")




# $ pipreqs /Users/celestedaleo/Desktop/streamLit



# To run the app type the following in the terminal:
# streamlit run stream_lit.py






'''
from azureml.core import Workspace, Experiment, ScriptRunConfig

# get workspace
ws = Workspace.from_config()

# get compute target
target = ws.compute_targets['target-name']

# get registered environment
env = ws.environments['env-name']

# get/create experiment
exp = Experiment(ws, 'experiment_name')

# set up script run configuration
config = ScriptRunConfig(
    source_directory='.',
    script='script.py',
    compute_target=target,
    environment=env,
    arguments=['--meaning', 42],
)

# submit script to AML
run = exp.submit(config)
print(run.get_portal_url()) # link to ml.azure.com
run.wait_for_completion(show_output=True)
'''