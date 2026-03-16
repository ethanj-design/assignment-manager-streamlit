import streamlit as st 
import json
from pathlib import Path
from datetime import datetime
import uuid
import time

# Page Setup
st.set_page_config(
    "Order Application",
    layout="wide",
    initial_sidebar_state="expanded"
)


# JSON setup
inventory_json = Path("inventory.json")
orders_json = Path("orders.json")

if inventory_json.exists():
    with open(inventory_json, "r") as f:
        inventory = json.load(f)
if orders_json.exists():
    with open(orders_json, "r") as f:
        orders = json.load(f)
else: 
    orders = []


# Session State Setup
if "page" not in st.session_state:
    st.session_state["page"] = "home"


# navtool
with st.sidebar:
    st.title("Navigation")
    if st.button("Home", key="home_btn", type="primary", use_container_width=True):
        st.session_state["page"] = "home"
        st.rerun()

    if st.button("Orders", key="order_btn", type="primary", use_container_width=True):
        st.session_state["page"] = "orders"
        st.rerun()


if st.session_state["page"] == "home": 

    col1, col2 = st.columns([4, 2])

    with col1:
        selected_category = st.radio("Select a Category", ["Orders", "Inventory"], horizontal=True)
        
        if selected_category == "Inventory":
            st.markdown("## Inventory")

            if len(inventory)>0:
                st.dataframe(inventory)
            else:
                st.warning("No Inventory found!")
            
        elif selected_category == "Orders":
            st.markdown("## Orders")

            if len(orders) > 0:
                st.datafram(orders)
            else:
                st.warning("No Orders are recorded yet.")
    
    with col2:
        
        if selected_category == "Inventory":
            
            st.metric("Total Inventory", value=f"{len(inventory)}")
        else:
            st.metric("Total Orders", value=f"{len(orders)}")



elif st.session_state["page"] == "orders": 
    st.markdown("## Under Construction!")

