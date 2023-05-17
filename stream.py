## jeu de données fruits
import pandas 
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
my_fruit_list

## menu breakfast
import streamlit

streamlit.title('My parents health Diner')
streamlit.text('Breakfast menu')
streamlit.text(' 🥣 Burger & tenders')
streamlit.text('ice cream and muffins')
