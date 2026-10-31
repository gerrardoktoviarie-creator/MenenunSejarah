# BRD — Business Requirements Document

## Sandi Leluhur: Mesin Biner Pertama
**Website Kompetisi Web Design TECHTOPIA Vol. 2 (Tingkat Nasional)**

| Atribut | Nilai |
|---|---|
| Versi | 1.1 (Disinkronkan dengan desain final) |
| Tanggal | 23 Oktober 2026 |
| Tema Lomba | PUSAKA: *Preserving Unity, Sustaining Ancestral Knowledge & Artistry* |
| Subtema | Pendidikan Berbasis Lokal & Ekonomi Kreatif |
| Dokumen Terkait | `PRD.md` (kebutuhan produk), `SRS.md` (spesifikasi teknis) |
| Sumber Perubahan | Hasil desain final (`MAIN.jpg`), redesign hero, Benang Sepanjang Situs, penyelarasan copy |

### Riwayat Revisi

| Versi | Tanggal | Perubahan Utama |
|---|---|---|
| 1.0 | 9 Okt 2026 | Draf awal untuk persetujuan tim |
| 1.1 | 23 Okt 2026 | Manifesto baru ("DITENUN, BUKAN DITULIS"); alur "Temukan → Pahami → **Tenun** → Lestarikan"; disiplin ruang lega dan satu titik fokus; token warna tambahan (Paper, Brass Ink, Ash); Benang Sepanjang Situs; header persisten dengan indikator langkah; halaman Kredit dinaikkan menjadi *Must*; OBJ-07 dan OBJ-08; BR-13 sampai BR-16; risiko R-11 sampai R-14; rujukan SRS disesuaikan dengan SRS 1.1 |

---

## 1. Ringkasan Eksekutif

**Sandi Leluhur: Mesin Biner Pertama** adalah website static (HTML, CSS, Vanilla JavaScript) yang membingkai ulang alat tenun Nusantara sebagai purwarupa komputasi: setiap benang lungsi yang diangkat atau diturunkan adalah keputusan biner, dan urutan baris tenun adalah sebuah program.

Proyek ini menjawab tema PUSAKA dengan **meretas** pusaka, bukan sekadar memajangnya. Pengunjung diajak memahami logika biner lewat tenun (pendidikan berbasis lokal), memprogram motif sendiri, lalu mengubah motif itu menjadi Sertifikat Digital "Penjaga Pusaka" yang berujung pada ajakan mendukung pengrajin UMKM nyata (ekonomi kreatif).

Arah visualnya adalah **Royal Brutalism**: agresivitas Brutalisme (tipografi raksasa, grid tebal, tata letak radikal) berbenturan dengan keanggunan arsip kerajaan dan museum, diatur oleh disiplin **ruang lega dan satu titik fokus per layar** (*quiet luxury*). Satu helai **benang** yang menyambung di seluruh halaman, dari serat menjadi angka biner, mengikat tema "masa lalu menenun masa depan". Keputusan teknis mengikuti aturan lomba secara ketat: static HTML, tanpa framework JS, tanpa build, navigasi ala SPA lewat `fetch()` + `history.pushState()`, dan kode terbaca penuh oleh juri.

**Pernyataan nilai tunggal:**
> Juri membuka satu website, tetapi merasakan tiga hal sekaligus: gagasan yang berani, pengalaman yang mulus di perangkat apa pun, dan kode yang bisa mereka baca dan percaya.

---

## 2. Latar Belakang dan Peluang

### 2.1 Konteks
Lomba menilai karya dari juri yang berlatar dosen dan praktisi UI/UX, Brand Identity, dan Full-Stack Development. Mereka terbiasa melihat banyak karya bertema budaya yang jatuh ke klise: ornamen batik sebagai dekorasi, palet cokelat-emas, dan tipografi aksara sebagai hiasan.

### 2.2 Peluang Diferensiasi
| Klise yang umum | Pendekatan Sandi Leluhur |
|---|---|
| Budaya sebagai ornamen visual | Budaya sebagai **sistem** (logika, struktur, algoritma) |
| Tampilan "nostalgia", palet hangat pudar | Benturan masa lalu dan masa depan lewat Royal Brutalism |
| Halaman informasi pasif | Interaksi bermakna: memprogram motif dan memiliki hasilnya |
| Budaya sebagai objek pameran | Budaya sebagai **sumber inovasi** dan pintu ke ekonomi kreatif |
| Kode berantakan di balik tampilan memukau | Kode bersih yang menjadi bagian dari bukti keahlian |

### 2.3 Insight Inti
> *"The future we search is in our past."*

Tenun adalah teknologi pengkodean pola yang sudah ada jauh sebelum komputer elektronik. Insight ini memberi proyek satu argumen yang bisa dipertahankan di depan juri akademik, asalkan dibingkai dengan kurasi yang jujur (lihat Risiko R-01).

---

## 3. Tujuan Bisnis

### 3.1 Tujuan Utama
Memaksimalkan skor penilaian lomba dengan karya yang **orisinal secara konsep, mulus secara pengalaman, dan kokoh secara teknis**.

### 3.2 Objektif Terukur (SMART)

| ID | Objektif | Indikator Keberhasilan | Tenggat |
|---|---|---|---|
| OBJ-01 | Konsep terbaca jelas dalam 60 detik pertama, dan pesan inti serta aksi utama terbaca dalam **5 detik** | Judul, subjudul, dan tombol aksi utama terlihat tanpa menggulir (*above the fold*) dan tidak tertunda efek ketik; manifesto terbaca tanpa interaksi tambahan | Sebelum pengumpulan |
| OBJ-02 | Seluruh fitur kunci bekerja di desktop dan mobile | 100% acceptance criteria PRD lulus pada matriks perangkat (lihat SRS §14) | Sebelum pengumpulan |
| OBJ-03 | Performa tidak menjadi alasan juri kehilangan kesan | Lighthouse (mobile, simulasi): Performance ≥ 85, Accessibility ≥ 95, Best Practices ≥ 95 | Sebelum pengumpulan |
| OBJ-04 | Kepatuhan aturan 100% | Nol framework terlarang, nol file minified, nol proses build, ≤ 10 file HTML | Gerbang rilis |
| OBJ-05 | Responsivitas tanpa cacat tata letak | Nol *horizontal scroll* pada lebar 320–1920 px | Sebelum pengumpulan |
| OBJ-06 | Alur edukasi hingga aksi tuntas | Pengguna dapat menyelesaikan Playground → Sertifikat → CTA UMKM tanpa panduan | Sebelum pengumpulan |
| OBJ-07 | Kejujuran konten | Nol klaim institusi, teknis, atau data yang tidak benar atau tidak dapat diverifikasi pada UI (mis. afiliasi lembaga, enkripsi, "terverifikasi"); setiap angka bersumber dari state nyata | Gerbang rilis |
| OBJ-08 | Konsistensi sistem | Satu spesifikasi header, label menu, dan indikator langkah di seluruh halaman | Sebelum pengumpulan |

---

## 4. Ruang Lingkup

### 4.1 Dalam Lingkup (In-Scope)
1. Lima halaman HTML: `index.html` (Beranda), `arsip.html`, `playground.html`, `dampak.html`, dan `kredit.html` (Kurasi & Kredit, dirancang penuh pada desain final dan menjadi dasar mitigasi R-01).
2. Booting Sequence bergaya terminal dan Interactive Cursor Trail beserta **alternatif sentuh (tap/swipe)**.
3. Navigasi ilusi SPA (`fetch()` + `history.pushState()`) tanpa *white flash*.
4. Exploded View alat tenun (SVG) dengan Reverse Time-Scroll.
5. Playground Biner: grid tenun interaktif, panel kontrol, penyimpanan `localStorage`.
6. Sertifikat Digital "Penjaga Pusaka" dan CTA dukungan pengrajin UMKM.
7. Arsitektur **mobile-first**, struktur folder `/css`, `/js`, `/assets`.
8. Dokumentasi: `README.md` proyek, `BRD.md`, `PRD.md`, `SRS.md`.
9. Header persisten dengan indikator langkah (Temukan, Pahami, Tenun, Lestarikan) yang disinkronkan oleh router.
10. **Benang Sepanjang Situs**: satu helai benang SVG yang digerakkan GSAP ScrollTrigger, berubah dari serat menjadi angka biner dan menyambung antarhalaman.
11. Manifest atribusi (`credits.json`) yang dapat diunduh dari halaman Kredit.

### 4.2 Di Luar Lingkup (Out-of-Scope)
- Backend, database, autentikasi, atau API pihak ketiga.
- Transaksi jual beli di dalam website (CTA hanya mengarahkan ke kanal pengrajin nyata).
- Framework JS, UI component library, website builder, dan SSG/proses build.
- CMS atau panel admin.
- Multi-bahasa (bahasa tunggal: Indonesia; istilah teknis boleh bilingual).
- Three.js, WebGL, dan library canvas/3D lain (benang dibuat dengan SVG + GSAP).
- Fitur akun pengguna (ikon profil pada salah satu header di mock tidak dipakai).

---

## 5. Pemangku Kepentingan

| Pemangku | Peran | Kepentingan |
|---|---|---|
| Juri (dosen dan praktisi UI/UX, Brand Identity, Full-Stack) | Penilai utama | Konsep orisinal, UX matang, kode bersih, responsif |
| Panitia TECHTOPIA | Penyelenggara | Kepatuhan aturan dan kesesuaian tema |
| Tim Pengembang | Pelaksana | Ruang lingkup realistis, dokumen jelas |
| Pengrajin UMKM mitra | Penerima manfaat | Eksposur dan jalur kontak yang akurat dan etis |
| Pengunjung umum | Pengguna sekunder | Pengalaman edukatif dan bermakna |

---

## 6. Konsep Strategis

### 6.1 Manifesto

Judul Booting Sequence: **"KOMPUTER PERTAMA DITENUN, BUKAN DITULIS"**

Subjudul: *"Naik atau turun. Satu atau nol. Pada helai lungsi, leluhur kita menyimpan sebuah bahasa, jauh sebelum ada layar."*

Aksi utama: **MULAI MENENUN →**

> Manifesto lama ("KOMPUTER PERTAMA KITA BUKAN KACA, MELAINKAN KAYU.") dipensiunkan karena ambigu ("kita" dapat dibaca sebagai kepemilikan), harus menebak makna "kaca" dan "kayu", dan terlalu panjang (5 baris di desktop). Idenya tetap hidup pada subjudul ("jauh sebelum ada layar").

Naratif empat bab yang konsisten di seluruh halaman, dan tampil sebagai indikator langkah pada header:
1. **Temukan** (Beranda): provokasi dan keheranan.
2. **Pahami** (Arsip): bedah anatomi tenun sebagai sistem biner.
3. **Tenun** (Playground): pengguna menjadi penenun yang memprogram motif.
4. **Lestarikan** (Dampak): pengguna menjadi penjaga pusaka dan diajak mendukung pengrajin.

Halaman **Kredit** berada di luar alur empat langkah; ia adalah halaman kurasi yang membingkai klaim secara jujur.

**Catatan klaim.** Kata "pertama" bersifat provokatif. Karena manifesto kini menyatakan "komputer pertama ditenun", kewajiban membingkainya sebagai analogi pada halaman Kredit (R-01) menjadi lebih penting, dan kutipan di halaman Kredit **harus** memakai teks manifesto yang aktif.

#### 6.1.1 Motif Pengikat: Benang Sepanjang Situs
Satu helai benang vertikal tidak pernah hilang saat berpindah halaman: bagian atas berupa serat berpilin (masa lalu), bagian bawah berupa angka biner (masa depan), dipisahkan simpul kuningan kecil (teropong). Saat menggulir, simpul naik sehingga serat berubah menjadi sandi. Benang adalah **pengikat identitas**, bukan momen "wow" keempat; ia bersifat sekunder terhadap judul dan tombol aksi.

### 6.2 Art Direction: *Royal Brutalism*
| Sisi Brutalis (Masa Depan) | Sisi Royal (Masa Lalu) |
|---|---|
| Tipografi raksasa memenuhi layar | *Serif* kontras tinggi yang anggun |
| Garis grid tebal dan tata letak radikal | Elemen struktural kerajaan, bingkai arsip museum |
| Terminal, kode, data mentah | Emas kuningan, kartu pos kuno, label artefak |
| Latar Void Black, aksi Merah Saga | Latar Putih Gading, narasi arsip |

Prinsip: **tipografi adalah arsitektur**, yaitu pembentuk ruang dan ritme halaman, bukan sekadar teks bacaan.

#### Disiplin Komposisi (*Quiet Luxury*)
Kemewahan datang dari ruang dan ketepatan, bukan dari banyaknya dekorasi.
- Minimal ≈ 40% area layar hero dan narasi dibiarkan kosong; margin sisi 120 px (desktop) dan 24 px (mobile).
- **Satu titik fokus per layar.** Urutan perhatian: judul → subjudul → satu aksi utama (tombol solid Merah Saga, maksimal satu per layar).
- **Struktur familiar, ekspresi orisinal.** Navigasi, tombol, dan formulir mengikuti pola yang dikenal pengguna; kreativitas dipakai pada tipografi, citra, dan tiga momen "wow".
- Anggaran ornamen: hanya siku kuningan pada bingkai, hairline kuningan, label bracket Mono, simbol ❖ sebagai pemisah, dan satu segel per layar. Dilarang pola latar (batik/tumpal), bingkai ganda, bayangan lembut, dan gradien besar.
- Semua judul menyatakan pesan lengkap (bukan label generik), karena pengunjung memindai, bukan membaca.

#### Kosakata Visual Desain Final
| Elemen | Wujud |
|---|---|
| Label bracket | `[ KODIFIKASI // KORPUS ]`, Mono kapital, jarak huruf lebar |
| Siku kuningan | Empat siku tipis pada bingkai (ilustrasi Arsip, grid Playground) |
| Pemisah | ❖ dan hairline kuningan 1 px |
| Papan data | Blok terminal Void dengan teks Concrete/Ivory (readout, kartu ID sertifikat) |
| Status strip | Baris Mono kecil berisi nilai nyata (lihat OBJ-07) |

### 6.3 Palet Warna dan Aturan Penggunaan

| Token | Nama | Hex | Peran |
|---|---|---|---|
| `--c-red` | Merah Saga (Brutalist Red) | `#D91604` | Aksi, ketegasan, tipografi ekspresif |
| `--c-ivory` | Putih Gading (Ivory White) | `#F5F2EB` | Fondasi elegan, latar narasi arsip |
| `--c-void` | Hitam Arang (Void Black) | `#0D0D0D` | Latar Hero, garis grid tebal |
| `--c-brass` | Emas Kuningan Mentah (Raw Brass) | `#C4A661` | Aksen artefak, ornamen halus |
| `--c-concrete` | Abu Beton (Concrete Gray) | `#A6A6A6` | Teks kode/data netral |
| `--c-paper` | Kertas Arsip (Paper) | `#FCF9F2` | Latar halaman Arsip, Playground, Dampak, Kredit (terukur dari desain final; Ivory tetap dipakai pada Beranda Scroll 2) |
| `--c-brass-ink` | Tinta Kuningan (Brass Ink) | `#8C6E2E` | Teks kuningan **informatif** di atas Paper/Ivory |
| `--c-ash` | Abu Tinta (Ash) | `#6C6B67` | Teks sekunder di atas Paper/Ivory |

**Matriks kontras (rumus WCAG 2.x, nilai pembulatan; verifikasi ulang dengan alat sebelum rilis):**

| Teks / Latar | Rasio | Keputusan |
|---|---|---|
| Ivory di atas Void | ≈ 17,4 : 1 | Aman untuk semua ukuran teks |
| Concrete di atas Void | ≈ 8,0 : 1 | Aman (teks kode/data di latar gelap) |
| Brass di atas Void | ≈ 8,3 : 1 | Aman |
| Merah di atas Ivory | ≈ 4,6 : 1 | Aman untuk teks biasa (batas tipis) |
| Merah di atas Void | ≈ 3,8 : 1 | **Hanya teks besar** (≥ 24 px, atau ≥ 18,66 px tebal) |
| Concrete di atas Ivory | ≈ 2,2 : 1 | **Dilarang untuk teks**; gunakan Void |
| Brass di atas Ivory | ≈ 2,1 : 1 | **Dekoratif saja**, tidak boleh membawa informasi |
| Brass Ink (`#8C6E2E`) di atas Paper | ≈ 4,55 : 1 | Aman untuk teks informatif (batas tipis); untuk teks ≤ 12 px disarankan `#7A5C14` (≈ 5,9 : 1) |
| Ash (`#6C6B67`) di atas Paper | ≈ 5,1 : 1 | Aman untuk teks sekunder |
| Merah di atas Paper | ≈ 4,9 : 1 | Aman untuk teks biasa |

Konsekuensi desain: teks Merah Saga di latar gelap hanya dipakai pada tipografi raksasa; teks kode abu (Concrete) hanya di latar Void, sedangkan teks sekunder di latar terang memakai Ash; label kuningan yang membawa informasi memakai Brass Ink, bukan Brass; informasi penting tidak boleh dibawa oleh warna saja.

### 6.4 Tipografi
- **Display Sans** (agresif, tebal, raksasa): rekomendasi *Anton* atau setara.
- **High-contrast Serif** (anggun, berkelas): rekomendasi *Playfair Display* (termasuk italic) atau setara.
- **Mono** (terminal dan data): rekomendasi *JetBrains Mono* atau setara.
- **Label bracket**: Mono kapital, jarak huruf ±0,12 em, ukuran minimum 11 px.
- Semua rekomendasi berlisensi SIL OFL. Tim wajib memverifikasi lisensi akhir dan *self-host* berkas `woff2` di `/assets/fonts` (dibatasi subset Latin, `font-display: swap`).

---

## 7. Pemetaan Strategi ke Metrik Penilaian Lomba

> Bobot yang disebutkan dalam brief: **Kreativitas 30%**, **UX 20%**, **Teknologi 15%**, **Responsivitas 15%**. Total 80%. Sisa **20% tidak disebutkan** dalam brief; diasumsikan mencakup kesesuaian tema dan kualitas presentasi/kode. **Tim perlu memverifikasi dengan buku panduan resmi lomba.**

### 7.1 Ringkasan

| Kriteria | Bobot | Strategi Pemenang | Bukti yang akan dilihat juri |
|---|---|---|---|
| Kreativitas | 30% | Reframing tenun sebagai mesin biner + Royal Brutalism | Manifesto, Cursor Trail, Exploded View, Playground, Sertifikat |
| UX | 20% | Alur naratif linear, umpan balik instan, transisi mulus | SPA tanpa white flash, state kosong/galat, aksesibilitas |
| Teknologi | 15% | Vanilla bersih, patuh aturan, manajemen memori | View Source, DevTools, struktur folder, nol build |
| Responsivitas | 15% | Mobile-first, alternatif sentuh, tanpa horizontal scroll | Uji DevTools device mode, ponsel asli |
| Lainnya (asumsi) | 20% | Kesesuaian tema, kurasi jujur, dokumentasi rapi | Halaman Kredit, README, tiga dokumen ini |

### 7.2 Kreativitas (30%): "Kenapa Royal Brutalism dan Sandi Leluhur menang"

1. **Konsep yang bisa dipertahankan.** Struktur tenun (benang lungsi diangkat atau diturunkan per baris) memang bersifat biner. Ini analogi yang kuat, bukan sekadar slogan. Kurasi pada halaman Kredit menjelaskan analogi ini (dan mengutip manifesto aktif) serta menyandingkannya dengan tonggak kartu berlubang pada alat tenun Jacquard (1804) yang kerap dikaitkan dengan awal pemrograman.
2. **Mendobrak klise.** Tidak ada ornamen batik sebagai hiasan. Motif muncul sebagai **data yang bisa diprogram**.
3. **Bahasa visual yang konsisten dan berani.** Benturan Display Sans raksasa dan Serif anggun menciptakan identitas yang langsung dikenali. Brand Identity Director akan membaca ini sebagai sistem identitas, bukan dekorasi.
4. **Tiga momen "wow" terkurasi** (ditambah Benang Sepanjang Situs sebagai pengikat identitas, bukan momen keempat) (masing-masing dirancang agar berbeda mekanismenya):
   - *Booting Sequence*: kejutan tipografi dan naratif.
   - *Cursor Trail*: kejutan interaktif (menenun waktu).
   - *Exploded View + Reverse Time-Scroll*: kejutan struktural dan edukatif.
5. **Kesesuaian tema dan subtema.**
   - *Pendidikan Berbasis Lokal*: Arsip Sandi dan Playground mengajarkan logika biner lewat pengetahuan tenun.
   - *Ekonomi Kreatif*: Sertifikat Digital dan CTA UMKM menghubungkan apresiasi dengan dukungan nyata kepada pengrajin.

### 7.3 UX (20%)

- **Alur naratif linear**: Boot → Trail → Arsip → Playground → Dampak (Temukan → Pahami → Tenun → Lestarikan), ditampilkan sebagai indikator langkah pada header.
- **Aturan 5 detik**: judul, subjudul, dan satu aksi utama terlihat tanpa menggulir pada layar pertama; tidak ada efek yang menunda keterbacaan lebih dari 3 detik.
- **Satu aksi utama per layar**; aksi sekunder tampil sebagai tombol garis atau tautan teks.
- **Umpan balik instan**: setiap klik pada grid langsung mengubah sel, penghitung, dan pembacaan biner.
- **Transisi mulus**: konten lama *fade-out* dan konten baru *fade-in*, tanpa *white flash*.
- **Menangani kondisi tepi**: state kosong (belum ada motif), `localStorage` tidak tersedia, gambar gagal dimuat, JS/CDN gagal.
- **Aksesibilitas nyata**: navigasi keyboard di grid, `prefers-reduced-motion`, kontras terukur, fokus terlihat.
- **Brutalisme tanpa mengorbankan keterbacaan**: ekspresif pada elemen dekoratif, tertib pada teks bacaan dan kontrol.

### 7.4 Teknologi (15%)

- Murni static HTML, CSS, Vanilla JS; ≤ 10 file HTML (rencana: 5).
- Navigasi SPA *ilusi* dengan `fetch()` + `history.pushState()`, termasuk penanganan tombol *back/forward*.
- Cursor Trail dan Grid Biner murni manipulasi DOM; animasi jejak memakai GSAP (CDN).
- Manajemen memori eksplisit: node jejak dihapus dari DOM, *listener* dilepas, `ScrollTrigger` dibersihkan saat pindah halaman.
- Benang Sepanjang Situs: SVG buatan sendiri + GSAP ScrollTrigger, hidup di lapisan persisten di luar `<main>`; tanpa Three.js/WebGL.
- Identitas motif: ID dan checksum dihitung nyata (FNV-1a), bukan angka statis.
- `localStorage` dengan validasi skema dan *fallback* bila tidak tersedia.
- Kode tidak di-minify, berkomentar, terstruktur; **tanpa proses build** dan tanpa SSG.

### 7.5 Responsivitas (15%)

- CSS ditulis **mobile-first** (basis 320 px, `min-width` media query).
- Setiap fitur punya perilaku mobile yang dirancang, bukan sekadar disusutkan: Cursor Trail → *Tap-to-Stamp* dan *Swipe-to-Weave*; Playground → tata letak bertumpuk; Exploded View → versi vertikal.
- Satuan modern (`dvh/svh`, `clamp()`), area aman (*safe-area*), target sentuh memadai.
- Bukti: matriks uji perangkat dan lebar (SRS §14).

---

## 8. Kebutuhan Bisnis (Business Requirements)

| ID | Kebutuhan | Prioritas | Metrik Terkait |
|---|---|---|---|
| BR-01 | Website HARUS menyampaikan manifesto dan konsep "tenun = mesin biner" dalam 60 detik pertama tanpa instruksi, dengan judul, subjudul, dan aksi utama terlihat dalam 5 detik pertama | Must | Kreativitas, UX |
| BR-02 | Identitas visual HARUS konsisten menerapkan Royal Brutalism (palet, tipografi, grid) di seluruh halaman | Must | Kreativitas |
| BR-03 | Website HARUS menyediakan pengalaman interaktif yang mengubah pengunjung dari pembaca menjadi pelaku (Playground) | Must | Kreativitas, UX |
| BR-04 | Website HARUS menautkan hasil karya pengguna ke aksi dukungan pengrajin UMKM nyata | Must | Tema, Kreativitas |
| BR-05 | Seluruh navigasi HARUS terasa mulus tanpa *white flash* | Must | UX, Teknologi |
| BR-06 | Seluruh fitur HARUS berfungsi optimal di perangkat mobile (**mobile-first**), termasuk alternatif sentuh untuk Cursor Trail | Must | Responsivitas |
| BR-07 | Teknologi HARUS patuh aturan lomba: static HTML/CSS/Vanilla JS, ≤ 10 HTML, tanpa framework terlarang, tanpa minify/obfuscate | Must | Teknologi, Kepatuhan |
| BR-08 | Struktur proyek HARUS rapi dan terbaca (`/css`, `/js`, `/assets`) **tanpa proses build** (tanpa SSG, bundler, atau transpiler) | Must | Teknologi |
| BR-09 | Performa HARUS stabil: tanpa kebocoran memori pada jejak kursor dan perpindahan halaman berulang | Must | Teknologi, UX |
| BR-10 | Aksesibilitas dasar HARUS dipenuhi (keyboard, kontras, reduced-motion, teks alternatif) | Should | UX |
| BR-11 | Konten HARUS dikurasi jujur: klaim historis dibingkai analogi, sumber dan kredit aset dicantumkan (halaman Kredit **dinaikkan ke Must** karena menjadi dasar mitigasi R-01) | Must | Tema, Lainnya (asumsi) |
| BR-12 | Dokumentasi (README, BRD, PRD, SRS) HARUS tersedia dan konsisten satu sama lain | Should | Lainnya (asumsi) |
| BR-13 | Website HARUS menampilkan **Benang Sepanjang Situs** yang menyambung antarhalaman dan menyatakan tema "masa lalu menenun masa depan"; minimum pada Beranda, sisanya mengikuti prioritas SRS §10.3 | Must (Beranda), Should (halaman lain) | Kreativitas |
| BR-14 | UI TIDAK BOLEH memuat klaim institusi, teknis, atau data yang tidak benar (afiliasi lembaga, enkripsi, "terverifikasi", "immutable", mitra atau sumber fiktif); setiap angka HARUS nyata atau dihapus | Must | Tema, Teknologi, Kepatuhan |
| BR-15 | Header persisten dengan label menu kanonik dan indikator langkah HARUS konsisten di seluruh halaman | Should | UX, Kreativitas |
| BR-16 | Setiap layar HARUS mengikuti urutan *above the fold* (judul, subjudul, satu aksi utama), dan ruang kosong serta satu titik fokus HARUS dijaga | Must | UX, Kreativitas |

---

## 9. Batasan dan Kepatuhan Aturan Lomba

| Aturan | Dampak pada Desain | Status Rencana |
|---|---|---|
| Static HTML, CSS, Vanilla JS; ≤ 10 file HTML | 5 file HTML; tanpa kompilasi | Patuh |
| Dilarang React, Vue, Svelte, Angular, Node.js | Tidak ada `package.json`, `node_modules`, atau server Node | Patuh |
| Dilarang UI library instan (Flowbite, DaisyUI) | Komponen UI ditulis sendiri | Patuh |
| Dilarang website builder (Wix, Webflow) | Tidak berlaku | Patuh |
| Dilarang kode minify/obfuscate | Semua berkas dibiarkan terbaca, berkomentar | Patuh |
| Boleh Tailwind/Bootstrap, GSAP, ScrollTrigger, jQuery via CDN | Rencana memakai **GSAP + ScrollTrigger (CDN)**; CSS ditulis manual dengan *design tokens* (alasan di SRS §3) | Patuh |
| Navigasi via `fetch()` + `history.pushState()`, tanpa white flash | Router SPA ilusi di `js/core/router.js` | Patuh |
| Cursor Trail dan Grid murni manipulasi DOM Vanilla | Tidak memakai canvas library atau plugin pihak ketiga untuk logika | Patuh |
| State tanpa backend via `localStorage` | Skema bervers, validasi, *fallback* memori | Patuh |
| Three.js, WebGL, dan library canvas/3D | **Tidak dipakai** (di luar daftar pustaka yang diizinkan); benang dibuat dengan SVG + GSAP | Patuh |
| Klaim dan atribusi | Tidak mencantumkan afiliasi institusi, mitra, atau sumber yang tidak ada | Patuh (gerbang rilis, SRS §13.4) |
| **Mobile-first** (Bagian 3 tambahan) | Basis CSS 320 px; `min-width` queries | Patuh |
| **Tanpa proses build SSG → static HTML** (Bagian 3 tambahan) | HTML ditulis langsung; tanpa generator | Patuh |

---

## 10. Asumsi dan Ketergantungan

### Asumsi
- A-01: Pengumpulan karya berupa URL hosting statis (misalnya GitHub Pages, Netlify) **dan/atau** berkas ZIP yang dibuka lokal. Desain mengakomodasi keduanya (lihat R-03).
- A-02: Juri memakai peramban *evergreen* modern (Chrome, Edge, Firefox, Safari dua versi terakhir).
- A-03: CDN (cdnjs/jsDelivr) dapat diakses saat penjurian, dengan *fallback* bila gagal.
- A-04: Rincian 20% bobot lainnya akan diverifikasi dengan panduan resmi.
- A-05: Desain final tersedia untuk desktop (1440 px). Mock mobile, state kosong Dampak, dan keadaan tanpa-JS belum dirancang dan mengikuti aturan SRS §12.
- A-06: Keputusan **CSS manual** (menggantikan Tailwind CDN pada SRS 1.0) perlu dikonfirmasi tim (SRS §3.1).

### Ketergantungan
- D-01: Aset foto close-up pusaka (serat tenun, keris, dsb.) berlisensi jelas atau milik sendiri.
- D-02: Kontak/URL mitra pengrajin UMKM nyata untuk CTA (**disediakan tim**; dokumen ini tidak mengarang organisasi).
- D-03: Kurasi istilah komponen alat tenun dan penanda tahun oleh narasumber atau referensi tepercaya.
- D-04: Nama motif tradisional (mis. "Pucuk Rebung") hanya boleh dipakai bila divalidasi kurator; pola 12-bit buatan pengguna tidak boleh diberi nama motif asli.
- D-05: Seluruh teks placeholder pada desain final (mitra pengrajin, sumber aset, lokasi) harus diganti data nyata atau dihapus sebelum rilis.

---

## 11. Risiko dan Mitigasi

| ID | Risiko | Dampak | Mitigasi |
|---|---|---|---|
| R-01 | Klaim "komputer pertama ditenun" dinilai berlebihan oleh juri akademik (manifesto baru menyatakan klaim lebih tegas) | Kredibilitas turun | Bingkai sebagai analogi pada halaman Kredit yang **mengutip manifesto aktif** (Jacquard 1804 sebagai tonggak kartu berlubang); headline tetap provokatif, isi halaman akurat; penanda tahun bertanda "perkiraan"; halaman Kredit berstatus Must |
| R-02 | Cursor Trail menyebabkan *lag* atau kebocoran memori, terutama di mobile | Skor Teknologi dan UX turun | Batas node aktif, hapus dari DOM, *throttle* lewat rAF, uji heap (SRS §11) |
| R-03 | Juri membuka berkas lewat `file://` sehingga `fetch()` SPA gagal | Navigasi rusak | Deteksi protokol: pada `file://` router dinonaktifkan dan tautan berjalan normal; JS memakai *classic script* (bukan ES module) agar tetap berjalan |
| R-04 | Pelanggaran hak cipta aset pusaka | Diskualifikasi atau citra buruk | Hanya foto sendiri atau lisensi CC0/CC BY dengan kredit di `kredit.html` |
| R-05 | Brutalisme mengorbankan keterbacaan dan usability | UX turun | Pisahkan zona ekspresif dan zona fungsional; aturan kontras; uji pengguna singkat |
| R-06 | CDN GSAP gagal dimuat saat penjurian | Animasi mati | Pin versi + SRI; *fallback* CSS (kelas `no-gsap`), konten tetap terbaca |
| R-07 | `localStorage` dinonaktifkan atau mode privat | Sertifikat kosong | *Fallback* memori selama sesi, pesan jelas kepada pengguna |
| R-08 | Ruang lingkup terlalu besar untuk waktu tersedia | Fitur setengah matang | Prioritas MoSCoW (PRD), potong dari **Could/Should** lebih dulu |
| R-09 | Tanpa build, header/footer terduplikasi di 5 HTML sehingga berisiko tidak sinkron | Inkonsistensi | Daftar periksa sinkronisasi nav di README; skrip validasi manual saat QA |
| R-10 | Pelanggaran aturan tak sengaja (minify, library terlarang) | Diskualifikasi | Gerbang rilis: audit berkas dan daftar artefak terlarang (SRS §13) |
| R-11 | Teks mock memuat klaim institusional atau teknis yang tidak benar (mis. `PUSAKA.GOV`, "Arsip Nasional Indonesia", "enkripsi BLAKE2B", "immutable") dan mitra atau sumber fiktif | Dianggap menyesatkan atau memalsukan afiliasi; kredibilitas dan penilaian etika turun | Aturan kejujuran konten (SRS §9.3); pencarian placeholder dan klaim pada gerbang rilis (SRS §13.4); nilai pada UI harus nyata |
| R-12 | Header, label menu, dan indikator langkah berbeda antarhalaman pada mock (6 varian header; Arsip memakai "Bengkel/Piagam/Kurasi", halaman lain "Playground/Dampak/Kredit") | UX dan identitas tampak tidak konsisten | Satu spesifikasi header (SRS §4.5); label kanonik mengikuti nama berkas; sinkronisasi oleh router (SRS §5.4) |
| R-13 | Benang SVG yang terikat scroll memperberat render atau menyita waktu pengerjaan | Skor Teknologi dan UX turun | Batas ≈ 60 node, tanpa filter SVG; prioritas bertingkat (Beranda Must, lainnya Should/Could); `prefers-reduced-motion` dan *fallback* statis |
| R-14 | Teks kecil berwarna kuningan/abu pada latar terang kurang kontras | Aksesibilitas turun | Token `--c-brass-ink` dan `--c-ash`; label minimum 11 px; verifikasi dengan alat kontras |

---

## 12. Kriteria Keberhasilan dan Gerbang Rilis

Karya siap dikumpulkan bila **seluruh** kriteria berikut terpenuhi:

1. Semua BR berprioritas *Must* terpenuhi dan lulus acceptance criteria di PRD.
2. Audit kepatuhan aturan lomba (§9) bersih, tanpa pengecualian.
3. Lighthouse mobile: Performance ≥ 85, Accessibility ≥ 95, Best Practices ≥ 95, SEO ≥ 90.
4. Nol galat di konsol pada semua halaman dan semua viewport uji.
5. Nol *horizontal scroll* pada 320, 360, 390, 768, 1024, 1440, 1920 px.
6. Uji memori lulus: tidak ada *detached DOM node* dan jumlah *listener* kembali ke baseline setelah 20 perpindahan halaman.
7. Seluruh aset memiliki atribusi dan lisensi tercatat di `kredit.html`.
8. `README.md`, `BRD.md`, `PRD.md`, `SRS.md` konsisten.
9. Tidak ada teks placeholder atau sisa prompt (mis. "MUSEUM SPEC", `© 2024`, `[Nama Mitra]`) dan tidak ada klaim palsu; pencarian SRS §13.4 bersih.
10. Setiap angka pada UI berasal dari state nyata atau telah dihapus (BR-14).
11. Uji 5 detik: ≥ 4 dari 5 penguji dapat menyebut isi situs dan aksi utama setelah melihat layar pertama Beranda selama 5 detik.

---

## 13. Rencana Tonggak (Relatif)

> Tenggat resmi belum diberikan; jadwal dinyatakan relatif terhadap tenggat (T−minggu).

| Tonggak | Waktu | Keluaran |
|---|---|---|
| M0 Fondasi | T−6 | Design tokens (termasuk Paper, Brass Ink, Ash), struktur folder, shell, header persisten, router SPA, transisi dasar |
| M1 Beranda | T−5 | Booting Sequence, Benang (hero), Cursor Trail (desktop + sentuh) |
| M2 Arsip | T−4 | Exploded View SVG, Reverse Time-Scroll, benang sebagai lungsi |
| M3 Playground | T−3 | Grid Biner, readout (hex, kerapatan), kontrol, penyimpanan |
| M4 Dampak | T−2 | Sertifikat Digital, CTA UMKM, halaman Kredit + manifest |
| M5 Penyempurnaan dan QA | T−1 | Performa, memori, aksesibilitas, matriks perangkat, audit konten (hapus placeholder dan klaim palsu) |
| Rilis | T | Audit kepatuhan, pengumpulan |

---

## 14. Matriks Keterlacakan (BRD → PRD → SRS)

| Kebutuhan Bisnis | Epic PRD | Modul SRS |
|---|---|---|
| BR-01 | E1 Booting Sequence | `features/boot-sequence.js`, §6 |
| BR-02 | E8 Design System | `css/tokens.css`, `css/components.css`, §4 |
| BR-03 | E5 Playground | `features/weave-grid.js`, §8 |
| BR-04 | E6 Dampak | `features/certificate.js`, §9 |
| BR-05 | E3 SPA | `core/router.js`, `core/transition.js`, §5 |
| BR-06 | E7 Mobile-First, E2 Trail | §7 (sentuh), §12 (mobile-first) |
| BR-07, BR-08 | E9 Kepatuhan | §3, §13 |
| BR-09 | E2, E3 | §10 (GSAP), §11 (memori) |
| BR-10 | E9 | §12.4 |
| BR-11 | E9 | `kredit.html`, §15 |
| BR-12 | — | `README.md`, `docs/` |
| BR-13 | E10 Benang | `features/thread.js`, §10.3 |
| BR-14 | E6, E9 | §8.4, §9.3, §13.4 |
| BR-15 | E3, E8 | `core/header.js`, §4.5, §5.4 |
| BR-16 | E1, E8 | §4.4, §6 |

---

## 15. Glosarium

| Istilah | Arti |
|---|---|
| Lungsi (warp) | Benang yang terentang memanjang pada alat tenun |
| Pakan (weft) | Benang yang disisipkan melintang menembus lungsi |
| Royal Brutalism | Gaya visual perpaduan Brutalisme web dan estetika arsip kerajaan |
| SPA ilusi | Navigasi tanpa muat ulang halaman penuh, dibangun manual dengan `fetch()` dan `pushState()` |
| GC (Garbage Collection) | Pelepasan memori otomatis; dibantu dengan menghapus referensi dan node DOM |
| SRI | *Subresource Integrity*, hash untuk memverifikasi berkas CDN |
| Benang (Thread) | Lapisan SVG persisten yang berubah dari serat menjadi angka biner mengikuti scroll |
| *Pick* | Satu lemparan benang pakan; satu baris grid Playground |
| Register biner / *hex dump* | Tampilan tiap baris motif sebagai string biner dan nilai heksadesimal |
| Kerapatan | Persentase sel bernilai 1 terhadap seluruh sel grid |
| Label bracket | Label Mono kapital berformat `[ LABEL // SUBLABEL ]` |
| FNV-1a | Fungsi hash 32-bit sederhana, dipakai untuk menurunkan ID dan checksum motif |
| *Quiet luxury* | Prinsip kemewahan lewat ruang kosong, ketepatan, dan satu titik fokus |
