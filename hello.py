import streamlit as st
from src.helper import parse_shopping_list, export_auctionator, export_tsm

txt = st.text_area(
    "Shopping list:",
    ""
)

df = parse_shopping_list(txt)
st.dataframe(df, width=800, hide_index=True)

st.text_area("export auctionator", export_auctionator(df))

st.text_area("export TSM", export_tsm(df))
