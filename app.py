import streamlit as st
import pandas as pd
import duckdb as db

data = {"article": [1, 2, 3, 4], "prix": [40, 50, 60, 30]}
df = pd.DataFrame(data)

st.write("Interpréteur sql")
tab1 = st.tabs(["SQL"])

st.write("Le dataframe (df) de départ :")
st.dataframe(df)
query = st.text_area(label="Entrez votre commande SQL")
st.write(f"Vous avez entré la query suivante : {query}")

st.write(db.sql(query).df())