import streamlit as st
import time
import sqlite3

st.set_page_config(layout="wide",page_icon=":tangerine:")
#global conn
#global cursor


def openConnection() -> any:
    conn = sqlite3.connect('form.db',check_same_thread=False)
    cursor = conn.cursor()
    return conn,cursor


conn,cursor = openConnection()
print (conn, cursor)

@st.dialog("WE-Arbeit")
def formCreation():
    st.write('Bitte ausfüllen')
    with st.form(key= "Reg Form",clear_on_submit=True):
        surname = st.text_input("Vorname: ")
        lastname = st.text_input("Nachname: ")
        age = st.date_input("Alter: ",format="DD.MM.YYYY")
        country = st.text_input("Land: ")
        birthcountry = st.text_input("Geburtsland: ")
        submit = st.form_submit_button(label = "Übernahme")
        
        if submit == True:
            st.toast("Übernommen")
            addinfo(surname,lastname,age,country,birthcountry)
            
    cclose = st.button("Connection Close")        
    if cclose == True:
        st.toast("Connection close") 
        closeConnection()  
            
def addinfo(a,b,c,d,e):
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS "testformreg" (SURENAME TEXT(50),LASTNAME TEXT(50),AGE TEXT(10),COUNTRY TEXT(50),BIRTHCOUNTRY TEXT(50))"""
    )
    cursor.execute("INSERT INTO testformreg VALUES (?,?,?,?,?) ", (a,b,c,d,e))
    conn.commit()
    #conn.close()
    st.toast('in SQLITE DB gesichert',icon='😍')
    
    
def getinfo() -> list:
    cursor.execute(
    """SELECT * FROM testformreg"""
    )
    data = cursor.fetchall()
    return data

def closeConnection():
    conn.close()
    st.toast("Connection close") 
    
    
    
if st.button("WE-Arbeit eintragen"):
    #openConnection()
    formCreation()
st.dataframe(getinfo())
closeConnection()

