Jurnal Armada Informatika
p-ISSN: 2598-0416

e- ISSN: 2615-6891

PERANCANGAN SISTEM PENJADWALAN
LABORATORIUM MENGGUNAKAN
METODE TABU SEARCH
Reza Alamsyah*1, Tongam E Panggabean2
STMIK Methodist Binjai; Jl. Jend. Sudirman No. 136 Binjai – Telp: 061-88742021
Teknik Informatika
1
email : * 89rezaalamsyah@gmail.com, 2tongampanggabean@gmail.com
Abstrak

adanya suatu proses penyusunan penjadwalan yang baik adalah sebuah hal yang penting. Secara
umum scheduling merupakan suatu permasalahan dalam hal melakukan sequencing terhadap sejumlah
operasi dan mengalokasikannya ke dalam slot waktu tertentu tanpa melanggar batasan teknis dan
keterbatasan kapasitas yang dimiliki. Hal ini berdasar pada kenyataan bahwa begitu banyak parameter
yang harus diperhatikan. Karena scheduling, khususnya job shop scheduling, merupakan suatu
permasalahan combinatorial optimization yang kompleks maka permasalahan scheduling dapat
dikategorikan sebagai permasalahan np-hard, yaitu suatu permasalahan yang pencarian solusinya (waktu
komputasinya) akan naik secara eksponensial seiring dengan naiknya ukuran permasalahan secara linier.
Dengan kemajuan ilmu pengetahuan dalam bidang komputasi cerdas, masalah penjadwalan di atas dapat
diotomatisasi sehingga dapat memberikan solusi optimal sesuai dengan batasan dan syarat yang sudah
ditentukan dengan menggunakn Metode Tabu Search.

Kata kunci : Tabu Search, Penjadwalan, Optimaze Combination
Abstract
The existence of a good scheduling process is an important thing. In general, scheduling is a

problem in terms of sequencing a number of operations and allocating them to certain time slots without
violating technical limitations and limited capacity. This is based on the fact that so many parameters
must be considered. Because scheduling, especially job shop scheduling, is a complex combinatorial
optimization problem, scheduling problems can be categorized as np-hard problems, ie problems whose
search for solutions (computation time) will rise exponentially as the size of the problem increases
linearly. With the advancement of science in the field of intelligent computing, scheduling problems above
can be automated so as to provide optimal solutions in accordance with the limits and conditions that
have been determined by using the Tabu Search Method.

Keywords : Tabu Search, Scheduling, Optimaze Combination
1. PENDAHULUAN
Dalam sebuah industri, baik itu industri manufaktur maupun jasa, adanya suatu proses
penyusunan penjadwalan yang baik adalah sebuah hal yang penting. Hal ini dikarenakan dengan
adanya penjadwalan yang baik akan dapat meningkatkan efektivitas serta efisiensi sistem
produksi industri tersebut yang pada akhirnya akan mengurangi production costs. Scheduling
dapat diartikan sebagai pengalokasian sejumlah resources (sumber daya) untuk melakukan
sejumlah tasks (tugas/operasi) dalam jangka waktu tertentu.
Secara umum scheduling merupakan suatu permasalahan dalam hal melakukan
sequencing terhadap sejumlah operasi dan mengalokasikannya ke dalam slot waktu tertentu

� 11
tanpa melanggar technical constraints (batasan teknis) dan capacitive constraints (keterbatasan
kapasitas yang dimiliki). Baik secara teori maupun prakteknya di lapangan, untuk dapat
melakukan suatu proses penjadwalan (scheduling) yang baik sangat sulit untuk dibuat. Hal ini
berdasar pada kenyataan bahwa begitu banyak parameter yang harus diperhatikan. Karena
scheduling, khususnya job shop scheduling, merupakan suatu permasalahan combinatorial
optimization yang kompleks maka permasalahan scheduling dapat dikategorikan sebagai
permasalahan np-hard, yaitu suatu permasalahan yang pencarian solusinya (waktu
komputasinya) akan naik secara eksponensial seiring dengan naiknya ukuran permasalahan
secara linier. Untuk itu diperlukan suatu metode yang lebih baik dalam memecahkan
permasalahan ini.
Umumnya penyusunan jadwal mata kuliah dilakukan secara manual, yaitu dengan
pencarian blok-blok atau kolom-kolom mana saja yang masih kosong, kemudian menempatkan
jadwal pada blok atau kolom tersebut. Jadwal yang dihasilkan dengan cara seperti ini cenderung
menghasilkan jadwal yang menumpuk dan tingkat keakuratannya tidak bisa dijamin. Jadwal
yang baik semestinya dapat mengakomodasi semua syarat yang telah ditentukan. Sebagai
contoh adalah seorang dosen hanya bisa mengajar pada waktu dan jam tertentu. Dengan syarat
ini seharusnya jadwal yang disusun menyediakan sejumlah solusi sehingga kelas yang diajarkan
oleh pengajar tersebut tidak bentrok dengan pengajar yang lainnya.
Dengan kemajuan ilmu pengetahuan dalam bidang komputasi cerdas, masalah
penjadwalan di atas dapat diotomatisasi sehingga dapat memberikan solusi optimal sesuai
dengan batasan dan syarat yang sudah ditentukan. Sejumlah metode dari berbagai disiplin ilmu
telah diusulkan dalam literatur, seperti: riset operasi, kecerdasan buatan, dan kecerdasan
komputasional. Metode-metode tersebut dapat di bagi ke dalam 4 (empat) kategori, yaitu:
Sequential Methods, Cluster Methods, Constraint Based Methods, dan Metaheuristic Methods,
seperti genetic algorithms, simulated annealing, dan tabu search.
Menyelesaikan masalah penjadwalan mata kuliah menggunakan tiga metode
metaheuristic, yaitu: simulated annealing (SA), tabu search (TS), dan genetic algorithm (GA).
Dari uji coba yang dilakukan diperoleh hasil bahwa semua metode metaheuristic dapat
menghasilkan solusi yang sangat baik dibandingkan dengan pengalokasian secara manual
2. METODE PENELITIAN
2.1. Pengertian Algoritma Genetik
Algoritma ini ditemukan di Universitas Michigan, Amerika Serikat oleh John Holland
(1975) melalui sebuah penelitian dan dipopulerkan oleh salah satu muridnya, David Goldberg
(1989). Dimana mendefenisikan algoritma genetik ini sebagai metode algoritma pencarian
berdasarkan pada mekanisme seleksi alam dan genetik alam. Algoritma genetik adalah
algoritma yang berusaha menerapkan pemahaman mengenai evolusi alamiah pada tugas-tugas
pemecahan-masalah (problem solving). Pendekatan yang diambil oleh algoritma ini adalah
dengan menggabungkan secara acak berbagai pilihan solusi terbaik di dalam suatu kumpulan
untuk mendapatkan generasi solusi terbaik berikutnya yaitu pada suatu kondisi yang
memaksimalkan kecocokannya atau lazim disebut fitness.
Generasi ini akan merepresentasikan perbaikan-perbaikan pada populasi awalnya. Dengan
melakukan proses ini secara berulang, algoritma ini diharapkan dapat mensimulasikan proses
evolusioner. Pada akhirnya, akan didapatkan solusi-solusi yang paling tepat bagi permasalahan
yang dihadapi. Untuk menggunakan algoritma genetik, solusi permasalahan direpresentasikan
sebagai khromosom. Tiga aspek yang penting untuk penggunaan algoritma genetik:
A. Defenisi fungsi fitness
B. Defenisi dan implementasi representasi genetic
C. Defenisi dan implementasi operasi genetic
Jika ketiga aspek di atas telah didefinisikan, algoritma genetik akan bekerja dengan baik.
Tentu saja, algoritma genetik bukanlah solusi terbaik untuk memecahkan segala masalah.

12
Sebagai contoh, metode tradisional telah diatur untuk untuk mencari penyelesaian dari fungsi
analitis convex yang “berperilaku baik” yang variabelnya sedikit. Pada kasuskasus ini, metode
berbasis kalkulus lebih unggul dari algoritma genetik karena metode ini dengan cepat
menemukan solusi minimum ketika algoritma genetik masih menganalisa bobot dari populasi
awal.
Untuk problem-problem ini pengguna harus mengakui fakta dari pengalaman ini dan
memakai metode tradisional yang lebih cepat tersebut. Akan tetapi, banyak persoalan realistis
yang berada di luar golongan ini. Selain itu, untuk persoalan yang tidak terlalu rumit, banyak
cara yang lebih cepat dari algoritma genetik. Jumlah besar dari populasi solusi, yang merupakan
keunggulan dari algoritma genetik, juga harus mengakui kekurangannya dalam dalam kecepatan
pada sekumpulan komputer yang dipasang secara seri-fitness function dari tiap solusi harus
dievaluasi. Namun, bila tersedia komputer-komputer yang paralel, tiap prosesor dapat
mengevaluasi fungsi yang terpisah pada saat yang bersamaan. Karena itulah, algoritma genetik
sangat cocok untuk perhitungan yang paralel.
2.2. Seleksi
Seleksi bertujuan memberikan kesempatan reproduksi yang lebih besar bagi anggota
populasi yang paling fit. Langkah pertama dalam seleksi ini adalah pencarian nilai fitness.
Masing-masing individu dalam suatu wadah seleksi akan menerima probabilitas reproduksi
yang tergantung pada nilai objektif dirinya sendiri terhadap nilai objektif dari semua individu
dalam wadah seleksi tersebut. Nilai fitness inilah yang nantinya akan digunakan pada tahap
seleksi berikutnya (Kusumadewi, 2003).
Kemampuan algoritma genetik untuk memproduksi kromosom yang lebih baik secara
progresif tergantung pada penekanan selektif (selective pressure) yang diterapkan ke populasi.
Penekanan selektif dapat diterapkan dalam dua cara. Cara pertama adalah membuat lebih
banyak kromosom anak yang dipelihara dalam populasi dan memilih hanya kromosomkromosom terbaik bagi generasi berikut. Walaupun orang tua dipilih secara acak, metode ini
akan terus menghasilkan kromosom yang lebih baik berhubungan dengan penekanan selektif
yang diterapkan pada individu anak tersebut. Cara lain menerapkan penekanan selektif adalah
memilih orang tua yang lebih baik ketika membuat keturunan baru. Dengan metode ini, hanya
kromosom sebanyak yang dipelihara dalam populasi yang perlu dibuat bagi generasi berikutnya.
Walaupun penekanan selektif tidak diterapkan ke level keturunan, metode ini akan terus
menghasilkan kromosom yang lebih baik, karena adanya penekanan selektif yang diterapkan ke
orangtua.
Ada beberapa metode untuk memilih kromosom yang sering digunakan antara lain adalah
seleksi roda rolet (roulette wheel selection), seleksi ranking (rank selection) dam seleksi
turnamen (tournament selection). Dalam penelitian ini, metode yang digunakan adalah seleksi
roda rolet (roulette wheel selection). Pada seleksi ini, orang tua dipilih berdasarkan fitness
mereka. Lebih baik kualitas suatu kromosom, lebih besar peluangnya untuk terpilih. Probabilitas
suatu individu terpilih untuk crossover sebanding dengan fitnessnya. Cara penyeleksian ini
merupakan peniruan dari permainan roda rolet.
2.3. Tabu Search
Penelitian ini dilakukan dengan membandingkan kinerja algoritma PACO dengan PACOTabu Search yang diusulkan penulis (PACO-TABU). Perbedaan kedua algoritma ini adalah
pada metode local search yang digunakan yaitu job index based untuk algoritma PACO dan
algoritma BF-TS untuk algoritma PACO-TABU. Permasalahan yang digunakan pada penelitian
ini adalah kombinasi penjadwalan flowshop dengan jumlah job 10, 20, 30, 40, dan 50 dengan
10, 20, dan 30 mesin. Algoritma dijalankan sebanyak 10 iterasi dengan masing-masing iterasi
100 kali pada masing-masing kombinasi jumlah job dan mesin. Ratarata makespan dan
computation time digunakan sebagai performance measure untuk perbandingan algoritma.
Semakin kecil rata-rata makespan dan computation time yang dihasilkan semakin baik juga
kinerja dari algoritma tersebut. Simulasi kedua algoritma menggunakan komputer dengan
processor Intel Core2Duo 1,66GHz dan memory 1,5GHz.

� 13
Algoritma PACO-TABU bekerja dengan menggunakan solusi awal dari algoritma NEH,
algoritma BF-TS (Lampiran: Gambar 4) dan algoritma ant colony. Solusi awal yang didapat dari
algoritma NEH ditingkatkan kinerjanya dengan menggunakan algoritma BF-TS. Peningkatan
kinerja algoritma BF-TS diteruskan dengan algoritma ant colony hingga menghasilkan solusi
terbaik pada saat stopping criteria. Beberapa metode local search yang dapat digunakan pada
algoritma BF-TS, yaitu:
a. Swapping, dilakukan dengan membangkitkan bilangan random i dan j. Bilangan
random ini menunjukkan posisi i dan posisi j. Proses swapping ini bekerja dengan
menukar job di posisi i dengan job di posisi j.
b. Insertion, proses pembangkitan bilangan random ini hampir sama dengan metode
swapping. Perbedaannya adalah job di posisi i dimasukkan ke posisi j.
c. Block insertion,proses ini dilakukan dengan membangkitkan bilangan i, j, dan k
kemudian memasukkan k job dimulai job i ke posisi j.
Algoritma BF-TS dilakukan dengan melakukan proses neighborhood dan memasukkan
beberapa proses neighborhood terakhir yang menghasilkan nilai optimum dalam tabu list.
Proses neighborhood dilakukan dengan menggunakan metode local search yang terpilih dan
tabu list yang ada berfungsi sebagai memori jangka pendek yang berguna menghindari
pengulangan perhitungan. Ukuran tabu list yang ditetapkan pada penelitian ini sebesar 7, dengan
ketentuan jika pasangan job dalam tabu list telah lebih dari 7 maka pasangan job pertama
dikeluarkan dari tabu list. Ukuran tabu list yang terlalu kecil dapat menghasilkan kemungkinan
solusi yang berulang (misalnya ukuran = 2) sedangkan jika terlalu besar akan berpeluang
menghasilkan local optimum. Algoritma pencarian ini juga menggunakan kombinasi
Intensification and Diversification Scheme yaitu menggabungkan antara penggunaan atribut
dari solusi-solusi yang didapat sebelumnya (intensification scheme) dengan penggalian solusi
dari daerah yang belum pernah dijelajahi (diversification scheme). Proses pencarian yang telah
dihasilkan akan dilanjutkan hingga memenuhi stopping criteria yang ditetapkan. Stopping
criteria yang dipakai pada algoritma BFTS adalah tidak terdapat perbaikan hasil pada suatu
kriteria antara 2 solusi yang dihasilkan dari diversification scheme atau mencapai jumlah
maksimum iterasi yang ditetapkan.
3. HASIL DAN PEMBAHASAN
Hasil Analisis Kebutuhan Hasil analisis yang diperoleh dari sistem penjadwalan kuliah ada
beberapa proses masukan dan keluaran.
3.1. Data Masukan Untuk Proses Masukan Data, terdiri dari :
a. Proses pemasukan data yang berupa data dosen, data matakuliah, data ruang, dan data waktu
kuliah. Data dosen diisi oleh Dosen sendiri dengan mengisi formulir data mengajar, sedangkan
ruangannya ditentukan oleh Sekretariat Program, bagian penjadwalan kuliah dan ujian untuk
disimpan dalam database.
b. Proses pemasukan data matakuliah yang ditawarkan tiap semesternya,termasuk penentuan
jumlah kelas per-matakuliah yang ditawarkan yang disesuaikan dengan kesanggupan dosen
mengajar.
3.2. Data Keluaran Data keluaran yang dihasilkan berupa :
a. Laporan ( print out) jadwal kuliah, yang berisi data matakuliah perjurusan yang diadakan tiap
semester. Laporan ini selanjutnya digunakan mahasiswa untuk key-in kuliah. Sedangkan jadwal
ujian diberikan satu minggu sebelum ujian dimulai.
b. Laporan ( print out) jadwal dosen, merupakan laporan mengajar dosen yang diserahkan
kepada dosen yang bersangkutan agar mengetahui jadwal mengajarnya. Sedangkan jadwal ujian
diberikan satu minggu sebelum ujian dimulai
3.3. Analisis kebutuhan Antar Muka Kebutuhan terhadap antarmuka (Interface) yang diinginkan
oleh user didasarkan atas hasil wawancara dengan pihak-pihak terkait. Interface yang diinginkan

14
yaitu sebaik mungkin sehingga bersifat ramah pengguna (user friendly), artinya user dapat
menggunakan perangkat lunak yang dibuat dengan senyaman mungkin, mudah untuk
dioperasikan dan meminimumkan kesalahan baik kesalahan input, proses maupun output yang
dihasilkan
3.4. Keamanan Data Keamanan data meliputi seluruh proses yang diperlukan untuk memastikan
keamanan data di dalam suatu sistem. Keamanan data merupakan salah satu unsur yang harus
dipertimbangkan dalam proses desain atau sistem, karena suatu sistem tanpa keamanan data
yang baik akan menimbulkan kerugian, seperti data akan bebas diakses oleh pihak-pihak yang
tidak berkepentingan. Keamanan data dapat diterapkan dengan pembuatan sandi ( password )
sehingga hanya pihak yang berhak saja yang dapat mengakses sistem.
3.5. Kebutuhan Perangkat Lunak Sistem penjadwalan kuliah ini dibangun dengan spesifikasi
perangkat lunak sebagai berikut :
a. Sistem operasi Windows Xp Profesional
b. Visual Basic sebagai tampilan antarmuka dan Access sebagai databasenya.
3.6. Perancangan
Perancangan dimulai dari diagram konteks bentuk yang paling umum, kemudian diturunkan
sampai bentuk yang paling detail. Dalam pembuatan konteks perlu menganalisis sistem
aplikasinya, apa saja yang dibutuhkan, sumber data dan tujuan atau hasil akhir yang diinginkan.
Dari hasil analisis tersebut diperoleh diagram konteks seperti yang terlihat pada gambar berikut:

Gambar 1 Diagram Konteks Penjadwalan Kuliah dan Ujian

Keterangan:
Pada diagram konteks terdapat external interactor dan proses, yaitu:
a. External interactor Sekretariat program adalah bagian yang menerima informasi data sebagai
masukan pada proses penjadwalan kuliah dan ujian.
b. Proses Perencanaan jadwal kuliah dan ujian adalah proses yang akan mengolah data yang
telah diinputkan sebelumnya.
3.7 Data Flow Diagram
Sistem Setelah dibuat diagram konteks, langkah selanjutnya adalah menurunkan diagram
konteks menjadi bentuk yang lebih detail, yaitu DFD (Data Flow Diagram) level 1. DFD level 1
mengilustrasikan bagaimana data diproses oleh sistem, dalam hal ini input dan output dari
sistem

� 15

Gambar 2 DFD level 1
3.8. IMPLEMENTASI SISTEM
Setelah sistem selesai dianalisis dan didesain secara rinci, maka langkah selanjutnya yang akan
dilakukan adalah implementasi atau penerapan sistem. Tahap implementasi sistem (system
implementation) merupakan tahap meletakkan sistem agar siap untuk dioperasikan. Tahap ini
termasuk juga kegiatan menulis kode program jika tidak digunakan paket perangkat lunak
aplikasi
3.9. DEFENISI IMPLEMENTASI SISTEM
Implementasi sistem merupakan prosedur yang dilakukan untuk menyelesaikan desain sistem
yang ada dalam dokumen desain yang disetujui, menguji sistem, menginstal, dan memulai
sistem yang baru yang telah diperbaiki.
3.10. Tujuan Implementasi Sistem
Adapun tujuan dari implementasi dari sistem tersebut diantaranya yaitu :
1. Membuat perancangan desain sistem
2. Menguji dan mendokumentasikan prosedur dalam program yang diperlukan oleh dokumen
perancangan sistem yang telah dibuat.
3. Menyelesaikan perancangan sistem yang ada didalam perancangan sistem yang telah
disetujui.
4. Memperhitungkan sistem yang telah dibuat sesuai kebutuhan pemakai.
3.11. Pemeliharaan Sistem
Berdasarkan hal diatas, maka dibutuhkan adanya pemeliharaan sistem agar sistem tersebut dapat
berjalan sebagaimana mestinya. Adapun tujuan pemeliharaan sistem antara lain adalah :
1. Mencegah adanya kelainan sistem yang dapat mendatangkan masalah-masalah baru.
2. Eksisitensi sistem dapat terjaga atau bertahan.

16

3.12. Hasil Pengolahan Data
3.12.1. Demonstrasi Program Demonstrasi program merupakan suatu prosedur yang
dilaksanakan untuk menampilkan hasil dari sistem yang diusulkan, dimana hasil yang telah
dijalankan. Adapun tampilan-tampilan sistem yang diusulkan penulis adalah sebagai berikut :

Gambar 3 Login admin

Gambar 4 Informasi Data Dosen

Gambar 5 Informasi Data Ruangan

� 17
Gambar 6 Informasi Data Mata Kuliah

Gambar 7 Form Tabel Pencocokan

Gambar 8 Pemberian Nilai Cost
4. KESIMPULAN
Adapun Kesimpulan yang didapat yaitu:
1.
2.

Metode Tabu Search dapat digunakan sebagai sistem penjadwalan kuliah dan ujian, karena
metode ini memilih langkah berikutnya (neighboursolution) berdasarkan constraint dan penalti.
Dengan menggunakan Tabu Search, aplikasi penjadwalan ini mempermudah bagian Sekretariat
Program untuk menyusun Jadwal Kuliah dan Ujian pada tiap semesternya. Karena dapat
mengidentifikasi permasalahan, kesempatan, hambatan yang terjadi dan kebutuhan penjadwalan
yang diharapkan.

5. SARAN
Dalam hal ini penulis menyadari bahwa sistem ini masih banyak kekurangan dan kelemahan oleh karena
itu disarankan untuk:
1. Dapat mengembangkan aplikasi ini dengan bahasa pemrograman yang lain, dan metode lain agar
dapat menampilkan semua solusi yang terdapat dalam sebuah problem penjadwalan kuliah atau
problem sejenisnya.
2. Dapat mengembangkan aplikasi ini dengan memperbaiki kekurangan yang dimiliki oleh aplikasi
ini. Sehingga dapat menghasilkan aplikasi yang lebih baik.

DAFTAR PUSTAKA

18
Arifin Suandy, et al. “Usulan Penerapan Penjadwalan dengan Menggunakan Metode Tabu Search di PT
Gistex Textile Division”. Jurnal Integral, 2013.
Leo Chandra S. “Penerapan Algoritma Tabu Search Untuk Penjadwalan Mata Pelajaran Di SMK Swasta
Pelita-2 Aekkanopan”. Jurnal Riset Komputer 2016.
Betrianis, dan Putu Teguh Aryawan. “Penerapan Algoritma Tabu Search Dalam Penjadwalan Job Shop”.
Jurnal Makara, Teknologi, 2003.
Rencus Siburian, dan Abadi Ginting SS. “Penjadwalan Produksi Job Shop Dengan Menggunakan
Algoritma Tabu Search Pada PT. XYZ”. Jurnal Teknik Industri FT. USU, 2013.
Olive Khoirul L. M. A, et al. “Optimasi Penjadwalan Mata Pelajaran Menggunakan Metode Tabu Search
(Studi Kasus: SMKN 2 Singosari)”. Jurnal Pengembangan Teknologi Informasi dan Ilmu Komputer,
2017.
Miswanto, et al. “Implementasi Algoritma Tabu Search Untuk Mengoptimasi Penjadwalan Preventive
Maintenance (Studi Kasus PT XYZ)”. Jurnal SENTIKA, 2018
Allwine, A., Simanjuntak, M. S., & Wijaya, R. (2019). SISTEM PAKAR MENDETEKSI TINGKAT
RESIKO PENYAKIT MELALUI GEJALA DAN POLA HIDUP MENGGUNAKAN METODE
FUZZY MAMDANI. Jurnal
Mantik Penusa, 3(3). Retrieved from https://ejurnal.pelitanusantara.ac.id/index.php/mantik/article/view/686

