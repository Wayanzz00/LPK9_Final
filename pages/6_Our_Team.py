import streamlit as st

# Title and Description
col1, col2, col3 = st.columns([1, 2, 0.5])
with col3:
    st.markdown=st.page_link("Home.py", label="Home", icon="🏠")

with col2:
    st.header("_Meet The Team_")
    
st.write('')

# Team Members
team_data = [
    {"name": "Aditiya Prayoga","IG": "@aditiya_p17", "image_url": "imgs/adit1.jpeg"},
    {"name": "Faiz Awanda A", "IG": "@faizawandaaziz", "image_url": "imgs/faiz.png"},
    {"name": "Ilham Alfitrah", "IG": "@alfitrah", "image_url": "imgs/ilham.png"},
    {"name": "Syaamil Maulana", "IG": "@syaamil_mln", "image_url": "imgs/syaamil.png"},
    {"name": "Wayan Raka S", "IG": "@yannnz___", "image_url": "imgs/wayan.jpg"}
]

# Display Team Members
col1, col2, col3, col4, col5 = st.columns(5)

for i, member in enumerate(team_data):
    with locals()[f"col{i % 5 + 1}"]:
        st.image(member["image_url"], use_column_width='auto', output_format='png', caption=f"{member['name']} {member['IG']}")

st.header(" ", divider="gray")
st.write('')
st.write('')

st.write('_Bagian dari project Praktik Logika dan Pemograman Komputer_')
st.write('')
st.write('Dosen Penanggung Jawab')
st.write('Dewi Pujo Ningsih, M.Si')

st.write('')
st.header(" ", divider="gray")
st.caption('<div style="text-align: center; transform: skewX(-20deg);">Powered by Politeknik AKA BOGOR</div>', unsafe_allow_html=True)

