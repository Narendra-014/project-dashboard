import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Dashboard Internal",
    page_icon="🔒",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown(
    "<meta name='robots' content='noindex, nofollow'>",
    unsafe_allow_html=True
)

with open("config.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config["credentials"],
    config["cookie"]["name"],
    config["cookie"]["key"],
    config["cookie"]["expiry_days"],
)

# === LOGIN (VERSI BARU, TIDAK RETURN APA-APA)
authenticator.login(location="sidebar")

# === AMBIL STATUS LOGIN
auth_status = st.session_state.get("authentication_status")
name = st.session_state.get("name")

if auth_status:
    authenticator.logout("Logout", "sidebar")
    st.success(f"Selamat datang, {name}")
    st.title("🔒 Dashboard Internal")
    # Simulasi data
    data = pd.DataFrame(
    np.random.randn(100, 3),
    columns=['Kolom A', 'Kolom B', 'Kolom C'])
    st.dataframe(data)
    st.line_chart(data)
    st.bar_chart(data)
    st.area_chart(data)


elif auth_status is False:
    st.error("Username atau password salah")

else:
    st.warning("Silakan login untuk mengakses dashboard")


#=============================================================

