import streamlit as st

def load_css():

    st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"]  {
    font-family: 'Poppins', sans-serif;
}

/* Background */

.stApp{
    background:#F3F6FB;
}

/* Sidebar */

[data-testid="stSidebar"]{
    background:#1E293B;
}

[data-testid="stSidebar"] *{
    color:white !important;
}

/* Title */

h1{
    color:#0F172A;
    font-weight:700;
}

h2,h3{
    color:#334155;
}

/* Buttons */

.stButton>button{

    width:100%;

    border-radius:12px;

    background:#3B82F6;

    color:white;

    border:none;

    font-size:17px;

    font-weight:600;

    padding:12px;

}

.stButton>button:hover{

    background:#2563EB;

}

/* Inputs */

.stTextInput input,
.stNumberInput input,
textarea{

    border-radius:12px !important;

    border:1px solid #CBD5E1 !important;

    background:white !important;

    color:black !important;

}

/* Select */

.stSelectbox{

    border-radius:12px;

}

/* Cards */

.metric-card{

    background:white;

    padding:20px;

    border-radius:18px;

    box-shadow:0px 5px 18px rgba(0,0,0,.08);

    text-align:center;

}

.metric-title{

    color:#64748B;

    font-size:18px;

}

.metric-value{

    color:#111827;

    font-size:32px;

    font-weight:bold;

}

</style>
""", unsafe_allow_html=True)