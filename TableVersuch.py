import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridUpdateMode
from st_aggrid.grid_options_builder import GridOptionsBuilder

st.set_page_config(layout="wide")

#@st.cache_resource
def data_upload():
    df = pd.read_csv("CBP2022.CB2200CBP-2024-10-11T073901.csv")
    return df

st.header("Streamlit")
df = data_upload()
st.dataframe(data=df)
st.info(len(df))



_funct =st.sidebar.radio(label="Test",options=["1","2"])

if _funct == "1":
    print (_funct)

st.header("AgGrid")
gd = GridOptionsBuilder.from_dataframe(df)
gd.configure_pagination(enabled=True)
gd.configure_default_column(editable=True,groupable=True)

sel_mode = st.radio('Selection Type', options= ['single','multiple'])
gd.configure_selection(selection_mode=sel_mode, use_checkbox=True)
gridoptions = gd.build()
grid_table = AgGrid(
    df,gridOptions=gridoptions,reload_data = True,update_mode=GridUpdateMode.SELECTION_CHANGED,height=500,
    allow_unsafe_jscode=True,theme='streamlit'
    )

sel_rows = grid_table["selected_rows"]
st.subheader("selektierte Ausgabe:")
st.write(sel_rows)
