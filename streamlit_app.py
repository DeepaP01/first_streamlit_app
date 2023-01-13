
import streamlit

streamlit.title('my parents New healthy dinner')
streamlit.header( '\N{flexed biceps}Breakfast Menu\N{flexed biceps}')
streamlit.text('🌶️ Omega 3 & Blueberry Oatmeal')
streamlit.text('🍂Kale, Spinach and Rocket Smoothie')
streamlit.text('🥚 Hard-Boiled Free Range Egg')
streamlit.text('🥑 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
#let put the list here
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
 #display the table here
streamlit.dataframe(fruits_to_show)

import requests
streamlit.header("Fruityvice Fruit Advice!")

fruit_choice = streamlit.text_input('what fruit would you like information about?', 'kiwi')
streamlit.write('the user entered',fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "fruit_choice")
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)
