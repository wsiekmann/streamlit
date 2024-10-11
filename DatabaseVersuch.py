import streamlit as st
import time
import sqlite3

conn = sqlite3.connect('form.db',check_same_thread=False)
cursor = conn.cursor()

def formCreation():
    st.write('Bitte ausfüllen')
    with st.form(key= "Reg Form"):
        surname = st.text_input("Vorname: ")
        lastname = st.text_input("Nachname: ")
        age = st.date_input("Alter: ",format="DD.MM.YYYY")
        country = st.text_input("Land: ")
        birthcountry = st.text_input("Geburtsland: ")
        submit = st.form_submit_button(label = "Übernahme")
        
        if submit == True:
            st.success("Übernommen")
            addinfo(surname,lastname,age,country,birthcountry)
            
def addinfo(a,b,c,d,e):
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS "testformreg" (SURENAME TEXT(50),LASTNAME TEXT(50),AGE TEXT(10),COUNTRY TEXT(50),BIRTHCOUNTRY TEXT(50))"""
    )
    cursor.execute("INSERT INTO testformreg VALUES (?,?,?,?,?) ", (a,b,c,d,e))
    conn.commit()
    conn.close()
    st.success('in SQLITE DB gesichert')
    
formCreation()
