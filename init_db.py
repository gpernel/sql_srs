# pylint: disable=missing-module-docstring
import io

import duckdb
import pandas as pd


con = duckdb.connect(database="data/exercises_sql_tables.duckdb", read_only=False)
#----------------------------------------------------------
# EXERCICES LIST
#----------------------------------------------------------
data = {
    "theme": ["cross_joins","cross_joins"],
    "exercise_name": ["beverages_and_food", "tailles_et_marques"],
    "tables": [["beverages", "food_items"], ["tailles", "marques"]],
    "last_reviewed": ["1980-01-01","1970-01-01"]
}
memory_state_df = pd.DataFrame(data)
con.execute("CREATE TABLE IF NOT EXISTS memory_state AS SELECT * FROM memory_state_df")


#----------------------------------------------------------
# CROSS JOIN EXERCISES
#----------------------------------------------------------

CSV1 = """
beverage, price_b
orange juice, 2.5
expresso,1.5
tea, 2
"""
beverages = pd.read_csv(io.StringIO(CSV1))
con.execute("CREATE TABLE IF NOT EXISTS beverages AS SELECT * FROM beverages")

CSV2 = """
food_item, price_f
cookie, 4
flan,2.5
muffin, 3
"""
food_items = pd.read_csv(io.StringIO(CSV2))
con.execute("CREATE TABLE IF NOT EXISTS food_items AS SELECT * FROM food_items")


CSV_TAILLES = """
size
S
M
L
XL
"""
tailles = pd.read_csv(io.StringIO(CSV_TAILLES))
con.execute("CREATE TABLE IF NOT EXISTS tailles AS SELECT * FROM tailles")

CSV_MARQUES = """
marques
Nike
Asphalte
Abercrombie
Lewis
"""
marques = pd.read_csv(io.StringIO(CSV_MARQUES))
con.execute("CREATE TABLE IF NOT EXISTS marques AS SELECT * FROM marques")

con.close()