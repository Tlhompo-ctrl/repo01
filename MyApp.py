# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 00:49:42 2025

@author: Lenovo
"""

import streamlit as st
import plotly.express as px
import pandas as pd

st.title("Streamlit is amazing")
st.write("Hello, Streamlit!")

data = pd.DataFrame({"Categories": ['A','B','C','D'], "Values": [1,2,3,4]})

#Dispaly the data in the STreamlit App
st.write(data)

#Create a Plotly figure
fig = px.bar(data, x="Categories", y="Values", title="Bar Plot Example")

#Display the plot in the Streamlit App
st.plotly_chart(fig)


