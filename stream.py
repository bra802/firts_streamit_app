
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
streamlit.dataframe(my_fruit_list)
