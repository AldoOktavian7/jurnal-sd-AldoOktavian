# views/dashboard_component.py

def fetch_data_from_api(api_function):
    print("[System] Mencoba menghubungkan ke API...")
    
    try:
        response = api_function()

        if response["status"] == "success":
            print("[Success] Data berhasil diambil dari API")
            return response["data"]

        else:
            error_message = response.get(
                "message",
                "Terjadi kesalahan pada server."
            )
            raise Exception(error_message)

    except Exception as e:
        print(f"[Error] Gagal Integrasi: {e}")
        return None


# Tambahkan fungsi ini di bawahnya agar app.py bisa mengimpornya
def render_dashboard(data):
    """
    Fungsi ini digunakan untuk menampilkan dashboard ke pengguna.
    """
    print("\n=== DASHBOARD UTAMA ===")
    if data is None:
        print("[Warning] Tidak ada data yang bisa ditampilkan.")
        return

    print(f"[UI] Menampilkan data dashboard: {data}")
    # Tulis logika tampilan komponen dashboard kamu di sini