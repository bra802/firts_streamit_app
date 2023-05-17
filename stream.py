## pandas avec jeu de données
import pandas as pd
my_fruits_list = pd.read_csv(" https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruits_list)

## Menu
import streamlit

streamlit.title('My parents health Diner')
streamlit.text('Breakfast menu')
streamlit.text(' 🥣 Burger & tenders')
streamlit.text('ice cream and muffins')
