import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_form = Image.open("images/kosim1.jpg")
img_lottie_animation = Image.open("images/seminar.jpeg")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Segera daftarkan diri anda :wave:")
    st.title("Seminar Digital Bussiness dan Web Programing")
    st.write(
        " Life Skill and workshop pembuatan website dengan teknologi Framework Laravel bersama Gautama S.W ,S.E,BBA,MM dan Ir.Made Sukawardika Dipl.SE."
    )
    st.write("[www.pttus.co.id ](https://pttus.co.id)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Pelatihan Gelombang Petama  27 dan 28 Januari 2023 di Kedai KOSIM Kertosono Nganjuk Jawa Timur")
        st.write("##")
        st.write(
            """
            Seminar dapat diikuti secara online dan offline di Kedai Kosim Kertosono mulai pukul 09.00 W.I.B
            dengan ketentuan :
            HTM offline : Rp. 75.000 (include snack dan coffe break)
            HTM Online  : Rp. 50.000 (include voucer kedai Kosim)
            Sertifikat keikut sertaan seminar dengan keterampilan dasar web programing website Laravel 
            Bimbingan Konsultasi pembuatan website bila telah memiliki domain hosting sendiri
            Keanggotaan Komunitas Laravel Jawa Timur
            Ditransfer ke rek Made Sukawardika BCA 0900881070 , lampirkan bukti transfer pada form pendaftaran

          
            """
        )
       
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header(" Even Community Laravel Jatim :")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Seminar Web Programming")
        st.write(
            """
            Seminar dan workshop pembuatan website dengan bahasa pemrograman Framework PHP Laravel,
            meliputi teori dasar dan praktek pemuatan website sederhana, dan latihan deploy ke cpanel domain hosting :
            1. Modul dasar pemrograman dan setting lingkungan pemrograman
            2. Prosedur dasar pembuatan web aplikasi
            3. Pengembangan website dengan thema gratis download
            4. Uji coba prosedur deploy atau upload web aplikasi Laravel ke share hosting atau C Panel
            """
        )
        
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Kedai Kopi Siang Malam Kertosono Nganjuk Jawa Timur ")
        st.write(
            """
            Kedai Kosim Kertosono pelopor cafe masakini, yang menyajikan minuman dan makanan yang berkualitas dan menjadi
            tempat bukan sekedar nongkrong tetapi sekaligus meningkatkan pengetahuan 
            """
        )
        st.markdown("[Tonton Kedai Kosim](https://www.youtube.com/watch?v=ItFJDgV0Mbk&t=26s)")
        
# ---- CONTACT ----
with st.container():
    st.write("---")
    st.subheader("Silahkan daftar melalui form pesan ini,lampirkan foto bukti transfernya!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form method="POST" action="https://formsubmit.co/sukawardika@gmail.com" enctype="multipart/form-data">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name=" Nama" placeholder=" Nama Lengkap" required>
        <input type="email" name="Email" placeholder=" Email yang masih aktip" required>
        <input type="text" name="Telephone" placeholder=" Nomor HP" required>
        <input type="text" name="Tanggal Sesi" placeholder=" Ketik Tanggal sesi yg diikuti 27 atau 28 Januari 2023" required>
        <textarea name="Alamat" placeholder=" Alamat lengkap  secara jelas" required></textarea>
        <input type="file" name="attachment" accept="image/png, image/jpeg">
        <button type="submit">Send /Kirim</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
