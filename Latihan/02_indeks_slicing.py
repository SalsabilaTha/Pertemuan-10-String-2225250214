#Input: Teks "Pemrograman" yang sudah ditentukan.
#Proses: Mengakses karakter pertama dan terakhir, mengambil sebagian teks, serta membalik urutan teks.
#Output: Karakter pertama P, karakter terakhir n, teks "Pemr", teks "raman", dan teks terbalik "namargormeP".

teks = "Pemrograman"

print("Karakter pertama:", teks[0])
print("Karakter terakhir:", teks[-1])
print("Empat karakter pertama:", teks[:4])
print("Mulai indeks ke-4:", teks[4:])
print("Teks terbalik:", teks[::-1])