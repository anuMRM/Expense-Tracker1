import streamlit as st
import pandas as pd

from database import (
    add_expense,
    add_income,
    get_expenses,
    get_income,
    delete_expense
)


CATEGORIES = [
    "🍔 Food",
    "🚗 Travel",
    "🛒 Shopping",
    "🏠 Rent",
    "💡 Bills",
    "🎬 Entertainment",
    "🏥 Medical",
    "📚 Education",
    "💼 Business",
    "📦 Others"
]


##############################################

def income_page(user):

    st.subheader("💰 Add Income")

    amount = st.number_input(
        "Income Amount",
        min_value=0.0,
        step=100.0
    )

    date = st.date_input("Date")

    if st.button("Add Income"):

        if amount <= 0:

            st.warning("Enter valid amount")

        else:

            add_income(
                user["id"],
                amount,
                str(date)
            )

            st.success("Income Added Successfully!")

            st.rerun()


##############################################

def expense_page(user):

    st.subheader("➕ Add Expense")

    title = st.text_input("Expense Title")

    amount = st.number_input(
        "Amount",
        min_value=0.0,
        step=10.0
    )

    category = st.selectbox(
        "Category",
        CATEGORIES
    )

    date = st.date_input(
        "Expense Date"
    )

    notes = st.text_area(
        "Notes"
    )

    if st.button("Save Expense"):

        if title == "" or amount <= 0:

            st.warning("Fill all required fields.")

        else:

            add_expense(

                user["id"],

                title,

                amount,

                category,

                str(date),

                notes

            )

            st.success(
                "Expense Added!"
            )

            st.balloons()

            st.rerun()


##############################################

def view_expenses(user):

    st.subheader("📋 Expense History")

    rows = get_expenses(user["id"])

    if len(rows) == 0:

        st.info("No expenses yet.")

        return

    df = pd.DataFrame(rows)

    search = st.text_input(
        "🔍 Search Expense"
    )

    if search:

        df = df[
            df["title"]
            .str.contains(
                search,
                case=False
            )
        ]

    category = st.selectbox(

        "Filter Category",

        ["All"] + CATEGORIES

    )

    if category != "All":

        df = df[
            df["category"] == category
        ]

    st.dataframe(

        df,

        use_container_width=True,

        hide_index=True

    )

    st.divider()

    st.subheader("Delete Expense")

    expense_ids = df["id"].tolist()

    if expense_ids:

        expense = st.selectbox(

            "Select Expense ID",

            expense_ids

        )

        if st.button("Delete"):

            delete_expense(expense)

            st.success(

                "Expense Deleted"

            )

            st.rerun()


##############################################

def income_history(user):

    st.subheader("Income History")

    rows = get_income(user["id"])

    if len(rows) == 0:

        st.info("No Income Records")

        return

    df = pd.DataFrame(rows)

    st.dataframe(

        df,

        use_container_width=True,

        hide_index=True

    )