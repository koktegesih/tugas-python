# Parkir

motor = 5000
mobil = 7000

jenisKendaraan = input("Jenis kendaraan (motor/mobil): ").lower()
lamaParkir = int(input("Lama parkir (dalam jam): "))

if jenisKendaraan == "motor":
    biaya = motor * lamaParkir
elif jenisKendaraan == "mobil":
    biaya = mobil * lamaParkir
else:
    biaya = 0
    print("Jenis kendaraan tidak tersedia.")
    exit()

namaTukangParkir = input("Masukkan nama tukang parkir: ")
igTukangParkir = input("Masukkan akun Instagram tukang parkir: ")
uang = float(input("Masukkan jumlah uang Anda: "))

if uang >= biaya:
    kembalian = uang - biaya
    print("======= Nota Parkir =======")
    print(f"Tukang Parkir      : {namaTukangParkir}")
    print(f"Akun Instagram     : {igTukangParkir}")
    print(f"Jenis Kendaraan    : {jenisKendaraan}")
    print(f"Lama Parkir        : {lamaParkir} jam")
    print(f"Biaya Parkir       : Rp{biaya:,.2f}")
    print(f"Uang Pembayaran    : Rp{uang:,.2f}")
    print(f"Kembalian          : Rp{kembalian:,.2f}")
    print("============================")
else:
    print("Uang Anda tidak cukup untuk membayar biaya parkir.")
    print("Silakan coba lagi dengan jumlah uang yang lebih besar.")