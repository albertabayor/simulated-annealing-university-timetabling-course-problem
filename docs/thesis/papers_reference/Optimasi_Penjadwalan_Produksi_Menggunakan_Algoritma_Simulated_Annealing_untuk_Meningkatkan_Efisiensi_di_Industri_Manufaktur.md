Jurnal Komputer dan Teknologi Informasi
Vol. 3, No. 2, Juli 2025, pp. 44~47
E-ISSN: 2986-7592, DOI: 10.26714/jkti.v3i2.16382



1

Optimasi Penjadwalan Produksi Menggunakan Algoritma
Simulated Annealing untuk Meningkatkan Efisiensi di Industri
Manufaktur
Sholikin1, Ahmad Ilham, S.Kom., M.Kom. 2
1

Program Studi Informatika, Fakultas Teknik dan Ilmu Komputer Universitas Muhammadiyah Semarang, Semarang, Indonesia
2
Program Studi Informatika, Fakultas Teknik dan Ilmu Komputer Universitas Muhammadiyah Semarang, Semarang, Indonesia

Info Artikel
Diterima 10 Mei 2025
Perbaikan 13 Juni 2025
Disetujui 28 Juli 2025

Keywords:
Penjadwalan Produksi
Simulated Annealing
Traveling Salesman Problem
Optimasi

ABSTRAK
Penjadwalan produksi adalah aspek penting dalam manajemen operasional
manufaktur untuk mengurangi waktu produksi, menghemat biaya, dan
meningkatkan efisiensi. Penelitian ini mengevaluasi algoritma metaheuristik
Simulated Annealing (SA) dalam menyelesaikan masalah penjadwalan,
menggunakan dataset Traveling Salesman Problem (TSP) dari Kaggle.
Algoritma SA bekerja secara iteratif dengan mengeksplorasi solusi secara
acak dan menghindari perangkap solusi lokal. Hasil menunjukkan bahwa SA
efektif menemukan solusi mendekati optimal dengan waktu produksi
minimum 52,55 pada generasi ke-20 dan rata-rata waktu eksekusi 1,67 detik
per iterasi. Penelitian ini mengindikasikan bahwa SA cocok untuk
penjadwalan produksi skala menengah. Studi lanjutan dapat mengembangkan
kombinasi SA dengan algoritma lain untuk skenario yang lebih kompleks.

ABSTRACT
Production scheduling is a crucial aspect of operational management in
manufacturing to reduce production time, save costs, and improve efficiency.
This study evaluates the Simulated Annealing (SA) metaheuristic algorithm in
addressing scheduling problems using the Traveling Salesman Problem (TSP)
dataset from Kaggle. The SA algorithm operates iteratively by exploring
random solutions and avoiding local optima traps. The results show that SA
effectively finds near-optimal solutions with a minimum production time of
52.55 at the 20th generation and an average execution time of 1.67 seconds
per iteration. This study indicates that SA is suitable for medium-scale
production scheduling. Future studies could develop combinations of SA with
other algorithms for more complex scenarios.

Ini adalah artikel akses terbuka di bawah lisensi CC BY-SA.

Penulis Korespondensi:
Sholikin
Program Studi Informatika, Fakultas Teknik Universitas Muhammadiyah Semarang
Alamat: Gedung FT-MIPA Lt. 7, Ruang 707, Jl.Kedungmundu Raya No.18, Semarang 50273, Indonesia
Email: sholikin.alafasy7@gmail.com

1.

PENDAHULUAN
Dalam industri manufaktur, penjadwalan produksi menjadi salah satu aspek penting dalam manajemen
operasional untuk memastikan kelancaran proses produksi. Penjadwalan yang optimal dapat mengurangi waktu
produksi, menghemat biaya, meningkatkan efisiensi sumber daya, serta memenuhi tenggat waktu pengiriman.

Journal homepage: http://ijeecs.iaescore.com

2



E-ISSN: 2986-7592

Tantangan utamanya adalah kompleksitas masalah penjadwalan yang seringkali sangat tinggi dan bersifat
kombinatorial, sehingga solusi optimal sulit dicapai dalam waktu singkat. [1]
Masalah penjadwalan produksi dapat dipandang sebagai kasus dari masalah Traveling Salesman Problem
(TSP), di mana setiap tugas diibaratkan sebagai kota yang perlu dikunjungi satu kali dalam urutan tertentu
dengan biaya atau jarak minimum. Pendekatan klasik membutuhkan waktu komputasi yang tinggi, terutama
untuk skala data besar. Oleh karena itu, algoritma heuristik dan metaheuristik banyak diterapkan untuk
mencapai solusi mendekati optimal secara efisien. [2]
Salah satu metode metaheuristik yang efektif adalah Simulated Annealing (SA), yang meniru proses fisika
pemanasan dan pendinginan material untuk mencari struktur dengan energi minimum. Dalam konteks
penjadwalan, algoritma SA dapat mengeksplorasi ruang solusi secara acak untuk menemukan urutan tugas
dengan waktu produksi minimum. Pendekatan ini memanfaatkan probabilitas penerimaan solusi suboptimal
untuk menghindari perangkap solusi lokal, sambil tetap mengarah pada konvergensi menuju solusi yang lebih
baik seiring penurunan suhu. [3]
Penelitian ini bertujuan untuk mengevaluasi kinerja algoritma Simulated Annealing dalam konteks
penjadwalan produksi. Dataset TSP dari Kaggle digunakan sebagai data nyata dalam eksperimen ini untuk
menguji kemampuan SA dalam mengoptimalkan urutan produksi pada kasus skala menengah. Dengan hasil
ini, diharapkan dapat dihasilkan pemahaman yang lebih dalam tentang keunggulan dan keterbatasan SA dalam
menyelesaikan masalah penjadwalan produksi di industri manufaktur.
2.

METODE
Algoritma Simulated Annealing adalah teknik metaheuristik yang terinspirasi dari proses fisika annealing,
yaitu pemanasan dan pendinginan material untuk mencapai struktur minimal energi. Dalam konteks optimasi,
SA bekerja dengan mencari solusi dari ruang solusi secara acak dan iteratif. Setiap iterasi, algoritma memilih
solusi baru dengan sedikit perubahan dari solusi sebelumnya. Jika solusi baru lebih baik, maka solusi tersebut
diterima; jika tidak, solusi dapat diterima dengan probabilitas yang ditentukan oleh parameter suhu. Secara
bertahap, suhu diturunkan sehingga algoritma semakin selektif terhadap solusi yang dipilih, memungkinkan
konvergensi menuju solusi optimal.
SA diterapkan pada masalah penjadwalan produksi di mana setiap tugas harus dijadwalkan dalam urutan
tertentu pada mesin-mesin. Algoritma ini menggunakan fungsi biaya yang menghitung waktu total produksi,
dan parameter suhu serta koefisien pendinginan untuk mengontrol proses pencarian solusi.
3.

DATA DAN IMPLEMENTASI
Dataset yang digunakan berasal dari kumpulan data Traveling Salesman Problem (TSP) yang tersedia di
Kaggle (https://www.kaggle.com/datasets/mexwell/traveling-salesman-problem), diadaptasi untuk kasus
penjadwalan produksi. Data ini berisi koordinat kota yang mewakili tugas-tugas dalam urutan tertentu.
Implementasi algoritma dilakukan di Google Colab menggunakan Python, khususnya pustaka seperti Pandas
untuk pengolahan data dan Matplotlib untuk visualisasi hasil.
Pertama, dataset diubah menjadi matriks jarak antar tugas yang kemudian digunakan sebagai masukan
untuk SA. Algoritma ini menginisialisasi populasi dengan beberapa solusi acak, dan pada setiap iterasi, solusi
diperbarui berdasarkan fungsi biaya yang ditentukan dari waktu total produksi. Implementasi menggunakan
proses mutasi dan pemilihan untuk menemukan solusi terbaik dari populasi solusi.
4.

HASIL DAN ANALISIS
Eksperimen dilakukan dengan menggunakan dataset TSP yang berisi koordinat titik-titik yang
merepresentasikan tugas atau pekerjaan yang perlu diselesaikan dalam urutan tertentu. Algoritma Simulated
Annealing diimplementasikan dalam Google Colab menggunakan Python. Proses eksperimen dimulai dengan
inisialisasi populasi solusi acak, di mana setiap solusi mewakili urutan tugas yang berbeda. Kemudian,
algoritma menjalankan proses iteratif dengan penurunan suhu secara bertahap, di mana setiap iterasi bertujuan
menemukan solusi yang lebih baik dari segi waktu produksi total.

J Kom & Tek Info, Vol. 3, No. 2,Juli 2025: p.44~47

3
J Kom & Tek Info

E-ISSN: 2986-7592



Hasil eksperimen menunjukkan bahwa Simulated Annealing berhasil menemukan solusi yang cukup
efisien dengan waktu eksekusi yang relatif cepat. Pada konfigurasi tertentu, SA berhasil mencapai nilai fitness
terbaik sebesar 52,55 pada generasi ke-20, yang mencerminkan total waktu produksi minimum dalam urutan
yang optimal untuk kasus ini. Rata-rata waktu eksekusi setiap iterasi mencapai 1,67 detik, yang menunjukkan
bahwa algoritma ini efisien untuk data dengan skala menengah. Visualisasi rute optimal yang diperoleh
menunjukkan pengurangan waktu produksi yang signifikan, dengan urutan tugas yang lebih singkat
dibandingkan urutan awal acak.
Algoritma SA mampu melakukan eksplorasi ruang solusi dengan cukup baik, meskipun beberapa iterasi
menerima solusi yang sedikit lebih buruk untuk menghindari jebakan solusi lokal. Penggunaan
singlePointCrossover menghasilkan variasi solusi yang optimal, dengan peningkatan fitness secara bertahap
pada tiap generasi. Pengujian beberapa konfigurasi suhu awal dan koefisien pendinginan juga memberikan
dampak pada hasil akhir, di mana suhu awal yang lebih tinggi cenderung membantu algoritma keluar dari
solusi lokal yang tidak optimal.

Secara keseluruhan, hasil menunjukkan bahwa Simulated Annealing efektif dalam menangani masalah
penjadwalan produksi, terutama untuk skala data menengah. Namun, untuk dataset yang lebih besar atau
skenario produksi yang lebih kompleks, pendekatan ini mungkin memerlukan penyesuaian lebih lanjut pada
parameter algoritma atau kombinasi dengan teknik metaheuristik lainnya untuk meningkatkan hasil optimasi.
5.

KESIMPULAN
Penggunaan algoritma Simulated Annealing dalam penjadwalan produksi terbukti efektif dalam
mengurangi waktu total produksi dan menemukan solusi mendekati optimal dengan efisiensi waktu yang baik.
Implementasi ini dapat menjadi solusi yang relevan bagi industri manufaktur untuk meningkatkan efisiensi
Optimasi Penjadwalan Produksi Menggunakan Algoritma Simulated Annealing untuk Meningkatkan
Efisiensi di Industri Manufaktur (Sholikin)



4

E-ISSN: 2986-7592

operasional. Penelitian lebih lanjut dapat mengkaji penggunaan algoritma lain atau kombinasi beberapa
algoritma metaheuristik untuk meningkatkan hasil optimasi.
REFERENSI
[1]
[2]
[3]

T. Morton, and D.W. Pentico, Heuristic Scheduling Systems: With Application to Production Systems and Project Management,
John Wiley & Sons, New York, 1993.
F.A. Ogbu and D.K. Smith, “Simulated Annealing for the Permutation Flowshop Problem”, Omega The International Journal of
Management Science, 19(1), pp. 64-67, 1990.
M.L. Pinedo, Scheduling:Theory, Algorithm and Systems, 3rd Ed.Prentice Hall, New Jersey, 2008.

J Kom & Tek Info, Vol. 3, No. 2,Juli 2025: p.44~47

