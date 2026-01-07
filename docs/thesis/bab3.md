# BAB 3
# METODOLOGI PENELITIAN

## 3.1 Metode Penelitian

Penelitian ini menggunakan pendekatan Research and Development (R&D) untuk mengembangkan Sistem Pendukung Keputusan (DSS) berbasis web untuk penjadwalan perkuliahan. Pendekatan R&D dipilih karena penelitian ini bertujuan untuk menghasilkan produk berupa sistem informasi yang dapat digunakan secara praktis. Menurut Sugiyono (2018), metode R&D adalah metode penelitian yang digunakan untuk menghasilkan produk tertentu dan menguji keefektifan produk tersebut. Dalam konteks penelitian ini, produk yang dihasilkan adalah DSS dengan algoritma optimasi SA-TS hybrid.

Paradigma penelitian yang digunakan adalah paradigma kuantitatif dengan fokus pada pengukuran performansi algoritma optimasi melalui metrik-metrik yang terukur. Pengukuran dilakukan terhadap kualitas solusi jadwal yang dihasilkan, waktu komputasi yang diperlukan, dan tingkat pelanggaran constraints. Teknik pengumpulan data meliputi studi literatur, dokumentasi sistem existing, dan pengujian sistem melalui eksperimen. Data yang digunakan adalah data institusional UISI meliputi data dosen, mata kuliah, ruangan, dan constraint requirements.

## 3.2 Alur Penelitian

Alur penelitian dalam penelitian ini dapat dibagi menjadi beberapa tahap utama yang saling berkaitan dan membentuk siklus pengembangan sistem. Tahap pertama adalah studi literatur dan analisis kebutuhan, di mana peneliti melakukan kajian mendalam terhadap literatur terkait UCTP, metaheuristik, dan pengembangan DSS. Tahap kedua adalah perancangan sistem yang mencakup perancangan arsitektur, basis data, dan algoritma. Tahap ketiga adalah implementasi sistem dengan mengembangkan kode program sesuai dengan rancangan yang telah dibuat. Tahap keempat adalah pengujian dan evaluasi untuk memverifikasi bahwa sistem berfungsi sesuai dengan spesifikasi dan mengukur kualitas solusi yang dihasilkan. Tahap kelima adalah dokumentasi dan publikasi hasil penelitian.

Tahap studi literatur dilakukan dengan mengkaji paper-paper penelitian terdahulu yang relevan, buku-buku teks tentang optimasi dan metaheuristik, serta dokumentasi teknis terkait teknologi yang digunakan. Kajian literatur memberikan fondasi teoretis yang kuat untuk pengembangan algoritma dan sistem. Analisis kebutuhan dilakukan dengan mempelajari proses penyusunan jadwal yang berjalan saat ini di UISI, mengidentifikasi constraint yang berlaku, dan mengumpulkan data yang diperlukan untuk pengujian sistem.

Tahap perancangan sistem dimulai dengan perancangan arsitektur keseluruhan sistem yang mencakup komponen-komponen utama dan interaksinya. Kemudian dilakukan perancangan basis data untuk menyimpan data akademis seperti data dosen, mata kuliah, ruangan, dan jadwal. Perancangan algoritma mencakup definisi struktur data untuk representasi solusi, implementasi fungsi fitness, dan pseudocode algoritma SA-TS hybrid. Hasil perancangan didokumentasikan dalam bentuk diagram UML dan spesifikasi teknis.

Tahap implementasi dilakukan dengan menulis kode program berdasarkan rancangan yang telah dibuat. Implementasi dilakukan secara iteratif dengan membangun komponen-komponen sistem satu per satu dan melakukan integrasi secara bertahap. Setiap komponen diuji secara individual sebelum diintegrasikan dengan komponen lainnya. Pengujian dilakukan secara terus-menerus selama proses implementasi untuk memastikan kualitas kode dan mencegah akumulasi bug.

## 3.3 Perancangan Sistem

### 3.3.1 Arsitektur Sistem

Sistem Pendukung Keputusan yang dikembangkan memiliki arsitektur berbasis web dengan pola client-server menggunakan REST API. Arsitektur ini dipilih karena memungkinkan akses modular terhadap algoritma optimasi, memisahkan logika bisnis dari presentasi, dan memfasilitasi integrasi dengan sistem lain di masa depan. Arsitektur sistem terdiri dari tiga lapisan utama yaitu lapisan presentasi (presentation layer), lapisan bisnis (business logic layer), dan lapisan data (data layer).

Lapisan presentasi diimplementasikan menggunakan React.js yang menyediakan antarmuka web yang responsif dan interaktif. Komponen-komponen React.js menangani interaksi pengguna, validasi input di sisi klien, dan rendering tampilan hasil optimasi. State management menggunakan React Hooks dan Context API untuk mengelola data yang bersirkulasi antar komponen. Styling menggunakan CSS Modules atau styled-components untuk memastikan konsistensi tampilan.

Lapisan bisnis diimplementasikan dalam backend menggunakan Node.js dengan Express.js sebagai framework web server. Lapisan ini menangani logika aplikasi, pemrosesan data, dan eksekusi algoritma optimasi. REST API endpoints didefinisikan untuk operasi-operasi seperti upload data, inisiasi proses optimasi, monitoring progress, dan download hasil jadwal. Algoritma SA-TS hybrid diimplementasikan sebagai modul terpisah yang dapat dipanggil oleh controller.

Lapisan data menggunakan database relasional PostgreSQL untuk menyimpan data struktural seperti data dosen, mata kuliah, ruangan, dan program studi. PostgreSQL dipilih karena mendukung fitur-fitur lanjutan seperti constraint validation, indexing untuk optimasi query, dan kemampuan untuk menangani data dalam jumlah besar. Untuk data yang bersifat semi-struktural seperti konfigurasi parameter algoritma dan hasil eksperimen, dapat digunakan MongoDB atau disimpan dalam format JSON.

Komunikasi antar lapisan menggunakan protokol HTTP dengan format data JSON. REST API mengadopsi prinsip-prinsip desain yang baik seperti penggunaan HTTP methods yang sesuai (GET untuk read, POST untuk create, PUT untuk update, DELETE untuk delete), URL yang deskriptif, dan response format yang konsisten. Autentikasi dan otorisasi diimplementasikan menggunakan JWT (JSON Web Token) untuk mengamankan akses ke endpoint-endpoint yang memerlukan hak akses khusus.

### 3.3.2 Diagram Konteks Sistem

Diagram konteks sistem DSS penjadwalan perkuliahan menunjukkan interaksi antara sistem dengan entitas-entitas eksternal. Entitas eksternal utama adalah Administrator Akademik yang bertanggung jawab memasukkan data, menjalankan proses optimasi, dan mengelola hasil jadwal. Sistem akademik internal (SIAKAD) dan sistem manajemen ruang (Ruang UISI) merupakan sistem eksternal yang dapat bertukar data dengan DSS. File data dalam format Excel atau CSV dapat diimpor ke sistem untuk input data. Hasil jadwal dapat diekspor dalam format yang kompatibel dengan sistem-sistem eksternal.

Proses bisnis utama yang mengalir melalui sistem dimulai dari输入 data berupa data master (dosen, mata kuliah, ruangan) dan data operasional (preferensi dosen, batasan jadwal). Data tersebut divalidasi untuk memastikan kelengkapan dan konsistensi. Setelah data siap, proses optimasi dijalankan menggunakan algoritma SA-TS hybrid. Progress optimasi dapat dimonitor secara real-time melalui antarmuka web. Hasil optimasi berupa jadwal perkuliahan dapat dilihat, diedit jika diperlukan, dan diekspor ke format yang diinginkan.

## 3.4 Implementasi Algoritma SA-TS Hybrid

### 3.4.1 Struktur Data Solusi

Representasi solusi dalam algoritma optimasi sangat mempengaruhi efisiensi dan efektivitas pencarian solusi. Penelitian ini menggunakan representasi berbasis matrix assignment di mana setiap slot waktu (hari × jam) memiliki entri yang menunjukkan mata kuliah yang dijadwalkan pada slot tersebut. Representasi ini dipilih karena intuitif dan memudahkan perhitungan pelanggaran constraint.

Struktur data utama untuk merepresentasikan jadwal adalah array dua dimensi dengan dimensi pertama adalah slot waktu dan dimensi kedua adalah ruangan. Setiap sel dalam array berisi identifier mata kuliah yang dijadwalkan pada kombinasi slot waktu dan ruangan tersebut. Data pendukung seperti informasi dosen, kapasitas ruangan, dan preferensi disimpan dalam lookup tables terpisah untuk memudahkan akses selama perhitungan fitness.

Konstruksi solusi awal menggunakan Greedy Algorithm dengan heuristik Largest-First yang mengurutkan mata kuliah berdasarkan jumlah mahasiswa secara descending. Untuk setiap mata kuliah dalam urutan tersebut, algoritma mencari slot waktu dan ruangan yang tersedia dan tidak melanggar hard constraints. Jika ditemukan multiple pilihan, dipilih yang paling sesuai dengan preferensi (soft constraints). Proses ini berlanjut hingga semua mata kuliah ditempatkan atau tidak ada slot yang tersedia.

### 3.4.2 Fungsi Fitness

Fungsi fitness mengevaluasi kualitas solusi dengan menghitung total penalti dari pelanggaran constraints. Implementasi fungsi fitness mengikuti formulasi matematika yang telah diuraikan pada Bab 2 dengan beberapa optimasi untuk meningkatkan efisiensi komputasi. Perhitungan dilakukan secara incremental untuk mengurangi overhead komputasi pada setiap evaluasi neighbor solution.

Fungsi fitness menerima parameter berupa solusi jadwal dan mengembalikan nilai numerik yang merepresentasikan total penalti. Nilai yang lebih rendah menunjukkan solusi yang lebih baik. Hard constraints diberikan penalti yang sangat tinggi (1000 per pelanggaran) untuk memastikan prioritas utama adalah feasibility. Soft constraints diberikan penalti yang lebih rendah (1-10 per pelanggaran) untuk memberikan fleksibilitas optimasi.

Implementasi perhitungan hard constraints menggunakan early termination strategy. Jika pada tahap perhitungan ditemukan pelanggaran hard constraint, fungsi langsung mengembalikan nilai fitness yang sangat tinggi tanpa melanjutkan perhitungan untuk constraint lainnya. Strategi ini mengoptimalkan runtime dengan menghindari perhitungan yang tidak diperlukan untuk solusi yang jelas infeasible.

### 3.4.3 Algoritma Simulated Annealing

Implementasi algoritma Simulated Annealing mengikuti pseudo-code standar dengan beberapa modifikasi yang disesuaikan untuk konteks UCTP. Parameter-parameter utama yang dikonfigurasi meliputi initial temperature, cooling rate, Markov chain length, dan final temperature. Penentuan initial temperature menggunakan metode adaptive berdasarkan variasi objective function dari solusi-solusi acak.

Pseudo-code algoritma SA yang diimplementasikan:

```
1. T₀ ← hitung_initial_temperature()
2. X ← Greedy_Algorithm_Initial_Solution()
3. f_best ← f(X)
4. X_best ← X
5. T ← T₀
6. WHILE T > T_final:
7.     FOR i = 1 TO Markov_Length:
8.         X' ← generate_neighbor(X)
9.         ΔE ← f(X') - f(X)
10.        IF ΔE ≤ 0 THEN
11.            X ← X'
12.            IF f(X) < f_best THEN
13.                X_best ← X
14.                f_best ← f(X)
15.            END IF
16.        ELSE
17.            IF exp(-ΔE/T) > random(0,1) THEN
18.                X ← X'
19.            END IF
20.        END IF
21.    END FOR
22.    T ← α × T (α = 0.95)
23. END WHILE
24. RETURN X_best
```

Neighbor generation menggunakan kombinasi dari beberapa move operators meliputi single move (memindahkan satu mata kuliah ke slot waktu/ruangan berbeda), swap (menukar dua mata kuliah), dan Kempe chain move (memindahkan chain event yang terhubung). Pemilihan move operator dilakukan secara adaptif berdasarkan Roulette Wheel Selection dengan probabilitas proporsional terhadap historical success rate masing-masing operator.

### 3.4.4 Algoritma Tabu Search

Implementasi algoritma Tabu Search menggunakan tabu list untuk menghindari cycling dan mendorong eksplorasi area solusi yang belum tereksplorasi. Tabu list menyimpan informasi tentang move yang telah dilakukan recently dan tidak boleh diulang dalam jangka waktu tertentu (tabu tenure). Ukuran tabu tenure dikonfigurasi berdasarkan kompleksitas dataset.

Pseudo-code algoritma Tabu Search yang diimplementasikan:

```
1. X ← Greedy_Algorithm_Initial_Solution()
2. f_best ← f(X)
3. X_best ← X
4. tabu_list ← empty
5. tenure_base ← |unplaced_events|
6. counter ← 0
7. WHILE counter < max_iterations:
8.     candidates ← generate_candidates(X)
9.     best_candidate ← NULL
10.    best_fitness ← ∞
11.    FOR each c in candidates:
12.        IF c not in tabu_list OR aspiration(c):
13.            IF f(c) < best_fitness THEN
14.                best_candidate ← c
15.                best_fitness ← f(c)
16.            END IF
17.        END IF
18.    END FOR
19.    X ← apply_move(X, best_candidate)
20.    tenure ← random(10) + tenure_base
21.    add_to_tabu_list(best_candidate, tenure)
22.    IF f(X) < f_best THEN
23.        X_best ← X
24.        f_best ← f(X)
25.        counter ← 0
26.    ELSE
27.        counter ← counter + 1
28.    END IF
29. END WHILE
30. RETURN X_best
```

Aspiration criteria yang diimplementasikan adalah if a move in tabu list produces a solution better than the current best, it is allowed to be used. Mekanisme ini memungkinkan algoritma untuk tidak melewatkan solusi yang sangat baik hanya karena status tabu.

### 3.4.5 Hybrid SA-TS

Pendekatan hybrid yang diimplementasikan menggunakan strategi cascade di mana output dari satu algoritma menjadi input untuk algoritma lainnya. Tahap pertama menggunakan Greedy Algorithm untuk menghasilkan solusi awal. Tahap kedua menggunakan Simulated Annealing untuk mengoptimalkan solusi dengan fokus pada exploration. Tahap ketiga menggunakan Tabu Search untuk intensifikasi dan exploitation.

Strategi hybrid yang dipilih adalah Sequential Hybrid dengan Tabu Search sebagai post-optimization step setelah SA. Hal ini didasarkan pada temuan Muklason et al. (2024) bahwa pendekatan sequential hybrid memberikan hasil yang lebih baik dibandingkan intrascheme hybrid atau parallel hybrid untuk masalah UCTP. SA efektif dalam menemukan promising regions dalam ruang solusi, kemudian TS melakukan intensif search di regions tersebut untuk menemukan local optimum.

## 3.5 Pengujian dan Evaluasi

### 3.5.1 Skenario Pengujian

Pengujian sistem dilakukan melalui beberapa skenario untuk memastikan bahwa sistem berfungsi sesuai dengan spesifikasi dan menghasilkan solusi berkualitas. Skenario pertama adalah pengujian unit untuk memverifikasi bahwa setiap komponen berfungsi dengan benar secara individual. Pengujian dilakukan menggunakan framework testing yang sesuai dengan bahasa pemrograman yang digunakan (Jest untuk JavaScript/Node.js, Pytest untuk Python).

Skenario kedua adalah pengujian integrasi untuk memverifikasi bahwa komponen-komponen sistem berinteraksi dengan benar satu sama lain. Pengujian ini mencakup integrasi antara frontend dan backend melalui REST API, integrasi antara algoritma optimasi dan database, serta integrasi antara modul-modul dalam algoritma SA-TS hybrid. Skenario ketiga adalah pengujian sistem secara keseluruhan untuk memverifikasi bahwa sistem dapat menjalankan seluruh alur proses dari input data hingga output jadwal.

Skenario keempat adalah pengujian performansi algoritma menggunakan dataset benchmark. Untuk validasi hasil, digunakan dataset dari Socha ITC-2007 yang merupakan standar de facto untuk evaluasi algoritma UCTP. Hasil yang diperoleh dibandingkan dengan hasil dari penelitian lain untuk memverifikasi efektivitas algoritma yang diimplementasikan.

### 3.5.2 Metrik Evaluasi

Evaluasi kualitas solusi jadwal yang dihasilkan menggunakan beberapa metrik utama. Metrik pertama adalah feasibility rate yang mengukur persentase solusi yang memenuhi semua hard constraints. Solusi dengan feasibility rate 100% adalah solusi yang valid dan dapat digunakan. Metrik kedua adalah total penalty score yang mengukur pelanggaran soft constraints. Nilai penalty yang lebih rendah menunjukkan solusi yang lebih baik dari perspektif kualitas.

Metrik ketiga adalah waktu komputasi yang mengukur lama proses optimasi diperlukan untuk mencapai solusi. Metrik ini penting untuk menilai efisiensi algoritma terutama untuk dataset berskala besar. Metrik keempat adalah consistency yang mengukur variasi kualitas solusi dari beberapa kali running algoritma dengan parameter yang sama. Consistency yang tinggi menunjukkan algoritma yang stabil dan reliable.

Metrik kelima adalah RPD (Relative Percentage Deviation) yang membasikan solusi yang diperoleh dengan solusi terbaik yang diketahui dari literatur. RPD dihitung dengan formula:

$$RPD = \frac{f_{obtained} - f_{best\_known}}{f_{best\_known}} \times 100\%$$

Nilai RPD yang mendekati 0 menunjukkan performansi algoritma yang kompetitif dibandingkan dengan metode-metode yang telah dipublikasikan.

## 3.6 Teknologi dan Tools

Implementasi sistem menggunakan teknologi-teknologi modern yang dipilih berdasarkan kebutuhan fungsional dan non-fungsional sistem. Pemilihan teknologi mempertimbangkan faktor-faktor seperti maturitas teknologi, ketersediaan dokumentasi, dukungan komunitas, dan kesesuaian dengan kebutuhan proyek.

Frontend dikembangkan menggunakan React.js sebagai library JavaScript untuk membangun user interface. React.js dipilih karena memiliki arsitektur berbasis komponen yang mendukung reusability, virtual DOM untuk performa rendering yang optimal, dan ekosistem yang kaya dengan berbagai libraries dan tools pendukung. State management menggunakan Redux Toolkit atau React Context API tergantung pada kompleksitas state yang dikelola. Styling menggunakan Tailwind CSS atau styled-components untuk pengembangan yang efisien.

Backend dikembangkan menggunakan Node.js dengan Express.js framework. Node.js dipilih karena memiliki event-driven architecture yang cocok untuk aplikasi real-time dan I/O intensive seperti optimasi penjadwalan. Express.js menyediakan routing yang intuitif dan middleware yang fleksibel untuk penanganan request-response cycle. Database menggunakan PostgreSQL untuk data relasional dan MongoDB opsional untuk data semi-struktural.

Algoritma SA-TS hybrid diimplementasikan dalam JavaScript/TypeScript untuk memudahkan integrasi dengan backend Node.js. Untuk komputasi yang intensif, dapat digunakan Web Workers atau child processes untuk menghindari blocking event loop. Library tambahan yang digunakan meliputi mathematical.js untuk operasi matrix dan numerical computation, papaparse untuk parsing file CSV/Excel, dan fs untuk operasi file system.

Version control menggunakan Git dengan GitHub sebagai remote repository. Continuous Integration/Continuous Deployment (CI/CD) menggunakan GitHub Actions untuk otomatisasi testing dan deployment. Dokumentasi menggunakan Markdown dan API documentation tools seperti Swagger/OpenAPI untuk endpoint-endpoint REST API.

## 3.7 Tahapan Implementasi

Implementasi sistem dilakukan secara bertahap dengan metodologi Agile yang memungkinkan iterasi dan penyesuaian berdasarkan feedback. Setiap sprint berfokus pada pembangunan fitur-fitur tertentu dengan Definition of Done yang jelas. Sprint planning dilakukan di awal setiap iterasi untuk menentukan scope dan deliverables.

Sprint pertama berfokus pada setup project infrastructure meliputi inisialisasi repository, konfigurasi development environment, setup database schema, dan implementasi basic routing di backend dan frontend. Deliverable sprint pertama adalah project skeleton yang dapat dijalankan dan diakses melalui browser.

Sprint kedua berfokus pada pengembangan data management module meliputi CRUD operations untuk data master (dosen, mata kuliah, ruangan), import functionality untuk bulk data upload, dan export functionality untuk hasil jadwal. Deliverable sprint kedua adalah modul pengelolaan data yang fully functional.

Sprint ketiga berfokus pada pengembangan core algorithm meliputi implementasi Greedy Algorithm untuk initial solution, implementasi Simulated Annealing, implementasi Tabu Search, dan integrasi kedua algoritma dalam hybrid approach. Deliverable sprint ketiga adalah algoritma optimasi yang dapat menerima input dan menghasilkan output jadwal.

Sprint keempat berfokus pada pengembangan frontend dan integration meliputi implementasi user interface untuk input data, monitoring progress, dan display hasil, integrasi frontend dengan REST API, dan implementasi feedback mechanisms. Deliverable sprint keempat adalah sistem yang dapat digunakan end-to-end.

Sprint kelima berfokus pada testing dan optimization meliputi comprehensive testing (unit, integration, system), performance optimization, bug fixing, dan user acceptance testing. Deliverable sprint kelima adalah sistem production-ready yang telah diuji dan dioptimasi.

## 3.8 Kerangka Pengerjaan

Kerangka pengerjaan penelitian dijadwalkan dalam rentang waktu tertentu dengan milestone yang jelas untuk setiap tahap. Tahap persiapan meliputi review literatur dan analisis kebutuhan yang memerlukan waktu untuk memahami konteks penelitian secara mendalam. Tahap perancangan meliputi desain arsitektur, database, dan algoritma yang memerlukan waktu untuk menghasilkan spesifikasi teknis yang komprehensif.

Tahap implementasi memerlukan waktu yang paling lama karena mencakup pengembangan fitur-fitur sistem dan algoritma. Pendekatan iterative memungkinkan delivery value yang berkelanjutan dan penyesuaian berdasarkan feedback. Tahap pengujian memerlukan waktu yang memadai untuk memastikan kualitas sistem dan validasi hasil. Tahap dokumentasi dilakukan secara parallel dengan tahap-tahap lainnya dan disempurnakan di akhir.
