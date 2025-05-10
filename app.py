import streamlit as st

from custom_components.my_component import my_component

st.write("hello world")

st.subheader("Component with constant args")

# Create an instance of our component with a constant `name` arg, and
# print its output value.
num_clicks = my_component("World")
st.markdown("You've clicked %s times!" % int(num_clicks))

st.markdown("---")
st.subheader("Component with variable args")

name_input = st.text_input("Enter a name", value="Streamlit")
num_clicks = my_component(name_input, key="foo")
st.markdown("You've clicked %s times!" % int(num_clicks))