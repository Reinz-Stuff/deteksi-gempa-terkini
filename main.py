"""
Aplikasi Deteksi Gempa terkini
"""
import gempa_terkini

if __name__ == "__main__":
    print('Aplikasi utama')
    result = gempa_terkini.ektraksi_data()
    gempa_terkini.tampilkan_data(result)