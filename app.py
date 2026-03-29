import streamlit as st
from src.crew import run_crew

st.title("🛒 E-commerce Support AI")

ticket = st.text_area("Customer Ticket")
order_context = st.text_area("Order Context (JSON)")

if st.button("Resolve"):
    result = run_crew(ticket, order_context)
    st.write(result)