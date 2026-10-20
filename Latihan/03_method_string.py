#Input: Nama " fATHIYYAH mUTHMAINNAH         " yang memiliki spasi berlebih dan huruf tidak beraturan.
#Proses: Menghapus spasi di awal dan akhir, mengubah huruf awal setiap kata menjadi kapital, dan mengubah seluruh huruf menjadi kapital.
#Output: Nama tanpa spasi tepi, "Fathiyyah Muthmainnah", dan "FATHIYYAH MUTHMAINNAH".

nama = " fATHIYYAH mUTHMAINNAH         "

print("Nama asli:", nama)
print("Nama tanpa spasi tepi:", nama.strip())
print("Nama format title:", nama.strip().title())
print("Nama huruf besar:", nama.strip().upper())