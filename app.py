import streamlit as st

from database import create_tables
from auth import signup, login
from expense import (
    expense_page,
    income_page,
    view_expenses,
    income_history
)
from dashboard import dashboard
from styles import load_css

create_tables()

st.set_page_config(
    page_title="Expense Tracker Pro",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_css()

if "user" not in st.session_state:
    st.session_state.user = None

########################################

if st.session_state.user is None:

    st.title("💰 Expense Tracker Pro")

    menu = st.sidebar.selectbox(
        "Menu",
        ["Login", "Signup"]
    )

    if menu == "Signup":

        st.header("Create Account")

        username = st.text_input("Username")

        email = st.text_input("Email")

        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Sign Up"):

            if signup(
                username,
                email,
                password
            ):

                st.success("Account Created!")

            else:

                st.error("User already exists.")

    else:

        st.header("Login")

        email = st.text_input("Email")

        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Login"):

            user = login(
                email,
                password
            )

            if user:

                st.session_state.user = user

                st.rerun()

            else:

                st.error("Invalid Login")

########################################

else:

    st.sidebar.title("Navigation")

    page = st.sidebar.selectbox(
    "📂 Navigation",
    [
        "📊 Dashboard",
        "💰 Income",
        "➕ Add Expense",
        "📋 Expense History",
        "💵 Income History"
    ]
)

    st.sidebar.write("---")

    if st.sidebar.button("Logout"):

        st.session_state.user = None

        st.rerun()

    ################################

    if page == "📊 Dashboard":
        dashboard(st.session_state.user)

    elif page == "💰 Income":

        income_page(st.session_state.user)

    elif page == "➕ Add Expense":

        expense_page(st.session_state.user)

    elif page == "📋 Expense History":

        view_expenses(st.session_state.user)

    elif page == "💵 Income History":

        income_history(st.session_state.user)