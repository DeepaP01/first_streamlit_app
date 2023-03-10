
import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

#import streamlit

streamlit.title('my parents New healthy dinner')
streamlit.header( '\N{flexed biceps}Breakfast Menu\N{flexed biceps}')
streamlit.text('πΆοΈ Omega 3 & Blueberry Oatmeal')
streamlit.text('πKale, Spinach and Rocket Smoothie')
streamlit.text('π₯ Hard-Boiled Free Range Egg')
streamlit.text('π₯ Avocado Toast')
streamlit.header('ππ₯­ Build Your Own Fruit Smoothie π₯π')
#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
#let put the list here
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
 #display the table here
streamlit.dataframe(fruits_to_show)

def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

streamlit.header("Fruityvice Fruit Advice!")
try:
   fruit_choice = streamlit.text_input('what fruit would you like information about?')
   if not fruit_choice:
        streamlit.error("Please select a fruit to get information")
   else:
        fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
        fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
        streamlit.dataframe(fruityvice_normalized)
       
except URLError as e:
    streamlit.error()
 
#old code
#streamlit.header("Fruityvice Fruit Advice!")
#fruit_choice = streamlit.text_input('what fruit would you like information about?', 'kiwi')
#streamlit.write('the user entered',fruit_choice)
#import requests
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#streamlit.text(fruityvice_response.json())

#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#streamlit.dataframe(fruityvice_normalized)
#streamlit.stop()
#end of old code

#import snowflake.connector
streamlit.header("the fruit load list contains:")
#snowflake -related functions
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
         my_cur.execute("SELECT * from fruit_load_list")
         return my_cur.fetchall()
   #add button to load the fruit
if streamlit.button('get fruit load list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    my_cnx.close()
    streamlit.dataframe(my_data_rows)
    
#streamlit.header("The fruit load list contains:")
#streamlit.dataframe(my_data_rows)
def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
         my_cur.execute("insert into fruit_load_list values('"+ new_fruit +"')")
         return "thanks fro adding " + new_fruit
add_my_fruit = streamlit.text_input('what fruit wound you like to add?')
if streamlit.button('Add a fruit to the list'):
   my_cnx=snowflake.connector.connect(**streamlit.secrets["snowflake"])
   back_from_function = insert_row_snowflake(add_my_fruit)
   streamlit.text(back_from_function)
   
#streamlit.write('the user entered',add_my_fruit)
#streamlit.write('Thanks for adding', add_my_fruit)

#my_cur.execute("insert into fruit_load_list values ('from streamlit')")
