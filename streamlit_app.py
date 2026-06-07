import streamlit as st

# ==========================
# KONFIGURASI HALAMAN
# ==========================

st.set_page_config(
    page_title="Kalkulator Bilangan Biner",
    page_icon="🔢",
    layout="wide"
)

st.title("🔢 Kalkulator Konversi Bilangan")
st.write("Konversi Bilangan Biner ↔ Desimal")

# ==========================
# SESSION STATE RIWAYAT
# ==========================

if "history" not in st.session_state:
    st.session_state.history = []

# ==========================
# LAYOUT
# ==========================

col1, col2 = st.columns([1,2])

# ==================================
# KOLOM TEORI
# ==================================

with col1:

    with st.container(border=True):

        st.subheader("📘 Teori Singkat")

        st.write("""
Bilangan biner adalah sistem bilangan berbasis 2 yang hanya menggunakan dua digit, yaitu 0 dan 1. Sistem ini menjadi dasar kerja komputer dan perangkat digital. Setiap digit biner disebut bit (binary digit).

Bilangan desimal adalah sistem bilangan berbasis 10 yang menggunakan digit 0 sampai 9 dan merupakan sistem bilangan yang paling umum digunakan dalam kehidupan sehari-hari.

Aplikasi ini digunakan untuk melakukan konversi antara bilangan biner dan bilangan desimal.
""")

# ==================================
# KOLOM KALKULATOR
# ==================================

with col2:

    menu = st.selectbox(
        "Pilih Jenis Konversi",
        [
            "Biner ke Desimal",
            "Desimal ke Biner"
        ]
    )

    # ==========================
    # BINER -> DESIMAL
    # ==========================

    if menu == "Biner ke Desimal":

        st.subheader("🔢 Biner → Desimal")

        biner = st.text_input(
            "Masukkan Bilangan Biner",
            placeholder="Contoh: 1011"
        )

        if st.button("Konversi"):

            if biner == "":

                st.warning(
                    "Masukkan bilangan terlebih dahulu"
                )

            elif not all(
                bit in "01"
                for bit in biner
            ):

                st.error(
                    "Gunakan hanya angka 0 dan 1"
                )

            else:

                hasil = int(
                    biner,
                    2
                )

                st.metric(
                    label="Hasil Desimal",
                    value=hasil
                )

                st.session_state.history.append(
                    f"{biner} → {hasil}"
                )

    # ==========================
    # DESIMAL -> BINER
    # ==========================

    else:

        st.subheader(
            "🔢 Desimal → Biner"
        )

        desimal = st.number_input(
            "Masukkan Bilangan Desimal",
            min_value=0,
            step=1,
            format="%d"
        )

        if st.button(
            "Konversi "
        ):

            hasil = bin(
                int(desimal)
            )[2:]

            st.metric(
                label="Hasil Biner",
                value=hasil
            )

            st.session_state.history.append(
                f"{int(desimal)} → {hasil}"
            )

# ==========================
# RIWAYAT
# ==========================

st.divider()

st.subheader(
    "📜 Riwayat Konversi"
)

if len(
    st.session_state.history
) == 0:

    st.write(
        "Belum ada riwayat"
    )

else:

    for item in reversed(
        st.session_state.history
    ):

        st.write(
            "•",
            item
        )

if st.button(
    "🗑 Hapus Riwayat"
):

    st.session_state.history = []

    st.rerun()

st.divider()

st.caption(
    "Made with ❤️ using Streamlit"
)
