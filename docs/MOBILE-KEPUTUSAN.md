# Keputusan mobile

Status: implementasi berjalan setelah pengguna membalas `lanjut`. Baseline Fase 0 tetap disimpan tanpa ditimpa.

## 1. Satu HTML, lima section, tanpa header global

Konteks: BRD/PRD/SRS menyimpan rancangan awal lima HTML, router fetch, header/menu. Revisi di awal ketiga dokumen dan keputusan pengguna terdahulu mempertahankan satu HTML, lima section dan tanpa header. Runtime cocok dengan revisi tersebut (`index.html`, `js/core/header.js`, `js/core/router.js`). Prompt mobile D/E kembali merinci header/menu dan lima HTML, sementara desktop ≥900 tidak boleh berubah.

Opsi: membangun ulang lima halaman/header; menambah shell hanya mobile; mempertahankan struktur executable dan mengadaptasi seluruh kontennya.

Keputusan aman fase audit: pertahankan struktur sekarang, laporkan bagian header/menu sebagai tidak ada pada baseline, jangan menciptakan salinan mobile/desktop atau lima entry point. Tidak ada elemen desktop yang boleh hilang. Penambahan shell bukan diasumsikan sudah disetujui; konflik ini dapat dikoreksi pengguna di gerbang inventaris.

## 2. Arsip sticky tanpa membuang empat penjelasan

Konteks: empat artikel sudah tersedia pada DOM; desktop non-reduced-motion staged/pin, mobile kini alur biasa tanpa sticky. Label SVG menyusut bersama viewBox.

Opsi: pin seluruh panggung mobile, menyembunyikan artikel, atau visual sticky + empat artikel mengalir.

Rencana: visual sticky dengan tinggi terbatas; semua artikel/register/CTA/marker dipertahankan; label HTML ≥11 px; `gsap.matchMedia()` memisahkan desktop dan mobile dan `destroy()` merevert. Tidak mengubah pin desktop. Reduced-motion tetap alur statis. Belum diterapkan.

## 3. Bilah aksi satu DOM

Konteks: kontrol Playground dan dukungan Dampak belum sticky.

Rencana: elemen asli menjadi sticky dalam batas section, bukan clone fixed global; safe-area dan ruang fokus diperhitungkan. Bila total kontrol tinggi, wrap dalam alur yang masih dapat dijangkau tanpa menutupi konten. Semua preset/readout/aksi sekunder tetap ada. Belum diterapkan.

## 4. Tabel dan definisi strict-visible

Konteks: tabel Kredit min-width 560 px memakai wadah overflow-x:auto berlabel/focusable. Pada snapshot ponsel kolom Lisensi tidak beririsan dengan wadah sehingga tidak tercatat strict-visible.

Keputusan audit: jangan menyamakan terpotong pada posisi awal wadah gulir dengan dihapus dari DOM. Kriteria final harus mencakup semua posisi gulir lokal atau kartu bersemantik tabel; semua baris/kolom wajib dapat dicapai. JSON mentah tetap menyimpan hasil strict tanpa menghapus selisih.

## 5. State data dan konten dinamis

Konteks: Dampak empty/ready dan teks identitas berbeda menurut motif; jumlah digit benang berkurang sesuai parameter yang diizinkan.

Keputusan: ambil dua state dalam konteks browser sementara. Inventaris gabungan mencatat keduanya, tidak memaksa empty/ready tampil bersamaan dan tidak mengubah skema localStorage v2. Selisih angka dekoratif tidak diperlakukan sebagai izin menghilangkan label bermakna.

## 6. Lindungi benang dan warna Kredit

Konteks: siteProgress lima section telah dikerjakan. Teks utama Kredit terang sudah Void; empat label hasil koreksi kontras memakai Brass Ink, bukan semuanya Void. Prompt B.7 meminta jangan merusak pekerjaan terdahulu.

Keputusan: tidak mengubah model progres, copy atau warna terdahulu pada fase mobile. Laporkan perbedaan label Brass Ink ini, jangan mengklaim seluruh teks terang hitam atau melakukan blanket override. Audit visual setelah implementasi akan membandingkan baseline sekarang.

## 7. C.4 dan permintaan langsung

Konteks: pesan meminta dikerjakan langsung tetapi juga eksplisit mewajibkan berhenti setelah inventaris dan menunggu `lanjut`.

Keputusan: kerjakan Fase 0 sungguhan hingga artefak dan eksekusi tersedia, lalu berhenti sesuai gerbang spesifik C.4. Bukan mengulang audit tanpa hasil; tidak mulai Fase 1 sebelum persetujuan tersebut.
