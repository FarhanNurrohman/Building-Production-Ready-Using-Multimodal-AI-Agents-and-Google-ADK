import os
from flask import Flask, jsonify, request
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Memuat konfigurasi environment variables dari file .env
load_dotenv()

app = Flask(__name__)

# Inisialisasi klien resmi Google GenAI SDK terbaru
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

@app.route("../app.py", methods=["POST"])
def analyze_multimodal_agent():
    try:
        # 1. Menangkap payload teks dari form request
        user_prompt = request.form.get("prompt", "Halo, berikan analisis dari input yang diberikan.")
        
        # 2. Menyiapkan System Instructions untuk mengarahkan perilaku AI Agent
        system_instruction = (
            "Anda adalah AI Agent profesional untuk analisis multimodal. "
            "Berikan respons yang terstruktur, akurat, analitis, dan langsung pada inti permasalahan."
        )

        # 3. Menyiapkan kontainer konten (multimodal hibrida: teks + file biner)
        contents = [user_prompt]

        # 4. Menangkap file biner (gambar/dokumen) jika dikirimkan dari frontend Streamlit
        if "file" in request.files:
            file = request.files["file"]
            if file.filename != "":
                # Mengonversi file biner menjadi Part yang didukung secara native oleh Google GenAI SDK
                file_part = types.Part.from_bytes(
                    data=file.read(),
                    mime_type=file.content_type or "application/octet-stream"
                )
                contents.append(file_part)

        # 5. Memanggil model Gemini menggunakan SDK resmi terbaru dengan parameter kontrol produksi
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=contents,
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                temperature=0.3,          # Kontrol kreativitas model
                max_output_tokens=1024,   # Batasan panjang token respons
            )
        )

        # 6. Mengembalikan respons teks ke frontend Streamlit
        return jsonify({
            "status": "success", 
            "result": response.text
        }), 200

    except Exception as e:
        return jsonify({
            "status": "error", 
            "message": str(e)
        }), 500

if __name__ == "__main__":
    # Menjalankan server Flask di port 5000 secara lokal
    app.run(debug=True, port=5000)