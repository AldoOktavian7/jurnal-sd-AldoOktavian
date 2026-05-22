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