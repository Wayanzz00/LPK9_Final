import pandas as pd
import streamlit as st
import numpy as np

col1, col2, col3 = st.columns([1, 2, 0.5])
with col3:
    st.markdown=st.page_link("Home.py", label="Home", icon="🏠")


with col2:
    st.title("Permanganometri")

# Fungsi untuk menghitung konsentrasi
def konsentrasi(gram, volume, BE):
    try:
        result = gram / (volume * BE)
        return result
    except ZeroDivisionError:
        return "Error: Silakan masukkan nilai yang valid (Kolom tidak boleh nol)."

# Fungsi untuk menghasilkan jawaban dari input pengguna
def materi_utama(materi):
    options = {
        "Pengertian Permanganometri": "Permanganometri adalah metode analisis kimia yang menggunakan reaksi redoks antara ion permanganat (MnO₄⁻) dan senyawa kimia lainnya dalam larutan. Reaksi ini sering digunakan untuk menentukan kadar senyawa reduktor dalam sampel, di mana permanganat bertindak sebagai agen pengoksidasi. KMnO4 bersifat oksidator kuat akan mengalami reduksi menjadi Mn2+ + H2O dan sampel akan mengalami reaksi oksidasi.",
        "Pemilihan Indikator": "Pada titrasi metode permanganometri KMno4 bersifat sebagai auto indikator. Karena kelebihan satu tetes KMnO4 akan terjadi perubahan warna larutan menjadi merah muda seulas. Perubahan warna ini ditetapkan sebagai warna titik akhir titrasi.",
        "Reaksi Umum": """Reaksi umum yang terjadi dalam standardisasi larutan KMnO4 dengan Asam Oksalat (H2C2O4) adalah :

    2 MnO4^- (aq) + 5 H2C2O4 (aq) + 6 H^+ -> 2 Mn^2+ (aq) + 10 CO2 (aq) + 8 H2O (l)

    Dengan Kalium Permanganat bereaksi dengan Asam Oksalat (H2C2O4) menghasilkan ion Mn^2+."""    ,
        "Rumus Perhitungan Normalitas": """Rumus untuk menghitung normalitas (N) adalah :
        
    N(titran) = massa titrat(mg)/(BE(titrat) x Volume Akhir(mL))
        
    Notes : 
        ~ N adalah Normalitas (mgrek/mL)
        ~ BE adalah Berat ekuivalen titrat(mg/mgrek)
        ~ V adalah Volume akhir titrasi (mL)"""
    }

    return options.get(materi)

# Fungsi untuk menghitung mean dan standard deviation
def data_pengamatan(df, nama_column):
    # Ekstrak Spesifik Kolom
    column_data = df[nama_column]

    # Fungsi untuk menghitung Mean, Standar Deviasi dan %RSD
    hasil_mean = np.mean(column_data)
    hasil_std_dev = np.std(column_data)
    hasil_rsd = (hasil_std_dev / hasil_mean) * 100 if hasil_mean != 0 else 0
    
    # Desimal Hasil Akhir
    hasil_mean = round(hasil_mean, 4)
    hasil_rsd = round(hasil_rsd, 2)
    hasil_std_dev = round(hasil_std_dev, 6)

    # Menampilkan Hasil Kalkulasi
    st.info(f"Rata-rata dari {nama_column}: {hasil_mean}")
    st.info(f"Standar Deviasi dari {nama_column}: {hasil_std_dev}")
    st.success(f"%RSD dari {nama_column}: {hasil_rsd}%")

def table(num_rows):
    data = {
        "Sample (mg)": [0.00] * num_rows,
        "Volume Titran (mL)": [0.00] * num_rows,
        "Normalitas Titran (N)": [0.00] * num_rows
    }
    return pd.DataFrame(data)

def main():
    
    # Pilihan konten menggunakan selection box
    selected_content = st.radio(
        "Pilih konten :",
        ["Materi Utama", "Kalkulator Konsentrasi", "Kalkulasi %RSD"],
        horizontal=True,
    )
    st.header(" ", divider="gray")

    # Tampilk konten terkait
    if selected_content == "Kalkulator Konsentrasi":
        st.header("Kalkulator Konsentrasi")
        gram = st.number_input("Masukkan jumlah massa (mg):", min_value=0.00)
        volume = st.number_input("Masukkan volume (mL):", min_value=0.00)
        BE = st.number_input("Masukkan nilai BE Titrat:", min_value=0.00)
        if st.button("Kalkulasi"):
            if gram == 0 or volume == 0 or BE == 0:
                st.error("Pastikan untuk mengisi semua nilai.")
            else:
                result = konsentrasi(gram, volume, BE)
                result_rounded = round(result, 4)
                st.success(f"Hasil perhitungan Normalitas : {result_rounded} N")
            
    elif selected_content == "Materi Utama":
        st.header("Materi Utama")
        user_input = st.selectbox("Pilih topik : ", ["Pengertian Permanganometri", "Pemilihan Indikator", "Reaksi Umum", "Rumus Perhitungan Normalitas"])
        if st.button("Kirim"):
            response = materi_utama(user_input)
            text_area_height = min(max(len(response.split('\n')) * 20, 200), 600)  # Adjust height dynamically
            st.text_area("Penjawab:", value=response, height=text_area_height, disabled=True)
        
      
    elif selected_content == "Kalkulasi %RSD":
        st.header("Kalkulasi %RSD")
    
        # Edit Spesifik Kolom
        st.sidebar.header("Column Settings")
        num_rows = st.sidebar.number_input("Jumlah Baris", min_value=3, value=3)
        df = table(num_rows)
        # Use sidebar.checkbox for column selection with default value as True
        selected_columns = [col for col in df.columns if st.sidebar.checkbox(col, value=True)]

        # Input judul kolom untuk dikalkulasi
        column_index = st.selectbox("Pilih kolom untuk dikalkulasi :", df.columns)
        
        updated_df = df.copy()
        if len(selected_columns) > 0:
            df_edit = df[selected_columns]
            edited_df = st.data_editor(df_edit, height=None)
            if st.button("Kalkulasi"):
                for column in selected_columns:
                    updated_df[column] = edited_df[column]

                # Kalkulasi melalui fungsi data_pengamatan
                data_pengamatan(updated_df, column_index)

if __name__ == "__main__":
    main()
