import streamlit as st
import sqlite3
import pandas as pd
import re

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

## Input Validation ##

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def is_valid_name(name):
    pattern = r'^[A-Za-z\s]+$'
    return re.match(pattern, name)

####

def main():
    st.title("SQL and Python Implementation using Streamlit")
    st.sidebar.title("SQL and Python Implementation using Streamlit")
    st.markdown("Submitted by: Berida, Ronabelle D.S.")
    st.sidebar.markdown("Created in October 10, 2025")
    st.markdown("This creates a database and view, add or delete a user's info depending "\
                "on what you've clicked. This implements the CRUD (Create, Read, Update, and "\
                "Delete) operations through the web interface")

    create_table()

    menu = ["Add User", "View Users", "Delete User"]
    choice = st.sidebar.selectbox("Click on what to perform", menu)

    df = pd.DataFrame(columns=["ID", "Name", "Email", "Age"])
    users = view_users()
    if users:
        df = pd.DataFrame(users, columns=["ID", "Name", "Email", "Age"])
        print("Database is empty. Please input some info.")

    row_count, col_count = df.shape

    if row_count == 0:
        print("Database is empty. Please input some info.")
    else:
        st.sidebar.write(f"**Rows:** {row_count}")
        st.sidebar.write(f"**Columns:** {col_count}")

    if choice == "Add User":
        st.subheader("Add New User")
        name = st.text_input("Name")
        email = st.text_input("Email")
        age = st.number_input("Age", 0, 120)
    
        if st.button("Submit"):
            if not is_valid_name(name):
                st.error("Wrong input for name. Please use letters only.")
            elif not is_valid_email(email):
                st.error("Invalid Email format. Please try again.")
            else:
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

        id_list = df["ID"].tolist()

        if len(id_list) > 0:
            min_id, max_id = min(id_list), max(id_list)
            user_id = st.number_input("Enter ID to delete", min_value=0)
        else:
            print("There's nothing to delete")

        if st.button("Delete"):
            delete_user(user_id)
            st.warning(f"User {user_id} deleted!")



if __name__ == '__main__':
    main()

