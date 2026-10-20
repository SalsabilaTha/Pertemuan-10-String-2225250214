#Input: Kalimat "data teks perlu dibersihkan".
#Proses: Memisahkan kalimat menjadi list kata menggunakan split() dan menggabungkan kata dengan tanda hubung menggunakan join().
#Output: List ['data', 'teks', 'perlu', 'dibersihkan'] dan teks "data-teks-perlu-dibersihkan".

kalimat = "data teks perlu dibersihkan"

kata = kalimat.split()

print("Daftar kata:", kata)
print("Kata dengan tanda hubung:", "-".join(kata))