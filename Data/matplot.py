import streamlit as st
import math

Your_Plan = 2500
Avg_Plan_Ref = 2500
Ref_Payout_Percent = 0.1
Sales_Conversion_Rate = 0.4
Response_Rate = 0.6
Payout=Ref_Payout_Percent*Avg_Plan_Ref
Referrals_Needed_to_BE=Your_Plan/Payout
Conversions_Needed=Referrals_Needed_to_BE/Sales_Conversion_Rate
Touch_Points_Needed=Conversions_Needed/Response_Rate

st.write("Payout:", Payout)
st.write("Referrals Needed to Break Even:", Referrals_Needed_to_BE)
st.write("Conversions Needed:", Conversions_Needed)
st.write("Touch Points Needed:", Touch_Points_Needed)