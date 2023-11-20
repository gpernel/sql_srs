# pylint: disable=missing-module-docstring
import ast
import logging
import os
import duckdb as db
import streamlit as st

if "data" not in os.listdir():
    logging.error(os.listdir())
    logging.error("creating folder data")
    os.mkdir("data")

if "exercises_sql_tables.duckdb" not in os.listdir("data"):
    exec(open("init_db.py").read())

con = db.connect(database="data/exercises_sql_tables.duckdb", read_only=False)


st.write(
    """
## SQL SRS
Spaced Repetition System SQL practice

"""
)

with st.sidebar:
    theme = st.selectbox(
        "What would you like to review ?",
        ("cross_joins", "GroupBy", "window_function"),
        index=None,
        placeholder="Select a theme...",
    )
    st.write("you selected: ", theme)
    exercise = con.execute(f"SELECT * FROM memory_state WHERE theme ='{theme}' ").df().sort_values("last_reviewed").reset_index()
    st.write(exercise)

    exercise_name = exercise.loc[0, "exercise_name"]
    with open(f"answers/{exercise_name}.sql", "r") as f:
        answer = f.read()
    solution_df = con.execute(answer).df()

st.header("Enter your code")

query = st.text_area(label="Type your code here...", key="user_input")


if query:
    result = con.execute(query).df()
    st.write(result)

    try:
        result = result[solution_df.columns]
        st.dataframe(result.compare(solution_df))
    except KeyError as e:
        st.write("Some columns are missing")

    # test de la longueur du dataframe
    n_line_differences = result.shape[0] - solution_df.shape[0]
    if n_line_differences != 0:
        st.write(
            f"result has {n_line_differences} lines difference with the solution"
        )

tab1, tab2 = st.tabs(["Tables", "Solution"])

with tab1:
    exercise_tables = exercise.loc[0, "tables"]
    for table in exercise_tables:
        st.write(f"table :'{table}'")
        df_table = con.execute(f"SELECT * FROM '{table}'").df()
        st.dataframe(df_table)


with tab2:
    st.text(answer)
