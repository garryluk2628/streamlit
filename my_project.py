import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

main = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()

with main:
	st.title('Demo on how to use the streamlit container')
	st.text('This is a good function')

with dataset:
	st.header('Diamonds dataset')
	st.text('https://144.214.222.179/HKU/diamonds.csv')

	df = pd.read_csv('http://144.214.222.179/HKU/diamonds.csv')
	st.write(df)
	#cut color clarity
	cut_dist = pd.DataFrame(df['cut'].value_counts())
	st.bar_chart(cut_dist)
	color_dist = pd.DataFrame(df['color'].value_counts())
	st.bar_chart(color_dist)
	clarity_dist = pd.DataFrame(df['clarity'].value_counts())
	st.bar_chart(clarity_dist)
with features:
	st.header('The feature that I created')
	

with model_training:
	st.header('Diamonds dataset training process')
	sel_col, disp_col = st.columns(2)
	max_depth = sel_col.slider('What should be the max_depth of the model?', min_value=10, max_value=100, value=20, step=10)
	n_estimators = sel_col.selectbox('How many trees should ther be?', options=[100,200,300,'No Limits'], index=0)
	input_feature = sel_col.text_input('Which feature would you like to input to the model?', 'carat')
	
	regr = RandomForestRegressor(max_depth=max_depth, n_estimators=n_estimators)
	X= df[[input_feature]]
	y = df[['price']]

	regr.fit(X,y)
	prediction = regr.predict(y)

	disp_col.subheader('Mean absolute error of the model is:')
	disp_col.write(mean_absolute_error(y,prediction))

	disp_col.subheader('Mean squared error of the model is:')
	disp_col.write(mean_squared_error(y,prediction))

	disp_col.subheader('R square score of the model is:')
	disp_col.write(r2_score(y,prediction))


