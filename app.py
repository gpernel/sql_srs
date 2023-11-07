import io

import streamlit as st
import pandas as pd
import duckdb as db

csv1 ="""
beverage, price
orange juice, 2.5
expresso,1.5
tea, 2
"""
beverages = pd.read_csv(io.StringIO(csv1))

csv2 ="""
food_item, price
cookie, 4
flan,2.5
muffin, 3
"""
food_items = pd.read_csv(io.StringIO(csv2))

answer = """
SELECT * FROM beverages
CROSS JOIN food_items
"""

solution = db.sql(answer).df()

st.write("""
## SQL SRS
Spaced Repetition System SQL practice

""")

with st.sidebar:
    option = st.selectbox(
        "What would you like to review ?",
        ("Join","GroupBy","Windows Functions"),
        index=None,
        placeholder='Select a theme...'
    )
    st.write('you selected: ', option)

st.header("Enter your code")

query = st.text_area(label="Type your code here...", key='user_input')
if query:
    st.write(db.sql(query).df())

tab1, tab2 = st.tabs(["Tables","Solution"])

with tab1:
    st.write('table : beverages')
    st.dataframe(beverages)
    st.write('table : food_items')
    st.dataframe(food_items)
    st.write('expected')
    st.dataframe(solution)

with tab2:
    st.write(answer)
