import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title('Mentor Portal')
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('Your Posts', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/Posts_Page.py')

if st.button('View Your Profile and Connections', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/Mentor_Information_Page.py')

if st.button("Review Courses",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/Review_Courses_Page.py')