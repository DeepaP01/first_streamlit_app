
import streamlit

streamlit.title('my parents New healthy dinner')
streamlit.header( '\N{flexed biceps}Breakfast Menu\N{flexed biceps}')
streamlit.text('🌶️ Omega 3 & Blueberry Oatmeal')
streamlit.text('🍂Kale, Spinach and Rocket Smoothie')
streamlit.text('🥚 Hard-Boiled Free Range Egg')
streamlit.text('🥑 Hard-Boiled Free Range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#let put the list here
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
 #display the table here
streamlit.dataframe(my_fruit_list)


