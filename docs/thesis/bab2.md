# BAB 2
# TINJAUAN PUSTAKA

## 2.1 Penelitian Terdahulu

Penelitian tentang optimasi penjadwalan perkuliahan telah berkembang secara signifikan selama beberapa dekade terakhir. Berbagai pendekatan telah diterapkan untuk menyelesaikan University Course Timetabling Problem (UCTP), mulai dari metode eksak hingga pendekatan metaheuristik. Pemahaman terhadap penelitian-penelitian terdahulu menjadi fondasi penting dalam pengembangan solusi yang lebih efektif dan efisien.

Berdasarkan kajian literatur yang sistematis, metode optimasi untuk penjadwalan dapat dikategorikan menjadi beberapa kelompok utama. Metode eksak seperti Integer Linear Programming dan Constraint Programming dapat memberikan solusi optimal untuk masalah berukuran kecil, namun menjadi tidak feasible untuk masalah berskala besar karena kompleksitas waktu komputasi yang eksponensial (Bashab et al., 2023). Oleh karena itu, pendekatan heuristik dan metaheuristik menjadi lebih populer untuk menyelesaikan UCTP dalam konteks praktis.

Simulated Annealing (SA) pertama kali diperkenalkan oleh Kirkpatrick, Gelatt, dan Vecchi pada tahun 1983 dalam paper seminal mereka yang berjudul "Optimization by Simulated Annealing" yang dipublikasikan dalam jurnal Science (Kirkpatrick et al., 1983). Sejak saat itu, SA telah menjadi salah satu metode paling populer untuk menyelesaikan berbagai masalah optimasi kombinatorial termasuk UCTP. Keunggulan utama SA terletak pada kemampuannya untuk menghindari local optimum melalui mekanisme penerimaan solusi worse secara probabilistik, menjadikannya sangat efektif untuk masalah dengan lanskap solusi yang kompleks dan memiliki banyak local minima (Geman & Geman, 1984).

Dalam konteks UCTP, penelitian oleh Wiktasari dan Suseno (2016) mendemonstrasikan penerapan SA dengan lima variabel utama: dosen, mata kuliah, slot waktu, hari, dan ruang kelas. Penelitian tersebut menunjukkan bahwa SA mampu menghasilkan jadwal dengan rata-rata 77,791% dari data dapat mencapai solusi optimal dengan standar deviasi 3,93, memvalidasi efektivitas metode ini untuk masalah penjadwalan perkuliahan di Indonesia (Wiktasari & Suseno, 2016). Studi serupa oleh Sukhoco et al. (2024) memperkuat temuan ini dengan membuktikan bahwa SA sangat sesuai diterapkan pada studi kasus penjadwalan akademik di lingkungan kampus dengan kompleksitas data yang tinggi.

Tabu Search sebagai algoritma metaheuristik dikembangkan oleh Fred Glover dan colleagues pada tahun 1980an. Berbeda dengan SA yang menggunakan probabilitas untuk menghindari local optimum, Tabu Search menggunakan struktur memori berupa tabu list untuk mengarahkan pencarian ke solusi-solusi yang belum dieksplorasi (Glover et al., 2007). Komponen utama Tabu Search adalah tabu list yang menyimpan informasi tentang solusi atau move yang telah dikunjungi recently dan tidak boleh dikunjungi kembali dalam beberapa iterasi berikutnya. Keunggulan Tabu Search terletak pada kemampuannya untuk melakukan eksploitasi yang intensif pada daerah solusi yang menjanjikan, menjadikannya komplementer dengan SA yang lebih kuat dalam eksplorasi.

Pendekatan hybrid yang menggabungkan SA dan Tabu Search telah menunjukkan performansi yang sangat kompetitif dalam menyelesaikan UCTP. Penelitian Muklason, Marom, dan Premananda (2024) mengembangkan algoritma Tabu-Simulated Annealing Hyper-Heuristics yang menggabungkan kedua metode tersebut dengan konsep hyper-heuristics. Studi mereka menggunakan Socha Dataset sebagai benchmark dan hasilnya menunjukkan bahwa algoritma yang dikembangkan menduduki peringkat kedua dari sepuluh algoritma yang diuji, dengan solusi terbaik pada 6 dari 11 dataset yang diuji. Hasil eksperimen menunjukkan bahwa algoritma hibrida SA-TS mampu menghasilkan penalty score yang rendah, dengan rata-rata penalty 0 untuk small instances dan rata-rata penalty di bawah 200 untuk medium instances (Muklason et al., 2024).

Penelitian lain yang mendukung pendekatan hybrid adalah Kaviani et al. (2014) yang menunjukkan bahwa algoritma hibrida TABUSA mampu menemukan solusi optimal pada sebagian besar kasus Quadratic Assignment Problem (QAP) dan memberikan relative percentage deviation (RPD) yang lebih rendah dibandingkan dengan Tabu Search murni. Keunggulan utama dari pendekatan hybrid SA-TS adalah keseimbangan antara exploitation dan exploration dalam proses pencarian solusi. Tabu Search memiliki kemampuan exploitation yang kuat melalui penggunaan tabu list untuk menghindari kunjungan ke solusi yang sama secara berulang, sementara SA memiliki kemampuan exploration yang baik melalui penerimaan solusi worse secara probabilistik untuk menghindari local optima.

Penggunaan Greedy Algorithm sebagai initial solution dalam konteks UCTP juga telah dibuktikan efektif oleh berbagai penelitian. Coşar, Say, dan Dökeroğlu (2022) mengembangkan algoritma Greedy-CB-CTT yang menggunakan berbagai heuristik seperti Largest-First, Smallest-First, Best-Fit, Average-weight first, dan Highest Unavailable course-first untuk mengassign mata kuliah ke ruangan yang tersedia. Hasil eksperimen pada 21 problem instance dari benchmark set ITC-2007 menunjukkan bahwa algoritma greedy yang diusulkan dapat menghasilkan solusi feasible dengan zero hard constraint violations pada 18 problem instance, menunjukkan bahwa Greedy Algorithm mampu memberikan solusi awal yang berkualitas tinggi dalam waktu komputasi yang sangat singkat.

Dalam aspek pengembangan sistem, Uysal et al. (2025) mengembangkan web-based DSS yang menggunakan algoritma Simulated Annealing untuk optimasi penjadwalan kursus online. Sistem yang dibangun memungkinkan koordinasi program untuk melakukan penyesuaian yang diperlukan, sementara mahasiswa dan dosen mengakses jadwal mereka melalui antarmuka yang ramah pengguna. Hasil eksperimen menunjukkan peningkatan substansial dalam distribusi koneksi concurrent dan efisiensi bandwidth. Penelitian Romaguera et al. (2023) juga mengembangkan web-based course timetabling system menggunakan Enhanced Genetic Algorithm dengan heuristic mutation yang concentrate pada mutasi gen yang infeasible untuk meningkatkan kemampuan exploration dan exploitation algoritma.

Ringkasan penelitian-penelitian terdahulu yang relevan dapat dilihat pada tabel berikut:

**Tabel 2.1 Ringkasan Penelitian Terdahulu terkait Optimasi Penjadwalan**

| No. | Peneliti (Tahun) | Metode | Jenis Masalah | Dataset/Benchmark | Hasil Utama | Keterangan |
|-----|------------------|--------|---------------|-------------------|-------------|------------|
| 1 | Kirkpatrick et al. (1983) | Simulated Annealing | Optimasi Kombinatorial General | - | Memperkenalkan konsep SA yang terinspirasi proses annealing dalam metalurgi | Paper seminal SA |
| 2 | Glover et al. (2007) | Tabu Search | Optimasi Kombinatorial General | - | Memperkenalkan konsep tabu list dan strategi intensification/diversification | Paper seminal TS |
| 3 | Metropolis et al. (1953) | Metropolis Criterion | Statistical Mechanics | - | Mengembangkan kriteria penerimaan probabilistik untuk SA | Dasar teoretis SA |
| 4 | Geman & Geman (1984) | Stochastic Relaxation | Image Restoration | - | Menurunkan fungsi Boltzmann untuk penerimaan solusi worse | Dasar teoretis SA |
| 5 | Wiktasari & Suseno (2016) | Simulated Annealing | UCTP Indonesia | Data perguruan tinggi Indonesia | 77.791% data mencapai solusi optimal, SD=3.93 | Validasi SA untuk konteks Indonesia |
| 6 | Sukhoco et al. (2024) | Simulated Annealing | UCTP | Data kampus Indonesia | SA sesuai untuk penjadwalan akademik kompleks | Penelitian SA terkini Indonesia |
| 7 | Muklason et al. (2024) | Tabu-Simulated Annealing Hyper-Heuristics | UCTP | Socha Dataset | Peringkat 2 dari 10 algoritma, solusi terbaik 6/11 dataset | Hybrid SA-TS dengan Hyper-Heuristics |
| 8 | Kaviani et al. (2014) | TABUSA (Hybrid TS-SA) | Quadratic Assignment Problem (QAP) | Benchmark QAP | RPD lebih rendah dibanding pure Tabu Search | Pendekatan hybrid untuk QAP |
| 9 | Coşar et al. (2022) | Greedy Algorithm (Greedy-CB-CTT) | Curriculum-based Course Timetabling | ITC-2007 (21 instances) | Zero hard constraint violations pada 18/21 instance | Efektif sebagai initial solution |
| 10 | Goh et al. (2017) | SAIRL (SA dengan Improved Reheating) | Post-Enrolment Course Timetabling | Socha Dataset | Meningkatkan kemampuan escape dari local optimum | Variasi SA dengan reheating |
| 11 | Xu et al. (2025) | Simulated Annealing | High-Dimensional Optimization | Synthetic high-dim data | Partial-coordinate updates lebih efisien | Move Schemes Impact on SA |
| 12 | Uysal et al. (2025) | Web-based DSS dengan SA | Online Course Timetabling | Data online education | Peningkatan distribusi koneksi concurrent dan efisiensi bandwidth | DSS berbasis web |
| 13 | Romaguera et al. (2023) | Enhanced Genetic Algorithm | Course Timetabling | - | Web-based system dengan heuristic mutation | GA untuk timetabling |
| 14 | Latpate et al. (2024) | AI-based Automatic Generator | Timetabling | - | Menghasilkan jadwal dalam menit dengan React UI | AI + React implementation |
| 15 | Cruz-Rosales et al. (2022) | Metaheuristic dengan Cooperative Processes | UCTP | - | Model matematika fungsi fitness dengan bobot penalti | Cooperative processes approach |
| 16 | Bashab et al. (2023) | Systematic Review | UCTP | Review 150+ paper | 35% publikasi terbaru menggunakan hybrid algorithm | State-of-the-art review |


## 2.2 University Course Timetabling Problem

University Course Timetabling Problem (UCTP) merupakan salah satu permasalahan kompleks yang sering dihadapi oleh institusi pendidikan tinggi di seluruh dunia. UCTP secara formal didefinisikan sebagai masalah optimasi kombinatorial yang bertujuan untuk mengalokasikan sumber daya berupa waktu, ruang, dosen, dan mata kuliah ke dalam slot waktu tertentu dengan mempertimbangkan berbagai constraint yang telah ditetapkan oleh institusi (Bashab et al., 2023).

Sebagai masalah NP-COP (Non-Polynomial Combinatorial Optimization Problem), UCTP memiliki karakteristik khusus yang membedakannya dari masalah optimisasi konvensional. Pertama, tidak ada metode yang dapat menyelesaikannya dalam waktu polinomial yang masuk akal, membuat pendekatan brute-force tidak feasible untuk kasus nyata. Kedua, waktu komputasi yang diperlukan untuk mencapai solusi feasible meningkat secara eksponensial seiring bertambahnya ukuran masalah (jumlah dosen, kelas, ruang, dan constraint). Solusi optimal hanya dapat dicapai untuk kasus-kasus berukuran kecil, sementara mayoritas kasus nyata memerlukan algoritma aproksimasi yang tidak menjamin optimalitas tetapi mampu menghasilkan solusi yang cukup baik (Bashab et al., 2023).

### 2.2.1 Hard Constraints dan Soft Constraints

Dalam konteks UCTP, constraint atau batasan dapat dikategorikan menjadi dua kategori utama yaitu hard constraints dan soft constraints. Hard constraints adalah batasan yang harus dipenuhi 100% untuk menghasilkan jadwal yang valid dan feasible. Pelanggaran terhadap hard constraints membuat jadwal tidak dapat digunakan sama sekali karena akan mengakibatkan konflik fundamental seperti dosen mengajar di dua kelas berbeda pada waktu yang sama, atau ruangan yang digunakan secara bersamaan oleh dua mata kuliah berbeda. Contoh hard constraints yang umum ditemukan meliputi lecturer conflict (tidak boleh terjadi bentrokan jadwal dosen), room capacity conflict (kapasitas ruangan harus sesuai dengan jumlah mahasiswa), daily SKS limit (dosen tidak boleh melebihi batas maksimal SKS per hari), dan exclusive room constraint (ruang laboratorium bersifat eksklusif untuk program studi tertentu) (Wiktasari & Suseno, 2016).

Soft constraints adalah batasan yang tidak wajib dipenuhi 100%, tetapi pelanggaran memberikan penalti yang mengurangi kualitas jadwal. Minimisasi pelanggaran soft constraints bertujuan untuk meningkatkan kepuasan pengguna (dosen dan mahasiswa) dengan mempertimbangkan preferensi dan kenyamanan. Contoh soft constraints meliputi teaching time preference (preferensi mengajar dosen pada waktu tertentu), room preference (kebutuhan ruang dengan teknologi spesifik), transit time between classes (waktu memadai untuk berpindah antar ruang), dan schedule density optimization (menghindari jadwal yang terlalu renggang atau terlalu padat). Penelitian oleh Bashab et al. (2023) menunjukkan bahwa semakin banyak constraint yang dipertimbangkan, semakin kompleks ruang solusi dan semakin sulit untuk menemukan jadwal yang optimal.

### 2.2.2 Kompleksitas dan Tantangan UCTP

Kompleksitas UCTP meningkat secara eksponensial dengan penambahan jumlah variabel dan constraint yang harus dipertimbangkan. Menurut Bashab et al. (2023), tantangan utama dalam menyelesaikan UCTP meliputi kebutuhan untuk mengakomodasi preferensi dari berbagai pihak (dosen, mahasiswa, administrator), kompleksitas dataset berskala besar dengan ratusan kelas, puluhan dosen, dan puluhan ruangan, serta kebutuhan khusus institusional yang bersifat context-specific seperti batasan religius atau jam istirahat fakultas.

Berdasarkan karakteristik tersebut, UCTP di Universitas Internasional Semen Indonesia (UISI) memiliki kompleksitas tambahan berupa constraint spesifik seperti religious time prohibition (tidak boleh ada jadwal pada jam sekitar Dzuhur/Maghrib dan periode Jumat) dan class category constraint (kelas pagi dan sore harus dijadwalkan sesuai waktunya). Kompleksitas ini memerlukan pendekatan algoritma yang sophisticated untuk dapat menghasilkan jadwal yang feasible dan optimal dalam waktu yang reasonable.

## 2.3 Decision Support System

Decision Support System (DSS) atau Sistem Pendukung Keputusan merupakan sistem informasi berbasis komputer yang membantu pengambil keputusan dalam memanfaatkan data, model analitis, dan alat komunikasi untuk mengidentifikasi dan memecahkan masalah (Uysal et al., 2025). DSS berbeda dari sistem informasi manajemen tradisional karena DSS fokus pada keputusan semi-terstruktur dan tidak terstruktur yang memerlukan judgment manusia, sedangkan sistem informasi manajemen tradisional lebih fokus pada keputusan terstruktur yang dapat diotomatisasi sepenuhnya.

Dalam konteks penjadwalan kuliah, DSS berfungsi sebagai alat bantu bagi pengambil keputusan (dalam hal ini bagian Administrasi Akademik) untuk menghasilkan jadwal kuliah yang optimal. Sistem DSS untuk penjadwalan memungkinkan pengguna untuk memasukkan parameter dan constraint yang diinginkan, menjalankan algoritma optimasi, dan menganalisis solusi yang dihasilkan untuk kemudian melakukan penyesuaian jika diperlukan. Penelitian Uysal et al. (2025) menunjukkan bahwa web-based DSS yang menggunakan algoritma Simulated Annealing dapat secara signifikan meningkatkan efisiensi proses penjadwalan dengan menghasilkan distribusi beban yang lebih seimbang dan meminimalkan konflik jadwal.

### 2.3.1 Arsitektur DSS untuk Penjadwalan

Arsitektur DSS untuk sistem penjadwalan umumnya terdiri dari beberapa komponen utama. Komponen pertama adalah Database Management System yang menyimpan data akademis seperti data dosen, mata kuliah, ruangan, dan mahasiswa. Komponen kedua adalah Model Management System yang mengandung berbagai model matematika dan algoritma untuk optimasi penjadwalan. Komponen ketiga adalah User Interface yang memungkinkan interaksi antara pengguna dan sistem untuk memasukkan parameter, menjalankan algoritma, dan menampilkan hasil. Komponen keempat adalah Communication System yang menghubungkan semua komponen dan memfasilitasi pertukaran data (Uysal et al., 2025).

Berdasarkan penelitian Romaguera et al. (2023), implementasi web-based DSS untuk penjadwalan memerlukan arsitektur yang memungkinkan akses online dan kemampuan untuk menangani berbagai jenis dataset. Sistem yang dibangun harus memiliki antarmuka yang ramah pengguna yang memungkinkan administrator dan faculty members untuk dengan mudah menggunakan sistem tanpa pelatihan khusus (Latpate et al., 2024). Arsitektur REST API menjadi pilihan yang populer karena memungkinkan integrasi yang modular dan skalabilitas yang tinggi.

## 2.4 Metaheuristik untuk Optimasi Penjadwalan

Metaheuristik merupakan pendekatan algoritma yang dirancang untuk menyelesaikan masalah optimasi kompleks dengan cara yang efektif dan efisien. Berbeda dengan metode eksak yang menjamin solusi optimal tetapi memerlukan waktu komputasi yang sangat lama untuk masalah besar, metaheuristik memberikan solusi yang cukup baik (near-optimal) dalam waktu yang reasonable. Penelitian terdahulu telah menunjukkan keefektifan berbagai metode metaheuristik dalam menyelesaikan UCTP, termasuk Simulated Annealing (SA), Tabu Search, Genetic Algorithm (GA), Particle Swarm Optimization (PSO), Ant Colony Optimization (ACO), dan pendekatan hybrid (Bashab et al., 2023).

### 2.4.1 Simulated Annealing

Simulated Annealing (SA) adalah algoritma metaheuristik yang terinspirasi oleh proses annealing dalam metalurgi, di mana material dipanaskan hingga suhu tinggi dan kemudian didinginkan secara perlahan untuk mencapai struktur kristal yang optimal. Algoritma ini pertama kali diperkenalkan oleh Kirkpatrick et al. (1983) dan sejak saat itu telah banyak digunakan untuk menyelesaikan berbagai masalah optimasi kombinatorial termasuk UCTP.

#### 2.4.1.1 Prinsip Dasar dan Mekanisme Algoritma

Simulated Annealing bekerja dengan cara mensimulasikan proses fisika annealing. Pada suhu tinggi, atom-atom dalam material bergerak secara acak dengan energi tinggi, memungkinkan mereka untuk keluar dari posisi lokal yang tidak optimal. Ketika suhu diturunkan secara bertahap, atom-atom mulai menetap pada konfigurasi dengan energi yang lebih rendah. Pada akhir proses, material mencapai konfigurasi ground state dengan energi minimum (Kirkpatrick et al., 1983).

Dalam konteks optimasi, konsep ini diterjemahkan sebagai berikut: solusi awal dihasilkan secara acak atau menggunakan heuristik tertentu. Kemudian, pada setiap iterasi, solusi saat ini dimodifikasi untuk menghasilkan solusi tetangga (neighbor solution). Jika solusi tetangga lebih baik (nilai objective function lebih rendah), maka solusi tersebut diterima. Jika solusi tetangga lebih buruk, maka solusi tersebut masih mungkin diterima dengan probabilitas tertentu yang bergantung pada perbedaan kualitas solusi dan suhu saat ini (Metropolis et al., 1953).

Probabilitas penerimaan solusi worse mengikuti fungsi Boltzmann yang dapat dirumuskan sebagai berikut (Geman & Geman, 1984):

$$P(accept) = \exp\left(-\frac{\Delta E}{T}\right)$$

Di mana:
- $P(accept)$ adalah probabilitas menerima solusi worse
- $\Delta E$ adalah perubahan nilai objective function ($\Delta E = f_{new} - f_{old}$)
- $T$ adalah suhu saat ini
- $\exp$ adalah fungsi eksponensial

Fungsi ini menunjukkan bahwa pada suhu tinggi, probabilitas menerima solusi worse menjadi lebih tinggi, memungkinkan algoritma untuk mengeksplorasi ruang solusi yang lebih luas. Ketika suhu menurun, probabilitas ini menurun secara dramatis, membuat algoritma lebih selektif dan fokus pada eksploitasi solusi-solusi yang berkualitas (Hajek, 1988).

#### 2.4.1.2 Parameter Penting dalam Simulated Annealing

Beberapa parameter penting yang mempengaruhi performansi SA meliputi:

**Initial Temperature (T₀)**: Suhu awal menentukan tingkat eksplorasi pada awal algoritma. Suhu yang terlalu rendah dapat menyebabkan algoritma terjebak dalam local optimum terlalu cepat, sementara suhu yang terlalu tinggi akan memperlambat konvergensi karena terlalu banyak iterasi yang dihabiskan pada pencarian yang tidak produktif. Penentuan suhu awal dapat dilakukan melalui beberapa metode, salah satunya adalah dengan menghitung perubahan rata-rata objective function dari solusi-solusi acak (Wiktasari & Suseno, 2016):

$$T_0 = \frac{\overline{\Delta E^+}}{\ln(2)}$$

Di mana $\overline{\Delta E^+}$ adalah rata-rata perubahan positif objective function dari sampel solusi acak.

**Cooling Rate (α)**: Faktor pendinginan menentukan seberapa cepat suhu menurun setiap iterasi. Scheduling pendinginan yang paling umum adalah geometric cooling (Kalivas, 1995):

$$T_{k+1} = \alpha \cdot T_k$$

Di mana $0.8 \leq \alpha \leq 0.99$ dan $k$ adalah iterasi saat ini. Nilai α yang lebih kecil akan menghasilkan pendinginan yang lebih cepat, sementara nilai yang lebih dekat dengan 1 akan menghasilkan pendinginan yang lebih gradual.

**Markov Chain Length**: Jumlah iterasi yang dilakukan pada setiap suhu sebelum suhu diturunkan. Panjang chain yang lebih besar memungkinkan eksplorasi yang lebih thorough pada setiap level suhu, tetapi juga meningkatkan waktu komputasi (van Laarhoven & Aarts, 1987).

**Final Temperature**: Suhu minimum yang menandakan akhir algoritma. Ketika suhu mencapai nilai ini, algoritma dihentikan meskipun solusi optimal belum tentu telah ditemukan.

#### 2.4.1.3 Neighbourhood Structure dan Move Generation

Pemilihan struktur neighborhood sangat mempengaruhi performansi SA. Neighborhood structure mendefinisikan bagaimana solusi baru dihasilkan dari solusi saat ini. Xu et al. (2025) menunjukkan bahwa pemilihan move scheme yang tepat sangat penting untuk efisiensi SA. Mereka menemukan bahwa memindahkan hanya satu koordinat pada setiap iterasi memberikan performansi paling efisien untuk masalah high-dimensional.

Untuk UCTP, beberapa move operators yang umum digunakan meliputi:

**Swap Operation**: Menukar dua elemen dalam jadwal, seperti menukar slot waktu dua mata kuliah atau menukar ruangan dua kelas.

**Single Move**: Memindahkan satu event ke slot waktu atau ruangan yang berbeda (Goh et al., 2017).

Pemilihan neighborhood structure yang tepat dapat mempengaruhi acceptance rate dan kecepatan konvergensi algoritma. Xu et al. (2025) menunjukkan bahwa partial-coordinate updates dapat mempertahankan acceptance rate yang lebih tinggi dibandingkan full-coordinate updates dalam setting high-dimensional.

#### 2.4.1.4 Acceptance Probability dan Metropolis Criterion

Metropolis criterion adalah aturan penerimaan yang paling umum digunakan dalam SA (Metropolis et al., 1953). Aturan ini dapat dirumuskan sebagai:

Jika $\Delta E \leq 0$ (solusi baru lebih baik atau sama), terima solusi baru.

Jika $\Delta E > 0$ (solusi baru lebih buruk), terima dengan probabilitas $P = \exp(-\Delta E/T)$.

Implementasi algoritma SA dengan Metropolis criterion dapat dituliskan sebagai pseudo-code berikut (Wiktasari & Suseno, 2016):

```
1. Pilih solusi awal X₀ dan hitung f(X₀)
2. Tentukan suhu awal T₀
3. WHILE kriteria penghentian belum terpenuhi:
    a. Pilih solusi tetangga X' dari neighborhood(X)
    b. Hitung ΔE = f(X') - f(X)
    c. IF ΔE ≤ 0 THEN
        X ← X'
       ELSE
        IF exp(-ΔE/T) > random(0,1) THEN
            X ← X'
        END IF
    d. T ← α × T (update suhu)
4. RETURN solusi terbaik yang ditemukan
```

#### 2.4.1.5 Reheating dan Variasi SA

Reheating adalah teknik yang digunakan dalam SA untuk meningkatkan suhu secara sementara ketika algoritma menunjukkan tanda-tanda stagnasi. Hal ini memungkinkan algoritma untuk keluar dari local optimum yang mungkin telah terjebak (Goh et al., 2017).

Simulated Annealing with Improved Reheating and Learning (SAIRL) yang dikembangkan oleh Goh et al. (2017) menggunakan reheating berdasarkan kondisi stuck, yaitu ketika perbaikan solusi tidak terjadi setelah sejumlah iterasi tertentu. Suhu reheating dapat dihitung sebagai:

$$T_{reheat} = [heat \times 0.2 \times f(current) + f(current)] \times \overline{\Delta f} \times D$$

Di mana $heat$ adalah langkah inkremental, $f(current)$ adalah nilai objective function saat ini, $\overline{\Delta f}$ adalah rata-rata perubahan biaya (cost changes) dari move uphill dan downhill, dan $D$ adalah koefisien.

Teknik lain yang meningkatkan performansi SA adalah penggunaan adaptive cooling schedule yang dapat menyesuaikan tingkat pendinginan berdasarkan kondisi saat ini.

#### 2.4.1.6 Keunggulan dan Kelemahan Simulated Annealing

Keunggulan utama SA meliputi:
- Kemampuan untuk menghindari local optimum melalui penerimaan probabilistik solusi worse
- Implementasi yang relatif sederhana
- Fleksibilitas untuk berbagai jenis masalah optimasi
- Tidak memerlukan gradient dari fungsi objective
- Dapat menghasilkan solusi berkualitas baik dalam waktu yang reasonable

Kelemahan SA meliputi:
- memerlukan tuning parameter yang tepat untuk performansi optimal
- Waktu komputasi dapat menjadi panjang untuk masalah yang sangat kompleks
- Tidak menjamin menemukan solusi optimal global
- Performansi sangat bergantung pada cooling schedule yang dipilih (Xu et al., 2025)

### 2.4.2 Tabu Search

Tabu Search adalah algoritma metaheuristik yang dikembangkan oleh Fred Glover pada tahun 1986. Berbeda dengan Simulated Annealing yang menggunakan probabilitas untuk menghindari local optimum, Tabu Search menggunakan struktur memori untuk mengarahkan pencarian solusi-solusi yang belum dieksplorasi. Tabu Search secara sistematis mengeksplorasi ruang solusi dengan mempertimbangkan solusi-solusi tetangga dan menggunakan memori untuk menghindari kunjungan berulang ke solusi yang sama (Glover et al., 2007).

#### 2.4.2.1 Komponen Utama Tabu Search

**Tabu List**: Struktur data yang menyimpan informasi tentang solusi atau move yang telah dikunjungi recently dan tidak boleh dikunjungi kembali dalam beberapa iterasi berikutnya. Tabu list mencegah algoritma dari cycling (kembali ke solusi yang sama dalam siklus pendek) dan mendorong eksplorasi area baru dari ruang solusi. Ukuran tabu list (tabu tenure) biasanya dipilih berdasarkan karakteristik masalah. Untuk UCTP, Goh et al. (2017) menggunakan tabu tenure:

$$tabu\_tenure = RANDOM[10) + |unplaced\_events|$$

Di mana $|unplaced\_events|$ adalah jumlah event yang belum ditempatkan.

**Aspiration Criteria**: Mekanisme yang memungkinkan mengunjungi kembali solusi yang berada dalam tabu list jika solusi tersebut cukup menjanjikan, yaitu kualitasnya lebih baik dari solusi terbaik yang pernah ditemukan. Aspiration criteria membantu algoritma untuk tidak melewatkan solusi yang sangat baik hanya karena tabu status.

**Intensification dan Diversification**: Tabu Search menggunakan dua strategi pencarian. Intensification mendorong pencarian lebih intensif di area solusi yang menjanjikan, sementara diversification mendorong eksplorasi area baru dari ruang solusi yang belum dieksplorasi (Glover et al., 2007).

#### 2.4.2.2 Algoritma Tabu Search

Pseudo-code dasar Tabu Search dapat dituliskan sebagai berikut:

```
1. Pilih solusi awal X dan hitung f(X)
2. Inisialisasi tabu list kosong
3. WHILE kriteria penghentian belum terpenuhi:
    a. Generate candidate solutions dari neighborhood(X)
    b. SELECT solusi terbaik dari candidates yang tidak tabu
       (atau memenuhi aspiration criteria)
    c. UPDATE tabu list (tambahkan move yang digunakan,
       hapus move yang expired)
    d. IF f(candidate) < f(best) THEN
        best ← candidate
       END IF
    X ← candidate
4. RETURN solusi terbaik (best)
```

#### 2.4.2.3 Keunggulan Tabu Search

Keunggulan Tabu Search terletak pada kemampuannya untuk melakukan eksploitasi yang intensif pada daerah solusi yang menjanjikan. Dengan menggunakan tabu list, algoritma dapat menghindari kunjungan ke solusi yang sama secara berulang dan lebih fokus pada eksplorasi daerah solusi yang belum dieksplorasi. Tabu Search juga memiliki mekanisme aspirasi yang memungkinkan mengunjungi kembali solusi yang berada dalam tabu list jika solusi tersebut cukup menjanjikan.

### 2.4.3 Pendekatan Hybrid Simulated Annealing dan Tabu Search

Pengembangan terkini dalam literatur menunjukkan bahwa pendekatan hibrida yang menggabungkan Simulated Annealing dan Tabu Search memberikan performansi yang sangat kompetitif dalam menyelesaikan UCTP. Penelitian Muklason et al. (2024) mengembangkan algoritma Tabu-Simulated Annealing Hyper-Heuristics yang menggabungkan kedua metode tersebut dengan konsep hyper-heuristics. Studi mereka menggunakan Socha Dataset sebagai benchmark dan hasilnya menunjukkan bahwa algoritma yang dikembangkan menduduki peringkat kedua dari sepuluh algoritma yang diuji, dengan solusi terbaik pada 6 dari 11 dataset yang diuji.

Keunggulan utama dari pendekatan hybrid SA-TS adalah keseimbangan antara exploitation dan exploration dalam proses pencarian solusi. Tabu Search memiliki kemampuan exploitation yang kuat melalui penggunaan tabu list untuk menghindari kunjungan ke solusi yang sama secara berulang. Sementara Simulated Annealing memiliki kemampuan exploration yang baik melalui penerimaan solusi worse secara probabilistik untuk menghindari local optima. Kombinasi kedua metode ini memungkinkan algoritma untuk secara efektif mencari solusi optimal dalam ruang solusi yang kompleks (Muklason et al., 2024).

Penelitian tersebut juga menggunakan Greedy Algorithm untuk menghasilkan solusi awal sebelum dilakukan optimasi dengan SA-TS hybrid. Penggunaan greedy initial solution memberikan titik awal yang berkualitas dan mempercepat konvergensi algoritma. Hasil eksperimen menunjukkan bahwa algoritma hibrida SA-TS mampu menghasilkan penalty score yang rendah, dengan rata-rata penalty 0 untuk small instances dan rata-rata penalty di bawah 200 untuk medium instances (Muklason et al., 2024).

### 2.4.4 Fungsi Fitness dan Perhitungan Constraint

Fungsi fitness merupakan komponen krusial dalam algoritma metaheuristik untuk optimasi UCTP. Fungsi fitness mengevaluasi kualitas solusi jadwal dengan mempertimbangkan pelanggaran terhadap hard constraints dan soft constraints. Penelitian Cruz-Rosales et al. (2022) mengembangkan model matematika komprehensif untuk fungsi fitness yang menggabungkan penalti untuk pelanggaran constraint dengan bobot yang sesuai. Formulasi matematika fungsi fitness dapat dituliskan sebagai berikut:

$$F(S) = \sum_{i=1}^{n} w_i \cdot HC_i(S) + \sum_{j=1}^{m} v_j \cdot SC_j(S)$$

Di mana:
- $F(S)$ adalah nilai fitness dari solusi jadwal $S$
- $HC_i(S)$ adalah pelanggaran hard constraint ke-$i$ dalam solusi $S$
- $SC_j(S)$ adalah pelanggaran soft constraint ke-$j$ dalam solusi $S$
- $w_i$ adalah bobot penalti untuk hard constraint ke-$i$ (diberikan nilai sangat tinggi)
- $v_j$ adalah bobot penalti untuk soft constraint ke-$j$
- $n$ adalah jumlah hard constraints
- $m$ adalah jumlah soft constraints

#### 2.4.4.1 Perhitungan Hard Constraints

Hard constraints adalah batasan yang harus dipenuhi 100% untuk menghasilkan jadwal yang valid. Pelanggaran terhadap hard constraints mengakibatkan jadwal tidak feasible dan harus dihindari sepenuhnya. Berdasarkan analisis terhadap literatur dan kebutuhan UISI, hard constraints yang dipertimbangkan meliputi (Cruz-Rosales et al., 2022):

**HC1 - Konflik Dosen**: Satu dosen tidak dapat mengajar di dua kelas berbeda pada slot waktu yang sama.

$$HC_1 = \sum_{t=1}^{T} \sum_{d=1}^{D} \max(0, \sum_{c=1}^{C} x_{c,d,t} - 1)$$

Di mana $x_{c,d,t} = 1$ jika mata kuliah $c$ dengan dosen $d$ dijadwalkan pada slot waktu $t$, dan $T$ adalah total slot waktu, $D$ adalah jumlah dosen, $C$ adalah jumlah mata kuliah.

**HC2 - Kapasitas Ruangan**: Jumlah mahasiswa dalam kelas tidak boleh melebihi kapasitas ruangan yang tersedia.

$$HC_2 = \sum_{r=1}^{R} \sum_{c=1}^{C} \max(0, n_mhs_c - capacity_r) \cdot y_{c,r}$$

Di mana $y_{c,r} = 1$ jika mata kuliah $c$ dijadwalkan di ruangan $r$, $n_mhs_c$ adalah jumlah mahasiswa untuk mata kuliah $c$, dan $capacity_r$ adalah kapasitas ruangan $r$.

**HC3 - Batas SKS Harian**: Total SKS yang diajar oleh seorang dosen dalam satu hari tidak boleh melebihi batas maksimal yang ditetapkan (maksimal 8 SKS per hari).

$$HC_3 = \sum_{d=1}^{D} \sum_{h=1}^{H} \max(0, \sum_{c=1}^{C} sks_c \cdot z_{c,d,h} - 8)$$

Di mana $z_{c,d,h} = 1$ jika mata kuliah $c$ dengan dosen $d$ dijadwalkan pada hari $h$.

**HC4 - Ketersediaan Ruangan Laboratorium**: Ruangan laboratorium bersifat eksklusif untuk program studi tertentu dan tidak dapat digunakan oleh program studi lain.

$$HC_4 = \sum_{r \in Lab} \sum_{c \notin prog(r)} w_{c,r}$$

Di mana $w_{c,r} = 1$ jika mata kuliah $c$ dari program studi yang tidak berhak menggunakan ruangan laboratorium $r$.

**HC5 - Konflik Waktu Eksklusif**: Tidak boleh ada jadwal pada periode waktu eksklusif yang telah ditetapkan institusi, seperti jam ibadah (sekitar Dzuhur, Maghrib, dan periode Jumat).

$$HC_5 = \sum_{c=1}^{C} \sum_{t \in Forbidden} u_{c,t}$$

Di mana $u_{c,t} = 1$ jika mata kuliah $c$ dijadwalkan pada slot waktu terlarang $t$.

#### 2.4.4.2 Perhitungan Soft Constraints

Soft constraints adalah batasan yang tidak wajib dipenuhi tetapi pelanggaran akan memberikan penalti yang mengurangi kualitas jadwal. Minimisasi pelanggaran soft constraints bertujuan meningkatkan kepuasan pengguna (dosen dan mahasiswa) dengan mempertimbangkan preferensi dan kenyamanan:

**SC1 - Preferensi Waktu Mengajar Dosen**: Dosen memiliki preferensi waktu mengajar tertentu (pagi, siang, atau sore) yang sebaiknya dipenuhi.

$$SC_1 = \sum_{d=1}^{D} \sum_{c=1}^{C} \sum_{t=1}^{T} (1 - pref_{d,t}) \cdot x_{c,d,t}$$

Di mana $pref_{d,t}$ adalah preferensi dosen $d$ terhadap slot waktu $t$ (nilai 0-1).

**SC2 - Waktu Pindah Antar Kelas**: Memberikan waktu yang memadai bagi mahasiswa untuk berpindah dari satu kelas ke kelas berikutnya (minimal 15 menit antar slot waktu).

$$SC_2 = \sum_{s=1}^{S} \sum_{c \in slot(s)} \sum_{c' \in slot(s+1)} dist(c,c')$$

Di mana $dist(c,c')$ adalah jarak waktu atau ruangan antara mata kuliah $c$ dan $c'$ yang dijadwalkan berurutan.

**SC3 - Keseimbangan Beban Harian**: Menghindari jadwal yang terlalu padat atau terlalu renggang untuk setiap kelas atau dosen.

$$SC_3 = \sum_{d=1}^{D} | \sum_{c} x_{c,d} - avg_load |$$

Di mana $avg_load$ adalah rata-rata beban mengajar dosen.

#### 2.4.4.3 Bobot Constraint dan Penalty Score

Penentuan bobot untuk setiap constraint sangat penting untuk menghasilkan jadwal yang berkualitas. Cruz-Rosales et al. (2022) merekomendasikan pendekatan multi-objective dengan bobot yang proporsional terhadap tingkat kepentingan constraint. Untuk implementasi dalam penelitian ini, penentuan bobot menggunakan pendekatan:

$$w_{HC} \gg v_{SC}$$

Di mana $w_{HC}$ adalah bobot hard constraints yang diberikan nilai sangat tinggi (misalnya 1000) untuk memastikan pelanggaran hard constraints dihindari sepenuhnya, sementara $v_{SC}$ adalah bobot soft constraints yang lebih rendah (misalnya 1-10) untuk memberikan fleksibilitas dalam optimasi.

### 2.4.5 Roulette Wheel Selection dalam Hyper-Heuristic

Roulette Wheel Selection, juga dikenal sebagai Fitness Proportionate Selection, adalah metode seleksi yang digunakan dalam algoritma evolusioner dan hyper-heuristic untuk memilih solusi atau operator berdasarkan probabilitas yang proporsional dengan nilai fitness-nya. Dalam konteks hyper-heuristic untuk UCTP, Roulette Wheel Selection digunakan untuk memilih operator neighborhood yang akan diterapkan pada solusi saat ini pada setiap iterasi (Muklason et al., 2024).

Prinsip dasar Roulette Wheel Selection adalah bahwa solusi atau operator dengan nilai fitness yang lebih tinggi memiliki probabilitas yang lebih besar untuk dipilih. Probabilitas pemilihan untuk operator $i$ dapat dihitung sebagai:

$$P(i) = \frac{fitness(i)}{\sum_{j=1}^{n} fitness(j)}$$

Di mana $fitness(i)$ adalah nilai fitness operator $i$ dan $n$ adalah jumlah total operator yang tersedia.

Dalam implementasi hyper-heuristic SA-TS, Roulette Wheel Selection digunakan untuk memilih antara berbagai move operators seperti swap, single move, dan Kempe chain move berdasarkan performansi historisnya. Operator yang secara konsisten menghasilkan peningkatan solusi akan memiliki probabilitas pemilihan yang lebih tinggi, sementara operator yang kurang efektif akan tetap memiliki kesempatan untuk dipilih untuk mempertahankan diversitas pencarian (Muklason et al., 2024).

Pseudo-code Roulette Wheel Selection dapat dituliskan sebagai berikut:

```
1. Hitung total fitness dari semua operator
2. Generate bilangan random r dalam interval [0, total_fitness)
3. Akumulasikan fitness operator hingga akumulasi ≥ r
4. Pilih operator pada titik akumulasi tersebut
5. RETURN operator yang dipilih
```

Keunggulan Roulette Wheel Selection dalam hyper-heuristic adalah kemampuannya untuk menyeimbangkan antara exploitation (memilih operator yang terbukti efektif) dan exploration (memberikan kesempatan kepada operator lain). Hal ini sangat relevan dalam konteks UCTP di mana karakteristik ruang solusi dapat berubah seiring proses optimasi berlangsung (Muklason et al., 2024).

#### 2.4.5.1 Modifikasi Hybrid Selection

Implementasi dalam penelitian ini mengadopsi modifikasi dari Roulette Wheel Selection murni yang disebut Hybrid Selection, yang terinspirasi oleh penelitian Cowling et al. (2002). Modifikasi ini bertujuan untuk meningkatkan robustnes algoritma dengan mempertahankan tingkat exploration yang memadai bahkan ketika beberapa operator mendominasi dalam hal success rate.

Hybrid Selection menggabungkan dua mekanisme:
- **70% Weighted Selection**: Pemilihan operator berdasarkan probabilitas proporsional dengan success rate (mirip Roulette Wheel murni)
- **30% Random Selection**: Pemilihan operator secara acak untuk mempertahankan diversitas pencarian

Formula untuk Hybrid Selection:

$$
P(i) = 
\begin{cases} 
0.7 \times \frac{success\_rate(i)}{\sum_{j=1}^{n} success\_rate(j)} + 0.3 \times \frac{1}{n} & \text{if selected} \\
0 & \text{otherwise}
\end{cases}
$$

Keunggulan modifikasi Hybrid Selection:
1. Mencegah konvergensi prematur ke lokal optimum
2. Memberikan kesempatan kepada operator yang kurang efektif untuk pulih ketika kondisi berubah
3. Lebih robust terhadap variasi dalam karakteristik masalah

Implementasi menyediakan dua mode seleksi yang dapat dikonfigurasi pengguna:
- `hybrid` (default): Modifikasi Hybrid Selection dengan 70% weighted + 30% random
- `roulette-wheel`: Roulette Wheel Selection murni sesuai formula teoritis

Pemilihan mode bergantung pada karakteristik masalah dan prioritas optimasi. Untuk masalah dengan lanskap solusi yang kompleks dan banyak lokal optimum, mode hybrid direkomendasikan. Untuk masalah yang well-understood dengan konvergensi cepat sebagai prioritas, mode roulette-wheel dapat digunakan.

## 2.5 Greedy Algorithm sebagai Initial Solution

Greedy Algorithm adalah pendekatan algoritma yang membuat pilihan optimal lokal pada setiap langkah dengan harapan dapat mencapai solusi optimal global. Dalam konteks UCTP, Greedy Algorithm dapat digunakan untuk menghasilkan solusi awal yang berkualitas tinggi sebelum dilakukan optimasi dengan algoritma metaheuristik seperti SA-TS hybrid. Penggunaan Greedy Algorithm sebagai initial solution memberikan beberapa keuntungan, yaitu memberikan titik awal yang berkualitas yang dapat mempercepat konvergensi algoritma dan mengurangi jumlah iterasi yang diperlukan untuk mencapai solusi yang baik (Coşar et al., 2022).

Penelitian Coşar et al. (2022) mengembangkan algoritma Greedy-CB-CTT yang menggunakan berbagai heuristik seperti Largest-First, Smallest-First, Best-Fit, Average-weight first, dan Highest Unavailable course-first untuk mengassign mata kuliah ke ruangan yang tersedia. Hasil eksperimen pada 21 problem instance dari benchmark set ITC-2007 menunjukkan bahwa algoritma greedy yang diusulkan dapat menghasilkan solusi feasible dengan zero hard constraint violations pada 18 problem instance.

Untuk implementasi dalam konteks UCTP, Greedy Algorithm dapat dirancang dengan langkah-langkah berikut:
1. Urutkan mata kuliah berdasarkan prioritas (misalnya: jumlah mahasiswa, jumlah SKS, atau kategori)
2. Untuk setiap mata kuliah dalam urutan tersebut:
   a. Cari slot waktu dan ruangan yang tersedia yang tidak melanggar hard constraints
   b. Pilih slot yang paling sesuai berdasarkan preferensi atau soft constraints
   c. Assign mata kuliah ke slot tersebut

Pendekatan greedy ini sangat cepat dalam menghasilkan solusi awal karena tidak memerlukan iterasi ekstensif seperti metaheuristik. Namun, solusi yang dihasilkan mungkin bukan solusi optimal karena keputusan lokal yang optimal tidak menjamin solusi global yang optimal.

## 2.6 REST API dan Pengembangan Web

REST (Representational State Transfer) API adalah arsitektur perangkat lunak yang memungkinkan komunikasi antara client dan server melalui protokol HTTP. REST API telah menjadi standar de facto untuk pengembangan layanan web karena kemudahan implementasinya, skalabilitas yang tinggi, dan fleksibilitas dalam berbagai platform. Dalam konteks DSS untuk penjadwalan, REST API memungkinkan akses modular terhadap algoritma optimasi yang dapat dipanggil oleh berbagai jenis client seperti web application, mobile application, atau sistem lain yang memerlukan kemampuan penjadwalan (Romaguera et al., 2023).

Penelitian Romaguera et al. (2023) menunjukkan bahwa implementasi web-based course timetabling system menggunakan arsitektur yang memungkinkan akses online dan kemampuan untuk menangani berbagai jenis dataset. Sistem yang dibangun harus memiliki antarmuka yang ramah pengguna yang memungkinkan administrator dan faculty members untuk dengan mudah menggunakan sistem tanpa pelatihan khusus (Latpate et al., 2024). Arsitektur REST API menjadi pilihan yang populer karena memungkinkan integrasi yang modular dan skalabilitas yang tinggi.

Dalam arsitektur yang diusulkan, backend sistem dibangun dengan arsitektur REST API yang menyediakan endpoint untuk berbagai operasi seperti input data, proses optimasi penjadwalan, dan output hasil jadwal. Frontend dikembangkan menggunakan React.js yang menyediakan antarmuka web yang responsif dan interaktif untuk pengguna. Arsitektur ini memungkinkan integrasi yang modular antara komponen-komponen sistem dan memfasilitasi pengembangan yang paralel antara frontend dan backend.

## 2.7 Daftar Pustaka

Lihat Daftar Pustaka di file terpisah: daftar_pustaka.md
