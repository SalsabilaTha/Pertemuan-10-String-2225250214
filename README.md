# Pertemuan 10 - String dan Pengolahan Teks
## Identitas

- Nama: Salsabila Thahira
- NIM: 2225250214
- Kelas: 3B

## Tujuan

mempelajari penggunaan string pada Python untuk mengolah teks. Praktikum meliputi pengenalan string, indeks dan slicing, penggunaan method string, pembersihan teks, pemisahan dan penggabungan kata, serta pencarian kata.

## Cara Menjalankan

Pastikan Python sudah terpasang dan interpreter Python telah dipilih di VS Code.

Buka terminal VS Code, kemudian jalankan setiap latihan menggunakan perintah berikut.

python latihan/01_dasar_string.py
python latihan/02_indeks_slicing.py
python latihan/03_method_string.py
python latihan/04_bersihkan_teks.py
python latihan/05_split_join.py
python latihan/06_pencarian_kata.py

Untuk menjalankan Tugas 4, gunakan perintah:

python tugas/normalisasi_data_mahasiswa.py

Masukkan nama mahasiswa dan kode kelas ketika diminta oleh program.

## Algoritma

1. Meminta pengguna memasukkan nama lengkap mahasiswa.
2. Meminta pengguna memasukkan kode kelas.
3. Menghapus spasi berlebih dan mengubah nama ke format title case.
4. Mengubah kode kelas menjadi huruf kapital.
5. Mengganti pemisah spasi pada kode kelas dengan tanda hubung.
6. Menghitung jumlah kata pada nama lengkap.
7. Membuat inisial berdasarkan huruf pertama setiap kata nama.
8. Menampilkan nama bersih, kode kelas, jumlah kata, dan inisial.

## Test Case

<table>
  <thead>
    <tr>
      <th>No.</th>
      <th>Input Nama</th>
      <th>Input Kode</th>
      <th>Hasil yang Diharapkan</th>
      <th>Hasil Aktual</th>
      <th>Status</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>aan hendrayana</td>
      <td>pmat a 2026</td>
      <td>Aan Hendrayana / PMAT-A-2026 / 2 / AH</td>
      <td>Aan Hendrayana / PMAT-A-2026 / 2 / AH</td>
      <td>Sesuai</td>
    </tr>
    <tr>
      <td>2</td>
      <td>fATHIYYAH mUTHMAINNAH</td>
      <td>kelas b</td>
      <td>Fathiyyah Muthmainnah / KELAS-B / 2 / FM</td>
      <td>Fathiyyah Muthmainnah / KELAS-B / 2 / FM</td>
      <td>Sesuai</td>
    </tr>
    <tr>
      <td>3</td>
      <td>BUDI</td>
      <td>pmtk 01</td>
      <td>Budi / PMTK-01 / 1 / B</td>
      <td>Budi / PMTK-01 / 1 / B</td>
      <td>Sesuai</td>
    </tr>
    <tr>
      <td>4</td>
      <td>siti nur aisyah</td>
      <td>kelas c</td>
      <td>Siti Nur Aisyah / KELAS-C / 3 / SNA</td>
      <td>Siti Nur Aisyah / KELAS-C / 3 / SNA</td>
      <td>Sesuai</td>
    </tr>
  </tbody>
</table>

Keterangan: Urutan hasil pada tabel adalah nama bersih, kode kelas, jumlah kata, dan inisial. Hasil aktual diisi berdasarkan hasil pengujian program di VS Code.

## Refleksi

Salah satu masalah teks yang ditemukan adalah adanya spasi berlebih dan penggunaan huruf besar serta kecil yang tidak konsisten. Masalah tersebut diperbaiki menggunakan strip() dan split() untuk membersihkan spasi, title() untuk merapikan penulisan nama, serta upper() dan join() untuk menormalkan kode kela