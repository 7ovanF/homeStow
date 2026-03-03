def normalisasi_ejaan(teks):
    # Kamus perubahan ejaan lama ke ejaan yang disempurnakan
    ejaan_lama_ke_baru = {
        "tj": "c",
        "dj": "j",
        "nj": "ny",
        "ch": "kh",
        "sj": "sy",
        "oe": "u",
        "j": "y"
    }

    # Pecah teks menjadi kata-kata
    for lama, baru in ejaan_lama_ke_baru.items():
        if lama in teks:
            teks = teks.replace(lama, baru)
    return teks

print(normalisasi_ejaan('kami bangsa indonesia dengan ini menjatakan, sesoenggoehnja'))
            