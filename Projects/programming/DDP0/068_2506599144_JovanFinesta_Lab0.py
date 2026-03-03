# Lab 00 - Pendaftaran Ekspedisi
# BY TAW, ICO
import math as m

print("=== SELAMAT DATANG DI FORM PENDAFTARAN EKSPEDISI ===")

print()  # Blank line untuk meningkatkan readability

print("== DATA KAPTEN ==")

# Daftar input-input ========================================
nama_kapten = input('Nama Kapten: ')
tanggal_lahir = input('Tanggal Lahir: ')
tinggi_badan = input('Tinggi Badan (dalam cm): ')
tempat_tinggal = input('Tempat Tinggal: ')
zodiak = input('Zodiak: ')

print()  # Blank line untuk meningkatkan readability
print("== DATA KAPTEN BERHASIL DISIMPAN ✓ ==")
print()  # Blank line untuk meningkatkan readability

print("== DATA ROKET ==")

nama_roket = input('Nama Roket: ')
tinggi_roket = input('Tinggi Roket (dalam meter): ')
tujuan_ekspedisi = input('Tujuan Ekspedisi: ')
# End daftar input ========================================

# Assign hasil-hasil dari modul math ke variabel
pi = m.pi
akar2 = m.sqrt(2)
# Perhitungan kecepatan
# Formula percepatan: v(t) = π * t^2 + √2 * t
waktu_perjalanan = float(tinggi_roket) / 2
kecepatan_roket = pi * float(waktu_perjalanan)**2 + \
    akar2 * float(waktu_perjalanan)

print()  # Blank line untuk meningkatkan readability

# Output hasil pendaftaran
print("Terdaftar! Kapten Anda adalah", nama_kapten, "yang berasal dari", tempat_tinggal + ". "
      "Tanggal lahir kapten Anda adalah", tanggal_lahir, "dan memiliki tinggi badan", tinggi_badan, "cm. Zodiak dari kapten Anda adalah", zodiak + ". "
      "Anda ingin berekspedisi ke", tujuan_ekspedisi, "menggunakan roket", nama_roket, "yang memiliki tinggi", tinggi_roket, "m. "
      "Roket Anda akan mencapai kecepatan", kecepatan_roket, "m/s selama", waktu_perjalanan, "detik setelah lepas landas.")

print()  # Blank line untuk meningkatkan readability

print("==== TERIMA KASIH TELAH MENDAFTAR! SELAMAT MENJELAJAH! ====")
