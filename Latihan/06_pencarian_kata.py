#Input: Teks "Python untuk data. Python untuk pendidikan." dan kata "python".
#Proses: Mengubah teks menjadi huruf kecil, memeriksa keberadaan kata, menghitung kemunculan, dan mencari posisi pertama kata.
#Output: Kata ditemukan bernilai True, jumlah kemunculan sebanyak 2 kali, dan posisi pertama pada indeks 0.

teks = "Python untuk data. Python untuk pendidikan."

teks = teks.lower()
kata = "python"

print("Apakah kata ditemukan?", kata in teks)
print("Jumlah kemunculan:", teks.count(kata))
print("Posisi pertama:", teks.find(kata))