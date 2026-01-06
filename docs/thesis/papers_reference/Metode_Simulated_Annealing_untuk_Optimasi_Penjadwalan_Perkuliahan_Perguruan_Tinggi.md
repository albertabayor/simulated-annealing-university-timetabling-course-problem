Jurnal Sistem Informasi Bisnis 02(2016)

On-line : http://ejournal.undip.ac.id/index.php/jsinbis

133

Metode Simulated Annealing untuk Optimasi Penjadwalan
Perkuliahan Perguruan Tinggi
Wiktasaria,*, Jatmiko Endro Susenob
a Universitas Islam Sultan Agung Semarang
cJurusan Fisika, Fakultas Sains dan Matematika, Universitas Diponegoro

Naskah Diterima : 21 Mei 2016; Diterima Publikasi : 11 Oktober 2016

DOI: 10.21456/vol6iss2pp133-143

Abstract
Course scheduling an assignment of courses and lecturers in the available time slots involving certain restrictions. Simulated
annealing is a heuristic method can be used as search method and provide acceptable solutions with good results. The research
aims to make scheduling courses at the college using simulated annealing using five variables data that lecturer courses, the
time slot is comprised of the day and the time period and class room. The research has two objective functions to be generated,
the first is the assignment of a lecturer on courses that will be of teaching, second lecturers and their assignment course on the
time slot and the room available. The objective function is calculated by taking into account the restrictions involved to produce
the optimal solution. The validation is performed by testing to simulated annealing method with an varian average of 77.791%
of the data variance can reach a solution with a standard deviation of 3.931509. In this research given the method of solution
in the use of the remaining search space to be reused by the data that is unallocated.
Keywords: Scheduling; Timetabling; Simulated annealing; Heuristic; Objective function; Constraint
Abstrak
Penjadwalan kuliah merupakan penugasan mata kuliah dan dosen pengampu pada slot waktu yang tersedia dengan melibatkan
batasan tertentu. Simulated annealing merupakan salah satu metode heuristic yang dapat digunakan sebagai metode pencarian
dan memberikan solusi yang dapat diterima dengan hasil yang baik. Penelitian ini bertujuan untuk membuat penjadwalan mata
kuliah pada perguruan tinggi menggunakan metode simulated annealing dengan lima variabel data yaitu dosen, mata kuliah,
slot waktu yang terdiri dari hari dan waktu periode dan variabel ruang. Penelitian ini memiliki dua fungsi tujuan yang akan
dihasilkan, pertama adalah penugasan dosen pada mata kuliah yang akan diampu, kedua penugasan mata kulia beserta dosen
pada slot waktu dan ruang yang tersedia. Fungsi tujuan dihitung dengan memperhatikan batasan yang terlibat untuk
menghasilkan solusi yang optimal. Validasi dilakukan dengan uji coba terhadap metode simulated annealing dengan
menghasilkan rata-rata varian sebesar 77,791% data dapat mencapai solusi dengan standar deviasi sebesar 3.931509. Pada
penelitian ini diberikan metode solusi dalam penggunaan ruang pencarian yang tersisa untuk dapat digunakan kembali oleh
data yang belum teralokasikan.
Kata kunci: Penjadwalan, Timetabling, Simulated annealing, Heuristic, Objective aunction, Batasan

1. Pendahuluan
Penjadwalan perguruan tinggi menjelaskan
dimana dan kapan sumber daya manusia dan sumber
daya pendukung ditempatkan pada waktu yang telah
ditentukan yang terdiri dari mahasiswa, dosen dan
staff pendukung sedangkan sumber daya ruang terdiri
dari kelas, ruang dan laboratorium (Chamber, 1998,
Basir et al., 2013).
Masalah penjadwalan (timetabling) mata kuliah
perguruan tinggi termasuk kedalam permasalahan
*) Penulisa korespondensi: wiktasari@unissula.ac.id

penjadwalan yang harus diselesaikan pada setiap
semester secara terus menerus, alokasi pada slot waktu
dan ruang dengan mempertimbangkan hard
constraints dan soft constraints. Penjadwalan mata
kuliah perguruan tinggi terdiri dari hard constraint
merupakan batasan yang harus dihindari dengan
berbagai kondisi dan soft constraint yang merupakan
batasan yang sedapat mungkin dihindari (Babei et al.,
2015).
Penjadwalan universitas dapat diperlakukan
sebagai permasalahan optimasi yang bertujuan untuk
optimasi objective function. Objective function dapat

134

Jurnal Sistem Informasi Bisnis 02(2016)

berupa kepuasan preferensi yang dimiliki dosen dalam
memilih slot waktu (timeslot) dalam sehari atau
seminggu (Daskalaki et al., 2004). Salah satu metode
yang digunakan untuk permasalahan optimasi adalah
simulated annealing (SA). SA telah digunakan untuk
permasalahan optimasi kombinatorial. SA merupakan
metode dengan pendekatan pencarian solusi yang
random (Mu et al., 2015).
Metode yang dipilih simulated annealing dapat
diterapkan pada berbagai jenis masalah timetabling
atau penjadwalan dengan menggunakan berbagai
macam hard constraint dan soft constraint didapatkan
fitness function yang baik atau optimum (Basir, 2013)
Penelitian ini bertujuan untuk membuat penjadwalan
mata kuliah pada perguruan tinggi menggunakan metode
simulated annealing dengan lima variabel data yaitu dosen,
mata kuliah, slot waktu yang terdiri dari hari dan waktu
periode dan variabel ruang. Manfaat yang diharapkan

dari hasil penelitian ini adalah dapat memaksimalkan
penggunaan sumber daya yang terlibat dalam proses
penjadwalan sehingga menghasilkan jadwal kuliah
lebih baik.
2. Kerangka Teori
2.1. Model Permasalahan Penjadwalan Mata Kuliah
Penjadwalan merupakan alokasi sumber daya yang
tersedia dari waktu ke waktu dalam menjalankan tugas
tertentu untuk mencapai tujuan tertentu (Kopanosa et
al., 2012). Jadwal tidak hanya terdiri dari daftar
operasi tetapi juga dapat berisi informasi mengenai
beberapa operasi yang mungkin dilaksanakan secara
bersamaan dan beberapa operasi perlu diselesaikan
sebelum operasi lain dimulai. Penjadwalan dan
pembebanan merupakan kunci efisiensi dalam
produksi dan operasi adalah kemampuan untuk
menyusun jadwal secara efektif (Yamit, 2011).
Penjadwalan mata kuliah perguruan tinggi
merupakan penugasan himpunan mata kuliah kedalam
slot waktu yang tersedia dengan memperhatikan
batasan. Optimasi himpunan dengan beberapa kriteria
variabel sebagai input akan menghasilkan keputusan
dengan memperhatikan batasan yang terkait untuk
menghasilkan jadwal kuliha. Model dataset
penjadwalan mata kuliah adalah sebagai berikut (Fong
et al., 2014):
Tujuan yang diharapkan dari penjadwalan adalah
dapat menjadwalkan semua mata kuliah C kedalam
slot waktu yang tersedia dengan menggunakan ruang
kelas yang tersedia dengan memperhatikan semua
hard constraint.
2.2. Formulasi Simulated Annealing
Terdapat beberapa kebutuhan dalam formulasi
optimasi metode SA yaitu (Kalivas, 1995):
1. Melakukan spesifikasi nilai tunggal dari objective
function baik dalam bentuk ekspresi tertutup
maupun sebuah prosedur untuk komputasi.
2. Mendeskripsikan variabel (argumen dari
objective function) dan daerah dimana akan

3.

4.

5.

On-line : http://ejournal.undip.ac.id/index.php/jsinbis

dilakukan pencarian solusi atau yang disebut
dengan constraint. Variabel yang digunakan
adalah variabel input yang terkait dengan variabel
dalam pengambilan keputusan.
Mendefinisikan tetangga dari variabel. Tetangga
ini harus bernilai kecil dibanding dengan nilai
objective function dari tetangga-tetangga
terdekatnya.
Membuat sebuah prosedur yang menghasilkan
langkah-langkah pseudo-random untuk melewati
tetangga.
Membuat kriteria perhentian langkah-langkah
random yang dibuat pada langkah 4. Langkah
perhentian dibedakan menjadi dua kasus, yaitu: a)
Nilai optimal objective function dan lokasi yang
akan ditentukan telah diketahui sebelumnya; b)
Baik nilai optimal maupun lokasinya tidak
diketahui.

2.3. Algoritma Simulated Annealing
SA memiliki kemampuan untuk keluar dari lokal
optimum berdasarkan aturan penerimaan solusi
kandidat. Aturannya adalah jika nilai objective
function pada solusi sekarang lebih kecil dibanding
solusi dulu, maka solusi sekarang diterima. T adalah
parameter pengendali temperatur. Parameter T
merupakan pengendali ruang pencarian atau ruang
penempatan partikel pada proses pendingingan.
Flowchart algoritma SA dapat dilihat pada Gambar
(Chibante, 2010).

Gambar 1. Flowchart Algoritma SA

Jurnal Sistem Informasi Bisnis 02(2016)

1.

On-line : http://ejournal.undip.ac.id/index.php/jsinbis

Populasi Awal
Menentukan definisi dari nilai parameter yang
akan digunakan.
2. Temperatur Awal
Temperatur atau suhu pada SA digunakan sebagai
parameter pengendali yang harus didefinisikan
secara hati-hati pada saat penentuan populasi
awal.
3. Mekanisme Gangguan
Metode yang berfungsi untuk membuat solusi
baru yang berasal dari solusi sekarang yiatu
melakukan eksplorasi tetangga dari solusi
sekarang dan melakukan perubahan pada solusi
sekarang. Pada umumnya SA digunakan dalam
optimasi bilangan integer untuk permasalahan
kombinatorial.
4. Objective Function
Objective function merupakan ekspresi yang
berhubungan dengan parameter dengan beberapa
property untuk diminimasi atau dimaksimasi.
5. Jadwal Pendinginan
Jadwal pendinginan pada umumnya digunakan
dalam aturan geometrik untuk variasi
temperature:
𝑇𝑖+1 = 𝑠𝑇𝑖
(1)
dengan 𝑠 < 1.
6. Kriteria Akhir
Terdapat beberapa metode untuk pengendali
perhentian dari sebuah algoritma, yaitu:
a. Jumlah maksimum perulangan
b. Nilai minimum temperatur
c. Nilai minimum objective function
d. Nilai minimum kecepatan penerimaan.
Ada 6 tahapan algoritma SA yang digunakan untuk
menyelesaikan permasalahan optimasi (Kalivas,
1995):
1. Memilih titik awal 𝑋0 secara acak atau
ditentukan terlebih dahulu berdasar pengetahuan
dari permasalahan yang dihadapi dan
menentukan nilai yang sesuai dengan objective
function 𝜙(𝑋0 );
2. Memilih langkah acak 𝑠 ∈ 𝑋;
3. Pada titik 𝑋𝑘 hitung perubahan sementara nilai
objective function
∆𝑓 ← 𝑓(𝑠 ′ ) − 𝑓(𝑠);
4. Memeriksa kriteria perhentian, jika memenuhi
berhenti, sebaliknya;
5. Untuk 𝛥𝑓 ≤ 0 tentukan 𝑋𝑘+1 + 𝛥𝑓, kembali ke
langkah (2);
6. Untuk 𝛥𝑓˃0 periksa 𝑒𝑥𝑝(−𝛽𝛥𝑓) pilih nilai acak
𝜌, 0 ˂ 𝜌 ˂ 1, dari beberapa spesifikasi distribusi
pada [0,1] kemudian bandingkan :
a. Jika 𝑒𝑥𝑝(−𝛽𝛥𝑓) ≤ 𝜌 kembali ke langkah
(5)
b. Jika 𝑒𝑥𝑝(−𝛽𝛥𝑓)˃𝜌 kembali ke langkah (2)

135

2.4. Constrain dalam Penjadwalan Kuliah
Dalam penjadwalan mahasiswa dan penjadwalan
mata kuliah terdapat beberapa hard constraint dan soft
constraint yaitu (Cacchiani dkk., 2013):
1. Hard constraint
a. Semua dosen untuk setiap mata kuliah harus
dijadwalkan.
b. Setiap dosen tidak dapat mengajar lebih dari
satu mata kuliah dalam satu waktu periode.
c. Setiap ruang tidak dapat memiliki dosen
lebih dari satu dalam satu waktu.
d. Waktu periode yang tidak ditawarkan tidak
dapat digunakan dalam penjadwalan.
2. Soft constraint
a. Jumlah kelas harus dijaga sesedikit mungkin
dan kelas sebisa mungkin harus memenuhi
kapasitas.
b. Setiap kelas memiliki jumlah mahasiswa
maksimum.
2.5. Pernyataan dan Formulasi Permasalahan
1. Himpunan
Himpunan yang digunakan dalam pemodelan
untuk permasalahan penjadwalan terdiri dari
himpunan dosen, mata kuliah, mahasiswa, hari, slot
waktu dan mata kuliah dengan dossen pengampu
dapat dinotasikan sebagai berikut di bawah ini
(Gunawan et al., 2012):
I
himpunan semua dosen
himpunan semua mata kuliah
J
H
himpunan semua mahasiswa
𝐿
himpunan semua hari yang tersedia
M
himpunan semua slot waktu (timeslot) yang
tersedia
ji
himpunan semua mata kuliah yang dapat
diajar oleh dosen i , J i  J
2.

i  I 

Parameter Input
Parameter input yang digunakan dalam pemodelan
untuk permasalahan penjadwalan dapat ditunjukkan
sebagai berikut :
𝑁𝑖
maksimum beban dosen
𝐶
jumlah ruang kelas yang tersedia per
waktu periode
𝐻𝑗
jumlah slot waktu yang dibutuhkan per
mata kuliah 𝑗 (𝑖∀∈ 𝐽)
𝑃𝐶𝑖𝑗
nilai preferensi yang diberikan untuk
dosen 𝑖 untuk ditugaskan mengajar mata
kuliah j(∀𝑖 ∈ 𝐼, ∀𝑗 ∈ 𝐽)
𝑃𝑇𝑖𝑙𝑚
nilai preferensi yang diberikan oleh
dosen 𝑖 untuk ditugaskan mengajar
dalam sehari dan waktu periode m (∀𝑖 ∈
𝐼, ∀𝑚 ∈ 𝑀).
𝐿𝑇𝑗
jumlah minimum dosen yang dapat
mengampu mata kuliah j(∀𝑖 ∈ 𝐽)
𝑈𝑇𝑗
jumlah maksimum dosen yang dapat
mengampu mata kuliah j (∀𝑖 ∈ 𝐽)

Jurnal Sistem Informasi Bisnis 02(2016)

136

3.

Variabel Keputusan
Variabel keputusan yang digunakan dalam
pemodelan untuk permasalahan penjadwalan dapat
ditunjukkan sebagai berikut :
𝑋𝑖𝑗𝑙𝑚 = 1 jika dosen 𝑖 mengajar mata kuliah 𝑗 pada
hari 𝑙 pada slot waktu 𝑚; sebaliknya 0
maka
(∀𝑖 ∈ 𝐼, ∀𝑗 ∈ 𝐽, ∀𝑙 ∈ 𝐿, ∀𝑚 ∈ 𝑀)
𝑌𝑖𝑗𝑙 = 1
jika dosen 𝑖 mengajar mata kuliah 𝑗 pada
hari 𝑙; sebaliknya 0 maka (∀𝑖 ∈ 𝐼, ∀𝑗 ∈
𝐽, ∀𝑙 ∈ 𝐿)
𝑈𝑖𝑗𝑙𝑚 = 1 jika dosen 𝑖 mengajar mata kuliah 𝑗 pada
hari 𝑙 dengan mulai pada slot waktu 𝑚;
sebaliknya 0 maka (∀𝑖 ∈ 𝐼, ∀𝑗 ∈ 𝐽, ∀𝑙 ∈
𝐿, ∀𝑚 ∈ 𝑀)
𝑃𝑖𝑗 = 1
jika dosen i mengajar mata kuliah j; 0
maka (∀𝑖 ∈ 𝐼, ∀𝑗 ∈ 𝐽)
𝐿𝑖
jumlah mata kuliah yang diajar oleh
dosen 𝑖(∀𝑖 ∈ 𝐼)
𝑉𝑖
jumlah mata kuliah yang diajar oleh
dosen 𝑖 setiap hari (∀𝑖 ∈ 𝐼)
4. Objective Function :
[𝑀𝑎𝑡𝑎𝐾𝑢𝑙𝑖𝑎ℎ − 𝐷𝑜𝑠𝑒𝑛]𝑀𝑎𝑥
= ∑ ∑ 𝑃𝐶𝑖𝑗 𝑃𝑖𝑗
𝑖∈𝐼

2.3)

𝑗∈𝐽

[𝑃𝑙𝑜𝑡𝑡𝑖𝑛𝑔 − 𝑆𝑙𝑜𝑡𝑊𝑎𝑘𝑡𝑢]𝑀𝑎𝑥
= ∑ ∑ ∑ ∑ 𝑃𝑇𝑖𝑙𝑚 𝑋𝑖𝑗𝑙𝑚

2.4)

𝑖∈𝐼 𝑗∈𝐽 𝑙∈𝐿 𝑚∈𝑀

Persamaan (2.1) merupakan objective function
yang akan dimaksimalkan, yang terdiri dari
penjumlahan nilai preferensi total untuk pengusana
mata kuliah j ke dosen i kemudian persamaan (2.2)
adalah objective function 2 yaitu penugasan mata
kuliah j dengan dosen pengampu i pada hari l pada slot
waktu (m ϵ M).
1 ≤ ∑ 𝑃𝑖𝑗 ≤ 𝑁𝑖 (𝑖 ∈ 𝐼)

(2.5)

𝑗∈𝐽

𝐿𝑇𝑗 ≤ ∑ 𝑃𝑖𝑗 ≤ 𝑈𝑇𝑗 (𝑗 ∈ 𝐽)

(2.6)

𝑖∈𝐼

∑ 𝑋𝑖𝑗𝑙𝑚 = 𝑌𝑖𝑗𝑙 𝐻𝑗 (𝑖 ∈ 𝐼, 𝑗 ∈ 𝐽, 𝑙 ∈ 𝐿)

(2.7)

𝑚∈𝑀

∑ 𝑋𝑖𝑗𝑙𝑚 ≤ 1 (𝑖 ∈ 𝐼, 𝑙 ∈ 𝐿, 𝑚 ∈ 𝑀)

(2.8)

𝑗∈𝐽

∑ ∑ 𝑋𝑖𝑗𝑙𝑚 ≤ 𝐶 (𝑚 ∈ 𝑀)

(2.9)

𝑖∈𝐼 𝑗∈𝐽

∑ ∑ 𝑌𝑖𝑗𝑙 = 1 (𝑗 ∈ 𝐽)
𝑖∈𝐼 𝑙∈𝐿

𝑋𝑖𝑗𝑙𝑚 = 0 (𝑖 ∈ 𝐼, 𝑗𝐽𝑖 , 𝑚 ∈ 𝑀)
∑ ∑ 𝑌𝑖𝑗𝑙 = 𝐿𝑖 (𝑖 ∈ 𝐼)

(2.10)
(2.11)
(2.12)

𝑗∈𝐽 𝑙∈𝐿

∑ 𝑌𝑖𝑗𝑙 ≤ 𝑉𝑖 (𝑖 ∈ 𝐼, 𝑙 ∈ 𝐿)

(2.13)

𝑗∈𝐽

𝑋𝑖𝑗𝑙𝑚 ∈ {0,1} (𝑖 ∈ 𝐼, 𝑗 ∈ 𝐽, 𝑙 ∈ 𝐿, 𝑚 ∈ 𝑀) (2.14)
(2.15)
𝑌𝑖𝑗𝑙 ∈ {0,1} (𝑖 ∈ 𝐼, 𝑗 ∈ 𝐽, 𝑙 ∈ 𝐿)

On-line : http://ejournal.undip.ac.id/index.php/jsinbis

(2.16)
𝑈𝑖𝑗𝑙𝑚 ∈ {0,1} (𝑖 ∈ 𝐼, 𝑗 ∈ 𝐽, 𝑙 ∈ 𝐿, 𝑚 ∈ 𝑀)
(2.17)
𝑃𝑖𝑗 ∈ {1,0} (𝑖 ∈ 𝐼, 𝑗 ∈ 𝐽)
(2.18)
𝐿𝑖 ∈ 𝑍 + (𝑖 ∈ 𝐼)
+ (𝑖
(2.19)
𝑉𝑖 ∈ 𝑍
∈ 𝐼)
Pers. (2.3) dan pers (2.4) menunjukkan objective
function yang akan dimaksimasi, merupakan
penjumlahan nilai preferensi yaitu penugasan dosen
ke mata kuliah, pemilihan hari dan slot waktu dosen
untuk mengajar dan penempatan slot waktu untuk
mata kuliah dalam dalam kurikulum yang sama. Pers.
(2.5) membatasi jumlah mata kuliah yang dapat
diampu oleh dosen, dosen paling tidak mengampu satu
mata kuliah.
Pers. (2.6) batasan jumlah minimum dan
maksimum dosen yang mengampu mata kuliah. Pers.
(2.7) merupakan penjumlahan slot waktu dosen
mengampu mata kuliah dalam sehari. Pers. (2.8)
memastikan bahwa setiap dosen hanya mengampu
satu mata kuliah tiap satu slot waktu. Pers. (2.9)
mencegah mata kuliah yang dijadwalkan pada satu
hari menggunakan slot waktu yang tersedia melebihi
jumlah kelas yang tersedia. Pers. (2.10) memastikan
hanya satu dosen yang mengampu satu mata kuliah.
Pers. (2.11) memastikan bahwa dosen tidak boleh
mengampu mata kuliah yang tidak dapat mereka
ampu. Pers. (2.12) menghitung jumlah mata kuliah
yang diampu oleh dosen. Pers. (2.13) menentukan
jumlah mata kuliah yang diampu dosen setiap harinya.
Pers. (2.14) – (2.17) merupakan konstrain atau batasan
dengan nilai 0-1 untuk variabel keputusan 𝑋𝑖𝑗𝑙𝑚 , 𝑌𝑖𝑗𝑙 ,
𝑈𝑖𝑗𝑙𝑚 , dan 𝑃𝑖𝑗 . Pers. (2.18) – (2.19) menentukan agar
nilai 𝐿𝑖 dan 𝑉𝑖 tidak negatif.
3. Metodologi
3.1. Alat dan Bahan Penelitian
Alat yang digunakan dalam penelitian ini
diantaranya: perangkat keras berupa Laptop Asus
Prosesor Intel® Core™ i3-3217U CPU @ 1.80GHz
1.70GHz, RAM 2.00 GB, Hardisk 500 GB dan
perangkat lunak yang digunakan adalah Microsoft
Windows 8 ultimate (32-bit) dan Matlab 2012a (32bit).
Bahan yang digunakan pada penelitian ini adalah
data program studi, data dosen, data mahasiswa aktif,
data mata kuliah, data ruang kelas serta kapasistas,
data jadwal semester aktif, dan data hari serta waktu
periode yang digunakan untuk perkuliahan. Data
tersebut diperoleh dari Fakultas Teknologi Industri
Unissula semester genap tahun ajaran 2015/2016.
Data yang terlibat dalam penelitian ini terdiri dari data
tiga program studi.
3.2. Prosedur Penelitian
Prosedur penelitian ini diawali dengan melakukan
identifikasi masalah, analisis kebutuhan sistem,
pengujian metode yang dipilih, membandingkan hasil
dengan metode lain. Hasil akhir penelitian ini adalah
penjadwalan mata kuliah pada perguruan tinggi.

Jurnal Sistem Informasi Bisnis 02(2016)

On-line : http://ejournal.undip.ac.id/index.php/jsinbis

Identifikasi
masalah
dengan
permasalahan
penjadwalan yang dihadapi yaitu, TACS (teacher
assignment course scheduling) merupakan penugasan
dosen pada mata kuliah untuk kemudian dialokasikan
ke slot waktu dan ruang yang tersedia. Dalam
penugasan dosen ke mata kuliah yang akan diampu
melibatkan penguasaan dosen terhadap mata kuliah,
dosen tidak dapat ditugaskan pada mata kuliah yang
tidak dikuasai secara materi. Selanjutnya adalah
alokasi mata kuliah dengan dosen pengampu pada slot
waktu dan ruang yang tersedia. Permasalahan ini
melibatkan bentrok dosen dalam slot waktu.
Agar penelitian yang dilakukan lebih terarah maka
dilakukan langkah-langkah dalam prosedur penelitian,
prosedur penelitian yang dilakukan dapat ditunjukkan
pada Gambar 2

137

Tahapan
berikutnya
adalah
melakukan
pembangunan sistem yang terdiri dari langkahlangkah perancangan sistem, desain sistem,
pembangunan sistem dan pengujian sistem yang
telah dibangun.
d. Saran Kesimpulan
Tahap terakhir adalah memberi kesimpulan atas
sistem yang telah dibangun dengan metode yang
digunakan mengenai efisiensi metode apakah telah
tepat digunakan untuk mengembangkan optimasi
penjadwalan mata kuliah pada perguruan tinggi.
3.3. Kerangka Sistem Informasi
Kerangka sistem informasi yang akan dibangun
terlihat pada Gambar 3 dengan input berupa data-data
yang dibutuhkan. Data yang dibutuhkan berupa data
dosen, data mata kuliah, data timeslot dan data
kurikulum. Pembuatan sistem melibatkan hard
constraint dan soft constraint. Hard constraint yang
terlibat adalah maksimum beban kerja dosen, jumlah
ruang yang tersedia dan jumlah waktu periode yang
tersedia. Soft constraint yang terlibat adalah preferensi
dosen untuk mengajar mata kuliah tertentu,
maksimum jumlah dosen yang dapat mengajar mata
kuliah tertentu, minimum jumlah dosen yang dapat
mengajar mata kuliah tertentu, dan preferensi dosen
mengajar mata kuliah tertentu dalam waktu periode
tertetu. Data input kemudian diolah sesuai ketentuan
dengan menggunakan metode simulated annealing
untuk optimasi baik proses maupun hasil.

Gambar 2 Prosedur Penelitian

Penjelasan tahapan prosedur penelitian:
a. Tahap Perencanaan
Tahapan ini menjelaskan tujuan utama dari
penelitian yang akan dilaksanakan.
b. Identifikasi Masalah
Merupakan tahapan dalam mengenali permasalahan
yang dihadapi mengenai penugasan dosen pada
mata kuliah yang diampu. Mata kuliah yang telah
memiliki dosen pengampu untuk kemudian
diplotkan pada slot waktu yang tersedia.
c. Studi Literatur
Setelah mengetahui permaslahan yang dihadapi
dilakukan studi literature mengenai permasalahan
tersebut. Studi literatur dilakukan dengan
melibatkan jurnal dan buku yang berkaitan serta
melakukan analisa kepada pihak-pihak yang
berhubungan dengan sistem penjadwalan di
Universitas.
d. Pembangunan Sistem

Gambar 3 . Kerangka sistem informasi

4. Hasil dan Pembahasan
4.1 Pengujian Sistem Informasi Penjadwalan Kuliah
Pada Gambar 4 menunjukkan distribusi mata
kuliah pada dosen pengampu. Dengan jumlah mata
kuliah sebanyak 152 didistribusikan pada 52 dosen
sesuai dengan bidang penguasaan materi. Data mata
kuliah dan dosen tersedia dalam bentuk excel, dimana
terdapat indexing dosen pengampu dalam penguasaan
materi. Data mata kuliah disertai jumlah sks dan dosen
pengampu. Dosen ditugaskan pada mata kuliah
dengan berbagai batasan yaitu jumlah minimum dan
maksimum dosen dapat mengampu mata kuliah dan
penguasaan mata kuliah oleh dosen. Antarmuka yang

138

Jurnal Sistem Informasi Bisnis 02(2016)

ditunjukkan menampilkan nama mata kuliah, kode
mata kuliah, jumlah sks dan dosen pengampu.

Gambar 4. Jadwal mata kuliah dan dosen pengampu

Jadwal dosen dan waktu slot pada Gambar 5
menunjukkan distribusi mata kuliah dengan dosen
pengampu pada waktu periode, hari dan ruang kelas
yang tersedia.Dengan jumlah mata kuliah sebanyak
152 dan slot (jumlah waktu periode X jumlah hari X
jumlah ruang) sebanyak 450 slot terdapat 129 mata
kuliah dengan sks yang sesuai mendapat plot pada slot
yang tersedia. Mata kuliah menempati slot waktu
sesuai dengan jumlah sks, jumlah sks yang digunakan
sesuai data pada studi kasus adalah 3 atau 2. Untuk
setiap sks adalah 50 menit, dan dalam 1 hari terdapat
10 waktu periode yang berarti 500 menit dalam sehari

On-line : http://ejournal.undip.ac.id/index.php/jsinbis

dan waktu istirahat pukul 12.00 – 13.00 tidak
digunakan dalam plotting mata kuliah. Waktu periode
dimulai dari pukul 07.00 untuk periode pertama dan
periode terakhir selesai pukul 16.20. Hari aktif yang
digunakan adalah hari senin hingga hari jumat dengan
ketersediaan ruang kelas dalam sehari adalah 9. Ruang
kelas yang digunakan adalah ruang kelas umum yang
dapat digunakan untuk perkuliahan biasa dan tersedia
sepanjang slot waktu.
4.2 Hasil Pengujian Sistem Informasi Penjadwalan
Kuliah
Hasil pengujian pengujian persamaan baik
objective function dan hard constraint. Objective
function 1 berfungsi untuk melakukan penugasan
dosen pada mata kuliah. Dalam penugasan dosen pada
mata kuliah melibatkan tiga batasan (hard constraints)
yaitu membatasi jumlah mata kuliah yang dapat
diampu oleh dosen paling tidak mengampu satu mata
kuliah (pers 2.5), memastikan hanya satu dosen yang
mengampu satu mata kuliah (pers 2.10) dan batasan
jumlah minimum dan maksimum dosen yang
mengampu mata kuliah (pers 2.6).
Pada Gambar 6 pada tabel pertama baris pertama
terlihat bahwa mata kuliah tepat diampu oleh satu
dosen berdasarkan hasil optimasi dengan jumlah yang
sama dengan data mentah (152). Data ini melakukan
pengujian persamaan 2.10 memastikan hanya satu
dosen yang mengampu satu mata kuliah.Sedangkan
pada tabel pertama baris kedua melakukan pengujian
terhadap persamaan 2.5 dimana satu dosen paling
tidak mengampu satu mata kuliah. Pada tabel kedua
melakukan pengujian terhadap persamaan 2.6 yaitu
dosen memiliki jumlah minimum dan maksimum
jumlah mata kuliah yang diampu

Gambar 5. Jadwal kuliah pada slot waktu

Jurnal Sistem Informasi Bisnis 02(2016)

On-line : http://ejournal.undip.ac.id/index.php/jsinbis

Tabel 1. Parameter Objective Function 1

Parameter
Total iterasi
Temperatur awal 𝑇0
Cooling factor 𝛼
Temperatur akhir 𝑇𝑛

139

sebanyak 95,3947. Hal ini berarti terdapat 7 mata
kuliah dengan dosen pengampu yang mengalami
bentrok. Dari jumlah mata kuliah yang tidak mendapat
plot slot waktu dan mata kuliah dengan dosen yang
mengalami bentrok maka didapat jumlah seluruh mata
kuliah yang tidak dapat mendapat plot pada slot waktu
yaitu sebanyak 30 mata kuliah atau setara dengan
80,2632%.

Nilai
|𝐼| 𝑥 |𝐽|
[1, 152]
{0.1}
0
Gambar 7. Optimasi jadwal dosen-matakuliah pada slot
waktu

Gambar 6. Optimasi data dosen dan mata kuliah

Pada Tabel 1 menunjukkan parameter yang
digunakan dalam persamaan objective function 1.
Total iterasi menunjukan jumlah perulangan dalam
pencarian dosen pengampu untuk mata kuliah yang
dapat diampu. Temperature awal menunjukan ruang
pencarian yaitu sebanyak jumlah data yang akan
dioptimasi. Faktor pendingin menunjukkan pengali
pada sekali iterasi pencarian solusi. Temperatur akhir
menunjukkan kondisi data setelah dioptimasi.
Tabel 2. Parameter Objective Function 1
Parameter
Nilai
Total iterasi
|𝐼| 𝑥 |𝐽|
[1, 152]
Temperatur awal 𝑇0
{0.1}
Cooling factor 𝛼
0
Temperatur akhir 𝑇𝑛
Pengujian objective function 2 pada persamaan
objective function 2 menghasilkan jadwal dosen dan
mata kuliah yang diampu. Setelah jadwal dosen dan
mata kuliah diketahui langkah selanjutnya adalah
menempatkan (plotting) jadwal dosen dan mata kuliah
pada slot waktu dan ruang yang tersedia. Slot waktu
terdiri dari jumlah hari dan periode yang tersedia.
Dalam penempatan jadwal dosen dan mata kuliah
melibatkan dua batasan (hard constraints) yaitu
mencegah mata kuliah yang dijadwalkan pada satu
hari menggunakan slot waktu yang tersedia melebihi
jumlah kelas yang tersedia (pers 2.9), dan memastikan
bahwa setiap dosen hanya mengampu satu mata kuliah
tiap satu slot waktu (pers 2.8).
152 mata kuliah dapat dialokasikan sebanyak 129
mata kuliah atau 84,8684%. Hal ini berarti terdapat 23
mata kuliah tidak dapat plotting pada slot waktu yang
tersedia. Pada baris kedua menunjukkan kondisi
bentrok dosen yang mengampu mata kuliah. Terlihat
bahwa terdapat sebanyak 145 mata kuliah dimana
dosen pengampu mata kuliah yang bersangkutan tidak
mengalami bentrok waktu periode yang tersedia atau

Pada Gambar 7 pada baris pertama terlihat bahwa
plotting mata kuliah pada slot waktu yang tersedia dari
Tabel 2 menunjukkan parameter yang digunakan
dalam persamaan objective function 2. Total iterasi
menunjukan jumlah perulangan dalam pencarian
dosen pengampu untuk mata kuliah yang dapat
diampu. Temperatur awal menunjukan ruang
pencarian yaitu sebanyak jumlah data yang akan
dioptimasi. Faktor pendingin menunjukkan pengali
pada sekali iterasi pencarian solusi. Temperatur akhir
menunjukkan kondisi data setelah dioptimasi.
Tabel 2. Parameter Objective Function 2
Parameter
Nilai
Total iterasi
|𝐼| 𝑥 |𝐽|
[1, 152]
Temperatur awal 𝑇0
{0.19}
Cooling factor 𝛼
30
Temperatur akhir 𝑇𝑛
Tabel 1 menunjukkan parameter yang digunakan
dalam persamaan objective function 2. Total iterasi
menunjukan jumlah perulangan dalam pencarian
dosen pengampu untuk mata kuliah yang dapat
diampu. Temperature awal menunjukan ruang
pencarian yaitu sebanyak jumlah data yang akan
dioptimasi. Faktor pendingin menunjukkan pengali
pada sekali iterasi pencarian solusi. Temperatur akhir
menunjukkan kondisi data setelah dioptimasi.
Temperatur awal menunjukkan jumlah data yang
akan dioptimasi yaitu data mata kuliah dengan dosen
pengampu sebanyak 152 data. Faktor pendingin 𝛼
merupakan faktor pengali pada percobaan diatas
menghasilkan nilai 0.19 yang menghasilkan
temperatur akhir yaitu 30. Temperatur akhir
menunjukkan jumlah mata kuliah yang tidak
mendapat plot pada slot waktu yang tersedia.
Sedangan analisa metode dengan data sampel dapat
ditunjukkan pada Tabel 3.

Jurnal Sistem Informasi Bisnis 02(2016)

140

On-line : http://ejournal.undip.ac.id/index.php/jsinbis

Tabel 3. Uji coba metode dengan data sampel
No

Objective Function 1
Dataset
Optimasi

𝑻𝟎

SA
𝜶

[1, 152]

{0.82}

26

[1, 10]

{0.7}

3

Dosen

Dosen-matkul

Hari x periode

Jumlah Kelas

Mata Kuliah

Dosen

Dosen-matkul

Dosen-matkul

𝑻𝒏

Mata Kuliah

Data

Dosen

𝑻𝒏

Mata Kuliah

𝑻𝟎

Dosen

(%)

Objective Function 2
dataset
Optimasi
(%)
Plotting slot waktu

Mata Kuliah

Data

SA
𝜶

1.

152

52

152

52

100

100

[1, 152]

{0.1}

0

152

5 x 10

9

129

149

126

2.

10

10

10

7

100

70

[1, 10]

{0.1}

0

10

5 x 10

9

8

9

7

82.8
9
70

3.
4.

10
10

10
10

10
10

7
7

100
100

70
70

[1, 10]
[1, 10]

{0.1}
{0.1}

0
0

10
10

5x5
5 x 10

9
2

7
10

9
9

6
9

60
90

[1, 10]
[1, 10]

{0.6}
{0.9}

4
1

5.
6.
7.
8.

10
10
10
10

10
5
5
5

10
10
10
10

7
5
5
5

100
100
100
100

70
100
100
100

[1, 10]
[1, 10]
[1, 10]
[1, 10]

{0.1}
{0.1}
{0.1}
{0.1}

0
0
0
0

10
10
10
10

5x5
5 x10
5x5
5 x 10

2
9
9
2

7
9
9
8

9
9
9
9

6
8
8
7

60
80
80
70

[1, 10]
[1, 10]
[1, 10]
[1, 10]

{0.6}
{0.8}
{0.8}
{0,7}

4
2
2
3

9.
10.

10
5

5
10

10
5

5
5

100
100

100
50

[1, 10]
[1, 5]

{0.1}
{0.1}

0
0

10
5

5x5
5 x 10

2
9

7
4

9
5

6
4

60
80

[1, 10]
[1, 5]

{0.6}
{0.4}

4
1

11.
12.

5
5

10
10

5
5

5
5

100
100

50
50

[1, 5]
[1, 5]

{0.1}
{0.1}

0
0

5
5

5x5
5 x 10

9
2

4
4

5
5

4
4

80
80

[1, 5]
[1, 5]

{0.4}
{0.4}

1
1

13.

5

10

5

5

100

50

[1, 5]

{0.1}

0

5

5 x 10

2

4

5

4

80

[1, 5]

{0.4}

1

Tabel 3 menunjukkan uji coba metode pada
beberapa variasi data. Data utama berupa data mata
kuliah dan data dosen yang digunakan bervariasi
dengan berbagai perbandingan. Variasi pertama
adalah perbandingan data mata kuliah dengan data
dosen 1:1. Dari percobaan untuk objective function 1
terlihat bahwa seluruh data baik mata kuliah dapat
teralokasi 100% sedangkan data dosen sebanyak 70%.
Temperatur awal adalah [1,10] yang merupakan
jumlah mata kuliah yang akan dialokasikan. Memiliki
faktor pendingin 𝛼 = 0,01. Dengan berbagai variasi
sumber daya berupa slot waktu, hari dan ruang kelas
didapat bahwa memiliki rata-rata 70 dalam optimasi
jadwal kuliah, yang memiliki arti rata-rata sebanyak
70% dari seluruh data yang harus dialokasikan.

Variasi kedua adalah perbandingan data mata
kuliah dengan data dosen 2:1. Untuk objective
function 1 didapatkan bahwa seluruh data dosen dan
data mata kuliah teralokasikan sebanyak 100%.
Dengan variasi jumlah waktu periode, hari dan jumlah
kelas maka didapat rata-rata alokasi mata kuliah ke
slot yang tersedia adalah 72,5 yang memiliki arti
sebanyak 72,5 % data mata kuliah dapat ditempatkan
pada slot yang tersedia.
Untuk variasi ketiga adalah perbandingan data
mata kuliah dengan data dosen 1:2. Data mata kuliah
100 % dapat dialokasikan sedang data dosen sebanyak
50 %. Dengan variasi jumlah waktu periode, hari dan
jumlah kelas maka didapat rata-rata alokasi mata
kuliah ke slot yang tersedia adalah 80 yang memiliki
arti sebanyak 80 % data mata kuliah dapat
ditempatkan pada slot yang tersedia.

Tabel 4. Analisa dengan variasi data sampel
Hari/Waktu Periode

Jumlah Ruang Kelas

Jumlah Dosen

Jumlah Mata Kuliah

Dosen-matkul

Dosen

Mata Kuliah

Dosen-matkul

Optimasi SA
Plotting pada
slot waktu dgn
batasan

Jumlah Mata Kuliah

Dataset

Jumlah Dosen

No

1.

10

10

5 x 10

9

7

10

10

9

8

7

2.

10

10

5x5

9

7

10

10

9

7

6

3.

10

10

5 x 10

2

7

10

10

9

10

9

Kesimpulan-Solusi

- Dengan jumlah mata kuliah dan dosen yang sama, dimana kemampuan dosen dalam
mengampu mata kuliah satu dan atau lebih maka ada dosen yang tidak dapat plot
mata kuliah.
- Menambah slot waktu dalam sehari
- Solusi untuk sisa mata kuliah yang tidak dapat diplotkan adalah meletakkan pada
slot waktu yang kosong
- Menambah slot waktu dalam sehari
- Solusi untuk sisa mata kuliah yang tidak dapat diplotkan adalah meletakkan pada
slot waktu yang kosong
- Solusi untuk sisa mata kuliah yang tidak dapat diplotkan adalah meletakkan pada
slot waktu yang kosong

Jurnal Sistem Informasi Bisnis 02(2016)

Hari/Waktu Periode

Jumlah Ruang Kelas

Jumlah Dosen

Jumlah Mata Kuliah

Dosen-matkul

Dosen

Mata Kuliah

Dosen-matkul

Optimasi SA
Plotting pada
slot waktu dgn
batasan

Jumlah Mata Kuliah

Dataset

Jumlah Dosen

No

On-line : http://ejournal.undip.ac.id/index.php/jsinbis

4.

10

10

5 x 10

2

7

10

10

9

7

6

5.

5

10

5 x 10

9

5

10

10

9

9

8

6.

5

10

5x5

9

5

10

10

9

9

8

7.

5

10

5 x 10

2

5

10

10

9

8

7

8.

5

10

5x5

2

5

10

10

9

7

6

9.

10

5

5 x 10

9

5

5

5

5

4

4

10.

10

5

5x5

9

5

5

5

5

4

4

11.

10

5

5 x 10

2

5

5

5

5

4

4

12.

10

5

5x5

2

5

5

5

5

4

4

Dari percobaan yang telah dilakukan variasi
perbadingan data dosen dengan mata kuliah dengan
perbadingan 1:1, 1:2 dan 2:1 memiliki hasil optimal
pada data dengan perbandingan 2:1. Dengan jumlah
slot waktu dan ruang kelas yang bervariasi prosentase
optimasi untuk jadwal kuliah memiliki nilai yang
stabil yaitu 80%. Dengan data dosen yang lebih
banyak maka penugasan dosen ke mata kuliah dapat
lebih optimal dengan mempertimbangkan batasanbatasan berupa jumlah maksimum dosen mengampu
mata kuliah. Dari percobaan dengan data real dapat
diketahui perbandingan jumlah mata kuliah yang lebih
banyak dari dosen dengan nilai 1:3 masih didapatkan
hasil optimal (100%) untuk penugasan dosen ke mata
kuliah.
Untuk objective function 1, hasil yang optimal
didapatkan dengan memperhatikan keseimbangan
jumlah dosen yang tersedia untuk mengampu mata
kuliah. Apabila jumlah dosen terlalu sedikit dibanding
dengan jumlah mata kuliah, maka pelanggaran
terhadap batasan jumlah maksimum dosen mengampu
mata kuliah akan terjadi. Untuk objective function 2,
hasil yang optimal didapat apabila jumlah slot waktu

141

Kesimpulan-Solusi

- Menambah slot waktu dalam sehari
- Solusi untuk sisa mata kuliah yang tidak dapat diplotkan adalah meletakkan pada
slot waktu yang kosong dan menambah slot waktu dan ruang
- Dengan jumlah mata kuliah lebih banyak dari jumlah dosen, maka semua mata
kuliah dapat terdistribusi ke seluruh dosen yang tersedia
- Solusi agar semua mata kuliah dapat terdistribusi adalah menambah jumlah dosen
- Solusi untuk sisa mata kuliah yang tidak dapat diplotkan adalah meletakkan pada
slot waktu yang kosong
- Dengan jumlah mata kuliah lebih banyak dari jumlah dosen, maka semua mata
kuliah dapat terdistribusi ke seluruh dosen yang tersedia
- Menambah slot waktu dalam sehari
- Solusi untuk sisa mata kuliah yang tidak dapat diplotkan adalah meletakkan pada
slot waktu yang kosong
- Dengan jumlah mata kuliah lebih banyak dari jumlah dosen, maka semua mata
kuliah dapat terdistribusi ke seluruh dosen yang tersedia
- Solusi untuk sisa mata kuliah yang tidak dapat diplotkan adalah meletakkan pada
slot waktu yang kosong
- Dengan jumlah mata kuliah lebih banyak dari jumlah dosen, maka semua mata
kuliah dapat terdistribusi ke seluruh dosen yang tersedia
- Solusi untuk sisa mata kuliah yang tidak dapat diplotkan adalah meletakkan pada
slot waktu yang kosong
- menambah slot waktu dan ruang
- Dengan jumlah mata kuliah lebih sedikit dari jumlah dosen yang tersedia , maka
distribusi dosen yang mengampu mata kuliah adalah sebanyak jumlah mata kuliah.
- Solusi untuk sisa mata kuliah yang tidak dapat diplotkan adalah meletakkan pada
slot waktu yang kosong
- Dengan jumlah mata kuliah lebih sedikit dari jumlah dosen yang tersedia , maka
distribusi dosen yang mengampu mata kuliah adalah sebanyak jumlah mata kuliah.
- Solusi untuk sisa mata kuliah yang tidak dapat diplotkan adalah meletakkan pada
slot waktu yang kosong
- Dengan jumlah mata kuliah lebih sedikit dari jumlah dosen yang tersedia , maka
distribusi dosen yang mengampu mata kuliah adalah sebanyak jumlah mata kuliah.
- Solusi untuk sisa mata kuliah yang tidak dapat diplotkan adalah meletakkan pada
slot waktu yang kosong
- Dengan jumlah mata kuliah lebih sedikit dari jumlah dosen yang tersedia , maka
distribusi dosen yang mengampu mata kuliah adalah sebanyak jumlah mata kuliah.
- Solusi untuk sisa mata kuliah yang tidak dapat diplotkan adalah meletakkan pada
slot waktu yang kosong

yang tersedia cukup untuk penempatan mata kuliah.
Beberapa solusi yang ditawarkan adalah sisa mata
kuliah yang tidak dapat diplotkan adalah meletakkan
pada slot waktu yang kosong, penambahan slot waktu
dan penambahan ruang kelas yang dapat digunakan.
Pada Tabel 5 dapat ditunjukkan hasil percobaan
dengan SA. Analisa penyimpangan hasil percobaan
metode SA pada Percobaan dengan data real dengan
menggunakan sebanyak 152 data mata kuliah dan 52
data dosen menghasilkan variasi terhadap prosentase
optimasi. Dari percobaan yang dilakukan sebanyak 20
kali seperti yang terlihat pada tabel 5 dilakukan
perhitungan simpangan baku atau standar deviasi.
Standar deviasi dari percobaan didapatkan nilai
3.931509.
1
𝑠 = √ ∑ 𝑓𝑖 (𝑥𝑖 − 𝑥)2 = 1.982803
𝑛
Dari hasil perhitungan didapat nilai standar deviasi
sebesar 1.982803, nilai ini menunjukkan keberagaman
hasil percobaan dengan beberapa data sampel dengan
nilai berkisar 3 merupakan nilai yang tidak begitu
besar sehingga dapat disimpulkan bahwa metode yang

Jurnal Sistem Informasi Bisnis 02(2016)

142

digunakan memiliki kestabilan dalam melakukan
optimasi untuk menghasilkan jadwal kuliah.

On-line : http://ejournal.undip.ac.id/index.php/jsinbis

diletakan dalam 1 hari kerja. Jumlah penambahan
waktu periode terbanyak adalah 15 x jumlah sks, maka
diperlukan penambahan 1 hari kerja untuk
penempatan mata kuliah.

Tabel 5. Penyimpangan hasil percobaan dengan SA
No

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20

Percobaan
ke1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
Rata-rata

Jumlah
Data
teroptimasi
118
116
122
113
116
118
116
112
118
122
115
119
119
121
124
120
122
118
117
119

Prosentase
(𝑋𝑖 )
77,63
76,31
80,26
74,34
76,31
77,63
76,31
73,68
77,63
80,26
75,65
78,28
78,28
79,60
81,57
78,94
80,26
77,63
76,97
78,28
77.791

Hasil pengujian dengan metode solusi Metode SA
awal digunakan memiliki rata-rata varian pembuatan
jadwal kuliah sebanyak 77.791 hal ini menunjukkan
bahwa ada mata kuliah yang tidak mendapat plot pada
slot waktu yang tersedia. Pada percobaan
dikembangakn metode solusi untuk mengatasi
permasalahan ini. Pada langkah metode pertama
memungkinkan adanya slot yang kosong dikarenakan
beberapa batasan yang digunakan. Metode solusi yang
ditawarkan melakukan penggunaan kembali slot-slot
yang tidak terpakai untuk mata kuliah yang belum
mendapat plot pada slot waktu. Pada tabel 6
menunjukkan beberapa hasil percobaan optimasi data
mata kuliah yang tidak mendapat slot pada metode
yang pertama.
Metode ini melakukan pengambilan slot yang
belum terpakai. Pada percobaan dengan jumlah hari
sebanyak 5, waktu periode sebanyak 10 dan ruang
kelas sebanyak 9 disimpulkan bahwa untuk
mengalokasikan seluruh data mata kuliah memerlukan
tambahan waktu periode. Tambahan waktu periode
dilakukan setelah periode terakhir dalam sehari.
Penambahan waktu periode dianggap lebih efisien
dibanding penambahan ruang kelas, karena tidak
memerlukan penambahan sumber daya ruang kelas
yang mungkin saja memiliki jumlah yang terbatas.
Penambahan waktu periode paling sedikit
berjumlah 9 x jumlah sks periode dengan asumsi
waktu periode maksimum untuk satu mata kuliah
adalah 3 sks atau 3 periode, maka dengan penggunaan
9 ruang kelas penambahan 9 waktu periode dapat

Tabel 6. Analisa optimasi dengan metode solusi
No

Metode SA
Mata Kuliah
tidak
Terplotting

Metode Solusi
Mata Kuliah
terplotting

Keterangan

1

34

25

9

2

36

19

17

3

30

21

9

4

39

22

17

5

36

21

15

6

34

25

9

7

36

19

17

8

40

24

16

9

34

16

18

10

30

19

11

11

37

22

14

12

33

19

14

13

33

14

19

14

31

21

10

15

28

18

10

16

32

19

13

17

30

19

11

18

34

11

13

19

35

21

14

20

33

21

12

Mata Kuliah
tidak
Terplotting
Membutuhkan
tambahan slot waktu
sebanyak
(9xjumlah_sks)
Membutuhkan
tambahan slot waktu
sebanyak
(17xjumlah_sks)
Membutuhkan
tambahan slot waktu
sebanyak
(9xjumlah_sks)
Membutuhkan
tambahan slot waktu
sebanyak
(17xjumlah_sks)
Membutuhkan
tambahan slot waktu
sebanyak
(15xjumlah_sks)
Membutuhkan
tambahan slot waktu
sebanyak
(9xjumlah_sks)
Membutuhkan
tambahan slot waktu
sebanyak
(17xjumlah_sks)
Membutuhkan
tambahan slot waktu
sebanyak
(16xjumlah_sks)
Membutuhkan
tambahan slot waktu
sebanyak
(18xjumlah_sks)
Membutuhkan
tambahan slot waktu
sebanyak
(11xjumlah_sks)
Membutuhkan
tambahan slot waktu
sebanyak
(14xjumlah_sks)
Membutuhkan
tambahan slot waktu
sebanyak
(14xjumlah_sks)
Membutuhkan
tambahan slot waktu
sebanyak
(19xjumlah_sks)
Membutuhkan
tambahan slot waktu
sebanyak
(17xjumlah_sks)
Membutuhkan
tambahan slot waktu
sebanyak
(17xjumlah_sks)
Membutuhkan
tambahan slot waktu
sebanyak
(17xjumlah_sks)
Membutuhkan
tambahan slot waktu
sebanyak
(17xjumlah_sks)
Membutuhkan
tambahan slot waktu
sebanyak
(17xjumlah_sks)
Membutuhkan
tambahan slot waktu
sebanyak
(14xjumlah_sks)
Membutuhkan
tambahan slot waktu
sebanyak
(12xjumlah_sks)

Jurnal Sistem Informasi Bisnis 02(2016)

On-line : http://ejournal.undip.ac.id/index.php/jsinbis

5. Kesimpulan
Berdasarkan hasil penelitian optimasi jadwal
kuliah dengan menggunakan metode simulated
annealing diperoleh kesimpulan sebagai berikut :
1. Dari hasil penelitian optimasi jadwal kuliah
dengan menggunakan Simulated Annealing
dengan menggunakan data mata kuliah sebanyak
152, data dosen sebanyak 52, data hari sebanyak 5,
data waktu periode per hari sebanyak 10 dan data
ruang sebanyak 9 diperoleh hasil rata-rata varian
alokasi mata kuliah pada slot waktu yang tersedia
adalah 77.791 dengan standar deviasi sebesar
1.982803
2. Pada hasil penelitian yang dilakukan dengan
menggunakan beberapa variasi data diperoleh
jumlah perbadingan ideal untuk hasil optimasi
yang maksimal adalah jumlah mata kuliah dan
dosen dengan perbandingan 1:3.
3. Metode
solusi
yang
ditawarkan
untuk
mendapatkan hasil optimal yaitu penempatan
seluruh mata kuliah pada slot waktu dapat
dilakukan dengan penggunaan kembali slot waktu
yang kosong dan penambahan slot waktu dengan
prosentase minimal mata kuliah yang ditempatkan
pada slot baru adalah 0.059% dan prosentase
maksimal mata kuliah yang ditempatkan pada slot
baru adalah 0.12%.
Daftar Pustaka
Babei, H., Karimpour, J., Hadidi, A., 2015. A survey
of approaches for university course timetabling
problem, Computers & Industrial Engineering 86,
43–59.

143

Basir, N., Ismail, W., Norwawi,. 2013. A Simulated
Annealing for Tahmidi course Timetabling,
Procedia Technology 11, 437 – 445.
Cacchiani, V., Caprara, A., Roberti, R., Toth, R.,
2013. A new lower bound for curriculum-based
course timetabling, Computers & Operations
Research 40, 2466-2477.
Chamber, L.D., 1998. Practical Handbook of Genetic
Algorithms: Complex Coding Systems, Volume 3,
New York: CRC Press.
Chibante, R., 2010. Simulated Annealing Theory with
Applications, Rijeka: Sciyo.
Daskalaki, S., Birbas, T., Housos, E., 2004. An integer
programming formulation for a case study in
university timetabling, European Journal of
Operational Research 153, 117–135.
Fong, C.W., Asmuni, H., McCollum, B., McMullan,
P., Omatu, S., 2014. A new hybrid imperialist
swarm-based optimization algorithm for university
timetabling problems, Information Sciences 283,
1–21.
Gunawan, A., Ng, K.M., Poh, K.L., 2012. A
hybridized Lagrangian relaxation and simulated
annealing method for the course timetabling
problem, Computers& Operations Research 39,
3074–3088.
Kalivas, J.H., 1995. Adaption of simulated annealing
to chemical optimization problems, Elsevier:
Amsterdam.
Mu, C.H., Xie, J., Liu, Y., Chen, F., Liu, Y., Jiao, L.C.,
2015. Memetic algorithm with simulated annealing
strategy and tightnessgreedy optimization for
community detection in networks, Applied Soft
Computing 34, 485–501.
Yamit, Zulian. 2011. Manajemen Produksi & Operasi.
Yogyakarta: Ekonisia.

