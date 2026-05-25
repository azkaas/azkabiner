import streamlit as st

st.set_page_config(page_title="Kalkulator Biner & Desimal")

st.title("🔢 Kalkulator Konversi Bilangan")
st.write("Konversi Bilangan Biner ↔ Desimal")

menu = st.selectbox(
    "Pilih Jenis Konversi",
    ["Biner ke Desimal", "Desimal ke Biner"]
)

# =========================
# Biner ke Desimal
# =========================
if menu == "Biner ke Desimal":

    biner = st.text_input("Masukkan Bilangan Biner")

    if st.button("Konversi ke Desimal"):

        try:
            # validasi biner
            if all(bit in "01" for bit in biner):

                desimal = int(biner, 2)

                st.success(f"Hasil Desimal: {desimal}")

            else:
                st.error("Input harus berupa angka biner (0 dan 1 saja)")

        except:
            st.error("Terjadi kesalahan input")


# =========================
# Desimal ke Biner
# =========================
elif menu == "Desimal ke Biner":

    desimal = st.number_input(
        "Masukkan Bilangan Desimal",
        min_value=0,
        step=1
    )

    if st.button("Konversi ke Biner"):

        biner = bin(int(desimal))[2:]

        st.success(f"Hasil Biner: {biner}")
