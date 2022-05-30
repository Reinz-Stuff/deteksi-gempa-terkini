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
        soup = BeautifulSoup(content.text, 'html.parser')
        result = soup.find('span', {'class': 'waktu'})
        result = result.text.split(', ')
        tanggal = result[0]
        waktu = result[1]

        result = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li')

        i = 0
        magnitudo = None
        kedalaman = None
        ls = None
        bt = None
        lokasi = None
        dirasakan = None

        for res in result:
            print(i, res)
            if res == 1:
                magnitudo = res.text
            i += 1

        hasil = dict()
        hasil['tanggal'] = tanggal
        hasil['waktu'] = waktu
        hasil['magnitudo'] = magnitudo
        hasil['kedalaman'] = '41 km'
        hasil['koordinat'] = {'lat': 4.61, 'lng': 102.75}
        hasil['lokasi'] = 'Pusat gempa berada di laut 25 km baratdaya Bengkulu Selatan'
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
    print(f"waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"koordinat: lat= {result['koordinat']['lat']} lng= {result['koordinat']['lng']}")
    print(f"Lokasi {result['lokasi']}")
    print(f"Dirasakan {result['dirasakan']}")

# if __name__ == "__main__":
#     print('ini adalah package gempa terkini')
#     print ('hai')
