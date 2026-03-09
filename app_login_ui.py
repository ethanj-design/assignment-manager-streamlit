import streamlit as st
import datetime
import json
from pathlib import Path
import time
import uuid

st.set_page_config(
    page_title="Course Manager",
    page_icon="",
    layout="centered",
    initial_sidebar_state="collapsed"
)

json_file = Path("users.json")

if json_file.exists:
    with json_file.open("r", encoding= "utf-8") as f:
        users = json.load(f)

tab1, tab2 = st.tabs(["Login", "Register"])

with tab1:
    with st.container(border=True):
        st.markdown(f"### Login")
        user_email = st.text_input("Email",placeholder="Enter your email address.")
        user_password = st.text_input("Password",placeholder="Enter your password.",type="password")
        btn_login = btn_save = st.button("Login", disabled=False)

        if btn_login:
            user_found = False
            password_found = False
            with st.spinner("Veriying"):
                time.sleep(1)
                if not user_email or not user_password:
                    st.warning("Enter Username or Password")
                else:
                    for user in users:
                        if user_email == user["email"]:
                            user_found = True
                            if user_password == user["password"]:
                                password_found = True
                                break
                    if user_found == True and password_found == True:
                        st.success("Welcome Back!")     
                    else:
                        st.error("Invalid email or password.")
    st.dataframe(users)

with tab2:
    st.markdown(f"### Create Account")
    new_email = st.text_input("Email",placeholder="Enter email address.",width=400,key="new_email")
    first_last = st.text_input("First and Last Name",placeholder="Enter your first and last name.",width=400,key="first_last")
    new_password = st.text_input("Password",placeholder="Enter password.",type="password",width=400,key="new_pw")
    st.selectbox("What is your role?",["Instructor"],width=400)
    btn_create = btn_save = st.button("Create Account",width=400, disabled=False,key="create_acct")



