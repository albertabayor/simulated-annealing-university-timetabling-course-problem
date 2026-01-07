# Bab 1
# Pendahuluan

## 1.1 Latar Belakang

Penyusunan jadwal perkuliahan merupakan salah satu aktivitas operasional yang sangat kritis dan fundamental dalam pengelolaan perguruan tinggi modern. Secara formal, permasalahan ini dikenal sebagai University Course Timetabling Problem (UCTP), yang secara matematis dikategorikan sebagai masalah optimasi Non-Polynomial Hard (NP-Hard) dan Combinatorial Optimization Problem (COP) (Bashab et al., 2023). Sebagai masalah NP-COP, UCTP memiliki karakteristik khusus yang membedakannya dari masalah optimisasi konvensional. Tidak ada metode yang dapat menyelesaikannya dalam waktu polinomial yang masuk akal, membuat pendekatan brute-force tidak feasible untuk kasus nyata. Waktu komputasi yang diperlukan untuk mencapai solusi feasible meningkat secara eksponensial seiring bertambahnya ukuran masalah (jumlah dosen, kelas, ruang, dan constraint). Solusi optimal hanya dapat dicapai untuk kasus-kasus berukuran kecil, sementara mayoritas kasus nyata memerlukan algoritma aproksimasi yang tidak menjamin optimalitas tetapi mampu menghasilkan solusi yang cukup baik. UCTP memerlukan pendekatan komputasional khusus dalam metaheuristik untuk menghasilkan jadwal yang optimal atau near-optimal, dengan tetap memenuhi sejumlah hard constraints (batasan ketat yang tidak dapat dilanggar) dan soft constraints (batasan lunak yang harus diminimalkan pelanggarannya dengan penalti) yang telah ditetapkan oleh institusi (Bashab et al., 2023).

Penelitian terdahulu telah menunjukkan keefektifan berbagai metode optimasi dalam menyelesaikan UCTP. Menurut systematic review komprehensif oleh Bashab et al. (2023), berbagai teknik metaheuristik seperti Simulated Annealing (SA), Genetic Algorithm (GA), Particle Swarm Optimization (PSO), Ant Colony Optimization (ACO), dan pendekatan hybrid telah terbukti mampu menghasilkan solusi berkualitas tinggi. Analisis statistik dari publikasi menunjukkan bahwa hybrid algorithm mendominasi publikasi terbaru dengan 35% dari total publikasi, menunjukkan tren menuju kombinasi multiple algorithms. Di antara metode-metode tersebut, Simulated Annealing menunjukkan keunggulan kompetitif yang signifikan dalam hal kecepatan komputasi dan kemampuan adaptasi terhadap constraint lokal spesifik institusi. SA bekerja lebih cepat dibandingkan algoritma berbasis populasi (population-based), yang menjadikannya cocok untuk instansi masalah berukuran besar dalam waktu terbatas. Dibandingkan dengan GA dan PSO yang memerlukan jutaan evaluasi fitness, SA hanya memerlukan iterasi yang jauh lebih sedikit untuk konvergen ke solusi yang acceptable (Wiktasari & Suseno, 2016). SA memiliki mekanisme penerimaan solusi yang lebih buruk dengan probabilitas tertentu, yang secara signifikan mengurangi risiko terjebak dalam local optima yang merupakan masalah umum dalam single-solution based approaches. Penelitian empiris oleh Wiktasari dan Suseno (2016) mendemonstrasikan bahwa Simulated Annealing mampu mengoptimalkan penjadwalan menggunakan lima variabel utama: dosen, mata kuliah, slot waktu, hari, dan ruang kelas. Penelitian lebih terkini oleh Sukhoco et al. (2024) memperkuat temuan ini dengan membuktikan bahwa SA sangat sesuai diterapkan pada studi kasus penjadwalan akademik di lingkungan kampus dengan kompleksitas data yang tinggi.

Pengembangan terkini dalam literatur menunjukkan bahwa pendekatan hibrida yang menggabungkan Simulated Annealing dan Tabu Search memberikan performansi yang sangat kompetitif dalam penyelesaian UCTP. Penelitian Muklason et al. (2024) mengembangkan algoritma Tabu-Simulated Annealing Hyper-Heuristics yang menggabungkan kedua metode tersebut dengan konsep hyper-heuristics. Studi mereka menggunakan Socha Dataset sebagai benchmark dan hasilnya menunjukkan bahwa algoritma yang dikembangkan menduduki peringkat kedua dari sepuluh algoritma yang diuji, dengan solusi terbaik pada 6 dari 11 dataset yang diuji. Keunggulan utama dari pendekatan hybrid SA-TS adalah keseimbangan exploitation dan exploration dalam proses pencarian solusi. Tabu Search memiliki kemampuan exploitation yang kuat melalui penggunaan tabu list untuk menghindari kunjungan ke solusi yang sama secara berulang, sementara Simulated Annealing memiliki kemampuan exploration yang baik melalui penerimaan solusi worse secara probabilistik untuk menghindari local optima. Penelitian tersebut juga menggunakan Greedy Algorithm untuk menghasilkan solusi awal sebelum dilakukan optimasi dengan SA-TS hybrid. Penggunaan greedy initial solution memberikan titik awal yang berkualitas dan mempercepat konvergensi algoritma. Hasil eksperimen menunjukkan bahwa algoritma hibrida SA-TS mampu menghasilkan penalty score yang rendah, dengan rata-rata penalty 0 untuk small instances dan rata-rata penalty di bawah 200 untuk medium instances. Penelitian lain yang mendukung pendekatan hybrid adalah Kaviani et al. (2014) yang menunjukkan bahwa algoritma hibrida TABUSA mampu menemukan solusi optimal pada sebagian besar kasus Quadratic Assignment Problem (QAP) dan memberikan relative percentage deviation (RPD) yang lebih rendah dibandingkan dengan Tabu Search murni. Berdasarkan temuan-temuan tersebut, pendekatan hibrida SA-TS dengan Greedy algorithm sebagai initial solution merupakan pilihan yang tepat untuk menyelesaikan UCTP, menggabungkan keunggulan kedua algoritma untuk mencapai solusi yang optimal secara efisien.

Penggunaan Greedy Algorithm sebagai initial solution dalam konteks UCTP telah dibuktikan efektif oleh berbagai penelitian. Coşar et al. (2022) mengembangkan algoritma Greedy-CB-CTT yang menggunakan berbagai heuristik seperti Largest-First, Smallest-First, Best-Fit, Average-weight first, dan Highest Unavailable course-first untuk mengassign mata kuliah ke ruangan yang tersedia. Hasil eksperimen pada 21 problem instance dari benchmark set ITC-2007 menunjukkan bahwa algoritma greedy yang diusulkan dapat menghasilkan solusi feasible dengan zero hard constraint violations pada 18 problem instance. Hal ini menunjukkan bahwa Greedy Algorithm mampu memberikan solusi awal yang berkualitas tinggi dalam waktu komputasi yang sangat singkat, menjadikannya kandidat ideal sebagai initial solution untuk algoritma metaheuristik seperti SA-TS hybrid.

Dari perspektif implementasi sistem, pengembangan Sistem Pendukung Keputusan (Decision Support System/DSS) berbasis web untuk penjadwalan kuliah telah menjadi tren penelitian yang signifikan. Uysal et al. (2025) mengembangkan web-based DSS yang menggunakan algoritma Simulated Annealing untuk optimasi penjadwalan kursus online. Sistem yang dibangun memungkinkan koordinasi program untuk melakukan penyesuaian yang diperlukan, sementara mahasiswa dan dosen mengakses jadwal mereka melalui antarmuka yang ramah pengguna. Hasil eksperimen menunjukkan peningkatan substansial dalam distribusi koneksi concurrent dan efisiensi bandwidth. Romaguera et al. (2023) juga mengembangkan web-based course timetabling system menggunakan Enhanced Genetic Algorithm dengan heuristic mutation yang concentrate pada mutasi gen yang infeasible untuk meningkatkan kemampuan exploration dan exploitation algoritma. Penelitian Latpate et al. (2024) menunjukkan implementasi AI-based automatic timetable generator menggunakan React yang dapat menghasilkan jadwal dalam hitungan menit dengan antarmuka yang intuitif.

Berdasarkan konteks tersebut, penelitian ini fokus pada pengembangan Sistem Pendukung Keputusan (Decision Support System) untuk penjadwalan perkuliahan di Kampus UISI. Sistem DSS yang dikembangkan berfungsi sebagai alat bantu bagi pengambil keputusan (dalam hal ini bagian Administrasi Akademik) untuk menghasilkan jadwal kuliah yang optimal. Berbeda dengan sistem terintegrasi yang langsung terhubung dengan sistem akademik internal, DSS yang dibangun dalam penelitian ini beroperasi secara independen sebagai aplikasi standalone yang dapat menghasilkan solusi penjadwalan yang kemudian dapat diimplementasikan secara manual. Pendekatan ini dipilih karena memberikan fleksibilitas lebih tinggi dalam pengembangan dan pengujian algoritma, serta memungkinkan integrasi di masa depan dengan memanfaatkan REST API yang telah dibangun. Sistem dibangun dengan arsitektur REST API dan web interface untuk memudahkan akses dan penggunaan oleh pihak-pihak terkait.

Pada konteks Universitas Internasional Semen Indonesia (UISI), proses penyusunan jadwal perkuliahan saat ini masih bersifat semi-otomatis dan tersegmentasi dalam beberapa tahap manual yang tidak terintegrasi. Pertama, pengumpulan preferensi dosen dilakukan melalui pertemuan tatap muka dan distribusi formulir manual. Kedua, input data manual dilakukan dengan memasukkan data dosen, mata kuliah, dan preferensi secara manual ke sistem ASC Timetables (sistem timetabling pihak ketiga). Ketiga, jadwal diekspor dari ASC Timetables dalam format tabel atau spreadsheet (Excel). Keempat, jadwal diinput ulang secara manual ke sistem akademik internal (SIAKAD) dan aplikasi manajemen ruang (Ruang UISI). Kelima, jadwal didistribusikan melalui berbagai channel (email, portal, cetak). Karakteristik UCTP di UISI sebagai NP-COP ini menghasilkan beberapa hambatan praktis yang signifikan, meliputi risiko kesalahan input (human error) pada setiap tahap transfer data antar sistem, waktu penyusunan yang lama, ketiadaan integrasi otomatis yang memaksa operator melakukan duplikasi input data, serta rendahnya fleksibilitas dalam menangani perubahan jadwal mendadak di tengah semester.

UISI memiliki hard constraints yang harus dipenuhi 100% untuk menghasilkan jadwal yang valid dan feasible, meliputi lecturer conflict (tidak boleh terjadi bentrokan jadwal dosen), room capacity conflict (kapasitas ruangan harus sesuai dengan jumlah mahasiswa), daily SKS limit (dosen tidak boleh melebihi batas maksimal SKS per hari), class category constraint (kelas pagi dan sore harus dijadwalkan sesuai waktunya), exclusive room constraint (ruang laboratorium bersifat eksklusif untuk program studi tertentu), dan religious time prohibition (tidak boleh ada jadwal pada jam sekitar Dzuhur/Maghrib dan periode Jumat). Selain itu, UISI juga memiliki soft constraints yang tidak wajib dipenuhi 100% tetapi pelanggaran memberikan penalti, meliputi research time allocation (pengalokasian waktu riset yang cukup bagi dosen), teaching time preference (preferensi mengajar dosen pada waktu tertentu), room preference (kebutuhan ruang dengan teknologi spesifik), transit time between classes (waktu memadai untuk berpindah antar ruang), schedule density optimization (menghindari jadwal yang terlalu renggang atau padat), dan program-specific rules (aturan khusus per program studi).

Kompleksitas kombinatorial dari UCTP di UISI menjadi tantangan utama. Menurut Bashab et al. (2023), kesulitan UCTP meningkat secara eksponensial dengan penambahan jumlah constraints. Research gap yang ditemukan meliputi belum adanya algoritma metaheuristik hibrida SA-TS dengan Greedy initial solution yang disesuaikan dengan constraint set UISI yang unik, belum adanya dokumentasi mengenai performance metrics dan parameter tuning dalam konteks dataset real Indonesia, serta belum adanya Sistem Pendukung Keputusan berbasis web dengan antarmuka modern yang mengintegrasikan algoritma SA-TS hybrid. Sistem Pendukung Keputusan yang dikembangkan dalam penelitian ini diharapkan dapat menjadi solusi untuk menghasilkan jadwal kuliah optimal secara efisien.

## 1.2 Rumusan Masalah

Berdasarkan latar belakang di atas, permasalahan yang dibahas dalam penelitian ini dirumuskan sebagai berikut:

1. Bagaimana merancang dan membangun Sistem Pendukung Keputusan berbasis web untuk penjadwalan perkuliahan di Kampus UISI?

2. Bagaimana mengimplementasikan algoritma hibrida Simulated Annealing dan Tabu Search dengan Greedy Algorithm sebagai initial solution untuk menyelesaikan UCTP?

3. Apakah DSS yang dikembangkan dapat menghasilkan jadwal kuliah yang valid dan feasible?

4. Bagaimana membangun sistem dengan arsitektur REST API dan web interface yang mudah digunakan?

## 1.3 Tujuan Penelitian

Tujuan dari penelitian ini adalah:

1. Merancang dan membangun Sistem Pendukung Keputusan berbasis web untuk penjadwalan perkuliahan di Kampus UISI.

2. Mengimplementasikan algoritma hibrida Simulated Annealing dan Tabu Search dengan Greedy Algorithm sebagai initial solution.

3. Menghasilkan jadwal kuliah yang valid dan feasible, yaitu bebas dari pelanggaran hard constraints.

4. Mengoptimalkan pemenuhan soft constraints sesuai dengan preferensi dosen dan kebijakan akademik UISI.

5. Memastikan sistem dapat menghasilkan jadwal kuliah dengan kualitas yang baik.

## 1.4 Batasan Masalah

Batasan masalah dari penelitian ini adalah:

1. Dataset penjadwalan yang digunakan merupakan data institusional spesifik milik Universitas Internasional Semen Indonesia (UISI).

2. Algoritma optimasi yang diimplementasikan adalah algoritma hibrida Simulated Annealing dan Tabu Search dengan Greedy Algorithm sebagai initial solution.

3. Sistem dibangun sebagai Decision Support System yang beroperasi secara independen, bukan sebagai integrasi langsung dengan sistem akademik internal UISI.

4. Frontend dikembangkan menggunakan React.js dan backend menggunakan arsitektur REST API.

5. Penelitian ini fokus pada penjadwalan untuk satu semester akademik penuh.

## 1.5 Manfaat Penelitian

Manfaat dari penelitian ini adalah:

1. Menambah literatur dalam bidang optimasi penjadwalan akademik dengan metaheuristik hibrida SA-TS dan Greedy initial solution.

2. Memberikan kontribusi praktis berupa Sistem Pendukung Keputusan yang dapat membantu bagian Administrasi Akademik UISI.

3. Mempercepat proses penyusunan jadwal perkuliahan.

4. Mengurangi terjadinya human error dalam proses timetabling.

5. Menghasilkan jadwal yang lebih konsisten dan berkualitas.

6. Memberikan proof-of-concept implementasi DSS untuk UCTP dengan arsitektur REST API dan web.

7. Berguna sebagai referensi pada penelitian di masa depan.
