#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st


# In[ ]:


st.markdown('''
<style>
.main{
background-color: #FFFFCC;
}
<style>
''',
unsafe_allow_html= True)


# In[ ]:


st.header('List of apps by Bhushan Borude')

st.markdown('* Predicting Penguin Species ([link](https://bhushan-b-borude-streamlit-project-03-pengu-penguins-app-z0wlcl.streamlit.app/))')
st.markdown('''
This project is about predicting Penguine species. 
The app takes user input either in the form of uploaded csv file or input from sliders.
Using the user input, the app predicts the penguin species.
I used random forest classifier to make predictions.''')

st.markdown('* Historical Stock Prices ([link](https://bhushan-b-borude-streamlit-project-02-stock-stocks-r0izr8.streamlit.app/))')
st.markdown('''
This app gets user input as company name, start and end dates.
It then uses it to create line graphs of stock closing prices and volume for the selected company.
It also calculates the percentage change in stock price for the selected period. 
I used 'yfinance' library to get the stock info of companies.''')

st.markdown('* Predicting Iris Flower Type ([link](https://bhushan-b-borude-streamlit-project-01-02-iris-ml-app-a3fuh9.streamlit.app/))')
st.markdown('''
In this project, I created an app which takes user input about iris flower and predicts the flower type.
The machine learning model used in prediction is random forest classifier.''')


# In[ ]:




