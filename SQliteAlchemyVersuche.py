import streamlit as st
import sqlite3

# Create the SQL connection to pets_db as specified in your secrets file.
conn = st.connection('pets_db', type='sql')

# Insert some data with conn.session.
with conn.session as s:
    s.execute('CREATE TABLE IF NOT EXISTS pet_owners (person TEXT, pet TEXT);')
    s.execute('DELETE FROM pet_owners;')
    pet_owners = {'jerry': 'fish', 'barbara': 'cat', 'alex': 'puppy'}
    for k in pet_owners:
        s.execute(
            'INSERT INTO pet_owners (person, pet) VALUES (:owner, :pet);',
            params=dict(owner=k, pet=pet_owners[k])
        )
    s.commit()

# Query and display the data you inserted
sqlQuery:str = str('SELECT * FROM pet_owners') #'select * from pet_owners'
pet_owners = conn.query(sql=sqlQuery)
#st.dataframe(pet_owners)