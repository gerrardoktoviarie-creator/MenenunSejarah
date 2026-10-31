# PRD — Product Requirements Document

> Revisi implementasi (31 Oktober 2026): pengguna mempertahankan satu `index.html` dengan lima section dan tanpa header. Rujukan lima HTML/router fetch/header di bagian lain adalah rancangan awal, bukan klaim runtime saat ini. Kontrak pengganti dan pengecualian dicatat di `CHANGES.md`; model benang terbaru mengikat pada §5.9 PRD / §10.3 SRS. Hasil QA lama bukan bukti versi baru.


## Sandi Leluhur: Mesin Biner Pertama
**Website Kompetisi Web Design TECHTOPIA Vol. 2 (Tingkat Nasional)**

| Atribut | Nilai |
|---|---|
| Versi | 1.1 (Disinkronkan dengan desain final) |
| Tanggal | 23 Oktober 2026 |
| Dokumen Induk | `BRD.md` |
| Dokumen Turunan | `SRS.md` |
| Prinsip Pengembangan | **Mobile-first**, static HTML/CSS/Vanilla JS, tanpa proses build |
| Sumber Perubahan | Hasil desain final (`MAIN.jpg`), redesign hero, Benang Sepanjang Situs, penyelarasan copy |

### Riwayat Revisi

| Versi | Tanggal | Perubahan Utama |
|---|---|---|
| 1.0 | 9 Okt 2026 | Draf awal |
| 1.1 | 23 Okt 2026 | Manifesto baru; alur Temukan → Pahami → **Tenun** → Lestarikan; US-105 dan US-106 (aturan 5 detik); Epic **E10 Benang Sepanjang Situs**; header persisten (§3.3, §5.8); readout biner baru (hex, kerapatan, koordinat); ID `SL-9A3F1B` dan nomor piagam; aturan kejujuran konten (US-607, US-907); halaman Kredit naik menjadi *Must* (§5.7); **Kamus Salin Final** (§7.1); Lampiran A: daftar selisih desain final yang perlu ditindaklanjuti |

---

## 1. Ringkasan Produk

### 1.1 Visi Produk
Mengubah alat tenun Nusantara dari "benda museum" menjadi **mesin yang bisa diprogram pengunjung**, sehingga pusaka dipahami sebagai pengetahuan yang hidup.

### 1.2 Tujuan Produk (Goals)
1. Juri memahami konsep "tenun = mesin biner" dalam 60 detik pertama, dan pesan inti serta aksi utamanya dalam **5 detik**.
2. Pengunjung menyelesaikan alur penuh: **Temukan → Pahami → Tenun → Lestarikan**.
3. Pengalaman setara di desktop dan mobile (mobile-first).
4. Kualitas kode dan perilaku teknis dapat diverifikasi juri lewat *View Source* dan DevTools.

### 1.3 Bukan Tujuan (Non-Goals)
- Bukan toko online atau platform transaksi.
- Bukan ensiklopedia tenun yang lengkap.
- Tidak ada akun pengguna atau penyimpanan di server.

### 1.4 Prinsip Produk
| Prinsip | Arti dalam praktik |
|---|---|
| **Provokatif, bukan dekoratif** | Setiap elemen visual membawa argumen (tenun = komputasi) |
| **Ekspresif di tepi, tertib di inti** | Brutalisme pada judul dan ornamen; kontrol dan teks bacaan tetap jelas |
| **Sentuh setara kursor** | Setiap interaksi hover punya padanan tap/swipe |
| **Jujur secara konten** | Analogi dinyatakan sebagai analogi; sumber dan kredit ditampilkan |
| **Bisa diperiksa** | Kode terbaca, tanpa kotak hitam |
| **Ruang adalah kemewahan** | Minimal ≈ 40% layar kosong; satu titik fokus dan satu aksi utama per layar |
| **Familiar di struktur, orisinal di ekspresi** | Navigasi dan tombol mengikuti pola umum; kreativitas ada pada tipografi, citra, dan momen "wow" |
| **Setiap angka di UI harus nyata** | Tidak ada klaim institusi, enkripsi, atau data palsu; nilai berasal dari state sebenarnya |

---

## 2. User Persona

> Persona bersifat **representatif/fiktif**, disusun dari profil juri yang disebutkan dalam brief.

### 2.1 Persona Primer: Juri

#### P1: Dr. Ayu Prameswari, M.Des. — Dosen UI/UX
| | |
|---|---|
| Usia / Konteks | 45 tahun; mengajar interaction design; menjuri puluhan karya per sesi |
| Tujuan | Menemukan karya dengan alur dan keputusan UX yang matang, bukan sekadar visual |
| Frustrasi | Animasi yang menghalangi tugas, navigasi membingungkan, state kosong dan galat yang diabaikan, aksesibilitas yang dilewati |
| Cara menilai | Mengikuti alur seperti pengguna baru; mencoba keyboard; mengubah ukuran jendela; membuka di ponsel |
| Sinyal kemenangan | Umpan balik instan di Playground, transisi halaman halus, `prefers-reduced-motion` dihormati, pesan jelas saat `localStorage` mati |

#### P2: Raka Mahendra — Praktisi Brand Identity
| | |
|---|---|
| Usia / Konteks | 38 tahun; Brand Identity Director studio kreatif |
| Tujuan | Melihat **sistem identitas** yang koheren: warna, tipografi, grid, nada suara |
| Frustrasi | Gaya "budaya = ornamen"; tipografi tidak punya sikap; palet tidak punya aturan |
| Cara menilai | Memindai tipografi dan palet; mencari konsistensi antarhalaman; menilai konsep dan manifesto |
| Sinyal kemenangan | Benturan Display Sans raksasa vs Serif elegan terasa disengaja; palet dipakai dengan aturan; manifesto kuat dan bernada konsisten |

#### P3: Dimas Wicaksono — Praktisi Full-Stack / Dosen Rekayasa Perangkat Lunak
| | |
|---|---|
| Usia / Konteks | 34 tahun; senior engineer sekaligus dosen tamu |
| Tujuan | Memverifikasi bahwa fitur nyata dibangun dengan kode asli, efisien, dan sesuai aturan |
| Frustrasi | Library tersembunyi, kode minified, kebocoran memori, `div` tanpa semantik |
| Cara menilai | *View Source*, tab Network/Performance/Memory, Lighthouse, membuka `/js` dan membaca |
| Sinyal kemenangan | Struktur `/css`, `/js`, `/assets` rapi; router `fetch()` + `pushState()` benar; jejak kursor menghapus node dari DOM; *heap* stabil |

#### Jalur Evaluasi Juri (10 Menit, Skenario Dominan)
| Menit | Aktivitas Juri | Fitur yang harus "menang" |
|---|---|---|
| 0–1 | Kesan pertama di desktop (5 detik pertama: judul, subjudul, tombol) | Booting Sequence, manifesto, aksi utama |
| 1–3 | Menggerakkan kursor, menggulir | Cursor Trail, transisi ke Ivory |
| 3–5 | Menjelajah Arsip | Exploded View, Reverse Time-Scroll |
| 5–7 | Mencoba Playground | Grid, readout biner, penyimpanan |
| 7–8 | Melihat Dampak | Sertifikat dari motif sendiri, CTA UMKM |
| 8–10 | DevTools, mode mobile, dan halaman Kredit | Kode rapi, memori stabil, responsif, alternatif sentuh, kurasi jujur |

### 2.2 Persona Sekunder: Pengunjung Umum

#### P4: Sari — Pelajar/Mahasiswa dan Calon Pendukung UMKM
| | |
|---|---|
| Konteks | 19 tahun; mengakses dari ponsel Android |
| Tujuan | Memahami tenun dengan cara baru, membuat sesuatu yang bisa dibagikan |
| Hambatan | Koneksi terbatas, layar kecil, tidak ada kursor |
| Sinyal kemenangan | Pengalaman ringan, interaksi sentuh alami, sertifikat yang layak dibagikan |

---

## 3. Struktur Informasi

### 3.1 Peta Halaman

| # | Berkas | Nama | Isi Utama | Prioritas |
|---|---|---|---|---|
| 1 | `index.html` | Beranda | Scroll 1: Booting Sequence + kolom Benang; Scroll 2: Cursor Trail | Must |
| 2 | `arsip.html` | Arsip Sandi | Exploded View alat tenun, Reverse Time-Scroll, register biner | Must |
| 3 | `playground.html` | Playground Biner | Grid tenun 12 × 12, readout biner (hex, kerapatan), panel kontrol | Must |
| 4 | `dampak.html` | Dampak (Epilog) | Sertifikat "Penjaga Pusaka", kolom aksi, CTA UMKM | Must |
| 5 | `kredit.html` | Kurasi & Kredit | Catatan kurasi, garis waktu, matriks atribusi, manifest `.json` | **Must** (naik dari Should; dasar mitigasi BRD R-01) |

Total 5 HTML (batas aturan: 10).

### 3.2 Alur Pengguna
```
Beranda (Boot) → Beranda (Trail) → Arsip → Playground → Dampak → [CTA UMKM]
                                                         ↑
                                          motif tersimpan di localStorage
```
Halaman Kredit berada di luar alur empat langkah (ia adalah halaman kurasi). Navigasi global tersedia di semua halaman dan semua viewport. Pada mobile, navigasi berupa menu layar penuh bergaya brutalis, sementara tombol aksi tetap terlihat di luar menu.

### 3.3 Sistem Header Global

Header **persisten** (tidak diganti saat navigasi SPA) dan disinkronkan router dari atribut `<body>` halaman baru (SRS §5.4).

| Elemen | Spesifikasi |
|---|---|
| Logo | `SL_` Mono dengan kursor Merah Saga berkedip; tautan ke Beranda |
| Menu kanonik | BERANDA · ARSIP · PLAYGROUND · DAMPAK · KREDIT (sama dengan nama berkas); tautan aktif bergaris bawah Merah Saga dan `aria-current="page"` |
| Indikator langkah | `1 Temukan · 2 Pahami · 3 Tenun · 4 Lestarikan`; langkah aktif Merah Saga; disembunyikan di Kredit |
| Label monograf | `MONOGRAF NO. 01–05` sesuai urutan halaman (opsional, hanya dekoratif) |
| Tombol aksi | Tombol garis `MULAI MENENUN`; disembunyikan di Playground dan Dampak |
| Nada | `void` atau `paper`, mengikuti bagian yang berada di bawah header |
| Dilarang | Ikon profil/akun, logo ganda, label menu berbeda antarhalaman |


---

## 4. Daftar Kebutuhan Fitur (Epic dan User Story)

> Prioritas: **M** = Must, **S** = Should, **C** = Could. Format kriteria: *Given / When / Then* diringkas.

### EPIC E1 — Booting Sequence (Beranda, Scroll 1)

| ID | User Story | Kriteria Penerimaan | Prio |
|---|---|---|---|
| US-101 | Sebagai juri, saya ingin melihat layar "booting" bergaya terminal agar langsung merasakan konsep komputasi | Latar Void Black. Log terminal 2–3 baris muncul bertahap, lalu manifesto **"KOMPUTER PERTAMA DITENUN, BUKAN DITULIS"** dalam Merah Saga raksasa (4 baris di desktop) disingkap per baris | M |
| US-102 | Sebagai pengguna mobile, saya ingin manifesto terbaca penuh tanpa terpotong | Pada 320 px teks tidak terpotong dan tidak memicu *horizontal scroll* (kata terpanjang "BUKAN DITULIS" muat) | M |
| US-103 | Sebagai pengguna yang tidak sabar, saya ingin bisa melewati animasi | Tautan teks "Lewati" (dan tombol `Esc`) menampilkan keadaan akhir seketika; urutan boot hanya otomatis sekali per sesi. *(Belum ada di mock.)* | S |
| US-104 | Sebagai pengguna *reduced-motion*, saya ingin manifesto tampil tanpa efek | Dengan `prefers-reduced-motion: reduce`, seluruh teks tampil statis penuh | M |
| US-105 | Sebagai juri, saya ingin memahami situs dan aksi utamanya dalam 5 detik | Pada 1440 × 900, judul, subjudul, tombol `MULAI MENENUN →`, dan baris kredibilitas terlihat tanpa scroll. Judul, subjudul, dan tombol adalah HTML nyata dan tampil penuh ≤ 3 detik; tetap tampil bila JS gagal (*failsafe*) | M |
| US-106 | Sebagai pengunjung, saya ingin satu aksi utama yang jelas | `MULAI MENENUN →` adalah satu-satunya tombol solid Merah Saga di layar pertama dan menaut ke Playground | M |

### EPIC E2 — Interactive Cursor Trail (Beranda, Scroll 2) + Alternatif Sentuh

| ID | User Story | Kriteria Penerimaan | Prio |
|---|---|---|---|
| US-201 | Sebagai juri desktop, saya ingin kursor "menenun waktu" dengan jejak kartu pusaka | Saat kursor bergerak di zona, tumpukan kartu gambar close-up (serat tenun, keris) muncul dengan jarak tertentu, lalu memudar | M |
| US-202 | Sebagai juri teknis, saya ingin jejak menghapus dirinya dari DOM | Setiap kartu dihapus dari DOM setelah animasi selesai; jumlah kartu aktif ≤ batas; tidak ada *detached nodes* | M |
| US-203 | Sebagai pengguna mobile, saya ingin padanan sentuh dari Cursor Trail | **Tap-to-Stamp**: ketuk menaruh satu kartu di titik ketukan. **Swipe-to-Weave**: seret horizontal menghasilkan jejak. Guliran vertikal tetap berfungsi | M |
| US-204 | Sebagai pengguna mobile yang belum tahu, saya ingin petunjuk yang jelas | Teks petunjuk adaptif: desktop "Gerakkan kursor", sentuh "Ketuk atau seret" | M |
| US-205 | Sebagai pengguna *reduced-motion*, saya ingin alternatif tanpa gerak | Tanpa jejak animatif; ketukan/klik menampilkan satu kartu statis yang diganti pada ketukan berikutnya | M |
| US-206 | Sebagai pengguna di ponsel lemah, saya ingin pengalaman tetap lancar | Batas kartu aktif dan ukuran kartu lebih kecil di sentuh; tidak ada *jank* terlihat | M |
| US-207 | Sebagai pengguna *screen reader*, saya tidak ingin gangguan dari elemen dekoratif | Lapisan jejak `aria-hidden="true"`, kartu tidak menangkap fokus maupun pointer | M |
| US-208 | Sebagai juri, saya ingin teks "Masa Lalu" (kiri) dan "Masa Depan" (kanan) bermakna dengan ruang kosong di tengah | Serif elegan di kiri dan kanan, masing-masing dengan keterangan Mono (`serat · pamor · benang emas` dan `kode · biner · mesin`); tengah kosong (≥ 600 px) sebagai kanvas jejak; pada mobile teks bertumpuk vertikal atau diletakkan di tepi atas/bawah | M |
| US-209 | Sebagai pengunjung, saya ingin judul bagian yang memberi tahu apa yang harus dilakukan | Judul Playfair "Gerakkan kursormu, tenun masa lalu ke masa depan." dan petunjuk Mono adaptif (desktop `GERAKKAN KURSOR DI AREA INI`, sentuh `KETUK ATAU SERET DI AREA INI`) | M |

### EPIC E3 — SPA Navigation dan Transisi

| ID | User Story | Kriteria Penerimaan | Prio |
|---|---|---|---|
| US-301 | Sebagai pengguna, saya ingin pindah halaman tanpa layar putih | Klik tautan internal: konten lama fade-out, konten baru fade-in; tidak ada kilatan putih | M |
| US-302 | Sebagai pengguna, saya ingin URL dan tombol *back/forward* tetap benar | URL berubah via `history.pushState()`; *back/forward* memuat halaman yang sesuai dengan transisi yang sama | M |
| US-303 | Sebagai juri, saya ingin halaman tetap berfungsi bila JS gagal atau dibuka lokal | Tautan berupa `<a href>` asli; pada `file://` atau galat `fetch`, perilaku jatuh ke navigasi normal | M |
| US-304 | Sebagai pengguna, saya ingin judul tab dan fokus ikut diperbarui | `document.title` berubah; fokus dipindahkan ke judul halaman baru (aksesibilitas) | M |
| US-305 | Sebagai pengguna di koneksi lambat, saya ingin tahu halaman sedang dimuat | Indikator progres tipis Merah Saga muncul bila muat > 150 ms | S |
| US-306 | Sebagai pengguna, saya ingin perpindahan terasa cepat | Prefetch saat *hover*/`touchstart`; cache sesi untuk halaman yang sudah dimuat | S |
| US-307 | Sebagai pengguna, saya ingin header selalu menunjukkan posisi saya | Setelah navigasi SPA, tautan aktif, langkah aktif, label monograf, dan nada header/footer ikut berubah tanpa header diganti | S |
| US-308 | Sebagai juri brand, saya ingin label menu yang sama di semua halaman | Menu memakai label kanonik (BERANDA, ARSIP, PLAYGROUND, DAMPAK, KREDIT) di seluruh halaman dan viewport | S |

### EPIC E4 — Arsip Sandi (Exploded View)

| ID | User Story | Kriteria Penerimaan | Prio |
|---|---|---|---|
| US-401 | Sebagai pengunjung, saya ingin melihat alat tenun "meledak" saat menggulir | Saat scroll ke bawah, bagian-bagian alat tenun (SVG) bergerak terpisah secara progresif (*scrub*) | M |
| US-402 | Sebagai pengunjung, saya ingin tahu fungsi tiap bagian dan perannya sebagai sistem biner | Tiap bagian punya label dan penjelasan singkat; penjelasan mengaitkan fungsi dengan logika 0/1 | M |
| US-403 | Sebagai pengunjung, saya ingin merasakan "perjalanan ke masa lalu" | Indikator tahun **berjalan mundur** seiring scroll (Reverse Time-Scroll), dari 2026 ke 1804 pada desain final, ditandai `≈` (perkiraan) | M |
| US-404 | Sebagai pengguna mobile, saya ingin Exploded View tetap jelas di layar sempit | Komposisi vertikal; label tidak saling menumpuk; interaksi cukup dengan scroll | M |
| US-405 | Sebagai pengguna *reduced-motion*, saya ingin informasi tanpa gerak berlebihan | Tampilan statis berurutan (tanpa pin/scrub) dengan seluruh label terbaca | M |
| US-406 | Sebagai pengunjung, saya ingin teks Arsip yang mudah dipindai | Judul `LUNGSI = 0 / 1` (berganti per bagian aktif), satu paragraf singkat, baris register biner 8-bit, tahun raksasa, keterangan tahun, dan aksi `UJI LOGIKA DI PLAYGROUND →` | M |
| US-407 | Sebagai juri akademik, saya ingin keterangan tahun yang tidak menyesatkan | Keterangan `≈ 1804` hanya merujuk kartu berlubang Jacquard; tenun gedogan tidak dikaitkan dengan tahun 1804 | M |

### EPIC E5 — Playground Biner

| ID | User Story | Kriteria Penerimaan | Prio |
|---|---|---|---|
| US-501 | Sebagai pengguna, saya ingin mengklik/mengetuk kotak untuk mengubah 0 ↔ 1 | Setiap sel berubah seketika; terlihat jelas bukan hanya lewat warna (glyph/pola) | M |
| US-502 | Sebagai pengguna, saya ingin melukis banyak sel dengan satu seretan | Seret pointer/jari melintasi sel menerapkan nilai yang sama; pada sentuh grid tidak ikut menggulir halaman | M |
| US-503 | Sebagai pengguna, saya ingin melihat representasi biner dari motif saya | Panel menampilkan tiap baris sebagai string biner, jumlah benang naik, dan nilai heks (mis. `R03 | 001100001100 | 4   0x30C`), diperbarui langsung | M |
| US-504 | Sebagai pengguna, saya ingin mengatur motif dengan cepat | Tombol: **Bersihkan**, **Balik (invert)**, **Acak** (ada di mock) dan **Cermin (mirror)**, **Preset motif** (belum dirancang; tambahkan ke desain atau turunkan ke Could) | S |
| US-505 | Sebagai pengguna, saya ingin membatalkan kesalahan | **Undo/Redo** (riwayat terbatas) | S |
| US-506 | Sebagai pengguna, saya ingin melihat motif "ditenun" | Tombol **Tenun** memutar pratinjau baris demi baris | S |
| US-507 | Sebagai pengguna, saya ingin motif otomatis tersimpan | Perubahan tersimpan ke `localStorage` (didebounce); saat kembali, motif dipulihkan | M |
| US-508 | Sebagai pengguna keyboard, saya ingin bisa memprogram grid tanpa mouse | Panah menggerakkan fokus antar-sel; Spasi/Enter mengubah nilai; fokus terlihat | M |
| US-509 | Sebagai pengguna mobile, saya ingin tata letak yang nyaman | Grid di atas, panel kontrol di bawah (sheet bawah yang mudah dijangkau ibu jari); ≥ 900 px: grid kiri, panel kanan | M |
| US-510 | Sebagai pengguna, saya ingin lanjut ke sertifikat | Tombol **"Simpan & Lihat Sertifikat"** menyimpan dan membuka halaman Dampak | M |
| US-511 | Sebagai pengguna di mode privat, saya ingin diberi tahu bila penyimpanan tidak tersedia | Banner informatif; aplikasi tetap bekerja dengan penyimpanan sementara selama sesi | S |
| US-512 | Sebagai pengguna, saya ingin ringkasan motif | Di bawah readout tampil `BENANG NAIK (1)`, `BENANG TURUN (0)`, dan `KERAPATAN` (persen, satu desimal), semuanya dihitung dari matriks | S |
| US-513 | Sebagai pengguna, saya ingin tahu posisi sel yang sedang saya tunjuk | Baris aktif disorot pada readout; `KURSOR: X:06 Y:04` mengikuti *hover* dan fokus keyboard | C |
| US-514 | Sebagai pengguna, saya ingin yakin sebelum menekan tombol utama | Di bawah `SIMPAN & LIHAT SERTIFIKAT →` tampil "Gratis · tanpa akun · motif tersimpan di perangkatmu saja" | S |

### EPIC E6 — Dampak (Epilog) dan Sertifikat

| ID | User Story | Kriteria Penerimaan | Prio |
|---|---|---|---|
| US-601 | Sebagai pengguna, saya ingin melihat motif saya menjadi Sertifikat Digital "Penjaga Pusaka" | Sertifikat merender matriks tersimpan dari `localStorage` | M |
| US-602 | Sebagai pengguna, saya ingin sertifikat terasa personal | Memuat nama (opsional, diisi pengguna), tanggal format Indonesia, **ID turunan pola** (mis. `SL-9A3F1B`, 6 heks), nomor piagam (`PUSAKA-2026-9A3F1B`), dan checksum yang dihitung nyata (FNV-1a) | M |
| US-603 | Sebagai pengguna tanpa motif, saya ingin diarahkan | State kosong menjelaskan situasi dan menautkan ke Playground; opsional menampilkan contoh motif | M |
| US-604 | Sebagai pengguna, saya ingin mendukung pengrajin UMKM nyata | Tombol CTA menuju kanal resmi mitra pengrajin; tautan dibuka aman (`rel="noopener noreferrer"`) | M |
| US-605 | Sebagai pengguna, saya ingin menyimpan atau membagikan sertifikat | Unduh sebagai gambar PNG; (opsional) tombol bagikan dengan Web Share API bila tersedia | S |
| US-606 | Sebagai juri, saya ingin desain yang menyatukan kartu pos kuno dan ID terminal | Tata letak kartu pos (bingkai, perangko, cap pos) bertemu elemen mono-terminal | M |
| US-607 | Sebagai juri, saya ingin sertifikat yang jujur | Tidak ada tulisan yang menyiratkan afiliasi pemerintah/lembaga, enkripsi, hash palsu, atau "immutable"; ada catatan "Piagam simbolis, bukan dokumen resmi"; tidak ada nama motif tradisional pada pola buatan pengguna (SRS §9.3) | M |
| US-608 | Sebagai pengguna, saya ingin ringkasan motif dan aksi lanjutan di samping kartu | Kolom aksi memuat `DUKUNG PENGRAJIN →` (satu-satunya tombol solid), `UNDUH PNG`, `BAGIKAN SERTIFIKAT`, `TENUN ULANG`, dan ringkasan nyata (ukuran matriks, jumlah naik/turun, lokasi simpan, checksum) | M |

### EPIC E7 — Mobile-First dan Responsivitas

| ID | User Story | Kriteria Penerimaan | Prio |
|---|---|---|---|
| US-701 | Sebagai pengguna ponsel, saya ingin seluruh halaman nyaman di 320–480 px | CSS basis untuk 320 px; peningkatan lewat `min-width`; nol *horizontal scroll* | M |
| US-702 | Sebagai pengguna, saya ingin target sentuh yang mudah ditekan | Navigasi/tombol utama ≥ 44×44 px; sel grid ≥ 24×24 px (batas WCAG 2.2 AA) | M |
| US-703 | Sebagai pengguna iOS/Android, saya ingin layout tidak melompat oleh bilah alamat | Hero memakai `svh/dvh` dengan *fallback* `vh`; *safe-area* dihormati | M |
| US-704 | Sebagai pengguna perangkat sentuh, saya tidak ingin interaksi bergantung pada hover | Efek hover hanya di `@media (hover: hover) and (pointer: fine)`; padanan sentuh tersedia | M |
| US-705 | Sebagai pengguna tablet/desktop lebar, saya ingin memanfaatkan ruang | Tata letak radikal Brutalis meningkat dari 900 px dan 1200 px; teks raksasa menskala via `clamp()` | M |

### EPIC E8 — Design System Royal Brutalism

| ID | User Story | Kriteria Penerimaan | Prio |
|---|---|---|---|
| US-801 | Sebagai desainer, saya ingin token desain konsisten | Warna (termasuk `--c-paper`, `--c-brass-ink`, `--c-ash`), tipografi, spasi (skala 8 px), tebal garis di `css/tokens.css` (CSS custom properties) | M |
| US-802 | Sebagai juri brand, saya ingin aturan penggunaan warna dipatuhi | Penggunaan sesuai matriks kontras BRD §6.3 (mis. teks Abu hanya di latar Void) | M |
| US-803 | Sebagai juri brand, saya ingin tipografi sebagai arsitektur | Judul raksasa membentuk ruang (mengisi lebar layar, memotong grid, ditumpuk); Serif untuk narasi arsip; Mono untuk data | M |
| US-804 | Sebagai pengguna, saya ingin kontrol yang konsisten | Komponen (tombol, sel, label, kartu) berbagi gaya garis tebal 3–4 px, sudut tajam, fokus jelas | M |
| US-805 | Sebagai juri brand, saya ingin kosakata visual yang konsisten | Label bracket, siku kuningan, ❖, dan hairline kuningan dipakai sama di semua halaman; ornamen tidak melebihi anggaran (satu segel per layar; tanpa pola latar atau bingkai ganda) | M |
| US-806 | Sebagai pengunjung, saya ingin layar yang lega dan terfokus | Margin sisi 120 px (desktop) / 24 px (mobile); ≈ 40% area kosong pada layar hero dan narasi; satu tombol solid Merah Saga per layar | M |

### EPIC E9 — Aksesibilitas, Kualitas, dan Kepatuhan

| ID | User Story | Kriteria Penerimaan | Prio |
|---|---|---|---|
| US-901 | Sebagai pengguna keyboard/*screen reader*, saya ingin semua fungsi inti dapat dioperasikan | Landmark semantik (`header/nav/main/footer`), *skip link*, fokus terlihat, urutan tab logis | M |
| US-902 | Sebagai pengguna sensitif gerak, saya ingin preferensi dihormati | `prefers-reduced-motion` menonaktifkan efek utama dengan padanan statis | M |
| US-903 | Sebagai juri, saya ingin konten tetap terbaca bila CDN/JS gagal | Konten inti berupa HTML nyata; kelas `no-gsap` mengaktifkan transisi CSS dasar | M |
| US-904 | Sebagai panitia, saya ingin kepatuhan aturan dapat diaudit | Daftar periksa kepatuhan di README; tidak ada artefak terlarang | M |
| US-905 | Sebagai juri, saya ingin halaman Kredit yang jujur | `kredit.html` menjelaskan analogi tenun-biner (mengutip manifesto aktif), menyebut sumber, dan mencantumkan atribusi aset | **M** |
| US-906 | Sebagai juri, saya ingin dapat memeriksa sumber dengan mudah | Halaman Kredit memuat garis waktu 4 penanda dengan sumber, matriks atribusi (aset, sumber, lisensi), dan tombol unduh `credits.json` yang identik dengan tabel | S |
| US-907 | Sebagai juri, saya ingin yakin tidak ada klaim palsu | Tidak ada placeholder atau sisa prompt (mis. "MUSEUM SPEC", `© 2024`, `[Nama Mitra]`), tidak ada afiliasi/enkripsi/verifikasi palsu; setiap angka di UI nyata; pencarian SRS §13.4 bersih | M |


### EPIC E10 — Benang Sepanjang Situs

| ID | User Story | Kriteria Penerimaan | Prio |
|---|---|---|---|
| US-1001 | Sebagai juri, saya ingin melihat benang yang berubah menjadi angka biner saat menggulir | Di kolom kanan hero: serat berpilin (merah dan kuningan) di atas, simpul kuningan, angka biner di bawah; titik transformasi naik dari 0,85 pada awal situs sampai 0 di dasar Kredit mengikuti siteProgress (§5.9) | M |
| US-1002 | Sebagai pengunjung, saya ingin benang yang menyambung antarhalaman | `#thread-layer` berada di luar `<main>` dan tidak diganti saat navigasi SPA; batas progres lima section menyambung; lompatan nonberurutan/back-forward diperhalus 600 ms | M |
| US-1003 | Sebagai pengunjung, saya ingin benang berperan di tiap halaman | Persediaan serat berkurang di lima section; dasar Kredit tidak menyisakan serat/simpul, hanya angka biner dan `SELESAI DITENUN`; gulir naik mengembalikan serat | S |
| US-1004 | Sebagai pengguna, saya ingin benang memakai motifku | Bila motif tersimpan, angka biner pada benang memakai bit motif tersebut; bila tidak, pola bawaan | S |
| US-1005 | Sebagai pengguna sensitif gerak atau berponsel lemah, saya ingin benang tidak mengganggu | `prefers-reduced-motion`: keadaan statis; `aria-hidden`; mobile ≤ 24 angka dan lebar ≈ 40 px; tidak menunda render judul; *fallback* statis bila GSAP gagal | M |
| US-1006 | Sebagai pengguna Playground, saya ingin teropong mengikuti baris yang aktif | Simpul benang berpindah ke baris yang sedang diedit atau ditenun | C |

---

## 5. Spesifikasi UX Fitur Utama

### 5.1 Cursor Trail ("Menenun Waktu")

**Tujuan.** Memberikan momen interaktif pertama yang membuat konsep "menenun waktu" dapat dirasakan: kursor/jari adalah *shuttle* yang menenun masa lalu ke masa depan.

**Tata letak zona.**
- Latar Ivory, tinggi minimal `100svh`, hairline kuningan di tepi atas.
- Judul Playfair di tengah atas: "Gerakkan kursormu, tenun masa lalu ke masa depan." dengan petunjuk Mono di bawahnya.
- Desktop (≥ 900 px): "Masa Lalu" (Serif italic, kiri) dan "Masa Depan" (Serif, kanan), masing-masing dengan keterangan Mono; ruang kosong ≥ 600 px di tengah.
- Mobile (< 900 px): "Masa Lalu" di bagian atas, "Masa Depan" di bagian bawah, ruang kosong di tengah sebagai kanvas.
- Strip bawah (Mono kecil): `SANDI LELUHUR // EDISI ARSIP PRESERVASI` (kiri) dan `KODIFIKASI BINER NUSANTARA` (kanan). Teks `1440 × 900 MUSEUM SPEC` pada mock adalah sisa prompt dan **dihapus**.

**Perilaku per jenis input.**

| Aspek | Desktop (mouse/pen) | Mobile (sentuh) |
|---|---|---|
| Pemicu utama | Gerak kursor (`pointermove`) | **Swipe-to-Weave**: seret jari |
| Pemicu sekunder | Klik menaruh satu kartu | **Tap-to-Stamp**: ketuk menaruh satu kartu |
| Jarak antar-kartu (*threshold*) | ≈ 80 px | ≈ 56 px |
| Kartu aktif maksimum | 12 | 8 |
| Ukuran kartu | ≈ 180 × 240 px | ≈ 120 × 160 px |
| Guliran halaman | Normal | Vertikal tetap berjalan (`touch-action: pan-y`); seret horizontal memicu jejak |
| Petunjuk | `GERAKKAN KURSOR DI AREA INI` (di bawah judul) | `KETUK ATAU SERET DI AREA INI` |
| Idle | Petunjuk berdenyut halus | Petunjuk berdenyut; (Could) jejak otomatis demonstratif setelah beberapa detik diam |

**Siklus hidup kartu.**
1. **Muncul** (≈ 0,25 dtk): *scale* 0,6 → 1, `opacity` 0 → 1, rotasi acak ±7°.
2. **Tahan** (≈ 0,45 dtk).
3. **Memudar** (≈ 0,7 dtk): `opacity` → 0.
4. **Dihapus dari DOM** saat selesai (*garbage collection*).

Kartu baru selalu di atas kartu lama (`z-index` bertambah), menciptakan kesan **tumpukan kartu**. Kartu tidak pernah menerima klik, fokus, maupun mengganggu teks.

**Konten kartu.** 8–12 foto close-up pusaka (serat tenun, benang emas songket, pamor keris, ukiran kayu, dll.) berukuran kecil (lihat §7).

**State dan kondisi tepi.**
| Kondisi | Perilaku |
|---|---|
| `prefers-reduced-motion` | Tanpa jejak animatif; ketukan/klik menampilkan satu kartu statis yang diganti pada interaksi berikutnya |
| Gambar gagal dimuat | Kartu dilewati; tidak ada ikon rusak |
| GSAP gagal dimuat | *Fallback* CSS: kartu muncul dan hilang dengan transisi `opacity` dasar |
| Tab tidak aktif | Tidak ada kartu baru; animasi tidak menumpuk |
| Berpindah halaman | Semua kartu dan listener dibersihkan (lihat SRS §11) |

**Metrik penerimaan.** 60 fps pada gerakan normal di desktop menengah; tidak ada *long task* > 50 ms akibat jejak; jumlah node jejak tidak pernah melampaui batas.

### 5.2 Transisi SPA (Tanpa White Flash)

**Tujuan.** Perpindahan antarhalaman terasa seperti satu pengalaman berkesinambungan.

**Urutan.**
1. Klik tautan internal → intersepsi → mulai *fade-out* (≈ 280 ms) paralel dengan `fetch()`.
2. Setelah keduanya selesai: ganti isi `<main>`, perbarui judul, `pushState`.
3. Inisialisasi halaman baru → *fade-in* (≈ 420 ms), disertai pergeseran `y` kecil (≈ 12–16 px).
4. Pindahkan fokus ke judul halaman; gulir ke atas.

**Aturan anti-white-flash.**
- `html` dan `body` berlatar **Void Black**, sehingga fade melewati hitam (efek "tirai" yang selaras), bukan putih.
- Header, benang, dan footer bersifat persisten; hanya `<main>` yang diganti. Status header (tautan aktif, langkah, label monograf, nada) disinkronkan dari atribut `<body>` halaman baru (§3.3, SRS §5.4).
- Semua CSS dimuat di setiap halaman sejak awal sehingga tidak ada kilatan gaya yang belum dimuat (FOUC).
- Tinggi minimum `<main>` dijaga untuk mencegah *layout shift*.

**State.**
| Kondisi | Perilaku |
|---|---|
| Muat > 150 ms | Garis progres Merah Saga di tepi atas |
| `fetch()` gagal | Jatuh ke navigasi normal (`location.assign`) |
| Klik berturut-turut | Navigasi terakhir menang (pembatalan otomatis) |
| *Back/forward* | Memakai transisi yang sama; posisi gulir direset ke atas |
| `file://` | Router nonaktif; tautan berjalan normal |
| `prefers-reduced-motion` | Pergantian cepat tanpa pergeseran; fade minimal |

### 5.3 Playground Biner

**Tujuan.** Mengubah pemahaman menjadi pengalaman: pengguna memprogram motif kain dengan logika 0/1.

**Model mental.** Satu baris grid adalah satu *pick* tenun. Sel `1` = benang lungsi **naik**; sel `0` = benang lungsi **turun**. Urutan baris adalah program yang menghasilkan motif.

**Tata letak.**

| Viewport | Tata letak |
|---|---|
| Mobile (< 900 px) | Judul ringkas → **grid** (lebar penuh, persegi) → **panel kontrol** di bawah (tombol besar, mudah dijangkau ibu jari) → readout biner |
| ≥ 900 px | **Kiri**: kanvas grid; **kanan**: panel kontrol dan readout (garis pemisah tipis) |

**Grid.**
- Default 12 × 12 ("MATRIKS 144-BIT"). Pilihan ukuran 8 / 12 / 16 bersifat opsional (Could); mock hanya memuat 12 × 12.
- Penggaris kolom `01`–`12` di atas grid dan label baris `01`–`12` di kiri; bingkai siku kuningan.
- Sel ber-glyph `0` / `1` (mono) untuk mendukung bukan-hanya-warna; sel aktif berlatar Merah Saga dengan glyph Ivory, sel mati berlatar Ivory/Void dengan glyph Concrete (hanya di latar gelap).
- Ukuran sel minimum 24 px.

**Interaksi.**

| Input | Perilaku |
|---|---|
| Klik/ketuk | Ubah satu sel |
| Seret | Lukis banyak sel dengan nilai sama dengan sel pertama yang disentuh (ketuk pertama pada `0` → melukis `1`) |
| Keyboard | Panah = pindah fokus; Spasi/Enter = ubah sel; `Ctrl/Cmd+Z` = Undo |
| Sentuh | Grid memakai `touch-action: none` agar seretan melukis, bukan menggulir; area di luar grid tetap menggulir |

**Panel kontrol (urutan prioritas).**
1. **Tenun** (pratinjau baris demi baris) — S
2. **Bersihkan**, **Balik**, **Acak** — S (ada di mock); **Cermin** — S (belum ada di mock)
3. **Preset motif** (3–4 motif geometris tradisional; nama divalidasi kurator) — C
4. **Undo/Redo** — S
5. **Nama Penjaga** (opsional, untuk sertifikat) — M
6. **Simpan & Lihat Sertifikat** (CTA utama, Merah Saga, label `[ SIMPAN & LIHAT SERTIFIKAT → ]`) dengan baris kepercayaan di bawahnya — M

**Readout biner (gaya terminal).** Dua kolom per baris:

```
R03 | 001100001100 | 4                0x30C
```

- Kiri: label baris, string biner, jumlah benang naik. Kanan: nilai heks baris (`HEX DUMP`).
- Baris yang terakhir diedit atau difokus **disorot** (garis kuningan di sisi kiri, teks tebal).
- Ringkasan di bawahnya: `BENANG NAIK (1): 72` · `BENANG TURUN (0): 72` · `KERAPATAN: 50.0%`.
- `KURSOR: X:06 Y:04` pada kepala kanvas mengikuti *hover* dan fokus keyboard.
- Semua nilai dihitung dari matriks, diperbarui seketika, tanpa render ulang penuh.

**State.**
| Kondisi | Perilaku |
|---|---|
| Pertama kali / kosong | Grid kosong + petunjuk "0 = benang turun, 1 = benang naik" |
| Kembali berkunjung | Motif dipulihkan dari `localStorage` |
| `localStorage` tidak tersedia | Banner informatif; sesi tetap berfungsi; tombol sertifikat tetap menyimpan sementara |
| Data tersimpan rusak | Diabaikan; mulai kosong tanpa galat |

**Metrik penerimaan.** Latensi klik→visual tidak terasa (< 100 ms); nol render ulang penuh saat sel berubah; seluruh fungsi bisa dilakukan hanya dengan keyboard.

### 5.4 Booting Sequence (Beranda, Scroll 1)

**Tujuan.** Dalam 5 detik, pengunjung tahu *apa* ini, *mengapa menarik*, dan *apa yang harus dilakukan*.

**Susunan (desktop 1440 × 900, semua dalam satu layar).**

| Urutan | Elemen | Isi |
|---|---|---|
| 1 | Log terminal | `> memuat sandi_leluhur.bin` / `> status: siap_` + kursor berkedip |
| 2 | **Judul** (Anton, Merah Saga, 4 baris) | KOMPUTER / PERTAMA / DITENUN, / BUKAN DITULIS |
| 3 | **Subjudul** (Playfair italic, Ivory) | "Naik atau turun. Satu atau nol. Pada helai lungsi, leluhur kita menyimpan sebuah bahasa, jauh sebelum ada layar." (jarak 48 px dari judul) |
| 4 | **Aksi utama** | Tombol Merah Saga `MULAI MENENUN →` (jarak 56 px dari subjudul) |
| 5 | Kepercayaan (opsional) | "Tanpa akun · tanpa unduhan · motifmu tinggal di perangkatmu" |
| 6 | Kredibilitas | `TECHTOPIA VOL. 2 · PUSAKA  |  Kartu berlubang Jacquard, ≈ 1804` |
| 7 | Petunjuk gulir | `GULIR ↓` |
| — | Kolom kanan (≈ 22–32% lebar) | **Benang** (§5.9). Pada mock masih panel gelap kosong |

**Perilaku.**
- Judul, subjudul, dan tombol adalah **HTML nyata**; efek hanya menyingkapnya. Judul disingkap **per baris** (bukan ketik per karakter), seluruhnya tuntas ≤ 3 detik. Efek ketik hanya untuk log terminal.
- Tombol "Lewati" (tautan teks kecil) dan `Esc` menampilkan keadaan akhir. Sekali per sesi (`sessionStorage`).
- Transisi ke Scroll 2 (Ivory): potongan keras dengan hairline kuningan; nada header berganti dari `void` ke `paper`.
- Tanpa JS atau saat `prefers-reduced-motion`: seluruh teks tampil statis.

### 5.5 Arsip Sandi (Exploded View + Reverse Time-Scroll)

**Susunan (desktop).** Latar Paper, dua kolom (≈ 60% / 40%).
- **Kiri:** ilustrasi alat tenun terurai (garis tipis) di dalam bingkai siku kuningan dengan empat label: `PENGGULUNG LUNGSI`, `SISIR (REED)`, `LUNGSI (WARP)` (garis Merah Saga), `GULUNGAN KAIN`.
- **Kanan, berurutan:** judul `LUNGSI = 0 / 1` (Anton, Merah Saga) → paragraf (2–3 kalimat) → baris Mono `REGISTER BINER // [ 1 0 1 1 0 0 1 0 ] · 8-BIT PER BARIS WEFT` → tahun raksasa `1804` → keterangan `≈ 1804 · KARTU BERLUBANG JACQUARD` → aksi `UJI LOGIKA DI PLAYGROUND →`.

**Perilaku.**
- Bagian sticky (*pinned*): SVG terurai saat scroll (`scrub`). Empat bagian (penggulung lungsi, sisir, lungsi, gulungan kain) aktif bergantian; judul dan paragraf kanan mengikuti bagian aktif, dengan padanan biner.
- Penghitung tahun berjalan **mundur** dari 2026 ke 1804 dan ditandai "perkiraan". Penanda yang lebih dalam hanya bila ditetapkan kurator (Q-04).
- Mobile: komposisi vertikal (ilustrasi di atas, teks di bawah).
- `prefers-reduced-motion`: tampilan statis berurutan.
- **Koreksi pada mock:** keterangan "… JACQUARD & MESIN TENUN GEDOGAN" dipisah; gedogan tidak berasal dari tahun 1804 (US-407).

### 5.6 Dampak (Sertifikat)

**Susunan (desktop).** Latar Paper. Strip katalog → header → status strip (nilai nyata) → eyebrow `[ EPILOG // PIAGAM PENJAGA PUSAKA ] :: [ NO. PUSAKA-2026-9A3F1B ]` → dua kolom: **kartu** (≈ 2/3) dan **kolom aksi** (≈ 1/3) → footer.

**Kartu.** Kartu pos kuno bertemu terminal: bingkai 4 px Void, bayangan keras, satu segel kuningan.
- Judul `PENJAGA PUSAKA` (Anton), kutipan "Dengan ini menenun masa lalu ke masa depan."
- Perangko berisi matriks motif pengguna (piksel Merah Saga/putih) dan cap pos bertanggal (mis. `9 OKT 2026`).
- Blok terminal (Void): `NAMA PENJAGA`, `ID MOTIF` (`SL-9A3F1B`), tiga baris biner pertama, `CHECKSUM (FNV-1A)`.
- Kaki: segel `SL 2026`, `SANDI LELUHUR · TECHTOPIA VOL. 2`, dan catatan "Piagam simbolis, bukan dokumen resmi."

**Kolom aksi (urutan perhatian).**
1. `DUKUNG PENGRAJIN →` (Merah Saga, satu-satunya tombol solid) + baris mitra nyata.
2. `UNDUH PNG`, `BAGIKAN SERTIFIKAT`, `TENUN ULANG (PLAYGROUND)` sebagai tombol garis.
3. Ringkasan nyata: `MOTIF: 12 × 12 · 72 NAIK · 72 TURUN`, `TERSIMPAN: DI PERANGKAT INI`, `CHECKSUM 0x9A3F1B`.

**Aturan kejujuran.** Tidak ada `PUSAKA.GOV`, "Otoritas Sertifikasi", "Direktorat", "Arsip Nasional Indonesia", "enkripsi", "SHA-256", "immutable", atau nama motif tradisional pada pola buatan pengguna (SRS §9.3).

**State.**
| Kondisi | Perilaku |
|---|---|
| Ada motif valid | Sertifikat dirender |
| Tidak ada motif/data rusak | State kosong: judul `PIAGAMMU MENUNGGU MOTIF PERTAMAMU`, kalimat "Tenun satu motif dalam 0 dan 1, dan piagam Penjaga Pusaka langsung jadi.", tombol `MULAI MENENUN →` *(mock belum ada)* |
| Ekspor PNG gagal | Pesan jelas; dapat dicoba ulang |
| Mitra belum diisi | **Gerbang rilis gagal** |

### 5.7 Kurasi & Kredit

**Tujuan.** Halaman bukti: klaim dibingkai jujur, sumber dapat diperiksa.

**Susunan (desktop).** Hero (`KURASI & KREDIT`, garis `ONTOLOGI TENUN & KOMPUTASI`, kartu `INDEX STATUS` berisi hitungan nyata) → dua kolom:
- **Utama (≈ 60%):** Seksi 01 *Catatan Kurasi: Nalar Analogi & Batas Historis* (analogi dan provokasi kuratorial, bukan klaim keutamaan kronologis; kutip manifesto aktif; Jacquard 1804 sebagai tonggak kartu berlubang; kotak penegasan) → Seksi 03 *Matriks Atribusi Arsip* (aset, sumber, lisensi; lima baris atau lebih; tombol `UNDUH MANIFEST (.JSON)`).
- **Samping (≈ 35%):** Seksi 02 *Kontinuum Nalar Biner*: empat penanda (≈ abad ke-8, 1804, 1843, 2026), masing-masing dengan judul, satu ringkasan, dan sumber.
- Footer gelap: panel telemetri **bernilai nyata** (berkas HTML: 5; pustaka pihak ketiga: 2; proses build: tidak ada).

**Aturan.** Tahun bertanda `≈` bila perkiraan; klaim "abad ke-8 / relief Candi Borobudur" hanya dengan sumber; kata "terdesentralisasi" tidak dipakai; sumber placeholder diganti data nyata; teks bacaan hitam di atas Paper.

### 5.8 Header Global dan Indikator Langkah
Lihat §3.3. Perilaku: header persisten; nada `void`/`paper` berganti mengikuti bagian di bawahnya (IntersectionObserver); pada mobile tombol `MULAI MENENUN` tetap terlihat di luar menu hamburger; tidak ada ikon akun.

### 5.9 Benang Sepanjang Situs

Benang adalah persediaan yang dipakai sampai tuntas: serat merah/kuningan di atas simpul berubah menjadi angka motif pengunjung di bawahnya. Lapisan persisten di luar `<main>`; tidak menimpa teks atau tombol.

Implementasi yang disetujui tetap satu HTML dengan lima section: Beranda, Arsip, Playground, Dampak, Kredit. `siteProgress = (indeksSection + progresGulirSection)/5`; `seratTersisa = 1-siteProgress`. Progres lokal bergerak dari awal section ke awal section berikutnya; akhir Kredit adalah dasar dokumen termasuk footer. Detail pengukuran/pin ada di SRS §10.3.

Simpul mulai di 85% tinggi layar, lalu naik monoton sampai 0%. Batas antar-section menyambung; lompatan nonberurutan/back-forward diperhalus 600 ms. Saat sisa <=4%, serat ditarik habis dan simpul menghilang maksimal300 ms; hanya angka dan `SELESAI DITENUN` yang tersisa. Label hilang lagi ketika sisa >8%. Seluruhnya reversibel.

Jika dokumen akhir tidak dapat digulir, penyelesaian dimulai 1,5 detik setelah konten siap. Reduced-motion menampilkan posisi statis tanpa tween, termasuk keadaan habis di dasar Kredit. Tanpa JS/GSAP, lapisan disembunyikan. Tetap56 digit desktop/24 mobile, sekitar60 node SVG, aria-hidden, pointer-events:none, bit motif nyata atau pola bawaan. Lebar dan desain konten dipertahankan.

---

## 6. Kebutuhan Non-Fungsional Produk

| Aspek | Target |
|---|---|
| Performa (mobile, Lighthouse simulasi) | Performance ≥ 85; LCP ≤ 2,5 dtk; CLS ≤ 0,1; INP baik |
| Berat halaman | Target ≤ 1,5 MB per halaman pada pemuatan awal; gambar kartu ≤ 60 KB masing-masing |
| Aksesibilitas | Accessibility ≥ 95; WCAG 2.2 AA untuk fungsi inti |
| Responsif | 320–1920 px tanpa *horizontal scroll* |
| Peramban | Dua versi terakhir Chrome, Edge, Firefox, Safari (desktop + mobile) |
| Ketahanan | Tetap terbaca tanpa JS/CDN; `localStorage` opsional |
| Keterbacaan kode | Tanpa minify; komentar; struktur folder jelas |
| Benang | ≥ 55 fps pada desktop menengah; ≤ 60 node SVG; tidak menunda render judul |
| Kontras teks informatif | ≥ 4,5 : 1 (gunakan Brass Ink dan Ash di latar terang) |
| Kejujuran konten | Nol klaim palsu dan nol placeholder pada rilis |

---

## 7. Kebutuhan Konten dan Aset

| Aset | Spesifikasi | Sumber / Lisensi |
|---|---|---|
| Foto close-up pusaka (8–12) | Format WebP/AVIF/JPEG, lebar ≈ 400 px, ≤ 60 KB; rasio konsisten | Foto sendiri atau CC0/CC BY (kredit wajib di `kredit.html`) |
| SVG alat tenun terurai | Dibuat sebagai grup SVG terpisah per komponen, `viewBox` jelas | Karya orisinal tim |
| Font | `woff2`, subset Latin, self-host | SIL OFL (verifikasi akhir) |
| Teks narasi | Bahasa Indonesia; istilah teknis tenun divalidasi | Kurasi tim/narasumber |
| Ikon | SVG inline sederhana | Karya sendiri |
| CTA UMKM | Nama mitra dan URL resmi nyata | **Disediakan tim** (tidak dikarang di dokumen ini) |
| Penanda tahun Reverse Time-Scroll | Daftar tonggak beserta penjelasan | Kurasi (tandai sebagai "perkiraan") |

**Panduan nada.** Tegas, ringkas, bernada manifesto (Brutalis), diselingi narasi hangat dan formal (Royal). Hindari klaim absolut tanpa dasar; headline boleh provokatif, isi harus akurat.


### 7.1 Kamus Salin Final

Sumber kebenaran teks antarmuka. Kolom **Catatan** menandai bagian yang dikoreksi terhadap mock.

**Global**

| Elemen | Teks |
|---|---|
| Menu | BERANDA · ARSIP · PLAYGROUND · DAMPAK · KREDIT |
| Langkah | 1 Temukan · 2 Pahami · 3 Tenun · 4 Lestarikan |
| Tombol header | MULAI MENENUN |
| Skip link | Lewati ke konten |

**Beranda: Booting Sequence**

| Elemen | Teks | Catatan |
|---|---|---|
| Log | `> memuat sandi_leluhur.bin` / `> status: siap_` | Sesuai mock |
| Judul | KOMPUTER PERTAMA DITENUN, BUKAN DITULIS | Sesuai mock |
| Subjudul | Naik atau turun. Satu atau nol. Pada helai lungsi, leluhur kita menyimpan sebuah bahasa, jauh sebelum ada layar. | Sesuai mock |
| Tombol | MULAI MENENUN → | Sesuai mock |
| Kepercayaan | Tanpa akun · tanpa unduhan · motifmu tinggal di perangkatmu | Belum ada di mock |
| Kredibilitas | TECHTOPIA VOL. 2 · PUSAKA \| Kartu berlubang Jacquard, ≈ 1804 | Di mock terpotong ("TECHTOPIA VOL. 2 · \|") |
| Gulir | GULIR ↓ | Sesuai mock |

**Beranda: Menenun Waktu**

| Elemen | Teks | Catatan |
|---|---|---|
| Judul | Gerakkan kursormu, tenun masa lalu ke masa depan. | Sesuai mock |
| Petunjuk | GERAKKAN KURSOR DI AREA INI | Sesuai mock |
| Kiri / kanan | Masa Lalu — serat · pamor · benang emas / Masa Depan — kode · biner · mesin | Sesuai mock |
| Strip bawah | SANDI LELUHUR // EDISI ARSIP PRESERVASI · KODIFIKASI BINER NUSANTARA | `1440 × 900 MUSEUM SPEC` dihapus |

**Arsip**

| Elemen | Teks | Catatan |
|---|---|---|
| Judul | LUNGSI = 0 / 1 | Sesuai mock |
| Paragraf | Benang lungsi yang terangkat membentuk logika biner murni: status '1' saat terangkat dan '0' saat diturunkan. Dari selang-seling inilah barisan tenun dieksekusi baris demi baris layaknya *punched card* sebelum era komputasi modern. | Perbaikan kecil ("baris demi baris") |
| Register | REGISTER BINER // [ 1 0 1 1 0 0 1 0 ] · 8-BIT PER BARIS WEFT | Sesuai mock |
| Tahun | 1804 — ≈ 1804 · KARTU BERLUBANG JACQUARD | Frasa "& mesin tenun gedogan" dihapus |
| Aksi | UJI LOGIKA DI PLAYGROUND → | Sesuai mock |

**Playground**

| Elemen | Teks | Catatan |
|---|---|---|
| Judul | PROGRAM MOTIFMU | Sesuai mock |
| Subjudul | 0 = benang turun (pakan terbenam), 1 = benang naik (lungsi timbul) — rekonstruksi geometri songket biner. | Sesuai mock |
| Pengantar panel | Koleksi rekaman biner Nusantara. Pola dasar: belah ketupat 12-bit dengan serat emas timbul. | "kodifikologi" dan "Intan Belah Ketupat" disederhanakan: istilah kodikologi tidak tepat, dan nama motif belum divalidasi |
| Contoh nama | Contoh: Dewi Lestari | Mock: "Raden Mas Joko // Penenun Kodikologi" |
| Tombol utama | [ SIMPAN & LIHAT SERTIFIKAT → ] | Sesuai mock |
| Kepercayaan | Gratis · tanpa akun · motif tersimpan di perangkatmu saja | Sesuai mock |

**Dampak**

| Elemen | Teks | Catatan |
|---|---|---|
| Eyebrow | [ EPILOG // PIAGAM PENJAGA PUSAKA ] :: [ NO. PUSAKA-2026-9A3F1B ] | Mock: "KONTRAK PRESERVASI BUDAYA", "SERTIFIKAT DIGITAL" |
| Kartu, kepala | KODEKS PRESERVASI NUSANTARA · LEMBAR PIAGAM DIGITAL | Mock: "KONTRAK RESMI LEMBAR SAH" |
| Kartu, nomor | NO. PIAGAM: PUSAKA-2026-9A3F1B // STATUS: DIBUAT UNTUKMU | Mock: "RESMI TEROTENTIKASI" |
| Kartu, asal | ASAL INSPIRASI: [diisi dari mitra nyata] | Mock: "LOKASI FISIK: TUBAN / SILUNGKANG" |
| Kartu, kode | KODE MOTIF: 0x9A3F1B // SANDI LELUHUR | Mock: "… // PUSAKA.GOV" |
| Terminal | TERMINAL REKAMAN // NODE: PERANGKAT-INI; NAMA PENJAGA; ID MOTIF; MOTIF BINER; CHECKSUM (FNV-1A) | Mock: enkripsi BLAKE2B, "SHA-256", nama motif |
| Kaki | SANDI LELUHUR · TECHTOPIA VOL. 2 · Dirancang oleh [Nama Tim] · Piagam simbolis, bukan dokumen resmi. | Mock: "Kodeks Nasional", "Direktorat", "Otoritas Sertifikasi Tingkat I" |
| Aksi | DUKUNG PENGRAJIN → · UNDUH PNG · BAGIKAN SERTIFIKAT · TENUN ULANG (PLAYGROUND) | Sesuai mock |
| Ringkasan | MOTIF: 12 × 12 · 72 NAIK · 72 TURUN; TERSIMPAN: DI PERANGKAT INI | Mock: "KONSENSUS ARSIP… TERPERMANENKAN (IMMUTABLE)" |
| State kosong | PIAGAMMU MENUNGGU MOTIF PERTAMAMU · Tenun satu motif dalam 0 dan 1, dan piagam Penjaga Pusaka langsung jadi. · MULAI MENENUN → | Belum ada di mock |

**Kredit**

| Elemen | Teks | Catatan |
|---|---|---|
| Judul | KURASI & KREDIT | Sesuai mock |
| Seksi 01 | Catatan Kurasi: Nalar Analogi & Batas Historis | Kutipan pembuka diganti dengan manifesto aktif |
| Seksi 02 | Kontinuum Nalar Biner | Penanda abad ke-8 menunggu sumber |
| Seksi 03 | Matriks Atribusi Arsip + UNDUH MANIFEST (.JSON) | Sumber placeholder diganti data nyata |
| Footer | © 2026 SANDI LELUHUR: MESIN BINER PERTAMA · TECHTOPIA VOL. 2 | Mock: `© 2024`, "ARSIP NASIONAL INDONESIA", "ENKRIPSI FISIK AKTIF" |

### 7.2 Placeholder yang Harus Diganti Sebelum Rilis

| Placeholder | Pengganti |
|---|---|
| `[Nama Mitra Pengrajin], [Daerah]` dan URL CTA | Mitra nyata (Q-03) |
| `[Nama Tim]` | Nama tim |
| Sumber aset pada matriks atribusi | Sumber dan lisensi nyata |
| `ASAL INSPIRASI` pada kartu | Diisi dari mitra nyata, atau dihapus |
| SRI GSAP | Hash resmi dari CDN |

---

## 8. Metrik Keberhasilan Produk

| Metrik | Cara Ukur | Target |
|---|---|---|
| Penyelesaian alur Playground → Sertifikat | Uji pengguna internal (5–8 orang) tanpa panduan | ≥ 80% berhasil |
| Uji 5 detik | 5 penguji melihat layar pertama Beranda 5 detik, lalu menyebut isi situs dan aksi utama | ≥ 4 dari 5 benar |
| Konsistensi header | Periksa label menu, langkah, dan logo di 5 halaman | 100% identik |
| Skor Lighthouse mobile | Lighthouse | Perf ≥ 85, A11y ≥ 95, BP ≥ 95, SEO ≥ 90 |
| Stabilitas memori | DevTools Performance Monitor, Heap Snapshot | Tidak ada *detached nodes*; heap stabil setelah 5 menit gerak kursor |
| Konsistensi *listener* | Jumlah event listener setelah 20 perpindahan halaman | Kembali ke baseline |
| Responsivitas | Uji matriks perangkat | Nol cacat tata letak, nol *horizontal scroll* |
| Kejujuran konten | Pencarian placeholder dan klaim (SRS §13.4) | Nol temuan |
| Kinerja benang | DevTools Performance, 30 detik scroll | ≥ 55 fps, tanpa *long task* > 50 ms |
| Kepatuhan aturan | Audit berkas | 100% |

---

## 9. Rilis dan Prioritas (MoSCoW)

| Kategori | Cakupan |
|---|---|
| **Must** | E1 (US-101, 102, 104–106), E2 (US-201–209), E3 (US-301–304), E4 (US-401–407), E5 (US-501–503, 507–510), E6 (US-601–604, 606–608), E7, E8, E9 (US-901–905, 907), E10 (US-1001, 1002, 1005) |
| **Should** | US-103, US-305–308, US-504–506, US-511, US-512, US-514, US-605, US-906, US-1003, US-1004 |
| **Could** | US-513, US-1006, jejak otomatis demonstratif saat idle, preset motif tambahan, pilihan ukuran grid 8/16, Web Share API, efek *wipe* peralihan Boot → Trail |
| **Won't (kali ini)** | Backend, akun pengguna, multi-bahasa, transaksi, Three.js/WebGL |

Bila waktu menipis, pemangkasan dilakukan dari **Could**, lalu **Should**; kepatuhan aturan dan mobile-first tidak pernah dipangkas.

---

## 10. Pertanyaan Terbuka

| ID | Pertanyaan | Pemilik | Dampak |
|---|---|---|---|
| Q-01 | Apa rincian 20% bobot penilaian lainnya? | Tim (cek buku panduan) | Penyesuaian prioritas |
| Q-02 | Bagaimana cara pengumpulan (URL hosting atau ZIP)? | Tim | Menentukan dukungan `file://` dan README |
| Q-03 | Siapa mitra pengrajin UMKM dan apa kanal kontaknya? | Tim | Konten CTA |
| Q-04 | Daftar tonggak tahun dan istilah komponen yang divalidasi? | Kurator/narasumber | Akurasi Arsip |
| Q-05 | Apakah juri menilai di perangkat mobile fisik atau emulasi? | Tim | Prioritas uji |
| Q-06 | Adakah batas ukuran total berkas pengumpulan? | Tim (cek panduan) | Anggaran aset |
| Q-07 | Apakah tim menyetujui **CSS manual** menggantikan Tailwind CDN (SRS §3.1)? | Tim | Struktur `/css`, dokumen |
| Q-08 | Apa sumber penanda "≈ abad ke-8" (mis. relief Candi Borobudur) pada garis waktu Kredit? Bila tak ada, gunakan rumusan netral | Kurator | Akurasi Kredit |
| Q-09 | Bolehkah pola 12-bit diberi nama motif tradisional? (disarankan **tidak** kecuali divalidasi kurator) | Kurator | Integritas budaya |
| Q-10 | Apakah panitia menerima berkas `*.min.js` milik pustaka CDN (GSAP) sebagai pengecualian aturan "tanpa minify"? | Tim (cek panduan) | Kepatuhan |
| Q-11 | Siapa nama tim dan mitra yang dicantumkan pada kaki sertifikat dan footer? | Tim | Konten |
| Q-12 | Apakah mock mobile dan state kosong Dampak akan dirancang, atau cukup mengikuti aturan SRS §12? | Tim desain | Cakupan QA |

---

## Lampiran A: Selisih Desain Final dan Spesifikasi (Perlu Ditindaklanjuti)

Daftar ini memuat hal-hal pada `MAIN.jpg` yang **tidak boleh dibawa apa adanya** ke kode, atau yang belum dirancang. Spesifikasi di PRD dan SRS 1.1 sudah memakai versi yang dikoreksi; mock perlu disesuaikan agar sama.

### A.1 Prioritas Tinggi (kejujuran dan kepatuhan)

| # | Temuan pada desain final | Mengapa masalah | Tindakan |
|---|---|---|---|
| 1 | Klaim institusi/teknis: `PUSAKA.GOV`, "Arsip Nasional Indonesia", "Otoritas Sertifikasi Tingkat I", "Direktorat Mesin Biner Pertama", "Kodeks Nasional Pusaka Digital", "Resmi Terotentikasi", "Enkripsi BLAKE2B/Fisik Aktif", "SHA-256", "Immutable", "Konsensus Arsip", "Terdesentralisasi", "99.98% Verifikasi" | Menyiratkan afiliasi pemerintah dan kemampuan yang tidak ada; juri teknis dapat memeriksa kodenya | Ganti dengan teks Kamus Salin §7.1 (SRS §9.3); BRD R-11 |
| 2 | Mitra dan sumber bernama: "Komunitas Penenun Tuban & Silungkang", "Laboratorium Tekstil Tradisional Silungkang", "Balai Pelestarian Kebudayaan Wilayah X", "Komunitas Penenun Tuban & Sikek", "Lokasi Fisik: Tuban / Silungkang" | BRD D-02: dokumen tidak boleh mengarang organisasi; mengaku bermitra dengan pihak yang tidak ada berisiko etika | Isi dengan mitra dan sumber nyata, atau hapus (Q-03) |
| 3 | Nama motif pada pola 12-bit buatan pengguna: "Pucuk Rebung", "Itik Pulang Patang", "Kancang Bapatola" | Menyiratkan pola buatan itu adalah motif tradisional asli; berisiko salah representasi budaya | Hapus, atau validasi kurator (Q-09, BRD D-04) |
| 4 | Sisa prompt `1440 × 900 MUSEUM SPEC` pada strip bawah Beranda Scroll 2 | Artefak pembuatan desain | Hapus |
| 5 | Klaim sejarah: "pola matriks tertua tercatat di relief Candi Borobudur" (≈ abad ke-8); kata "terdesentralisasi" pada 2026 | Tanpa sumber / tidak benar | Rumusan netral atau tambahkan sumber (Q-08) |

### A.2 Prioritas Sedang (konsistensi dan kelengkapan)

| # | Temuan | Tindakan |
|---|---|---|
| 6 | Enam varian header; menu Arsip memakai "BENGKEL · PIAGAM · KURASI" sedangkan halaman lain "PLAYGROUND · DAMPAK · KREDIT"; langkah ditulis berbeda ("1 Temukan", "02 BACA", "FASE 03 TENUN"); logo ganda "SL SL_" pada Dampak | Satu header dan label kanonik (§3.3; BRD R-12) |
| 7 | Ikon profil pengguna pada header Dampak | Hapus (non-goal: tanpa akun) |
| 8 | Header Beranda Scroll 2 menandai "2 Pahami", padahal bagian itu masih langkah "1 Temukan" | Perbaiki mock; nada header berganti, langkah tidak |
| 9 | Beranda Boot: belum ada tautan "Lewati" dan baris kepercayaan; baris kredibilitas terpotong; kolom benang masih panel kosong | Lengkapi sesuai §5.4 dan §5.9 |
| 10 | Kartu jejak masih blok abu/hitam | Ganti foto close-up nyata (8–12), lisensi tercatat |
| 11 | Keterangan tahun Arsip mencampur "Jacquard & mesin tenun gedogan" | Pisahkan (US-407) |
| 12 | Playground: Cermin, Undo/Redo, Preset, pilihan ukuran belum ada pada mock; contoh nama "Raden Mas Joko // Penenun Kodikologi"; istilah "kodikologi" tidak tepat | Tambahkan ke desain atau turunkan prioritas; ganti contoh (§7.1) |
| 13 | Mock hanya desktop; state kosong Dampak, mobile, dan keadaan tanpa-JS belum ada | Rancang, atau ikuti SRS §9.5 dan §12 (Q-12) |
| 14 | Tahun `© 2024` pada Playground, Dampak, dan footer | Ganti `© 2026` |
| 15 | Kutipan pembuka Kurasi masih memakai rumusan lama ("tenun tradisional Nusantara adalah komputer biner pertama") | Kutip manifesto aktif |
| 16 | Teks informatif kecil berwarna kuningan dan abu pada latar terang (label, hex dump, keterangan) mendekati batas kontras | Pakai token `--c-brass-ink` dan `--c-ash`; label minimum 11 px; verifikasi dengan alat kontras (BRD R-14) |
| 17 | Kepadatan label bracket, ❖, dan tag pada Playground, Dampak, dan Kredit lebih tinggi dari prinsip ruang lega | Tinjau pada QA visual; pangkas label sekunder bila mengurangi satu titik fokus |
| 18 | Tailwind CDN (SRS 1.0) vs CSS manual (BRD §9 dan SRS 1.1) | Konfirmasi (Q-07) |

### A.3 Prioritas Rendah

| # | Temuan | Tindakan |
|---|---|---|
| 19 | *Drop cap* "P" pada Catatan Kurasi terpisah dari katanya | Perbaiki kait `::first-letter` |
| 20 | Lebar mock ± 1280 px, target spesifikasi 1440 px | Verifikasi pada 1440 px |
| 21 | Format ID berbeda: `SL-3F9A12C0` (PRD 1.0, 8 heks) vs `SL-9A3F1B` (mock, SRS) | Diseragamkan ke 6 heks (§US-602) |
| 22 | Kisi nama dan latar: Beranda Scroll 2 memakai Ivory `#F5F2EB`, halaman lain Paper `#FCF9F2` | Disahkan sebagai token `--c-paper` (BRD §6.3) |
