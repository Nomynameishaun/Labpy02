# Labpy02\
Halo, tujuan saya membuat ini adalah untuk memenuhi tugas yang diberikan

# Program Diskon Tiket
![tiketflow](<tiketflow.png>)
## Input tipe tiket dan status member dari user
tipe_tiket = input("Masukkan tipe tiket (reguler/vip): ").lower()
member = input("Apakah Anda memiliki kartu member? (y/n): ").lower()

## Harga tiket
harga_reguler = 50000
harga_vip = 100000

## Menentukan harga awal berdasarkan tipe tiket
harga_awal = harga_reguler if tipe_tiket == "reguler" else harga_vip

## Menghitung total harga dengan diskon jika memiliki member
diskon = 0.2 * harga_awal if member == "y" else 0
total_harga = harga_awal - diskon

## Menampilkan hasil total harga yang harus dibayar
print(f"Total harga yang harus dibayar: Rp{total_harga}")





