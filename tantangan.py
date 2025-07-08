# Tantangan 1.5.1 Python Syntax
print('Tege Manusia Biasa')

# Tantangan 1.6.1 Python Variables
x = 15
y = 'Hello World'
print(x)
print(y)

# Tantangan 1.7.1 Comment
# Komentar ini tidak akan dieksekusi
print('Komentar tidak dieksekusi')

# Tantangan 1.8.9 Python Data Types
a = 30
print(type(a))  # Output: <class 'int'>
b = 3.14
print(type(b))  # Output: <class 'float'>
c = 'Python'
print(type(c))  # Output: <class 'str'>
d = False
print(type(d))  # Output: <class 'bool'>
e = [1, 2, 3, 4, 5]
print(type(e))  # Output: <class 'list'>
f = (10, 9, 8, 7, 6)
print(type(f))  # Output: <class 'tuple'>
g = {1, 2, 3, 4, 5}
print(g)  # Output: {1, 2, 3, 4, 5}
print(type(g))  # Output: <class 'set'>
h = {'nama': 'Tege', 'umur': 20}
print(type(h))  # Output: <class 'dict'>
print(h)  # Output: {'nama': 'Tege', 'umur': 20}

# Tantangan 1.9.1 Python if else
num = 10
if num % 2 == 0:
    print('Genap')
else:
    print('Ganjil')

# Tantangan 1.9.3 
nilai = 75
if nilai >= 75:
    print('Lulus')
print('Selesai')

# Tantangan 1.9.5
nilai = 60
if nilai >= 85:
    print('A')
elif nilai >= 70:
    print('B')
elif nilai >= 55:
    print('C')
else:
    print('D')

# Tantangan 1.9.7
num = 10
if num > 0: print('Positif')

# Tantangan 1.9.9
nilai = 80
print('Lulus' if nilai >= 75 else 'Tidak Lulus')

# Tantangan 1.9.11
num = 15
if num > 0:
    print('Positif')
    if num % 2 == 0:
        print('Genap')
    else:
        print('Ganjil')
else:
    print('Negatif')

# Tantangan 1.9.13
num = 10
if num > 5:
    pass # Placeholder
print('Selesai')

# Tantangan 1.10.2
nama = ['Dika', 'Udin', 'Fajrul']
for i in nama:
    print(i)
    
# Tantangan 1.10.4
for i in 'Tege':
    print(i)
    
# Tantangan 1.10.6
angka = [1, 3, 5, 6, 7]
for i in angka:
    if i % 2 == 0:
        break
    print(i, 'Genap')

# Tantangan 1.10.8
for i in range(6):
    if i % 2 == 0:
        continue
    print(i)

# Tantangan 1.10.10
for i in range(2, 11, 2):
    print(i)
    
# Tantangan 1.10.12
for i in range(3):
    print(i)
else:
    print("Loop selesai")

# Tantangan 1.10.14
for huruf in ['A', 'B']:
    for angka in [1, 2]:
        print(huruf, angka)
 
# Tantangan 1.10.16       
for i in range(3):
    pass # Tidak melakukan apapun
print("Loop selesai")

# Tantangan 1.11.2
i = 1
while i <= 5:
    print(i)
    i += 1

# Tantangan 1.11.4
i = 1
while True:
    if i == 4:
        break
    print(i)
    i += 1

# Tantangan 1.11.6
i = 1
while i <= 5:
    if i % 2 != 0:
        i += 1
        continue
    print(i)
    i += 1

# Tantangan 1.11.8
i = 1
while i <= 3:
    print(i)
    i += 1
else:
    print("Loop selesai")
    
# Tantangan 1.12.4
def ucapan(nama):
    print(f"Selamat datang, {nama}!")

ucapan("Tege")

# Tantangan 1.12.6
def kurang(a, b):
    print(a - b)
    
kurang(5, 4)

# Tantangan 1.12.8
def cetak_nama(*nama):
    print('Nama pertama:', nama[0])
    
cetak_nama('Ali', 'Budi', 'Cici')

# Tantangan 1.12.10
def biodata(nama, hobi):
    print(f'Nama: {nama}, Hobi: {hobi}')
    
biodata(hobi='Membaca', nama='Tege')

# Tantangan 1.12.12
def cetak_info(**data):
    for key, value in data.items():
        print(f"{key}: {value}")
        
cetak_info(nama="Risky", umur=20, hobi="Coding")

# Tantangan 1.12.14
def salam(nama="Teman"):
    print(f"Halo, {nama}!")
    
salam()
salam("Tege")

# Tantangan 1.12.16
def jumlah_total(angka_list):
    total = sum(angka_list)
    print(f"Total: {total}")
    
jumlah_total([1, 2, 3, 4, 5])

# Tantangan 1.12.18
def kuadrat(x):
    return x ** 2

hasil = kuadrat(4)
print(hasil)

# Tantangan 1.12.20
def fungsi_kosong():
    # Fungsi ini akan diisi nanti
    pass

# Tantangan 1.12.22
def info(nama, umur, /):
    print(f"Nama: {nama}, Umur: {umur}")

info("Tege", 20)
info(nama="Risky", umur=20)

# Tantangan 1.12.24
def info(*, nama, umur):
    print(f"Nama: {nama}, Umur: {umur}")

info(nama="Tege", umur=20)
info("Risky", 20)

# Tantangan 1.12.26
def jumlah_rekursif(n):
    if n == 1:
        return 1
    return n + jumlah_rekursif(n - 1)
print(jumlah_rekursif(5))