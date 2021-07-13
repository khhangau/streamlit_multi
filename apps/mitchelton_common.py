import streamlit as st
from multiapp import MultiApp
import pandas as pd
import base64
from apps import common

def app():
    common.app('Mitchelton AL',\
               "BCC_Meta.out",\
               '#####START_HYDROGRAPHS_CTC_01_00000',\
               '#####END_HYDROGRAPHS_CTC_01_00000',\
               'CTC_01_00000',\
               "interp_CTC_01_00000.csv",\
               "g.csv",\
               "end_dt")
