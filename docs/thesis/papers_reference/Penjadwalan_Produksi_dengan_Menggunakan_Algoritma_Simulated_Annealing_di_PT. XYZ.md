TALENTA Conference Series: Energy & Engineering

R

PAPER – OPEN ACCESS

Penjadwalan Produksi dengan Menggunakan Algoritma Simulated
Annealing di PT. XYZ
Author
DOI
Electronic ISSN
Print ISSN

: Mulya Sultoniq Lubis dan Rosnani Ginting
: 10.32734/ee.v2i3.758
: 2654-704X
: 2654-7031

Volume 2 Issue 3 – 2019 TALENTA Conference Series: Energy & Engineering (EE)

This work is licensed under a Creative Commons Attribution-NoDerivatives 4.0 International License.
Published under licence by TALENTA Publisher, Universitas Sumatera Utara

EE Conference Series 02 (2019)

TALENTA Conference Series
Available online at https://talentaconfseries.usu.ac.id

Penjadwalan Produksi dengan Menggunakan Algoritma Simulated
Annealing di PT. XYZ
Mulya Sultoniq Lubis1, Rosnani Ginting2
1

2

Jl. Bahagia, Padang Bulan, Kota Medan 20155, Indonesia
Kampus USU, Jl. Almamater, Padang Bulan, Kota Medan 20155, Indonesia
1mulya.usu@yahoo.com, 2rosnani_usu@yahoo.co.id

Abstrak
PT. XYZ adalah perusahaan yang bergerak di bidang manufaktur yang memproduksi cangkir plastik. Produksi dilakukan
berdasarkan pesanan pelanggan (job order). Penjadwalan produksi yang diterapkan pada perusahaan sesuai dengan urutan job pada
pesanan. Job yang datang pertama harus diselesaikan terlebih dahulu dari job lain (yang memiliki batas waktu pengerjaan yang
sama). Hal ini memberikan dampak terhadap keterlambatan pengiriman produk ke tangan konsumen. Keterlambatan pengiriman
produk dapat dihindarkan melalui penjadwalan produksi di perusahaan guna meminimalkan waktu penyelesaian produk
(makespan). Algoritma heuristik yang digunakan dalam penelitian ini adalah Simulated Annealing. Algoritma Simulated Annealing
termasuk dalam algoritma heuristik karena memiliki potensi besar untuk menyelesaikan permasalahan optimasi. Parameter yang
0
digunakan adalah temperatur awal (Ti) sebesar 200 C, faktor suhu reduksi (s) sebesar 0,95, iterasi sebanyak 15 kali. Waktu
Penyelesaian produk (makespan) pada Algoritma Simulated adalah 20149,89 menit. Dapat disimpulkan bahwa dengan
menggunakan metode usulan tersebut, maka terdapat pengurangan makespan sebesar 4418.86 menit = 75,65 jam = 3,06 hari.
Sehingga penjadwalan job tidak terjadi keterlambatan dari due date yang telah ditetapkan yaitu 14 hari. Sehingga dapat disimpulkan
Algoritma Simulated Annealing lebih efektif daripada metode First Come First Served.
Kata kunci: Penjadwalan produksi; Makespan; Algoritma Heuristik, Simulated Annealing.
Abstract
PT. XYZ is a manufacturing company that produces plastic and joly cups based on customer orders (job orders). The clear plastic
cup product is the company's flagship product because it is always ordered by customers in large quantities. The company
implements production scheduling according to the order of the jobs on the order, where every first job that comes must be
completed first from another job (which has the same deadline for processing). This has an impact on late delivery of products to
consumers. To avoid delays in product shipments, it is necessary to schedule production at the company to minimize product
turnaround time (makespan). This study uses a Simulated Annealing Algorithm. Simulated Annealing algorithm is a type of
heuristic method because it has a great potential to solve the optimization problem, where the parameters used are initial
temperature (Ti) of 2000C, reduction of temperature factor (s) of 0.95, the number of iterations by 15 times. The initial solution to
the Simulated Annealing Algorithm uses the First Come First Served method. From the results of the study, the makepan produced
on the First Come First Served method was 24568.75 minutes, while the Simulated Annealing Algorithm method was 20149.89
minutes. It can be seen that by using the proposed method, there is a reduction in makespan of 4418.86 minutes = 75.65 hours =
3.06 days. So that job scheduling can be fulfilled on time and there are no delays from the due date set at 14 days. So it can be
concluded that the Simulated Annealing Algorithm is more effective than the First Come First Served method
Keywords: Production scheduling, Simulated Annealing Algorithm, Flow Shop, Makespan.

c 2019 The Authors. Published by TALENTA Publisher Universitas Sumatera Utara
Selection and peer-review under responsibility of The 3nd National Conference on Industrial Engineering (NCIE)
2019
p-ISSN: 2654-7031, e-ISSN: 2654-704X, DOI: 10.32734/ee.v2i3.758

398

Mulya Sultoniq Lubis dan Rosnani Ginting / EE Conference Series 02 (2019)

1. Pendahuluan
Hampir di setiap perusahaan manufaktur pasti memiliki serangkaian proses produksi untuk menghasilkan produk.
Proses produksi dapat berjalan dengan baik apabila diikuti dengan pekerja dan fasilitas yang sesuai dengan kebutuhan
perusahaan. Mengefisienkan pekerja merupakan salah satu hal yang sangat berpengaruh terhadap peningkatan
produktivitas.
Penjadwalan merupakan kegiatan mengalokasikan sumber daya yang terbatas untuk menyelesaikan sejumlah
pekerjaan. Keterbatasan sumber daya yang dimiliki menimbulkan proses penjadwalan sehingga diperlukan adanya
pengaturan sumber-sumber daya tersebut secara efisien. Unit-unit produksi (resources) dapat dimanfaatkan secara
optimum dengan dilakukan pengurutan pekerjaan ini. Berbagai model penjadwalan telah dikembangkan untuk
mengatasi persoalan penjadwalan tersebut (Rosnani, 2016).
Penjadwalan Flowshop adalah suatu unit-unit yang bergerak secara terus menerus melalui suatu rangkaian stasiunstasiun kerja yang disusun berdasarkan produk. Sumber daya yang dialokasikan pada pejadwalan flowshop akan
dilewati oleh setiap job secara berurutan. Setiap job memiliki urutan tahap atau rute pengerjaan yang sama. Kriteria
yang digunakan memmpengaruhi ukuran performansi penjadwalan, antara lain: total waktu untuk penyelesaian semua
job minimum (makespan), rata-rata keterlambatan yang minimum (mean tardiness), rata-rata waktu penyelesaian
setiap job yang minimum (mean flow time), dan sebagainya.Penentuan jadwal yang memenuhi seluruh kriteria yang
ada sangat sulit untuk dilakukan. Oleh karena itu, minimasi makespan dapat mewakili seluruh kriteria yang ada.
Annealing adalah satu teknik yang dikenal dalam bidang metalurgi, digunakan dalam mempelajari proses
pembentukan kristal dalam suatu materi. Agar dapat terbentuk susunan kristal yang sempurna, diperlukan pemanasan
sampai suatu tingkat tertentu, kemudian dilanjutkan dengan pendinginan yang perlahanlahan dan terkendali dari
materi tersebut. Pemanasan materi di awal proses annealing, memberikan kesempatan pada atom-atom dalam materi
itu untuk bergerak secara bebas, mengingat tingkat energi dalam kondisi panas ini cukup tinggi. Proses pendinginan
yang perlahan-lahan memungkinkan atom-atom yang tadinya bergerak bebas itu, pada akhirnya menemukan tempat
yang optimum, di mana energi internal yang dibutuhkan atom itu untuk mempertahankan posisinya adalah minimum
(Santosa dan Willy 2011).
PT. XYZ menggunakan sistem flowshop pada produksinya. Perusahaan dalam permintaannya bersifat make to
order yang menyadari akan pentingnya ketepatan waktu penyelesaian. Penjadwalan produksi dilakukan dengan aturan
First Come First Served (FCFS). Pada penjadwalan FCFS ini, order yang tiba lebih dahulu akan dilayani lebih dahulu.
Pada PT. XYZ masih ditemukan beberapa jadwal yang tidak tepat. Hal ini dikarenakan besarnya waktu
penyelesaian (makespan) yang terdapat di lantai pabrik.
Data Keterlambatan diatas menunjukan adanya keterlambatan order yang terjadi sebanyak 11 kali dalam satu
tahun,. Diperlukan adanya metode penjadwalan produksi yang tepat untuk menghindari hal semacam ini. Dengan
adanya metode penjadwalan produksi yang tepat, diharapkan total waktu penyelesaian keseluruhan produk
(makespan) menjadi lebih singkat. Berdasarkan masalah yang telah diuraikan, model alternatif model yang akan
dianalisis adalah model penjadwalan Algoritma Simulated Annealing.
Data pada jurnal ini diperoleh dari tugas sarjana Sarah Hutahaean dengan judul Penjadwalan Produksi dengan
Menggunakan Algoritma Simulated Annealing di PT. XYZ.
Pada PT. XYZ jumlah order per bulan yaitu sebanyak 164 order, dengan total produksi sebanyak 61.100 buah,
dan jumlah keterlambatan yaitu sebanyak 11 order per 12 periode.

2. Metodologi Penelitian
Penelitian ini termasuk kedalam penelitian deskriptif (Deskriptive Research) yaitu suatu penelitian yang
memaparkan masalah terhadap suatu masalah yang ada sekarang berdasarkan data secara sistematis. (Sukaria
Sinulingga, 2019). Pada penelitian ini meliputi proses pengumpulan, penyajian dan pengolahan data serta analisa dan
interpretasi.
Penelitian dilakukan di PT. XYZ. Jenis penelitian ini adalah penelitian deskriptif yaitu suatu jenis penelitian
yang bertujuan untuk mendeskripsikan secara sistematik, faktual dan akurat tentang fakta-fakta dan sifat-sifat suatu

Mulya Sultoniq Lubis dan Rosnani Ginting / EE Conference Series 02 (2019)

399

objek atau populasi tertentu. Objek penelitian ini adalah proses pembuatan Cangkir Plastik Bening. Alasan pemilihan
produki jenis ini adalah karena Cangkir Plastik Bening merupakan produk yang paling banyak dipesan oleh pelanggan.
Langkah-langkah pengolahan data adalah sebagai berikut:
1. Melakukan uji keseragaman dan kecukupan data.
2. Menghitung waktu normal dan waktu standar.
3. Menghitung waktu total penyelesaian (proses) pada tiap tipe produk.
4. Menghitung makespan awal dengan Metode FCFS (First Come First Served).
5. Menentukan penjadwalan produksi dengan menggunakan Algoritma Simulated Annealing.
Variabel penelitian yang digunakan dalam penelitian ini, yaitu:
1. Variabel Dependen
Variabel dependen adalah variabel penelitian yang nilainya ditentukan oleh variabel lain (bebas). Variabel yang
termasuk dalam kategori ini, yaitu:
a. Penjadwalan Optimal
Variabel ini menunjukkan urutan penjadwalan yang paling optimum dengan kriteria makespan terkecil.
2. Variabel Independen
Variabel independen adalah variabel penelitian yang nilainya tidak dipengaruhi oleh variabel lain. Variabel yang
termasuk dalam kategori ini, yaitu:
a. Waktu Proses
Varibel ini menunjukkan waktu proses tiap work center.
b. Jumlah Order
Variabel ini menunjukkan banyaknya unit produk yang diminta oleh konsumen per periode dimana
ukurannya dilihat dalam satuan unit.
c. Urutan Job
Variabel ini menunjukkan job mana yang lebih diprioritaskan untuk diproduksi terlebih dahulu dimana
ukurannya dilihat dalam kode.
Berikut ini merupakan block diagram dari pengolahan data yang digunakan:

Gambar 1. Block Diagram Pengolahan Data Simulated Annealing

Tujuan dari penelitian ini dapat diuraikan menjadi dua bagian, yaitu:
1. Tujuan Umum
Tujuan umum yang ingin dicapai adalah untuk mendapatkan suatu model penjadwalan yang mampu memberikan
nilai makespan yang minimum dengan menggunakan metode Algoritma Simulated Annealing.
2. Tujuan Khusus
Tujuan khusus yang ingin dicapai adalah untuk mendapatkan suatu kondisi optimum dari penjadwalan yang
dilakukan diantaranya:
a. Mengaplikasikan metode Simulated Annealing dalam mengurutkan job-job yang akan diproses disetiap stasiun
kerja.

400

Mulya Sultoniq Lubis dan Rosnani Ginting / EE Conference Series 02 (2019)

b. Meminimisasi total waktu pengerjaan seluruh jenis produk (makespan) sehingga dapat meminimalkan
keterlambatan.
Data yang digunakan dalam pemecahan masalah penjadwalan, adalah:
Gambar 3. Flow Chart Simulated Annealing dalam Pengurutan Job

1. Data Primer. Data primer adalah data yang diperoleh langsung dari pengamatan di lapangan dengan menggunakan
tool untuk mengukur data-data secara langsung. Instrumen yang digunakan adalah stopwatch dengan merk ROXSW8-2008 untuk mengukur waktu proses. Data primer pada penelitian ini, yaitu
a. Waktu siklus dan waktu set up pada tiap work center, diperoleh melalui pengukuran waktu, dimana instrumen
yang digunakan adalah stopwatch.
b. Rating factor diperoleh melalui pengukuran yang diamati pada saat operator sedang bekerja pada setiap stasiun
kerja.
c. Faktor kelonggaran (allowance), diperoleh melalui pengamatan secara langsung pada saat operator sedang
bekerja.
d. Data jumlah stasiun kerja, diperoleh melalui wawancara di PT. XYZ.
e. Data jumlah mesin di setiap stasiun kerja, diperoleh melalui wawancara di PT. XYZ.
2. Data Sekunder. Data sekunder adalah data yang diperoleh dari perusahaan tanpa melakukan pengukuran atau
pengamatan secara langsung yang diperoleh dari arsip-arsip perusahaan. Data sekunder pada penelitian ini, yaitu:
a. Tipe dan spesifikasi produk.
b. Data jumlah permintaan (order).
c. Gambaran umum perusahaan.
Perbandingan Kriteria Performansi Penjadwalan yang Dilakukan oleh Pihak Perusahaan dengan yang Dilakukan
dengan Simulated Annealing (SA). Prosedur penelitian dapat dilihat melalui blok diagram pada Gambar 3.

Mulya Sultoniq Lubis dan Rosnani Ginting / EE Conference Series 02 (2019)

401

3. Hasil dan Pembahasan
Data permintaan yang dikumpulkan dalam penelitian ini diambil dari permintaan cangkir plastik bening pada bulan
Juli 2013. Data permintaan produk dapat dilihat pada Tabel 2
Tabel 2. Data Permintaan Produk

No
1
2
3
4
5
6

Kode
Job 1
Job 2
Job 3
Job 4
Job 5
Job 6

Tipe Produk
MGT 20
MK AD 110
MK 125 D
MG 180
MK EM 180
MGA 150

Jumlah (Pcs)
1.800.000
900.000
300.000
750.000
1.350.000
1.200.000

Data permintaan yang dikumpulkan dalam penelitian ini diambil dari permintaan cangkir plastik bening pada bulan
Juli 2013.
Data yang diambil merupakan data jumlah mesin yang terdapat pada masing-masing stasiun kerja, jumlah operator,
waktu setup setiap mesin, jam kerja dan jumlah shift. Data kapasitas work center setiap periode dapat dilihat pada
Tabel 3.
Tabel 3. Data Kapasitas Work center

Stasiun Kerja
Proses mixing

Jumlah

Waktu
Jumlah
Setup
Operator/Mesin

Mesin
(unit)

(menit)

(orang)

(jam)

1

10

2

8

3

1

20

1

8

3

1

25

1

8

3

Mesin Die
Heater

1

15

1

8

3

Mesin Roll
Jumbo

1

10

2

8

3

Mesin Dong
Long

3

10

3

8

3

Nama
Mesin
Mesin Mixer

Jam
Kerja/Hari

Jumla
h

material
Pemanasan
material

Mesin Barel

bagian I

Heater

Penyaringan
material

Mesin
Screen
Heater

Pemanasan
Material
bagian I
Pencetakan
gulungan
material
Pencetakan
Cangkir
Plastik Bening

Proses produksi dibagi ke dalam enam stasiun kerja (WC). Uraian pekerjaan pada setiap stasiun kerja dapat dilihat
sebagai berikut:
1.
WC I : Proses mixing material (Nomor proses T-1, I-1, T-2, O-1)
2.
WC II : Proses pemanasan material bagian I (Nomor proses T-3, O-2)
3.
WC III: Proses Penyaringan material (Nomor proses O-3)
4.
WC IV: Proses pemanasan material bagian II (Nomor proses T-5, O-4)
5.
WC V : Proses pencetakan gulungan material (Nomor proses T-6, O-5, T- 7, O-6, T-8, I-2, T-11)

402

Mulya Sultoniq Lubis dan Rosnani Ginting / EE Conference Series 02 (2019)

6.

WC VI: Proses pencetakan Cangkir plastik bening (O-8, T-12, I-3, T-13, O-10)

Catatan waktu siklus selama pengamatan untuk seluruh tipe cangkir plastik bening yang yang ditunjukkan pada tabel
4. sampai tabel 9. Data waktu untuk WC I sampai WC VI dalam satuan menit. Data ini merupakan data
Tabel 4. Rekapitulasi Perhitungan Makespan Awal (Menit)
Job
WC
I

II

III

IV

V

VI

Ket

MGT 20 (1)

MK AD 110 (2)

MK 125 D (3)

MG 180 (4)

MK EM 180 (5)

MGA 150 (6)

Mulai

0

3286,76

4620,38

5036,55

6070,96

7987,03

Selesai

3286,76

4620,38

5036,55

6070,96

7987,03

9660,03

Mulai

3286,76

5777,92

7080,32

7504,76

8604,38

10476,64

Selesai

5777,92

7080,32

7504,76

8604,38

10476,64

12185,07

Mulai

5777,92

7584,56

8585,00

8888,64

10476,64

12185,07

Selesai

7584,56

8585,00

8888,64

9691,42

11773,88

13433,88

Mulai

7584,56

9986,65

11221,77

11648,22

12683,25

14505,28

Selesai

9986,65

11221,77

11648,22

12683,25

14505,28

16053,87

Mulai

9986,65

13947,38

15932,32

16594,80

18260,83

21227,75

Selesai

13947,38

15932,32

16594,80

18260,83

21227,75

23909,73

Mulai

13947,38

15932,32

16594,80

18260,83

21227,75

23909,73

Selesai

14831,45

16366,28

16738,75

18626,51

21894,10

24480,71

Pada algoritma Simulated Annealing, sekumpulan parameter harus didefenisikan terlebih dahulu diawal proses,
Pendefenisian parameter-parameter ini disebut cooling schedule, yang melibatkan:
1.
Nilai awal untuk parameter kontrol atau temperatur awal (Ti), Untuk penelitian ini nilai Ti ditentukan sebesar
200 0C,
2.
Fungsi/faktor penurunan nilai parameter kontrol (s), Nilai ini menentukan seberapa cepat parameter kontrol
mengalami penurunan, Nilai yang digunakan dalam penelitian ini ialah F = 0,95
3.
Jumlah iterasi dalam tiap nilai parameter kontrol (L), Untuk penelitian ini nilai L ditentukan sebanyak 15
kali iterasi,
4.
Kriteria terminasi untuk menghentikan eksekusi, Kriteria steady state proses pencarian dalam algoritma SA
dapat berupa dicapainya suatu jumlah iterasi tertentu di mana selama itu tidak ada solusi baru yang diterima atau
dicapainya temperatur akhir yang telah ditetapkan sebelumnya, Dalam penelitian ini temperatur akhir yang digunakan
adalah 0,01 0C, Kriteria steady state yang pertama terjadi apabila tidak terdapat iterasi yang menghasilkan solusi baru
yang diterima, walaupun temperatur belum mencapai temperatur akhir yang ditetapkan (0,01 0C), maka iterasi
dihentikan, Kondisi kedua terjadi apabila terdapat iterasi yang menghasilkan solusi baru yang diterima dan temperatur
mencapai 0,01 0C, maka dengan demikian iterasi akan dihentikan.
Pada temperatur T = 180,5 tidak ada solusi yang diterima, Kondisi ini disebut steady state, dan iterasi dihentikan
karena solusi umum telah didapat, Sehingga yang menjadi solusi sekarang adalah T = 180,5 yaitu S= 21317,95 menit,
Gambar 4. menunjukkan grafik simulated annealing pada setiap iterasi suhu 180,5.
Pengujian distribusi dilakukan untuk mendapatkan hipotesis apakah nilai makespan yang dihitung akan menghasilkan
grafik uniform dengan menggunakan uji Chi-Square, Nilai makespan yang dipakai dalam pengujian distribusi adalah
nilai iterasi pada Ti = 180,5.

Mulya Sultoniq Lubis dan Rosnani Ginting / EE Conference Series 02 (2019)

403

Gambar 4. Grafik Simulated Annealing

4. Kesimpulan dan Saran
Berdasarkan penelitian yang dilakukan di PT. XYZ dapat ditarik beberapa kesimpulan sebagai berikut:
1. Jadwal yang diperoleh dengan menggunakan Metode Simulated Annealing adalah job 3-1-4-6
2. Metode penjadwalan produksi yang memberikan hasil yang optimum adalah Algoritma Simulated Annealing
dengan Total makespan sebesar 20091,71 menit 334,99 jam = 13,95 ≈ 14 hari sedangkan makespan yang
didapat dari metode penjadwalan aktual yang diterapkan di PT. XYZ dengan aturan First Come First Serve
sebesar 24480,71 menit = 408,01 jam = 17 hari.
3. Nilai Efficiency Index (EI) sebesar 1,21 menunjukkan bahwa penjadwalan dengan Algoritma Simulated
Annealing.
4. Nilai Beda Relatif (RE) menunjukkan bahwa penghematan makespan yang diperoleh antara Algoritma
Simulated Annealing dengan metode perusahaan adalah 21,79 %
Referensi
[1] Ginting, Rosnani. 2016. Penjadwalan Mesin.
[2] Sinulingga, Sukaria. 2016.Metode Penelitian.
[3] Sutalaksana, Iftikar Z. 1979. Teknik Tata Cara Kerja. Bandung : Jurusan Teknik Institut Teknologi Bandung.
[4] Hutahaean, Sarah. 2014. Penjadwalan Produksi dengan Menggunakan Algoritma Simulated Annealing di PT. Guna Kemas Indah.
[5] Siregar, Anggiat. 2009. Analisa Perbandingan Kinerja Antara Algoritma Heuristic pour dan Algoritma Nawaz

