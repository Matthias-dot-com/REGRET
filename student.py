import streamlit as st
import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('students.db')

# Create a cursor object
cur = conn.cursor()

# Create table
cur.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,\n
    name TEXT NOT NULL,\n
    email TEXT NOT NULL,\n
    age INTEGER NOT NULL
)
''')

# Commit changes and close the connection
conn.commit()
conn.close()

# Function to insert data into SQLite database
def insert_data(name, email, age):
    conn = sqlite3.connect('students.db')
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO students (name, email, age) VALUES (?, ?, ?)
    ''', (name, email, age))
    conn.commit()
    conn.close()

# Streamlit app
st.title("Student Registration Form")

# Create a form
with st.form(key='student_form'):
    name = st.text_input("Name")
    email = st.text_input("Email")
    age = st.number_input("Age", min_value=1, max_value=100)
    submit_button = st.form_submit_button(label='Submit')

# Handle form submission
if submit_button:
    if name and email and age:
        insert_data(name, email, age)
        st.success("Data submitted successfully!")
    else:
        st.error("Please fill all the fields.")


st.text_area("Write something intresting about yourself in 500 words")

st.number_input("Select your age : ",18,100)
st.time_input("Select the time slot : ")
st.date_input("What date should be it : ")