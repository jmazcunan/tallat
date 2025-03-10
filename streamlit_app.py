import streamlit as st

st.set_page_config(page_title = "Tallat Láser", 
                   page_icon = "🔥",
                   layout="wide"
                   )

st.title("Tallat  -  Fallas 2025 🔥")



with st.expander("Pulseras", expanded=True):
    st.caption("Peineta")
    cols = st.columns(3)
    cols[0].image("static/pulseras1.jpg")
    cols[1].image("static/pulseras2.jpg")
    cols[2].image("static/pulseras3.jpg")


with st.expander("Broches", expanded=True):
    st.caption("Llama")
    cols = st.columns(3)
    cols[0].image("static/broche2.jpg")
    cols[1].image("static/broche1.jpg")
    cols[2].image("static/broche3.jpg")

    st.caption("Peineta")
    cols = st.columns(3)
    cols[0].image("static/broche_p1.jpg")
    cols[1].image("static/broche_p2.jpg")
    cols[2].image("static/broche_p3.jpg")