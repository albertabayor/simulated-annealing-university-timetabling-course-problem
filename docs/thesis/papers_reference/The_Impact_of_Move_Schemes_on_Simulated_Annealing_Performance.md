# Analisis Paper: The Impact of Move Schemes on Simulated Annealing Performance

## Informasi Publikasi

- **Judul:** The Impact of Move Schemes on Simulated Annealing Performance
- **Penulis:** Ruichen Xu, Haochun Wang, Yuefan Deng*
- **Affiliasi:** Department of Applied Mathematics and Statistics, Stony Brook University, New York, USA
- **Tipe:** arXiv Preprint
- **arXiv ID:** 2504.17949v1 [math.OC]
- **Tanggal:** 24 April 2025
- **Status:** Ongoing work (belum dipublikasikan secara resmi)
- **DOI:** N/A (preprint)

---

## Abstrak

Paper ini membahas tantangan dalam merancang **move-generation function** yang efektif untuk Simulated Annealing (SA) pada model kompleks. Penulis mengkaji secara teoritis dan eksperimental bagaimana berbagai parameter move-generation — seperti **berapa banyak partikel yang digerakkan** dan **seberapa jauh** setiap iterasi — mempengaruhi performa di berbagai cooling schedule dan ukuran sistem.

**Temuan utama:** Moving exactly one randomly chosen particle per iteration memberikan performa paling efisien. Paper ini menganalisis acceptance rates, exploration properties, dan convergence behavior, menunjukkan bahwa **partial-coordinate updates** dapat mengungguli full-coordinate moves pada setting high-dimensional.

**Keywords:** Simulated Annealing, Move Generation, Partial Update, Metropolis-Hastings

---

## Latar Belakang Teoritis

### Simulated Annealing sebagai MCMC Process

Penulis memandang SA sebagai **Markov Chain Monte Carlo (MCMC)** process yang beroperasi pada berbagai suhu. Perspektif ini mengungkap bagaimana acceptance behavior dan chain efficiency dipengaruhi oleh cara proposal variance dialokasikan across coordinates.

**Konsep kunci:**
- Ketika fewer coordinates di-update, resulting moves lebih moderate
- Moves yang lebih moderate → higher acceptance rates → faster mixing
- Partial-coordinate updates dapat menghindari pitfalls dari full-coordinate updates

### Kerangka Teoritis

Paper ini menggunakan kerangka **Metropolis-Hastings (MH)** algorithm sebagai dasar:

```
Metropolis-Hastings untuk SA:

1. Pada state x, generate proposal x' ~ Q(x' | x)
2. Hitung acceptance probability:
   α = min(1, exp(-(f(x') - f(x))/T))
3. Terima x' dengan probabilitas α, tetap di x otherwise
```

Dengan f(x) = objective function, T = temperature.

---

## Kontribusi Utama Paper

### 1. Partial-Coordinate vs Full-Coordinate Updates

| Aspect | Full-Coordinate | Partial-Coordinate |
|--------|-----------------|-------------------|
| **Updates per iteration** | Semua variabel | Subset variabel |
| **Proposal magnitude** | Besar (dikalokasikan ke semua dimensi) | Kecil (terkonsentrasi) |
| **Acceptance rate** | Rendah | Tinggi |
| **Chain mixing** | Lambat | Cepat |
| **Ergodicity** | Potensi terganggu | Terjaga |

### 2. Teori Konvergensi

**Geman (1984):** Coordinate-wise Gibbs sampler dengan annealing converges ke global optimum di bawah cooling schedule yang sesuai.

**SA dengan partial updates:**
- Tetap ergodic
- Converge globally dengan cooling rate yang sesuai
- Menghindari masalah synchronous updates

### 3. Trade-off Exploration vs Exploitation

```
Exploration (Local)          Exploitation (Global)
     ←---------------------------------------→
     ↑                                    ↑
Small moves                      Large moves
High acceptance                  Low acceptance
```

Paper ini menunjukkan bahwa **balance optimal** dicapai dengan:
- Moving exactly ONE particle per iteration
- Dengan magnitude yang sesuai (variance allocation)

---

## Metodologi Penelitian

### Masalah Uji

#### 1. Lennard-Jones Potential

Masalah molecular modeling klasik untuk menemukan konfigurasi minimum energi dari cluster atom.

**Objective function:**
$$V_{LJ} = 4\epsilon \sum_{i<j} \left[\left(\frac{\sigma}{r_{ij}}\right)^{12} - \left(\frac{\sigma}{r_{ij}}\right)^6\right]$$

**Karakteristik:**
- High-dimensional (N atoms × 3 coordinates)
- Many local minima
- Complex energy landscape

#### 2. Benchmark Tambahan

Paper juga menguji pada benchmark lain untuk validasi generalisasi.

### Desain Eksperimen

**Variabel yang diuji:**
1. **Number of particles moved per iteration** (k = 1, 2, ..., N)
2. **Move distance/variance** (σ values)
3. **Temperature schedules** (exponential, logarithmic)
4. **System sizes** (various N)

**Metrik Evaluasi:**
1. **Acceptance rate:** Persentase proposal yang diterima
2. **Convergence speed:** Iterasi untuk mencapai target energy
3. **Final solution quality:** Energy minimum yang ditemukan
4. **Mixing time:** Autocorrelation time dari chain

---

## Temuan Utama

### Hasil Numerik

#### 1. Acceptance Rates

Temuan: Moving fewer particles → higher acceptance rates

```
Acceptance Rate vs Number of Particles Moved:

k=1:  ████████████████████  ~80-90%
k=2:  ████████████████░░░░  ~70%
k=3:  ██████████████░░░░░░  ~60%
k=N:  ████░░░░░░░░░░░░░░░░  ~20-30%
```

#### 2. Convergence Speed

Temuan: k=1 (single-particle move) converges paling cepat

**Rumusan teoritis:**
$$t_{mix} \propto \frac{1}{\alpha}$$

Dimana α = acceptance rate, t_mix = mixing time.

#### 3. Solution Quality

Single-particle moves menemukan energy minimum yang lebih baik daripada multi-particle moves.

### Insight Kunci

1. **Single-particle optimal:**
   - Moving exactly one particle per iteration memberikan performa terbaik
   - Trade-off terbaik antara exploration dan exploitation

2. **Variance allocation matters:**
   - Fixed total variance → better untuk dialokasikan ke 1 coordinate daripada spread across all
   - Avoids large collective perturbations

3. **Temperature-dependent optimal:**
   - Pada suhu tinggi: larger moves dapat diterima
   - Pada suhu rendah: smaller moves diperlukan

4. **System size scaling:**
   - Partial-coordinate updates lebih menguntungkan untuk high-dimensional problems
   - Benefit meningkat dengan meningkatnya dimensi

---

## Implikasi untuk Penelitian UCTP

### Relevansi dengan University Course Timetabling

Walaupun paper ini fokus pada molecular modeling (Lennard-Jones), prinsip-prinsipnya relevan untuk UCTP:

| Lennard-Jones | UCTP |
|--------------|------|
| N atoms dengan 3 coordinates | N events dengan (timeslot, room) |
| Energy minimization | Penalty minimization |
| Physical constraints (atomic interactions) | Scheduling constraints (hard/soft) |
| High-dimensional (3N) | High-dimensional (N × attributes) |

### Rekomendasi untuk Proyek Ini

#### 1. Move Strategy untuk UCTP

Berdasarkan temuan paper, gunakan **single-event move**:

```javascript
// Rekomendasi: Move satu event per iterasi
function generateNeighbor(currentSolution) {
  // Pilih SATU event secara acak
  const eventIdx = Math.floor(Math.random() * numEvents);

  // Generate move untuk event tersebut
  const newSlot = pickNewTimeslot(eventIdx);
  const newRoom = pickNewRoom(eventIdx);

  return applySingleMove(currentSolution, eventIdx, newSlot, newRoom);
}
```

**JANGAN gunakan:** Multi-event moves (memindahkan banyak events sekaligus)

#### 2. Proposal Variance

Untuk UCTP, "variance" berarti seberapa jauh event dipindahkan:

**Approach yang disarankan:**
- **Nearby moves:** Pindahkan ke timeslot yang berdekatan (hari berbeda, jam dekat)
- **Random moves:** Pindahkan ke timeslot acak (lebih besar variance)

```javascript
// Nearby move (recommended)
function pickNewTimeslot(eventIdx) {
  const currentSlot = solution[eventIdx].slot;
  // Pilih dari neighborhood (misal ±5 timeslots)
  const candidates = getNearbySlots(currentSlot, 5);
  return randomChoice(candidates);
}

// Full random move (less recommended)
function pickNewTimeslot(eventIdx) {
  return randomChoice(allSlots); // Terlalu besar variance
}
```

#### 3. Adaptive Strategy

Paper menunjukkan optimal move strategy mungkin temperature-dependent:

```javascript
function adaptiveMoveSize(temperature) {
  if (temperature > T_high) {
    // High temp: larger moves OK
    return generateDistantMove();
  } else if (temperature > T_medium) {
    // Medium temp: moderate moves
    return generateNearbyMove(3);
  } else {
    // Low temp: small moves
    return generateNearbyMove(1);
  }
}
```

#### 4. Comparison: Single vs Multi-Event Moves

| Aspect | Single-Event Move | Multi-Event Move |
|--------|-------------------|------------------|
| **Acceptance rate** | Tinggi (small perturbation) | Rendah (large perturbation) |
| **Exploration** | Local, gradual | Global, potentially disruptive |
| **Convergence** | Faster mixing | Slower mixing |
| **Implementation** | Simple | More complex |

---

## Kekurangan dan Keterbatasan Paper

### 1. Domain-Specific

- Hanya menguji pada Lennard-Jones dan satu benchmark tambahan
- Tidak ada generalisasi ke masalah combinatorial optimization (seperti UCTP)
- Energy landscape molecular modeling berbeda dengan constraint satisfaction

### 2. Preprint Status

- Belam melalui peer review
- Bisa berubah signifikan sebelum publikasi resmi
- Validitas scientific belum diverifikasi oleh community

### 3. Kurang Analisis Teoretis Mendalam

- Teori konvergensi tidak dikembangkan secara formal
- Kurang proof mengapa single-particle optimal
- Eksplanasi lebih intuitif daripada rigorous

### 4. Parameter Sensitivity

- Tidak ada analisis sensitivitas parameter secara lengkap
- Optimal variance allocation tidak diturunkan secara teoritis
- Cooling schedule interaction tidak dieksplorasi secara sistematis

### 5. Komputasi Time

- Tidak membandingkan waktu komputasi per iterasi
- Single-particle moves mungkin butuh lebih banyak iterasi total
- Trade-off antara iterasi dan acceptance rate tidak dianalisis

---

## Arah Penelitian Lanjutan

### Untuk Tesis Anda

Berdasarkan gap dan temuan paper ini:

#### 1. Validasi pada UCTP

**Research question:** Apakah single-event move lebih efektif untuk UCTP?

**Eksperimen:**
- Implementasi SA dengan single-event move
- Implementasi SA dengan multi-event move (2, 3, 5 events)
- Bandingkan acceptance rate, convergence, solution quality

#### 2. Adaptive Move Strategy

**Research question:** Bagaimana mengadaptasi move size dengan temperature?

**Eksperimen:**
- Implementasi adaptive move strategy
- Bandingkan dengan fixed move strategy
- Analisis performance di berbagai cooling schedules

#### 3. Hybrid Approach

**Research question:** Can we combine single and multi-event moves?

**Ide:**
- Gunakan single-event moves di low temperature (exploitation)
- Gunakan multi-event moves di high temperature (exploration)
- Transisi strategis berdasarkan cooling schedule

#### 4. Neighborhood Structure

**Research question:** Apa struktur neighborhood terbaik untuk UCTP?

**Eksperimen:**
- Single move: timeslot only, room only, both
- Swap moves: two events, three events
- Kempe chain: complex neighborhood

---

## Catatan Implementasi

### Pseudocode SA dengan Single-Event Move

```javascript
/**
 * Simulated Annealing untuk UCTP dengan Single-Event Move
 * Berdasarkan rekomendasi dari Xu et al. (2025)
 */

function simulatedAnnealingUCTP(data, params) {
  const {
    T0 = 1000,           // Initial temperature
    Tf = 0.01,           // Final temperature
    alpha = 0.995,       // Cooling rate
    movesPerTemp = 100   // Iterations per temperature
  } = params;

  // 1. Inisialisasi solusi
  let current = generateInitialSolution(data);
  let currentPenalty = calculatePenalty(current, data);
  let best = copySolution(current);
  let bestPenalty = currentPenalty;

  let T = T0;
  let stats = {
    accepted: 0,
    rejected: 0,
    improvement: 0
  };

  // 2. Main SA loop
  while (T > Tf) {
    for (let i = 0; i < movesPerTemp; i++) {
      // Generate neighbor dengan SINGLE-EVENT MOVE
      const neighbor = generateSingleEventMove(current, data);
      const neighborPenalty = calculatePenalty(neighbor, data);
      const delta = neighborPenalty - currentPenalty;

      // Metropolis criterion
      if (delta < 0 || Math.random() < Math.exp(-delta / T)) {
        current = neighbor;
        currentPenalty = neighborPenalty;
        stats.accepted++;

        if (delta < 0) stats.improvement++;

        // Update best
        if (currentPenalty < bestPenalty) {
          best = copySolution(current);
          bestPenalty = currentPenalty;
        }
      } else {
        stats.rejected++;
      }
    }

    // Cool down
    T *= alpha;

    // Log progress
    const acceptanceRate = stats.accepted / (stats.accepted + stats.rejected);
    console.log(`T=${T.toFixed(2)}, Penalty=${currentPenalty}, Accept=${acceptanceRate.toFixed(2)}`);
  }

  return {
    solution: best,
    penalty: bestPenalty,
    statistics: stats
  };
}

/**
 * Generate neighbor dengan single-event move
 * Berdasarkan prinsip: move exactly one event per iteration
 */
function generateSingleEventMove(solution, data) {
  const neighbor = copySolution(solution);

  // Pilih SATU event secara acak
  const eventIdx = Math.floor(Math.random() * solution.events.length);
  const event = solution.events[eventIdx];

  // Strategy: nearby moves (higher acceptance rate)
  const currentSlot = event.slot;
  const currentRoom = event.room;

  // Pilih new slot (nearby or random based on preference)
  const newSlot = pickNewSlot(currentSlot, data.slots);
  const newRoom = pickNewRoom(currentRoom, event, data.rooms);

  // Apply move
  neighbor.events[eventIdx] = {
    ...event,
    slot: newSlot,
    room: newRoom
  };

  return neighbor;
}

/**
 * Pick new timeslot dengan nearby strategy
 */
function pickNewSlot(currentSlot, allSlots) {
  // Nearby strategy: pilih dari slot yang berdekatan
  const nearbyRange = 5; // ±5 slots
  const nearby = getNearbySlots(currentSlot, allSlots, nearbyRange);
  return nearby[Math.floor(Math.random() * nearby.length)];
}
```

### Implementasi Multi-Event Move (untuk perbandingan)

```javascript
/**
 * Generate neighbor dengan multi-event move (untuk comparison)
 */
function generateMultiEventMove(solution, data, k = 2) {
  const neighbor = copySolution(solution);

  // Pilih K events secara acak
  const indices = randomSample(
    Array.from({length: solution.events.length}, (_, i) => i),
    k
  );

  // Apply moves ke K events
  for (const idx of indices) {
    const event = solution.events[idx];
    neighbor.events[idx] = {
      ...event,
      slot: randomChoice(data.slots),
      room: randomChoice(data.rooms)
    };
  }

  return neighbor;
}
```

---

## Kesimpulan

Paper ini memberikan kontribusi penting dalam memahami move-generation strategies untuk Simulated Annealing:

### Temuan Utama

1. **Single-particle/coordinate moves optimal** - Moving exactly one element per iteration memberikan performa terbaik
2. **Partial-coordinate updates unggul** - Better acceptance rates dan faster mixing dibanding full-coordinate updates
3. **Variance allocation matters** - Fixed total variance lebih baik dikonsentrasikan ke satu coordinate daripada spread

### Rekomendasi untuk UCTP

1. **Implement single-event moves** - Pindahkan satu event per iterasi
2. **Use nearby move strategy** - Higher acceptance rate dengan gradual exploration
3. **Consider adaptive strategy** - Sesuaikan move magnitude dengan temperature
4. **Validate empirically** - Uji pada dataset UCTP untuk konfirmasi

### Research Questions untuk Tesis

1. Apakah single-event move lebih efektif untuk UCTP daripada multi-event moves?
2. Bagaimana struktur neighborhood terbaik untuk UCTP (timeslot-only, room-only, or both)?
3. Dapatkah adaptive move strategy meningkatkan performa SA pada UCTP?

---

## Referensi

- Xu, R., Wang, H., Deng, Y. (2025). "The Impact of Move Schemes on Simulated Annealing Performance." *arXiv preprint* arXiv:2504.17949.
- Geman, S., Geman, D. (1984). "Stochastic Relaxation, Gibbs Distributions, and the Bayesian Restoration of Images." *IEEE Transactions on Pattern Analysis and Machine Intelligence*.
- Metropolis, N., et al. (1953). "Equation of State Calculations by Fast Computing Machines." *Journal of Chemical Physics*.
- Kirkpatrick, S., et al. (1983). "Optimization by Simulated Annealing." *Science*.

---

*Analisis ini ditulis untuk mendukung penelitian tesis tentang University Course Timetabling Problem menggunakan Simulated Annealing. Paper ini adalah preprint 2025 yang membahas move-generation strategies untuk SA.*
