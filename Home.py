import streamlit as st
import base64
import requests
from streamlit_lottie import st_lottie  


def img_to_base64(image_path):
    """Convert image to base64"""
    with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    
    # Import gambar & konversi ke base64
img_path = "imgs/icon_aka.png"  
img_base64 = img_to_base64(img_path)
st.sidebar.markdown(
    f'<img src="data:image/png;base64,{img_base64}" style="width: 100%; height: auto;">',
    unsafe_allow_html=True,
)

st.sidebar.markdown("---")
st.sidebar.header("~~~ PROJECT LPK ~~~")



# Pembuatan 2 kolom
col1, col2 = st.columns([1, 2])

with col1 :
    st.title (" ")
    st.title (" ")
    st.title("TITRIMETRI")

    st.page_link("Home.py", label="Home", icon="🏠")
    st.page_link("pages/1_Asidimetri.py", label="Asidimetri", icon="1️⃣")
    st.page_link("pages/2_Alkalimetri.py", label="Alkalimetri", icon="2️⃣")
    st.page_link("pages/3_Permanganometri.py", label="Permanganometri", icon="3️⃣")
    st.page_link("pages/4_Iodometri.py", label="Iodometri", icon="4️⃣")
    st.page_link("pages/5_Kompleksometri.py", label="Kompleksometri", icon="5️⃣")
    st.page_link("pages/6_Our_Team.py", label="Our Team", icon="👥")
    st.page_link("http://www.google.com", label="Google", icon="🌎")

# file json format (File path)
lottie_url = "https://lottie.host/cbcd7e7b-3119-45a2-862a-858ba07d3e39/TlOccKrpDV.json"

# Fungsi untuk memproses lottie url
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Memproses animasi lottie
lottie_json = load_lottie_url(lottie_url)

# Menampilkan animasi lottie
with col2 :
    if lottie_json is not None:
        st_lottie(lottie_json)
    else:
        st.write("Failed to load Lottie animation.")


st.caption('<div style="text-align: center;">"Tiba di sini, pintu gerbang ilmu terbuka lebar. Selamat datang di web pembelajaran titrimetri, tempat di mana pengetahuan bertemu pengalaman untuk mengukir keahlian titrimetrimu."</div>', unsafe_allow_html=True)
