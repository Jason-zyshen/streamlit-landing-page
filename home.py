import streamlit as st
from streamlit_option_menu import option_menu
import time

st.set_page_config(
    page_title="Social Secretary"
    initial_sidebar_state="collapsed"
)

selected = option_menu(
    menu_title="",
    options=["Home", "Projects", "Contacts"],
    orientation="horizontal"
)
st.title("hello")
# with st.sidebar:

#     # st.success("yeah")
#     # with st.echo():
#     #     st.write("This code will be printed to the sidebar.")


if 'my_input' not in st.session_state:
    st.session_state['my_input'] = ""

my_input = st.text_input("type here", st.session_state['my_input'])
submit = st.button("Submit")
if submit:
    st.session_state['my_input'] = my_input
    "You have entered: " + my_input
