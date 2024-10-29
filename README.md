# Labpy02
Halo, repository ini saya buat untuk memenuhi tugas yang diberikan

# Program Diskon Tiket
## Flowchart
![tiketflow](<gambar/tiketflow.png>)
## Program
```ruby
tipe_tiket = input("Masukkan tipe tiket (reguler/vip): ").lower()
member = input("Apakah Anda memiliki kartu member? (y/n): ").lower()
harga_reguler = 50000
harga_vip = 100000
harga_awal = harga_reguler if tipe_tiket == "reguler" else harga_vip
diskon = 0.2 * harga_awal if member == "y" else 0
total_harga = harga_awal - diskon
print(f"Total harga yang harus dibayar: Rp{total_harga}")
```

## Langkah - langkah

### Input tipe tiket dan status member dari user
```ruby
tipe_tiket = input("Masukkan tipe tiket (reguler/vip): ").lower()
member = input("Apakah Anda memiliki kartu member? (y/n): ").lower()
```
### Harga tiket
```ruby
harga_reguler = 50000
harga_vip = 100000
```
### Menentukan harga awal berdasarkan tipe tiket
```ruby
harga_awal = harga_reguler if tipe_tiket == "reguler" else harga_vip
```
### Menghitung total harga dengan diskon jika memiliki member
```ruby
diskon = 0.2 * harga_awal if member == "y" else 0
total_harga = harga_awal - diskon
```
### Menampilkan hasil total harga yang harus dibayar
```ruby
print(f"Total harga yang harus dibayar: Rp{total_harga}")
```

Apabila program dieksekusi hasilnya akan seperti berikut:
![tiketvip](<gambar/tiketvip.png>)

# kalkulator
## Flowchart
![tiketflow](<gambar/kalkulator.png>)
## Program
```ruby
angka1 = float(input("Masukkan angka pertama: "))
operator = input("Masukkan operator (+, -, *, /): ")
angka2 = float(input("Masukkan angka kedua: "))

if operator == "+":
    hasil = angka1 + angka2
elif operator == "-":
    hasil = angka1 - angka2
elif operator == "*":
    hasil = angka1 * angka2
elif operator == "/":
    if angka2 != 0:
        hasil = angka1 / angka2
    else:
        hasil = "Error: Pembagian dengan nol tidak diperbolehkan."
else:
    hasil = "Operator tidak valid!"

print(f"Hasil: {hasil}")
```
## Langkah - langkah

### Meminta input dari user
```ruby
angka1 = float(input("Masukkan angka pertama: "))
operator = input("Masukkan operator (+, -, *, /): ")
angka2 = float(input("Masukkan angka kedua: "))
```
### Menghitung hasil berdasarkan operator yang dipilih
```ruby
if operator == "+":
    hasil = angka1 + angka2
elif operator == "-":
    hasil = angka1 - angka2
elif operator == "*":
    hasil = angka1 * angka2
elif operator == "/":
    if angka2 != 0:
        hasil = angka1 / angka2
    else:
        hasil = "Error: Pembagian dengan nol tidak diperbolehkan."
else:
    hasil = "Operator tidak valid!"
```
### Menampilkan hasil
```ruby
print(f"Hasil: {hasil}")
```

Apabila program dieksekusi hasilnya akan seperti berikut:
![tiketvip](<gambar/kalkulasi.png>)
