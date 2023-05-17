
## menu breakfast
import streamlit

streamlit.title('My parents health Diner')
streamlit.text('Breakfast menu')
streamlit.text(' 🥣 Burger & tenders')
streamlit.text('ice cream and muffins')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

## jeu de donnée fruit

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.dataframe(my_fruit_list)

#filtrer les données du tableau en fonction des fruits qu'un client choisira
streamlit.multiselect("pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])

# display the table on the page
streamlit.dataframe(my_fruit_list)

## filter les données
fruits_selected = streamlit.multiselect("pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
