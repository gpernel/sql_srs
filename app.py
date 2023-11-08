# pylint: disable=missing-module-docstring
import io

import duckdb as db
import pandas as pd
import streamlit as st

CV1 = """
beverage, price
orange juice, 2.5
expresso,1.5
tea, 2
"""
beverages = pd.read_csv(io.StringIO(CV1))

CV2 = """
food_item, price
cookie, 4
flan,2.5
muffin, 3
"""
food_items = pd.read_csv(io.StringIO(CV2))

ASWER_STR = """
SELECT * FROM beverages
CROSS JOIN food_items
"""

solution_df = db.sql(ASWER_STR).df()

st.write(
    """
## SQL SRS
Spaced Repetition System SQL practice

"""
)

with st.sidebar:
    option = st.selectbox(
        "What would you like to review ?",
        ("Join", "GroupBy", "Windows Functions"),
        index=None,
        placeholder="Select a theme...",
    )
    st.write("you selected: ", option)

st.header("Enter your code")

query = st.text_area(label="Type your code here...", key="user_input")
if query:
    result = db.sql(query).df()
    st.write(result)

    # test de la longeur des colonnes pour pouvoir donner des messages d'erreurs adéquats
    if len(result.columns) != len(solution_df.columns):
        st.write("Some columns are missing")
    try:
        result = result[solution_df.columns]
        st.dataframe(result.compare(solution_df))
    except KeyError as e:
        st.write("Some columns are missing")

    # test de la longeur du dataframe
    n_lines_differencies = result.shape[0] - solution_df.shape[0]
    if n_lines_differencies != 0:
        st.write(
            f"results has {n_lines_differencies} lines diffrence with the solution_df"
        )

tab1, tab2 = st.tabs(["Tables", "Solution"])

with tab1:
    st.write("table : beverages")
    st.dataframe(beverages)
    st.write("table : food_items")
    st.dataframe(food_items)
    st.write("expected")
    st.dataframe(solution_df)

with tab2:
    st.write(ASWER_STR)
