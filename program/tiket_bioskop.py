tipe_tiket = input("Masukkan tipe tiket (reguler/vip): ").lower()
member = input("Apakah Anda memiliki kartu member? (y/n): ").lower()

harga_reguler = 50000
harga_vip = 100000

harga_awal = harga_reguler if tipe_tiket == "reguler" else harga_vip

diskon = 0.2 * harga_awal if member == "y" else 0
total_harga = harga_awal - diskon

print(f"Total harga yang harus dibayar: Rp{total_harga}")