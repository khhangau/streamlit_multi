import streamlit as st
from multiapp import MultiApp
import apps
import apps_more
from PIL import Image
import sys
import pydeck as pdk
import pandas as pd

def pdk_func():
    df = pd.read_csv('r.csv')

    layer = pdk.Layer(
        "ScatterplotLayer",
        df,
        pickable=True,
        opacity=0.8,
        filled=True,
        radius_scale=2,
        radius_min_pixels=10,
        radius_max_pixels=500,
        line_width_min_pixels=0.01,
        get_position='[Longitude, Latitude]',
        get_fill_color=[255, 0, 0],
        get_line_color=[0, 0, 0],
    )
    
    # Set the viewport location
    view_state = pdk.ViewState(latitude=df['Latitude'].iloc[-1], longitude=df['Longitude'].iloc[-1], zoom=13, min_zoom= 10, max_zoom=30)
    
    # Render
    r = pdk.Deck(layers=[layer], map_style='mapbox://styles/mapbox/light-v9',
                 initial_view_state=view_state, tooltip={"html": "<b>Point ID: </b> {PointID} <br /> "
                                                                 "<b>Longitude: </b> {Longitude} <br /> "
                                                                 "<b>Latitude: </b>{Latitude} <br /> "
                                                                 "<b> Value: </b>{Value} <br /> "
                                                                 "<b>Number: </b>{Number} <br /> "
                                                                 "<b>Name: </b>{Name}"})
    r

app = MultiApp()

title = '<p style="font-family:sans-serif; color:Blue; font-size: 42px;">Rainfall-Runoff App</p>'
st.markdown(title, unsafe_allow_html=True)

st.markdown("""
This multi-page app is using the [streamlit-multiapps](https://github.com/upraneelnihar/streamlit-multiapps) framework developed by [Praneel Nihar](https://medium.com/@u.praneel.nihar).
# Real-Time Simulations

[//]: # ()
Go to [Historical results](http://it07916:8501/). *Contact:* """'<a href="mailto:kim.hang@moretonbay.qld.gov.au">Kim Hang</a>', unsafe_allow_html=True)

selection = st.sidebar.radio('Navigation:', ['Main','Summary','Rating','Map'])

if selection == 'Main':
    # Add all your application here
    for i in apps.__all__:
        __import__("apps." + i)
        app.add_app(i, sys.modules["apps."+i].app)
    # The main app
    app.run()
    st.sidebar.title('Main')
    st.sidebar.title('')
    st.sidebar.checkbox('Enable Alerts')
    st.sidebar.title('')
    with st.sidebar.form(key='form'):
        lp = st.slider('Lag Parameter:', min_value=1.5, max_value=1.7)
        il = st.select_slider('Initial Loss (mm):', options=[0,10,20])
        lr = st.select_slider('Loss Rate (mm/h):', options=[0,2.5,5])
        submit_button = st.form_submit_button(label='Submit')
    st.sidebar.write('lp=' + str(lp) + ', il=' + str(il) + ', lr=' + str(lr))
    with open('form.txt', 'w') as f:
        f.write('lp=' + str(lp) + ', il=' + str(il) + ', lr=' + str(lr))
elif selection == 'Summary':
    st.sidebar.title('Summary')
    st.sidebar.text('TBC')
    st.image(Image.open(r"Capture.JPG"))
elif selection == 'Rating':
    # Add all your application here
    for i in apps_more.__all__:
        __import__("apps_more." + i)
        app.add_app(i, sys.modules["apps_more."+i].app)
    # The main app
    app.run()
    st.sidebar.title('Rating')
else:
    st.sidebar.title('Map')
    pdk_func()
