import streamlit as st

# Konfigurasi halaman
st.set_page_config(
    page_title="Kalkulator Bilangan Biner",
    page_icon="🔢",
    layout="centered"
)

# Judul
st.title("🔢 Kalkulator Konversi Bilangan Biner")
st.write("Konversi Bilangan Biner ↔ Desimal")

st.divider()

# ==========================
# TEORI SINGKAT
# ==========================

st.subheader("📘 Teori Singkat")

st.write("""
Bilangan biner adalah sistem bilangan berbasis 2 yang hanya menggunakan dua digit, yaitu 0 dan 1. Sistem ini menjadi dasar kerja komputer dan perangkat digital. Setiap digit biner disebut bit (binary digit).

Bilangan desimal adalah sistem bilangan berbasis 10 yang menggunakan digit 0 sampai 9 dan merupakan sistem bilangan yang paling umum digunakan dalam kehidupan sehari-hari.

Aplikasi ini digunakan untuk melakukan konversi antara bilangan biner dan bilangan desimal.
""")

st.divider()

# ==========================
# PILIH KONVERSI
# ==========================

menu = st.selectbox(
    "Pilih Jenis Konversi",
    ["Biner ke Desimal", "Desimal ke Biner"]
)

# ==========================
# BINER -> DESIMAL
# ==========================

if menu == "Biner ke Desimal":

    st.subheader("Konversi Biner ke Desimal")

    biner = st.text_input(
        "Masukkan Bilangan Biner",
        placeholder="Contoh: 1011"
    )

    if st.button("Konversi ke Desimal"):

        if biner == "":
            st.warning("Masukkan bilangan biner terlebih dahulu")

        else:

            try:

                if all(bit in "01" for bit in biner):

                    hasil = int(biner, 2)

                    st.success(
                        f"Hasil konversi {biner}₂ = {hasil}₁₀"
                    )

                else:

                    st.error(
                        "Input tidak valid. Gunakan hanya angka 0 dan 1"
                    )

            except:

                st.error("Terjadi kesalahan input")


# ==========================
# DESIMAL -> BINER
# ==========================

elif menu == "Desimal ke Biner":

    st.subheader("Konversi Desimal ke Biner")

    desimal = st.number_input(
        "Masukkan Bilangan Desimal",
        min_value=0,
        step=1,
        format="%d"
    )

    if st.button("Konversi ke Biner"):

        hasil = bin(int(desimal))[2:]

        st.success(
            f"Hasil konversi {int(desimal)}₁₀ = {hasil}₂"
        )

st.divider()

st.caption("Made with ❤️ using Streamlit")
