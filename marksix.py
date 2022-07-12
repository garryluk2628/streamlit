import random
import streamlit as st

number = st.number_input('#Enter how many lines of marksix you want: ')
#number = st.text_input('Enter how many lines of marksix you want: ')
number = int(number)
if number > 1:
	st.write('You want to generate ',number,' lines of marksix')

for i in range(number):
  marksix = list(range(1,50))

  l = random.sample(marksix,6)
  l.sort()
  st.write(l)
