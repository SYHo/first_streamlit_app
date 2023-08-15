import streamlit

streamlit.title("Hello Toffee")
streamlit.header('Sit!  Stop barking.')
streamlit.text('Good dog!')
streamlit.text('Do you like 🐔chicken or 🍞bread?')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#Let's put a pick list her so they can pick the fruit they want
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

#display the table on the page
streamlit.dataframe(my_fruit_list)
