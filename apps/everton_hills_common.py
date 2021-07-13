import streamlit as st
from multiapp import MultiApp
import pandas as pd
import base64
from apps import common

def app():
    common.app('Everton Hills AL',\
               "BCC_Meta.out",\
               '#####START_HYDROGRAPHS_KED_01_00000',\
               '#####END_HYDROGRAPHS_KED_01_00000',\
               'KED_01_00000',\
               "interp_KED_01_00000.csv",\
               "g.csv",\
               "end_dt")
