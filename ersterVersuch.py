import streamlit as st
import time

st.markdown(
    r"""
    <style>
    .stBaseButton-header {
            visibility: hidden;
        }
    </style>
    """, unsafe_allow_html=True
)
#i : int = 0
def butClick(i):
    print("click " + str(i)) 
c: list      
c = st.columns(10)
#c1,c2,c3,c4,c5,c6,c7,c8,c9,c10 = st.columns(10)
for i in range(10):
    #i = i + 1
    btn = c[i].button(label="Test",key="button" + str(i),on_click=butClick(i))
    c[i].image("2024-08-20 08.30.27.jpg",caption="Test",width=20)
    
val = st.time_input("set")   
print(val) 
    
bar = st.progress(0)
for i in range(10):
    bar.progress((i +1) *10)
    time.sleep(1.5)
