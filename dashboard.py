import streamlit as st
import pandas as pd
import plotly.express as px

from database import (
    get_income,
    get_expenses,
    total_income,
    total_expense
)
st.write("")
st.write("")

def dashboard(user):

    st.markdown("""
# 👋 Welcome Back

Track your finances in one place.
""")

    income = total_income(user["id"])
    expense = total_expense(user["id"])
    balance = income - expense

    c1, c2, c3 = st.columns(3)

    c1,c2,c3=st.columns(3)

    with c1:
        st.markdown(f"""
    <div class="metric-card">

    <div class="metric-title">

    💰 Income

    </div>

    <div class="metric-value">

     ₹{income:,.0f}

    </div>

    </div>
    """,unsafe_allow_html=True)

    with c2:

       st.markdown(f"""
    <div class="metric-card">

    <div class="metric-title">

    💸 Expenses

    </div>

    <div class="metric-value">

    ₹{expense:,.0f}

    </div>

    </div>
    """,unsafe_allow_html=True)

    with c3:

      st.markdown(f"""
    <div class="metric-card">

    <div class="metric-title">

    🏦 Balance

    </div>

    <div class="metric-value">

    ₹{balance:,.0f}

    </div>

    </div>
    """,unsafe_allow_html=True)

    st.divider()

    ##################################################

    expenses = get_expenses(user["id"])

    if len(expenses) == 0:

        st.info("No expenses added yet.")
        return

    df = pd.DataFrame(expenses)

    ##################################################

    left, right = st.columns(2)

    with left:

        st.subheader("🥧 Expense Categories")

        pie=px.pie(

df,

values="amount",

names="category",

hole=.65,

color_discrete_sequence=px.colors.qualitative.Set2

)

    ##################################################

    with right:

        st.subheader("📈 Expense Trend")

        monthly = (

            df.groupby("expense_date")["amount"]

            .sum()

            .reset_index()

        )

        line=px.area(

monthly,

x="expense_date",

y="amount",

markers=True

)

        st.plotly_chart(

            line,

            use_container_width=True

        )

    ##################################################

    st.divider()

    st.subheader("📋 Recent Expenses")

    show = df[

        [

            "title",

            "category",

            "amount",

            "expense_date"

        ]

    ]

    st.subheader("Recent Transactions")

    st.dataframe(
    show,
    use_container_width=True,
    hide_index=True,
    height=300
)

    ##################################################

    st.divider()

    st.subheader("📊 Statistics")

    c1, c2, c3 = st.columns(3)

    c1.metric(

        "Transactions",

        len(df)

    )

    c2.metric(

        "Highest Expense",

        f"₹ {df['amount'].max():,.2f}"

    )

    c3.metric(

        "Average Expense",

        f"₹ {df['amount'].mean():,.2f}"

    )
