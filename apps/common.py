import streamlit as st
from multiapp import MultiApp
import pandas as pd
import base64

def app(site, file, start, end, code, interpfile, gfile, end_dt):
    st.write("""
    ## WBNM Stream Levels and Discharges Dashboard

    Shown are the stream **Levels** and **Discharges** of 

    """)

    st.markdown(
        f'***{site}***'
    )

    interpDf = pd.read_csv(interpfile)
    gDf = pd.read_csv(gfile)

    skiprows = 0
    #get line number of phrase in file
    lookup = start
    with open(file) as metaFile:
        for num, line in enumerate(metaFile, 1):
            if lookup in line:
                skiprows = num

    nrows = 0
    #get line number of phrase in file
    lookup = end
    with open(file) as metaFile:
        for num, line in enumerate(metaFile, 1):
            if lookup in line:
                nrows = num

    df_wbnm = pd.read_csv(file,delimiter=r"\s+",skiprows=skiprows,nrows=nrows-skiprows-2)
    df_wbnm.Time = pd.to_numeric(df_wbnm.Time)
    df_wbnm.Time = df_wbnm.Time.div(1440)
    with open(end_dt) as f:
        df_wbnm.Time += float(f.read())
    df_wbnm.Time = pd.to_datetime(df_wbnm.Time, unit='d')
    qDf = pd.concat([df_wbnm.Time, df_wbnm.Qout_OS, interpDf.Q_interp], axis=1, keys=['Time', 'Q (C)', 'Q (R&I)'])
    qDf.set_index('Time', inplace=True)

    data_q = base64.b64encode(qDf.to_csv().encode()).decode()

    hDf = pd.concat([df_wbnm.Time, interpDf.H_interp, gDf[code]], axis=1, keys=['Time', 'H (C&I)', 'H (R)'])
    hDf.set_index('Time', inplace=True)

    data_h = base64.b64encode(hDf.to_csv().encode()).decode()

    runfile = file.replace('_Meta.out', '.wbn')
    with open(runfile) as f:
        run = f.read()
    runcode = base64.b64encode(run.encode()).decode()
    st.markdown(
        f'<a href="data:file/csv;base64,{runcode}" download="run.wbn">Download Run File</a>',
        unsafe_allow_html=True
    )

    rDf = pd.concat([df_wbnm.Time, df_wbnm.Rain], axis=1, keys=['Time', 'Rain'])
    rDf.set_index('Time', inplace=True)

    data_r = base64.b64encode(rDf.to_csv().encode()).decode()

    st.write("""
    ## WBNM Levels
    """)
    st.line_chart(hDf)
    st.markdown(
        f'<a href="data:file/csv;base64,{data_h}" download="hdata.csv">Download Data</a>',
        unsafe_allow_html=True
    )
    st.write("""
    ## WBNM Discharges
    """)
    st.area_chart(qDf)
    st.markdown(
        f'<a href="data:file/csv;base64,{data_q}" download="qdata.csv">Download Data</a>',
        unsafe_allow_html=True
    )
    st.write("""
    ## Rainfall
    """)
    st.bar_chart(rDf)
    st.markdown(
        f'<a href="data:file/csv;base64,{data_r}" download="rdata.csv">Download Data</a>',
        unsafe_allow_html=True
    )
