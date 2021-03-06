import streamlit, pandas
  
streamlit.title('My Mom\'s New Healthier Dinner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣  Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#add pick list for fruit
fruits_selected = streamlit.multiselect("Pick Some Fruit:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
#display the table
streamlit.dataframe(fruits_to_show)
