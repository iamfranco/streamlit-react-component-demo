import os
import streamlit.components.v1 as components

def percentage_component(percentage: float, label: str = "Percentage", key=None, use_built_component=True):
    if use_built_component:
        parent_dir = os.path.dirname(os.path.abspath(__file__))
        build_dir = os.path.join(parent_dir, "frontend/build")
        _component_func = components.declare_component(
            "percentage_component", 
            path=build_dir
        )
    else:
        _component_func = components.declare_component(
            "percentage_component",
            url="http://localhost:3001",
        )
        
    _component_func(percentage=percentage, label=label, key=key, default=0)

def _example_usage(use_built_component: bool):
    import streamlit as st

    col1, col2, col3 = st.columns(3)

    with col1:
        num1 = st.number_input("Enter a number", min_value=0.0, max_value=100.0, value=20.0, format="%0.1f", key="num1")
        percentage_component(percentage=num1, key="1", use_built_component=use_built_component)
        st.metric("Percentage", f"{num1:.1f}%", border=True)

    with col2:
        num2 = st.number_input("Enter a number", min_value=0.0, max_value=100.0, value=55.5, format="%0.1f", key="num2")
        percentage_component(percentage=num2, label="Some Label", key="2", use_built_component=use_built_component)

    with col3:
        num3 = st.number_input("Enter a number", min_value=0.0, max_value=100.0, value=83.1, format="%0.1f", key="num3")
        percentage_component(percentage=num3, label="Another Percentage", key="3", use_built_component=use_built_component)

if __name__ == "__main__":
    _example_usage(use_built_component=False)