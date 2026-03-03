def num_printable_bytes(filename):
    with open(filename, "rb") as file:
        count = 0
        for b in file.read():
            count += (0x20 <= b <= 0x7e)
        return count

filename = 'bytes.bin'
print(num_printable_bytes(filename))
