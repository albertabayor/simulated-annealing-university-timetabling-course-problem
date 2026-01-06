Journal Industrial Servicess Vol. 4 No. 1 Oktober 2018

Penerapan Algoritma Simulated Annealing untuk meminimasi Makespan
pada Penjadwalan Flow Shop

Yusraini Muharni
Jurusan Teknik Industri Universitas Sultan Ageng Tirtayasa Cilegon
Jl. Jend. Sudirman Km. 3 Cilegon, Banten 42435
E-mail: yusraini@untirta.ac.id

ABSTRAK
Penjadwalan produksi merupakan proses alokasi sumber-sumber atau mesin-mesin yang ada untuk
menjalankan serangkaian tugas dalam jangka waktu tertentu. Penjadwalan produksi adalah sarana yang
diperlukan oleh perusahaan untuk menyusun suatu prioritas pekerjaan (job). PT XYZ merupakan perusahaan
yang bergerak dibidang manufaktur yang memproduksi bar mill dan section mill. Selama ini, Perusahaan
menghadapi kendala yaitu waktu penyelesaian seluruh pesanan yang cukup lama. Untuk Tipe bar mill yang
memiliki permintaan cukup tinggi adalah tipe D.16, D.19, D.22, D.25 dan D.32. Pendekatan Simulated
Annealing diterapkan untuk mendapatkan jadwal optimal sehingga dapat menurunkan nilai makespan.
Kata Kunci: Flowshop, Makespan, Penjadwalan, Simulated Annealing.

109

Journal Industrial Servicess Vol. 4 No. 1 Oktober 2018

Dalam produksinya ke lima produk tersebut
menggunakan lintasan dan mesin yang sama yang
membedakan adalah waktu prosesnya saja. Tipe
aliran pada proses pembuatan bar mill tersebut
adalah flowshop dengan 7 mesin. Jenis mesin yang
digunakan yaitu mesin reheating furnace, roughing
stand, intermediate stand, finishing stand, cooling
bed, cold shear dan stacking machine. Urutan
pengerjaan job dilakukan tidak menggunakan
metode apapun dan terkadang pengerjaan job
dilakukan dari urutaan permintaaan tanpa melihat
banyaknya permintaan sehingga PT XYZ membuat
produk jika ada pesanan atau make to order, waktu
penyelesaian untuk seluruh job menjadi lama.
Minimasi makespan yang dilakukan dapat
memendekan waktu penyelesaian seluruh job,
sehingga dapat mencapai target produksi dan dapat
meningkatkan kapasitas produksi. Tujuan dalam
penelitian ini yaitu mencari urutan produksi yang
optimal dan meminimasi nilai makespan atau total
waktu produksi.

1.

PENDAHULUAN
Penjadwalan produksi didefinisikan sebagai
proses pengalokasian sumber-sumber atau mesinmesin yang ada untuk menjalankan sekumpulan
tugas dalam jangka waktu tertentu. Penjadwalan
produksi sangat diperlukan oleh perusahaan untuk
menyusun suatu prioritas pekerjaan (job). Suatu
proses produksi perlu dijadwalkan mendapatkan
suatu penugasan pekerjaan yang paling efektif pada
setiap stasiun kerja dengan tujuan meningkatkan
produktivitas, mengurangi makespan, mengurangi
persediaan barang setengah jadi (work in process),
mengurangi keterlambatan dan meminimasi ongkos
produksi (Baker & Trietsch, 2013).
Berdasarkan pola aliran produksi, ada dua
jenis penjadwalan produksi yaitu penjadwalan job
shop dan penjadwalan flow shop (Baker & Trietsch,
2013). Pada penelitian ini permasalahan
penjadwalan difokuskan pada pola aliran flow shop
yang sesuai dengan kondisi di lapangan. Hampir
semua permasalahan utama dari lantai produksi
flow shop sebuah perusahaan adalah masalah
penjadwalan produksi, terutama dalam menentukan
efisiensi urutan pekerjaan (job) yang akan
dikerjakan agar menghasilkan nilai makespan yang
kecil sehingga kapasitas produksi dapat lebih besar
dan biaya produksi tidak terlalu tinggi.
Permasalahan
penjadwalan
permutation
flowshop merupakan permasalahan yang memiliki
n job dengan waktu proses pada m mesin. Urutan
operasi job pada semua mesin adalah searah untuk
masing-masing job dan sama pada setiap mesin
(Aulia, 2012). Penjadwalan permutation flowshop
merupakan masalah combinatorial optimization.
Selain itu juga permasalahan combinatorial
optimization merupakan Non Polynomial-hard
(NP-hard)
Metode Simulated Annealing merupakan
metode metaheuristik yang dapat diterapkan pada
persoalan permutation flowshop problem sehingga
diharapkan mampu memberikan solusi dalam
menyelesaikan permasalahan terkait penjadwalan
permutation flow shop
PT XYZ merupakan perusahaan yang
bergerak dibidang manufaktur yang memproduksi
bar mill dan section mill. Produk Bar mill yang
diproduksi oleh PT XYZ terdiri dari 2 jenis bar
mill yaitu bar mill deformed dan bar mill plain
dengan diameter yang berbeda – beda. Berikut
adalah jenis produk bar mill yang paling tinggi
permintaannya yaitu tipe D.16, D.19, D.22, D.25
dan D.32.

2.
2.1

TINJAUAN PUSTAKA
Penjadwalan
Penjadwalan produksi didefinisikan sebagai
proses pengalokasian sumber-sumber atau mesinmesin yang ada untuk menjalankan sekumpulan
tugas dalam jangka waktu tertentu (Baker &
Trietsch, 2013). Penjadwalan merupakan proses
pengambilan keputusan yang mempunyai peran
yang penting dalam kebanyakan industri
manufaktur dan jasa.
Input dari sistem penjadwalan antara lain
pekerjaan-pekerjaan yang merupakan alokasi
kapasitas untuk order-order, penugasan prioritas
job,
dan
pengendalian
jadwal
produksi
membutuhkan informasi
terperinci dimana
informasi-informasi tersebut akan menyatakan
masukan dari penjadwalan. Untuk memastikan
bahwa suatu aliran kerja yang lancar akan melalui
beberapa tahapan produksi maka sistem
penjadwalan harus membentuk aktivitas-aktivitas
output yaitu loading, sequencing, dispatching dan
pengendalian kinerja penjadwalan
Tujuan dari penjadwalan diantaranya adalah
mengurangi
waktu
proses,
meningkatkan
produktivitas, mengurangi persediaan barang
setengah
jadi,
mengurangi
keterlambatan,
membantu pengambilan keputusan mengenai
perencanaan kapasitas pabrik dan jenis kapasitas
yang dibutuhkan, mengurangi waktu mesin
menganggur dan meminimasi ongkos produksi.

110

Journal Industrial Servicess Vol. 4 No. 1 Oktober 2018

Prosedur diatas diilustrasikan pada Gambar 1

2.2

Metode Simulated Annealing
Sejak dipublikasikan oleh Kirkpatrick,
Metode Simulated Annealing (SA) adalah salah
satu metode metaheuristik yang banyak diterapkan
dalam
memecahkan
persoalan
optimasi
kombinatorial (Ishibuchi, 1995).
Algoritma
Simulated Annealing (SA) bekerja dengan meniru
proses annealing untuk memecahkan persoalan
optimisasi. SA menggunakan parameter suhu yang
mengontrol pencarian. Parameter suhu biasanya
dimulai dari suhu tinggi dan secara perlahan
menurun pada setiap iterasi. Pada tiap-tiap iterasi
satu titik baru dibangkitkan dan jaraknya terhadap
titik semula merupakan proporsional terhadap suhu.
Jika titik yang baru mempunyai nilai fungsi yang
lebih baik, maka titik tersebut menggantikan titik
semula dan penghitungan iterasi dinaikkan. Adalah
hal yang mungkin untuk berpindah ke titik yang
lebih buruk, hal ini terkait secara langsung pada
pengaruh suhu. Langkah seperti ini terkadang
membantu menemukan area pencarian baru dalam
upaya mendapatkan nilai mimimum yang lebih
baik (Liao, Tjandradjaja, & Chung, 2012).
Prosedur standar untuk menerapkan algoritma
Simulated Annealing adalah:
Langkah 1: pada saat i=0, Inisialisasi solusi
awal, s0 secara random dan temperature awal,
x0
Langkah 2: Inisialisasi solusi awal, s0 secara
random dari wilayah terdekat S(x0). Naikkan
nilai i=i+1
Langkah 3: Tentukan fungsi penurunan
temperature (jadwal pendinginan), dalam
makalah ini fungsi pendinginan mengikuti
persamaan:
T(k)= x0 x ()k

Mulai

Set Temperatur awal dengan
nilai yang cukup tinggi

Update Temperature

Tidak

Bangkitkan Ruang
Solusi terdekat

Nilai fitness
lebih baik ?

Pindah ke titik terdekat

Titik terdekat = Solusi baru

Ya

Tidak

Solusi baru >
Solusi terbaik

Ya

Solusi baru = Solusi
terbaik

Selesai

Gambar 1. Framework Algoritma Simulated
Annealing
3.

METODE PENELITIAN
Berikut ini merupakan flow chart penelitian
yang terdapat dalam penelitian yang dilakukan di
PT. XYZ:

Langkah 4 : Perpindahaan x0  x1 , sehingga
ı = f (s) − f (s0) If ı < 0 s0 = s
selain itu bangkitkan r∼U(0, 1) jika r <
exp(−ı/t) maka s0 = S
Langkah 5: f (s) > f (s0) maka solusi terbaik
diperoleh

111

Journal Industrial Servicess Vol. 4 No. 1 Oktober 2018

pada gambar 3. Adapun urutan penjadwalan yang
peroleh adalah:

Mulai

Studi Literatur

Observasi Lapangan

Rumusan Masalah

Tujuan Penelitian

Batasan Masalah

Pengumpulah Data :
1. Data Permitaan Produk Bar Mill
2. Jam kerja karyawan
3. Stasiun kerja dan proses produksi
4. Data jumlah mesin dan kapasitas
mesin
5 Waktu proses
6. . Waktu set up

Gambar 3. Luaran Penjadwalan dengan
Algoritma Simulated Annealing

Pengolahan Data :
1.Mentransformasi algoritma Simulated annealing dengan bahasa
pemrograman MATLAB
2. Membuat penjadwalan mesin dengan algoritma Simulated
Annealing

5.
Analisa

KESIMPULAN

Penjadwalan hasil luaran algoritma Simulated
Annealing memberikan nilai makespan 319 jam,
sedangkan makespan pada penjadwalan awal
adalah 721.87 jam.

Kesimpulan dan Saran

Selesai

6.

SARAN
Adapun saran untuk penelitian selanjutnya
antara lain :

Gambar 2. Diagram Alir Metode Penelitian

1. Penelitian
selanjutnya
dapat
membandingkan
beberapa
pendekatan
metaheuristik dalam persoalan penjadwalan.
2. Pengembangan algoritma metaheuristik
untuk persoalan penjadwalan pada kasus
mesin bottleneck
3. Mengambil kasus pada perusahaan dengan
aliran job shop.

4.

HASIL DAN PEMBAHASAN
Pemecahan persoalan penjadwalan mesin
dengan algoritma Simulated Annealing dilakukan
dengan bantuan perangkat lunak MATLAB.
Algoritma Simulated Annealing dikustomisasi
untuk memecahkan persoalan penjadwalan
flowshop dengan 5 order yang harus dijadwalkan
kedalam 7 mesin. Persoalan penjadwalan multi
prosessor
sendiri
terdiri dari menemukan
distribusi optimal dari penempatan tugas pada
sekelompok mesin Waktu yang dibutuhkan untuk
menyelesaikan tugas pada satu prosesor sudah
dikumpulkan dalam file data. Tiap-tiap prosessor
bekerja secara independen, tetapi masing-masing
prosesor hanya dapat memproses 1 job pada satu
waktu. Tujuan dari masalah ini adalah menentukan
jadwal terpendek untuk serangkaian tugas yang
harus dikerjakan.
Proses optimasi dengan Algoritma Simulated
Annealing diperoleh setelah iterasi mendekati nilai
1000 dengan t0= 474,7969, hal ini dapat dilihat

DAFTAR PUSTAKA
Baker, K. R., & Trietsch, D. (2013). Principles of
sequencing
and
scheduling.
https://doi.org/10.1002/9780470451793
Ishibuchi, H. (1995). Modified Simulated
Annealing algorithms for the flow shop
sequencing problem.
Liao, C., Tjandradjaja, E., & Chung, T. (2012). An
approach using particle swarm optimization
and bottleneck heuristic to solve hybrid flow
shop scheduling problem. Applied Soft
Computing Journal, 12(6), 1755–1764.
https://doi.org/10.1016/j.asoc.2012.01.011
Aulia, Indra. (2012). Penerapan Harmony Search
Algorithm dalam Permasalahan Penjadwalan
112

Journal Industrial Servicess Vol. 4 No. 1 Oktober 2018

Flow Shop. Universitas Sumatera Utara.
Medan.
Firdaus, Muhammad. (2015). Penjadwalan
Flowshop Dengan Menggunakan Simulated
Annealing. Universitas Muhammadiyah Malang

113

