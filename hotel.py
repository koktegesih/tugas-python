# Hotel Coconut

namaHotel = "Hotel Coconut"
frontEnd = 150000
backEnd = 200000
system = 250000

print(f"--- Selamat datang di {namaHotel} ---")

nama = input("Masukkan nama Anda: ")
jenisKamar = input("Masukkan jenis kamar (FrontEnd/BackEnd/System): ").lower()
jumlahHari = int(input("Masukkan lama menginap (dalam hari): "))
jumlahOrang = int(input("Masukkan jumlah orang yang menginap: "))

# Hitung biaya menginap
if jenisKamar == "frontend":
    biaya = jumlahHari * frontEnd
elif jenisKamar == "backend":
    biaya = jumlahHari * backEnd
elif jenisKamar == "system":
    biaya = jumlahHari * system
else:
    biaya = 0
    print("Jenis kamar tidak tersedia.")
    exit()

hari = input("Hari pemesanan, Senin-Minggu: ").lower()
jamCekIn = float(input("Masukkan jam check-in (00.00-23.00): "))
jamCekOut = float(input("Masukkan jam check-out (00.00-23.00): "))
metodePembayaran = input("Masukkan jenis pembayaran (Cash/Qris/Kredit): ").lower()

if jumlahOrang > 3:
    biaya += 100000 * jumlahHari

if hari == "jumat":
    biaya -= (biaya * 0.10)

if jamCekOut > jamCekIn:
    biaya += (150000 * (jamCekOut - jamCekIn))

if metodePembayaran == "cash":
    if biaya > 50000:
        biaya -= (biaya * 0.10)
elif metodePembayaran == "qris":
    if biaya > 500000:
        biaya -= (biaya * 0.15)
elif metodePembayaran == "kredit":
    if biaya > 500000:
        biaya -= (biaya * 0.05)
else:
    print("Metode pembayaran tidak dikenali.")
    exit()
    
print(f"Total biaya: Rp{biaya:,.2f}")
    
uang = float(input("Masukkan jumlah uang Anda: "))

if uang >= biaya:
    kembalian = uang - biaya
    print("======= Nota Pembayaran =======")
    print(f"Hotel             : {namaHotel}")
    print(f"Nama pelanggan    : {nama}")
    print(f"Jenis kamar       : {jenisKamar}")
    print(f"Lama menginap     : {jumlahHari} hari")
    print(f"Jumlah orang      : {jumlahOrang}")
    print(f"Jam Check-In      : {jamCekIn}")
    print(f"Jam Check-Out     : {jamCekOut}")
    print(f"Metode Pembayaran : {metodePembayaran}")
    print(f"Total bayar       : Rp{biaya:,.2f}")
    print(f"Uang Pembayaran   : Rp{uang:,.2f}")
    print(f"Kembalian         : Rp{kembalian:,.2f}")
    print("================================")
else:
    print("Mohon Maaf, Uang anda kurang!")
    print("Silakan coba lagi dengan jumlah uang yang lebih besar.")