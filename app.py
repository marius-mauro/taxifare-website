import streamlit as st
import datetime
import requests
import pandas as pd

st.set_page_config(
            page_title="TaxiFareModel front", # => Quick reference - Streamlit
            page_icon="🐍",
            layout="centered", # wide
            initial_sidebar_state="auto") # collapsed

'''
# TaxiFareModel
'''

# st.markdown('''
# Remember that there are several ways to output content into your web page...

# Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
# ''')

# '''
# ## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

# 1. Let's ask for:
# - date and time
# - pickup longitude
# - pickup latitude
# - dropoff longitude
# - dropoff latitude
# - passenger count
# '''


d = st.date_input(
    "Select date",
    datetime.date(2024, 5, 24))

t = st.time_input('Set time', datetime.time(8, 45))

# Combine date and time into a single datetime string
pickup_datetime = datetime.datetime.combine(d, t).strftime("%Y-%m-%d %H:%M:%S")

pickup_longitude = st.number_input('Insert pickup longitude')
pickup_latitude = st.number_input('Insert pickup latitude')
dropoff_longitude = st.number_input('Insert dropoff longitude')
dropoff_latitude = st.number_input('Insert dropoff latitude')

@st.cache_data
def get_select_box_data():

    return pd.DataFrame({
          'first column': list(range(1, 9)),
        })

df = get_select_box_data()

option = st.selectbox('Select the number of passengers', df['first column'])

# '''
# ## Once we have these, let's call our API in order to retrieve a prediction

# See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

# 🤔 How could we call our API ? Off course... The `requests` package 💡
# '''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

#     st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

# '''

# 2. Let's build a dictionary containing the parameters for our API...

# 3. Let's call our API using the `requests` package...

# 4. Let's retrieve the prediction from the **JSON** returned by the API...

# ## Finally, we can display the prediction to the user
# '''
    params = {'pickup_datetime': pickup_datetime, 'pickup_longitude': pickup_longitude, 'pickup_latitude': pickup_latitude, 'dropoff_longitude': dropoff_longitude, 'dropoff_latitude': dropoff_latitude,
            'passenger_count': int(option)}

    response = requests.get(url=url, params=params)
    response_json = response.json()

        # Display the response in the app
    st.write(response_json['fare'], unsafe_allow_html=True)
