import streamlit as st
import streamlit.components.v1 as components


st.markdown("<h1 style='text-align: center; color: #002060;'> Panel de Control 📊 📈 </h1>", unsafe_allow_html=True)

def main():
    html_temp = """<script type='module' src='https://prod-useast-b.online.tableau.com/javascripts/api/tableau.embedding.3.latest.min.js'></script><tableau-viz id='tableau-viz' src='https://prod-useast-b.online.tableau.com/t/betilopezandueza/views/DashboardFinal/Dashboard5?:origin=card_share_link&:embed=n' width='100%' height='900'' ></tableau-viz>"""
    st.components.v1.html(html_temp, width=1600, height=900)
    

if __name__ == "__main__":    
    main()


