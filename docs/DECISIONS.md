# Keputusan & Selisih Dokumen

> Revisi 31 Oktober 2026: keputusan terbaru di CHANGES.md menggantikan pengecualian Lenis dan rancangan header/fetch lama. Satu HTML/desain tanpa header dipertahankan atas pilihan pengguna; runtime hanya GSAP + ScrollTrigger. Benang memakai progres lima section dan selesai di Kredit.

Format: konteks → keputusan → alasan.

1. **Tidak ada referensi visual (Figma/MAIN.jpg).** Tata letak, proporsi kolom, dan teks mengikuti SRS 1.1
   dan Kamus Salin PRD §7.1. Perlu dicocokkan ulang bila mock tersedia (SRS §14.3).
2. **Sinkron fade-out + fetch.** Contoh kode SRS §5.1 berurutan (`out().then(fetch)`), padahal teksnya
   menyebut paralel. Router memakai `Promise.all([out(), fetch()])`.
3. **Arah seret di grid.** PRD §5.3 menulis "nilai sama dengan sel pertama", tapi contohnya terbalik.
   Diikuti SRS §8.5: nilai lukis = kebalikan sel pertama yang disentuh.
4. **Checksum.** `CHECKSUM (FNV-1A)` di terminal dan ringkasan = 8 heks penuh (`0x936A442B`).
   `KODE MOTIF` = 6 heks (`0x6A442B`), `CHKSUM` di status strip = 16 bit rendah (`0x442B`). Ketiganya
   dihitung dari matriks, jadi sebutan "checksum" tidak lagi dipakai untuk kode motif.
5. **Benang memakai `gsap.quickTo`**, bukan `gsap.to` baru di setiap `onUpdate` (contoh SRS §10.3),
   agar tween tidak menumpuk.
6. **Benang digambar dalam piksel lapisan** (viewBox = ukuran lapisan), bukan `viewBox 0 0 120 1000` + `slice`,
   supaya angka dan label tidak terdistorsi saat lebar kolom berubah. Tanpa GSAP / reduced-motion:
   benang statis yang digambar JS, jadi `thread-fiber.svg` tidak diperlukan.
7. **Perangko**: `POS PUSAKA 7500 // IDR` diganti `POS PUSAKA // 12 × 12`. Nominal 7500 IDR bukan angka nyata (BR-14).
8. **Garis waktu Kredit**: `≈ ABAD KE-8` diganti `JAUH SEBELUM 1804` dengan sumber "menunggu kurasi narasumber",
   karena belum ada sumber (PRD Q-08). Jacquard dan Lovelace bersumber Encyclopaedia Britannica.
9. **Kutipan Lovelace** (Note A, 1843: "…weaves algebraical patterns just as the Jacquard-loom weaves flowers
   and leaves") dipakai di Catatan Kurasi sebagai terjemahan bebas, karena menguatkan analogi dengan sumber primer.
10. **Font cadangan dengan `size-adjust`** (Impact, Georgia, Consolas) supaya font swap tidak menggeser baris.
    Tanpa ini CLS Playground di Lighthouse 0,23; sesudahnya 0.
11. **Preload font dihapus**: `<link rel="preload" crossorigin>` memicu galat CORS di `file://`.
12. **Tombol DUKUNG PENGRAJIN** saat mitra kosong adalah `<button disabled>`, bukan `<a>` tanpa href
    (Lighthouse: tautan tidak dapat dirayapi). Bila `SL.config` terisi, JS menggantinya dengan `<a target="_blank" rel="noopener noreferrer">`.
13. **Dua `<h1>` di Dampak** (state kosong dan siap); hanya satu yang tampil. Router memfokuskan `<h1>` yang terlihat.
14. **Grid di ponsel < 480 px** melebar hampir selebar layar dan benang disembunyikan di Playground,
    karena 12 sel × 24 px tidak muat dengan ruang benang (WCAG 2.5.8, PRD US-702).
15. **Arsip di ponsel**: tanpa pin; ilustrasi terurai mengikuti scroll dan keempat bagian tampil berurutan.
16. **Kartu jejak** berupa 10 tekstur tenun SVG orisinal, bukan foto (belum ada foto berlisensi; BRD D-01).
    Atribusinya jujur sebagai ilustrasi generatif.
17. **Peningkatan yang diterapkan**: I-01 (tekan tombol), I-02 (`text-wrap: balance`, tabular-nums, `::selection`),
    I-04 (`SL.inspect()` + `console.info`), I-10 (log boot menampilkan status motif nyata), I-11 sebagian
    (kemiringan kartu mengikuti arah gerak), I-12 (crossfade nada header), I-20 (penanda bagian Arsip),
    I-21 (garis penunjuk label digambar), I-22 (register per bagian), I-33 (preset bernama geometris), I-40 (cap pos).
18. **Lenis 1.1.13 (smooth scroll) ditambahkan** atas keputusan tim, walau tidak tercantum di daftar pustaka
    BRD §9 / SRS §2.3; risiko aturan lomba (R-10) diterima tim. Dimuat via jsDelivr dengan SRI, digerakkan
    `gsap.ticker` dan disinkronkan ke ScrollTrigger (`js/core/smooth-scroll.js`). Tanpa Lenis/GSAP atau dengan
    reduced-motion, situs kembali ke gulir bawaan. Atribusi: tabel Kredit, `credits.json` (A-09), telemetri footer.
