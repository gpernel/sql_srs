# pylint: disable=missing-module-docstring
import ast
import duckdb as db
import streamlit as st


con = db.connect(database="data/exercises_sql_tables.duckdb", read_only=False)

# solution_df = db.sql(ASWER_STR).df()
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
    exercise = con.execute(f"SELECT * FROM memory_state WHERE theme ='{theme}' ").df()
    st.write(exercise)


st.header("Enter your code")

query = st.text_area(label="Type your code here...", key="user_input")


if query:
    result = con.execute(query).df()
    st.write(result)
#
#     # test de la longeur des colonnes pour pouvoir donner des messages d'erreurs adéquats
#     if len(result.columns) != len(solution_df.columns):
#         st.write("Some columns are missing")
#     try:
#         result = result[solution_df.columns]
#         st.dataframe(result.compare(solution_df))
#     except KeyError as e:
#         st.write("Some columns are missing")
#
#     # test de la longeur du dataframe
#     n_lines_differencies = result.shape[0] - solution_df.shape[0]
#     if n_lines_differencies != 0:
#         st.write(
#             f"results has {n_lines_differencies} lines diffrence with the solution_df"
#         )

tab1, tab2 = st.tabs(["Tables", "Solution"])

with tab1:
    exercise_tables = ast.literal_eval(exercise.loc[0, "tables"])
    for table in exercise_tables:
        st.write(f"table :'{table}'")
        df_table = con.execute(f"SELECT * FROM '{table}'").df()
        st.dataframe(df_table)


with tab2:
    exercise_name = exercise.loc[0, "exercise_name"]
    with open(f"answers/{exercise_name}", "r") as f:
        answer = f.read()
    st.write(answer)