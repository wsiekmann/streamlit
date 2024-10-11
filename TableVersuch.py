import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridUpdateMode
from st_aggrid.grid_options_builder import GridOptionsBuilder
#import base64, M2Crypto
#import uuid, OpenSSL
import secrets
import datetime as dt


st.set_page_config(layout="wide")
st.markdown(
    r"""
    <style>
    .st-emotion-cache-1wbqy5l.e17vllj40 {
            visibility: hidden;
        }
    .eyeqlp53.st-emotion-cache-1pbsqtx.ex0cdmw0 {
            visibility: hidden;
        }
    </style>
    """, unsafe_allow_html=True
)

def make_token():
    """
    Creates a cryptographically-secure, URL-safe string
    """
    return secrets.token_urlsafe(16) 

# def generate_session_id(num_bytes = 16):
#     return base64.b64encode(M2Crypto.m2.rand_bytes(num_bytes))

#st.session_state

if 'sessiontoken' not in st.session_state:
    st.session_state.sessiontoken = ""
    

a: list 
if st.session_state.sessiontoken == "":
    st.session_state.sessiontoken  = make_token() #uuid.UUID(bytes = OpenSSL.rand.bytes(16))       
    print("[" + dt.datetime.now().strftime("%d.%m.%Y %H:%M:%S") + "] sessionstart -- " + st.session_state.sessiontoken )
a = st.columns(3)    
a[2].write("sessiontoken: " + st.session_state.sessiontoken)



#st.dialog()
@st.dialog("Cast your vote")
def vote(item):
    st.write(f"Why is {item} your favorite?")
    reason = st.text_input("Because...")
    if st.button("speichern..."):
        st.session_state.vote = {"item": item, "reason": reason}
        st.rerun()

if "vote" not in st.session_state:
    st.write("Vote for your favorite")
    if st.button("A"):
        vote("A")
    if st.button("B"):
        vote("B")
else:
    f"You voted for {st.session_state.vote['item']} because {st.session_state.vote['reason']}"


#@st.cache_resource
def data_upload():
    df = pd.read_csv("CBP2022.CB2200CBP-2024-10-11T073901.csv")
    return df

st.header("Streamlit")
df = data_upload()
st.dataframe(data=df)
st.info(len(df))

def slider_change():
    print(_sliderValue)
    
def radio_change():
    print (_funct)

_funct =st.sidebar.radio(label="Test",options=["1","2"],horizontal=True,on_change=radio_change)
_sliderValue = st.sidebar.slider(label="Testslider",max_value=100, value= 50, help="Help",on_change=slider_change)


# if _funct == "1":
#     print (_funct)

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


