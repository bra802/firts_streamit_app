## jeu de données fruits
import pandas 
my_fruit_list = pandas.read_csv("C:/Users/mba.ndiaye/Downloads\fruits.csv")
streamlit.dataframe(my_fruit_list)

## menu breakfast
import streamlit

streamlit.title('My parents health Diner')
streamlit.text('Breakfast menu')
streamlit.text(' 🥣 Burger & tenders')
streamlit.text('ice cream and muffins')
