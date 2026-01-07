import streamlit as st
import pandas as pd
import requests
from streamlit_autorefresh import st_autorefresh
import plotly.express as px


# -------------------------
# Page config
# -------------------------
st.set_page_config(page_title="📞 AI Voice Agent Dashboard", layout="wide")
st.title("📞 AI Voice Agent Dashboard")

# -------------------------
# Backend URL
# -------------------------
BACKEND_URL = "http://127.0.0.1:8000"

# -------------------------
# Auto-refresh every 5 seconds
# -------------------------
st_autorefresh(interval=5000, key="datarefresh")

# -------------------------
# Fetch leads from backend
# -------------------------
def get_leads():
    try:
        response = requests.get(f"{BACKEND_URL}/leads")
        if response.status_code == 200:
            data = response.json()
            if data:
                df = pd.DataFrame(data)
                return df
            else:
                return pd.DataFrame()
        else:
            st.error("Failed to fetch leads from backend.")
            return pd.DataFrame()
    except Exception as e:
        st.error(f"Error connecting to backend: {e}")
        return pd.DataFrame()

# -------------------------
# Simulate next call
# -------------------------
def call_next_lead():
    try:
        response = requests.post(f"{BACKEND_URL}/call-next")
        if response.status_code == 200:
            result = response.json()
            st.success(result["message"])
        else:
            st.error("Failed to call next lead.")
    except Exception as e:
        st.error(f"Error connecting to backend: {e}")

# -------------------------
# Sidebar Controls
# -------------------------
st.sidebar.header("Controls")
if st.sidebar.button("Call Next Lead"):
    call_next_lead()

st.sidebar.markdown("---")
st.sidebar.header("Filters")
service_filter = st.sidebar.multiselect("Service", [])
status_filter = st.sidebar.multiselect("Status", ["pending", "called", "failed"])
location_filter = st.sidebar.multiselect("Location", [])

# -------------------------
# Fetch data
# -------------------------
df = get_leads()

# Update filters dynamically
if not df.empty:
    service_filter_options = df["service"].unique().tolist()
    location_filter_options = df["location"].unique().tolist()
    service_filter = st.sidebar.multiselect("Service", service_filter_options, default=service_filter_options)
    location_filter = st.sidebar.multiselect("Location", location_filter_options, default=location_filter_options)

    # Apply filters
    if service_filter:
        df = df[df["service"].isin(service_filter)]
    if status_filter:
        df = df[df["status"].isin(status_filter)]
    if location_filter:
        df = df[df["location"].isin(location_filter)]

# -------------------------
# Show metrics
# -------------------------
if not df.empty:
    total = len(df)
    pending = len(df[df["status"] == "pending"])
    called = len(df[df["status"] == "called"])
    failed = len(df[df["status"] == "failed"])

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Leads", total)
    col2.metric("Pending ⏳", pending)
    col3.metric("Called ✅", called)
    col4.metric("Failed ❌", failed)

# -------------------------
# Display table with color coding
# -------------------------
if not df.empty:
    # Reorder columns
    columns_order = ["id", "name", "phone", "service", "location", "budget", "email", "notes", "status"]
    df = df[[c for c in columns_order if c in df.columns]]

    # Color-code status
    def color_status(val):
        if val == "pending":
            color = "yellow"
        elif val == "called":
            color = "#8BC34A"  # green
        elif val == "failed":
            color = "#F44336"  # red
        else:
            color = "white"
        return f"background-color: {color}"

    st.subheader("All Leads")
    st.dataframe(df.style.applymap(color_status, subset=["status"]))

    # -------------------------
    # Show queue vs processed chart
    # -------------------------
    st.subheader("Lead Status Chart")
    status_counts = df["status"].value_counts()
    st.bar_chart(status_counts)

    # -------------------------
    # Download CSV
    # -------------------------
    st.download_button("Download Leads CSV", df.to_csv(index=False), "leads.csv")
else:
    st.write("No leads yet. Add leads via backend `/lead` endpoint.")

