import streamlit as st
import requests
import time

FLASK_API_URL = "http://127.0.0.1:5000/api/analyze"

st.set_page_config(page_title="Multimodal Flask + Streamlit Agent", layout="wide")

st.markdown("""
    <style>
    .main-header {
        font-size: 2.2rem;
        color: #1F6FEB;
        font-weight: 700;
    }
    .sub-text {
        color: #656D76;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h2 class="main-header">🚀 Production-Grade Multimodal AI Agent</h2>', unsafe_allow_html=True)

col_input, col_output = st.columns([1, 1], gap="large")
with col_input:
    st.subheader("📥 Input Data & Dokumen")
    
    # Kotak unggah file dengan border rapi
    uploaded_file = st.file_uploader(
        "Unggah Gambar / Dokumen Pendukung:", 
        type=["jpg", "jpeg", "png", "pdf"],
        help="Mendukung format gambar dan dokumen untuk analisis visual/teks."
    )
    
    # Text area untuk instruksi
    user_input = st.text_area(
        "Instruksi atau Pertanyaan Analisis:", 
        placeholder="Contoh: Analisis dokumen laporan ini dan berikan ringkasan keuangan...", 
        height=180
    )
    
    # Tombol aksi utama dengan lebar penuh
    submit_btn = st.button("🔍 Jalankan Analisis AI", use_container_width=True)


with col_output:
    st.subheader("📊 Hasil Output")
    
    output_container = st.container(border=True)

    with output_container:
        if submit_btn:
            if not user_input:
                st.warning("⚠️ Mohon masukkan instruksi teks terlebih dahulu.")

            with st.spinner("⏳ Menghubungkan ke Flask Backend & Memproses Gemini..."):
                try:
                    FLASK_API_URL = "http://127.0.0.1:5000/api/analyze"
                                    
                    user_prompt = {"prompt": user_input}
                    file_payload = None
                                    
                    if uploaded_file is not None:
                        file_payload = {
                            "file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)
                            }
            
                        # Mengirim request ke Flask Backend
                        response = requests.post(FLASK_API_URL, data=user_prompt, files=file_payload)
            
                        if response.status_code == 200:
                            result = response.json()
                            st.success("✅ Analisis Berhasil & Tervalidasi Pydantic!")
                                        
                            # Menampilkan hasil JSON dari backend
                            output_data = result.get("data") or result.get("result", str(result))
                            st.code(output_data, language="json")
                        else:
                            st.error(f"❌ Server merespons dengan error (Status Code: {response.status_code})")
                            st.json(response.text)
                                        
                except requests.exceptions.ConnectionError:
                    st.error("❌ Koneksi Ditolak! Pastikan server Flask backend sudah dinyalakan di terminal (`python app.py`).")
                except Exception as e:
                    st.error(f"❌ Terjadi kesalahan sistem: {e}")
        else:
            st.info("👈 Silakan masukkan input di sebelah kiri lalu klik 'Jalankan Analisis AI'.")

st.markdown('<p class="sub-text">Workshop DevFest Cloud Surabaya: Building Production-Ready Using Multimodal AI Agents And Google ADK.</p>', unsafe_allow_html=True)