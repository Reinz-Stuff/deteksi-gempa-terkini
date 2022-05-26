def huruf_abjad():
    abjad = dict()
    abjad['tanggal'] = '23 Mei 2022'
    abjad['pertama'] = 'abcde'
    abjad['kedua'] = 'fghij'

    return abjad


def shower_data(a):
    print(f"abjad pertama {a['tanggal']}")


if __name__ == '__main__':
    b = huruf_abjad()
    shower_data(b)



