from altair import Column
import pandas as pd
import streamlit as st
import numpy as np
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie

#contoh 3
# Define the HTML code with CSS to set the background image
background = """
<style>
    .stApp {
        background-image: url('https://img.freepik.com/free-vector/hand-painted-watercolor-pastel-sky-background_23-2148902771.jpg');
        background-size: cover;
    }
</style>
"""

# Apply the HTML code to set the background image
st.markdown(background, unsafe_allow_html=True)

# Your Streamlit app code goes here

#Option Menu Sidebar
with st.sidebar :
    selected = option_menu (
       menu_title="Main Menu",
       options=["Halaman Utama", "Materi Utama", "Kalkulator Konsentrasi", "Kalkulasi %RSD"]
    )

#Halaman Utama
if selected == "Halaman Utama":
    st.title("Home")


#Materi Utama 
if selected == "Materi Utama" :
    st.title("Materi Utama")
    user_input = st.selectbox("Pilih topik : ", ["Pengertian Alkalimetri", "Pemilihan Indikator", "Reaksi Umum", "Rumus Perhitungan Normalitas"])
    if st.button("Kirim"):
        options = {
            "Pengertian Alkalimetri": "Alkalimetri adalah titrasi yang dilakukan dengan menggunakan larutan titran yang bersifat basa dan menggunakan larutan baku primer yang bersifat asam. Dari volume larutan baku asam yang diperlukan untuk mencapai titik akhir titrasi, konsentrasi larutan basa dapat dihitung menggunakan stoikiometri reaksi titrasi yang terjadi.",
            "Pemilihan Indikator": "Indikator yang ideal untuk titrasi alkalimetri adalah indicator dengan perubahan warna di sekitar pH titik ekivalensi ( pH di mana jumlah ekivalen asam dan basa dalam larutan menjadi sama). Contoh titik ekivalensi dalam titrasi NaOH dengan asam oksalat terjadi ketika asam oksalat sepenuhnya bereaksi dengan NaOH membentuk garam oksalat dan air. Salah satu pilihan yang umum digunakan adalah fenolftalein. Yang merupakan indikator yang berubah warna dari semula tidak berwarna menjadi merah muda seulas di kisaran pH 8,2 - 10, sehingga sesuai untuk menandai titik akhir titrasi NaOH dengan asam oksalat.",
            "Reaksi Umum": """Reaksi umum yang terjadi dalam standardisasi larutan NaOH dengan Asam Oksalat adalah :

    2 NaOH (aq) + H2C2O4 (aq) -> Na2C2O4 (aq) + 2 H2O (l)

    Dengan Natrium Hidroksida bereaksi dengan Asam Oksalat (H2C2O4) menghasilkan Natrium Oksalat (Na2C2O4).""",
            "Rumus Perhitungan Normalitas": """Rumus untuk menghitung normalitas (N) adalah :
        
    N(titran) = massa titrat(mg)/(BE(titrat) x Volume Akhir(mL))
        
    Notes : 
        ~ N adalah Normalitas (mgrek/mL)
        ~ BE adalah Berat ekuivalen titrat(mg/mgrek)
        ~ V adalah Volume akhir titrasi (mL)"""

        }
        response = options.get(user_input)
        text_area_height = min(max(len(response.split('\n')) * 25, 200), 600)  # Adjust height dynamically
        st.text_area("Penjawab:", value=response, height=text_area_height, disabled=True)

#Kalkulator Konsentrasi
if selected == "Kalkulator Konsentrasi" :
    st.title("Kalkulator Konsentrasi")
    gram = st.number_input("Masukkan jumlah massa (mg):", min_value=0.0, format="%.4f")
    volume = st.number_input("Masukkan volume titran (mL):", min_value=0.0)
    BE = st.number_input("Masukkan nilai BE Titrat (mg/mgrek):", min_value=0.00)
    if st.button("Kalkulasi"):
        try:
            result = gram / (volume * BE)
            result_rounded = round(result, 4)
            st.write(f"Hasil perhitungan Normalitas : {result_rounded} N")
        except ZeroDivisionError:
            st.write("Error: BE tidak boleh nol. Silakan masukkan nilai yang valid.")

#Kalkulasi %RSD 
if selected == "Kalkulasi %RSD":
    st.title("Kalkulasi %RSD")

    # Sample DataFrame
    data = {
        "Sample (mg)": [0.01, 0.02, 0.03],
        "Volume Titran (mL)": [0.00, 0.00, 0.00],
        "Normalitas Titran (N)": [0.00, 0.00, 0.00]
    }
    df = pd.DataFrame(data)

    st.header("Kalkulasi Statistik")
    # Allow users to input the column index
    column_index = st.selectbox("Pilih kolom data :", df.columns)

    # Allow users to edit a specific column
    
    selected_columns = []
    selected_columns.append(column_index)

    updated_df = df.copy()
    if len(selected_columns) > 0:
        df_edit = df[selected_columns]
        edited_df = st.data_editor(df_edit)
        if st.button("Kalkulasi"):
            updated_data = {}
            for column in selected_columns:
                updated_data[column] = edited_df[column]
            
            # Calculate and display mean and standard deviation
            for column in selected_columns:
                column_data = updated_data[column]
                hasil_mean = np.mean(column_data)
                hasil_std_dev = np.std(column_data)
                hasil_rsd = (hasil_std_dev / hasil_mean) * 100 if hasil_mean != 0 else 0

                # Round the results to four decimal places
                hasil_mean = round(hasil_mean, 4)
                hasil_rsd = round(hasil_rsd, 2)
                hasil_std_dev = round(hasil_std_dev, 6)

                # Display the results
                st.write(f"Rata-rata dari {column}: {hasil_mean}")
                st.write(f"Standar Deviasi dari {column}: {hasil_std_dev}")
                st.write(f"%RSD dari {column}: {hasil_rsd}%")
