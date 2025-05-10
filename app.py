import streamlit as st

from custom_components.percentage_component import percentage_component

col1, col2, col3 = st.columns(3)

with col1:
  num1 = st.number_input("Enter a number", min_value=0.0, max_value=100.0, value=30.5, format="%0.1f", key="num1")
  percentage_component(percentage=num1, key="1")

with col2:
  num2 = st.number_input("Enter a number", min_value=0.0, max_value=100.0, value=60.0, format="%0.1f", key="num2")
  percentage_component(percentage=num2, key="2")

with col3:
  num3 = st.number_input("Enter a number", min_value=0.0, max_value=100.0, value=80.1, format="%0.1f", key="num3")
  percentage_component(percentage=num3, key="3")