# pylint: disable=missing-module-docstring
import io

import duckdb
import pandas as pd


con = duckdb.connect(database="data/exercises_sql_tables.duckdb", read_only=False)
#----------------------------------------------------------
# EXERCICES LIST
#----------------------------------------------------------
data = {
    "theme": ["cross_joins","window_function"],
    "exercise_name": ["beverages_and_food","simple_window"],
    "tables": [["beverages", "food_items"],"simple_window"],
    "last_reviewed": ["1970-01-01","1970-01-01"]
}
memory_state_df = pd.DataFrame(data)
con.execute("CREATE TABLE IF NOT EXISTS memory_state AS SELECT * FROM memory_state_df")


#----------------------------------------------------------
# CROSS JOIN EXERCISES
#----------------------------------------------------------

CV1 = """
beverage, price
orange juice, 2.5
expresso,1.5
tea, 2
"""
beverages = pd.read_csv(io.StringIO(CV1))
con.execute("CREATE TABLE IF NOT EXISTS beverages AS SELECT * FROM beverages")

CV2 = """
food_item, price
cookie, 4
flan,2.5
muffin, 3
"""
food_items = pd.read_csv(io.StringIO(CV2))
con.execute("CREATE TABLE IF NOT EXISTS food_items AS SELECT * FROM food_items")

