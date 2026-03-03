def funct(filename, number):

    hasil_akhir = []

    negative_number = (-number) & 0xFF
    
    with open(filename, 'rb') as f:

        data_bytes = f.read()

        for byte in data_bytes:

            hasil = (byte + negative_number) & 0xFF

            hasil_akhir.append(hasil)

    return hasil_akhir

print(funct('array.bin', 5))

# with open('array.bin', 'wb') as file:
#     binary = bytearray([11,2,5,4,43])
#     file.write(binary)