import streamlit
streamlit.title('Breakfast Favorites')
streamlit.header('🫐 🥝 🍓Fruit Your Own Fruit Smoothie')
streamlit.text('🥬 Leafy GreenKale, Spinach')
streamlit.text ('🥘 Hard-Boiled Free-Range Egg')
streamlit.text('🥑 Avocado Toast ')

import pandas
my_fruit_list = pandas.read_csv ("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe (my_fruit_list)
       
