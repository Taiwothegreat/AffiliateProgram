import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Set the title
st.title("Sales Pipeline Forecast Model: Affiliate Program")
# Load the logo image
logo_image = Image.open('Affiliate Program (1).png')
# Add the logo image to the sidebar
st.sidebar.image(logo_image, use_column_width=True)
# Sidebar inputs
st.sidebar.header("Enter Parameters")
your_plan = st.sidebar.number_input("Your Plan", value=2500)
average_plan_referrals = st.sidebar.number_input("Average Plan Referrals", value=2500)

your_plan_formatted = f"${your_plan}"
average_plan_referrals_formatted = f"${average_plan_referrals}"

st.write("Your Plan:", your_plan_formatted)
st.write("Average Plan Referrals:", average_plan_referrals_formatted)

referral_payout_percent = st.sidebar.slider("Referral Payout Percentage", min_value=0.0, max_value=1.0, value=0.1)
sales_conversion_rate = st.sidebar.slider("Sales Conversion Rate", min_value=0.0, max_value=1.0, value=0.4)
response_rate = st.sidebar.slider("Response Rate", min_value=0.0, max_value=1.0, value=0.6)

# Calculate metrics
payout = referral_payout_percent * average_plan_referrals
referrals_needed_to_break_even = your_plan / payout
conversions_needed = referrals_needed_to_break_even / sales_conversion_rate
touch_points_needed = conversions_needed / response_rate

st.metric("Payout", int(payout))
st.metric("Referrals Needed to Break Even", int(referrals_needed_to_break_even))
st.metric("Conversions Needed", int(conversions_needed))
st.metric("Touch Points Needed", int(touch_points_needed))






