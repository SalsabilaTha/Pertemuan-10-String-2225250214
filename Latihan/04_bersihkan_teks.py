#Input: Teks " belajar    python  untuk           pendidikan       " yang memiliki spasi berlebih.
#Proses: Menghapus spasi di awal dan akhir, merapikan spasi antar kata menjadi satu spasi, dan mengubah huruf pertama menjadi kapital.
#Output: Teks "Belajar python untuk pendidikan" yang sudah dibersihkan.

teks = " belajar    python  untuk           pendidikan       "

teks = " ".join(teks.split())

print("Teks setelah dibersihkan:", teks.capitalize())