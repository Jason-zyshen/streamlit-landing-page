import streamlit as st
import time

st.title("Projects")
"On homepage: " + st.session_state['my_input']


@st.cache_data
def sleepy():
    data = time.sleep(3)


data_load_state = st.text('Loading data...')
sleepy()
data_load_state.text('Loading data...done! by cahcing')


st.markdown(
    "Text can be :blue[azul], but also :orange[laranja]. And of course it can be :red[red]. And :green[verde]. And look at this :violet[violeta]!")


# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )
