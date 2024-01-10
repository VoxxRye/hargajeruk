# Masukkan harga barang per kg dalam rupiah
harga_per_kg = 5000

# Masukkan besar diskon
besar_diskon = 0.05

# Masukkan berat buah jeruk yang dibeli dalam kg
berat_jeruk = float(input("Masukkan berat buah jeruk yang dibeli (dalam kg): "))

# Hitung total harga sebelum diskon
total_harga_sebelum_diskon = harga_per_kg * berat_jeruk

# Hitung diskon sebesar 5%
diskon = total_harga_sebelum_diskon * besar_diskon

# Hitung total harga setelah diskon
total_harga_setelah_diskon = total_harga_sebelum_diskon - diskon

# Tampilkan hasil perhitungan
print("Total harga sebelum diskon: Rp", total_harga_sebelum_diskon)
print("Diskon: Rp", diskon)
print("Total harga setelah diskon: Rp", total_harga_setelah_diskon)