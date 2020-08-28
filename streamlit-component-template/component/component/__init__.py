import os
import streamlit.components.v1 as components


# When we dont want to release we will just set it as True
_RELEASE = False

if not _RELEASE:
    
    _component_func = components.declare_component(
        # CHANGE HERE: with component name
        "streamlit_component", url="http://localhost:3001",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    # CHANGE HERE: with component name
    _component_func = components.declare_component("streamlit_component", path=build_dir)

def create_function_here(user_argument):
    # this python_argument gets passed to react js this.props.args["python_argument"]
    result = _component_func(python_argument=user_argument)
    # this result variable will get the string we have passed from react
    return result 
    # and this function's return value wll be received inside the user's streamlit script



if not _RELEASE:
    create_function_here(1)