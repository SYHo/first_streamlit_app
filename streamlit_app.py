import streamlit

streamlit.title("Hello Toffee")
streamlit.header('Sit!  Stop barking.')
streamlit.text('Good dog!')
streanlit.text('Do you like 🐔chicken or 🍞bread?')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
