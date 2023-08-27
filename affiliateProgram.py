import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Set the title
st.title("Sales Pipeline Forecast Model: Affiliate Program")
# Sidebar inputs
st.sidebar.header("Enter Parameters")
your_plan = st.sidebar.number_input("Your Plan", value=2500)
average_plan_referrals = st.sidebar.number_input("Average Plan Referrals", value=2500)
referral_payout_percent = st.sidebar.slider("Referral Payout Percentage", min_value=0.0, max_value=1.0, value=0.1)
sales_conversion_rate = st.sidebar.slider("Sales Conversion Rate", min_value=0.0, max_value=1.0, value=0.4)
response_rate = st.sidebar.slider("Response Rate", min_value=0.0, max_value=1.0, value=0.6)

# Calculate metrics
payout = referral_payout_percent * average_plan_referrals
referrals_needed_to_break_even = your_plan / payout
conversions_needed = referrals_needed_to_break_even / sales_conversion_rate
touch_points_needed = conversions_needed / response_rate

# Display results
st.write("Payout: ", payout)
st.write("Referrals Needed to Break Even: ", referrals_needed_to_break_even)
st.write("Conversions Needed: ", conversions_needed)
st.write("Touch Points Needed: ", touch_points_needed)




