import requests
from bs4 import BeautifulSoup


def ektraksi_data():
    """
    Tanggal       : 23 Mei 2022
    Waktu         : 19:32:02 WIB
    Magnitudo     : 4.9
    Kedalaman     : 41 km
    Lokasi        : LAT: 4.61 LON : 102.75
    Pusat Gempa   : Pusat gempa berada di laut 25 km baratdaya Bengkulu Selatan
    Dirasakan     : Dirasakan (Skala MMI): IV Manna, IV Argamakmur, IV Lampung Barat,
                    III-IV Kepahiang, III-IV Kota Bengkulu.
    :return:
    """
    try:
        content = requests.get('https://www.bmkg.go.id/')
    except Exception:
        return None
    if content.status_code == 200:
        print(content.text)

        # soup = BeautifulSoup(content)
        # print(soup.prettify())

        hasil = dict()
        hasil['tanggal'] = '23 Mei 2022'
        hasil['waktu'] = '19:32:02 WIB'
        hasil['magnitudo'] = 4.9
        hasil['kedalaman'] = '41 km'
        hasil['lokasi'] = {'lat': 4.61, 'lng': 102.75}
        hasil['pusat'] = 'Pusat gempa berada di laut 25 km baratdaya Bengkulu Selatan'
        hasil['dirasakan'] = 'Dirasakan (Skala MMI): IV Manna, IV Argamakmur,' \
                             ' IV Lampung Barat,III-IV Kepahiang, III-IV Kota Bengkulu.'
        return hasil
    else:
        return None


def tampilkan_data(result):
    if result is None:
        print('Tidak menemukan data gempa terkini')
        return
    print("Gempa terakhir berdasarkan BMKG")
    print(f"Tanggal {result['tanggal']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Lokasi lat= {result['lokasi']['lat']} lng= {result['lokasi']['lng']}")
    print(f"Pusat Gempa {result['pusat']}")
    print(f"Dirasakan {result['dirasakan']}")


# if __name__ == "__main__":
#     print('ini adalah package gempa terkini')
#     print ('hai')