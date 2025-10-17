import streamlit as st
import sqlite3
import pandas as pd

## LIST OF FUNCTIONS ##
def create_table():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER ' \
        'PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT, age INTEGER)')
    conn.commit()
    conn.close()

def add_user(name, email, age):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('INSERT INTO users(name, email, age) ' \
              'VALUES (?, ?, ?)', (name, email, age))
    conn.commit()
    conn.close()

def view_users(): 
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users')
    data = c.fetchall()
    conn.close()
    return data

def delete_user(user_id):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('DELETE FROM users WHERE id=?', (user_id,))
    conn.commit()
    conn.close()

####

def main():
    st.title("SQL and Python Implementation using Streamlit")
    st.sidebar.title("SQL and Python Implementation using Streamlit")
    st.markdown("Submitted by: Berida, Ronabelle D.S.")
    st.sidebar.markdown("Created in October 10, 2025")

    create_table()

    menu = ["Add User", "View Users", "Delete User"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Add User":
        st.subheader("Add New User")
        name = st.text_input("Name")
        email = st.text_input("Email")
        age = st.number_input("Age", 0, 120)
    
    if st.button("Submit"):
        add_user(name, email, age)
        st.success(f"{name} added successfully!")

    elif choice == "View Users":
        st.subheader("View All Users")
        users = view_users()
        df = pd.DataFrame(users, columns=["ID", "Name", "Email", "Age"])
        st.dataframe(df)

    elif choice == "Delete User":
        st.subheader("Delete User")
        st.subheader("Delete a User")
        users = view_users()
        df = pd.DataFrame(users, columns=["ID", "Name", "Email", "Age"])
        st.dataframe(df)
        user_id = st.number_input("Enter ID to delete", 1)
        if st.button("Delete"):
            delete_user(user_id)
            st.warning(f"User {user_id} deleted!")



if __name__ == '__main__':
    main()

