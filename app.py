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
img_contact_form = Image.open("images/caput.png")
img_lottie_animation = Image.open("images/tus1.png")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, Apa khabar perkenalkan saya Mbahde :wave:")
    st.title("Asisten teknis komputer  PT Thaufiq Unun Sejahtera")
    st.write(
        " Nama lengkap Ir.Made Sukawardika Dipl.SE, sebagai pengrajin IT yg telah puluhan tahun bergelut dengan berbagai teknis informasi  akan sharing khusus tentang Framework PHP Laravel dan wawasan web programing terkini lainnya."
    )
    st.write("[www.pttus.co.id ](https://pttus.co.id)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Rencana Pelatihan Januari 2023 di Kedai KOSIM Kertosono Nganjuk")
        st.write("##")
        st.write(
            """
            Dalam pengenalan program web aplikasi dan pembuatan website meliputi:
            1. Setting Laptop
            2. Download dan Install Program yang dibutuhkan
            3. Pengenalan VC , PHP , HTML ,CSS, Bootstrap,Laravel ,Gitbush,Python,Streamlit
            4. Download thema bootstrap untuk pembuatan website Laravel
            5. Pembuatan website dengan Framework Laravel
            6. Latihan Deploy website atau upload ke C Panel

            Bila para peserta sbg kelanjutannya ingin berkomunikasi bertanya dapat menghubungi hp : 085234100496 dan email : sukawardika@gmail.com
            """
        )
       
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header(" Website Laravel portofolio :")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Website PT Thaufiq Unun Sejahtera www.pttus.co.id")
        st.write(
            """
            Website PT TUS dibuat dengan frame work Laravel didalam website tersebut terdapat web aplikasi tentang sistem admin inventory pengelolaan kegiatan usaha
            """
        )
        
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Website tentang calon Bupati Kabupaten Buleleng Bali www.doktercaput.com ")
        st.write(
            """
            Website ini memuat aplikasi database calon konstituen dan berbagai dokumentasi kegiatan selama kandidat ini bersosialisasi,website ini sedikit lebih kompleks juga dibuat dengan framework Laravel.
            """
        )
        st.markdown("[Tonton Video Dokter Caput](https://www.youtube.com/watch?v=2sjGho5CX1o)")
        
# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Silahkan daftar melalui form pesan ini!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/sukawardika@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="Nama" placeholder="Nama lengkap" required>
        <input type="email" name="Email" placeholder=" Email yang masih aktip" required>
        <input type="text" name="Telephone" placeholder=" Nomor HP" required>
        <input type="text" name="Tanggal Sesi" placeholder=" Ketik Tanggal sesi yg diikuti 27 atau 28 Januari 2023" required>
        <textarea name="Alamat" placeholder=" Alamat lengkap  secara jelas" required></textarea>
        <button type="submit">Kirim</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
