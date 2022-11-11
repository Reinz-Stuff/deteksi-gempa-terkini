"""
Aplikasi Deteksi Gempa terkini
"""
import gempa_terkini

if __name__ == "__main__":
    print(f'Aplikasi utama menggunakan package yang memiliki deskripsi {gempa_terkini.description}')
    result = gempa_terkini.ektraksi_data()
    gempa_terkini.tampilkan_data(result)