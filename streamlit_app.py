import streamlit
streamlit.title('Breakfast Favorites')
streamlit.header('🫐 🥝 🍓Fruit Your Own Fruit Smoothie')
streamlit.text('🥬 Leafy GreenKale, Spinach')
streamlit.text ('🥘 Hard-Boiled Free-Range Egg')
streamlit.text('🥑 Avocado Toast ')

import pandas
my_fruit_list = pandas.read_csv ("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index ('Fruit')
#Let´s put a pick list here so they can pick the fruit they wnt to include
fruits_selected = streamlit.multiselect ("Pick soe frutis:", list (my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc [fruits_selected]
#display the table on the page 
streamlit.dataframe (fruits_to_show)
       
