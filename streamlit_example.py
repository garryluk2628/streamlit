import streamlit as st
import datetime

st.write("""
# Show how to display message with Streamlit

# This is a test

This without heading format
""")
option = 'Apple'
option = st.selectbox('Select the Furit that you like', ('Apple','Orange','Banana','Water melon','Grape','Lemon'))

if option == 'Apple':
	st.write('I like ',option,' very much')
if option =='Orange':
	st.write('I like ',option,' very much')
if option == 'Banana':
	st.write('I like ',option,' very much')
if option == 'Water melon':
	st.write('I like ',option,' very much')
if option == 'Grape':
	st.write('I like ',option,' very much')
if option == 'Lemon':
	st.write('I like ',option,' very much')