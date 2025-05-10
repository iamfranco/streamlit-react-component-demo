import os
import streamlit.components.v1 as components

def my_component(name, key=None, use_built_component=True) -> int:
    """Create a new instance of "my_component".

    Parameters
    ----------
    name: str
        The name of the thing we're saying hello to. The component will display
        the text "Hello, {name}!"
    key: str or None
        An optional key that uniquely identifies this component. If this is
        None, and the component's arguments are changed, the component will
        be re-mounted in the Streamlit frontend and lose its current state.

    Returns
    -------
    int
        The number of times the component's "Click Me" button has been clicked.
        (This is the value passed to `Streamlit.setComponentValue` on the
        frontend.)

    """

    if use_built_component:
        parent_dir = os.path.dirname(os.path.abspath(__file__))
        build_dir = os.path.join(parent_dir, "frontend/build")
        _component_func = components.declare_component(
            "my_component", 
            path=build_dir
        )
    else:
        _component_func = components.declare_component(
            "my_component",
            url="http://localhost:3001",
        )
        
    component_value = _component_func(name=name, key=key, default=0)

    return int(component_value)

def _example_usage(use_built_component: bool):
    import streamlit as st

    st.write("hello world")

    st.subheader("Component with constant args")

    # Create an instance of our component with a constant `name` arg, and
    # print its output value.
    num_clicks = my_component("World", use_built_component=use_built_component)
    st.markdown("You've clicked %s times!" % num_clicks)

    st.markdown("---")
    st.subheader("Component with variable args")

    name_input = st.text_input("Enter a name", value="Streamlit")
    num_clicks = my_component(name_input, key="foo", use_built_component=use_built_component)
    st.markdown("You've clicked %s times!" % num_clicks)

if __name__ == "__main__":
    _example_usage(use_built_component=False)