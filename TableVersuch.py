import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder


#@st.cache_resource
def data_upload():
    df = pd.read_csv("test.csv")
    return df

st.header("Streamlit")
df = data_upload()
st.dataframe(data=df)
st.info(len(df))

st.header("AgGrid")
gd = GridOptionsBuilder.from_dataframe(df)
gd.configure_pagination(enabled=True)
gd.configure_default_column(editable=True,groupable=True)

sel_mode = st.radio('Selection Type', options= ['single','multiple'])
gd.configure_selection(selection_mode=sel_mode, use_checkbox=True)
gridoptions = gd.build()
AgGrid(df,gridOptions=gridoptions)

