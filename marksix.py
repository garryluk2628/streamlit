import random
import streamlit as st

original_title = '<p style="font-family:Courier; color:Blue; font-size: 40px;">Enter how many lines of marksix you want: </p>'
st.markdown(original_title, unsafe_allow_html=True)

number = st.number_input(' ')
#number = st.text_input('Enter how many lines of marksix you want: ')
number = int(number)
if number > 1:
	new_title = '<p style="font-family:Courier; color:Blue; font-size: 40px;">Enter how many lines of marksix you want: </p>',number,'<p style="font-family:Courier; color:Blue; font-size: 40px;"> lines of marksix</p>'
	st.markdown(new_title, unsafe_allow_html=True)
#	st.write('You want to generate ',number,' lines of marksix')

for i in range(number):
  marksix = list(range(1,50))

  l = random.sample(marksix,6)
  l.sort()
  st.write(l)
