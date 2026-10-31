# Blocker Rilis

Hal yang harus diisi tim sebelum pengumpulan. Situs berjalan tanpa ini, tetapi gerbang rilis BRD §12 belum lulus penuh.

| # | Butuh | Perilaku sekarang (fallback jujur) | Di mana mengisi |
|---|---|---|---|
| 1 | Nama mitra pengrajin + daerah + URL kanal resmi (PRD Q-03, BRD D-02) | Tombol `DUKUNG PENGRAJIN` nonaktif + "Kanal mitra belum ditetapkan." | `js/core/config.js` (`mitraNama`, `mitraDaerah`, `mitraUrl`) |
| 2 | Nama tim (PRD Q-11) | Baris "Dirancang oleh …" dihapus dari sertifikat dan PNG | `js/core/config.js` (`namaTim`) |
| 3 | 8–12 foto close-up pusaka berlisensi (BRD D-01) | Kartu jejak memakai 10 tekstur SVG orisinal | `assets/img/` + `IMAGES` di `cursor-trail.js` + tabel Kredit + `credits.json` |
| 4 | Sumber untuk penanda sebelum 1804 (PRD Q-08) | "JAUH SEBELUM 1804", sumber "menunggu kurasi narasumber" | `kredit.html` (garis waktu) |
| 5 | Validasi istilah komponen alat tenun oleh kurator (PRD Q-04) | Istilah umum: lungsi, penggulung, sisir, gulungan kain | `arsip.html` |
| 6 | Konfirmasi panitia: `*.min.js` dari CDN diterima (PRD Q-10) | GSAP dimuat dari cdnjs dengan SRI | — |
| 7 | Rincian 20% bobot penilaian lain (PRD Q-01) | — | — |
| 8 | Uji di ponsel fisik, Safari/iOS, dan Firefox | Baru diuji di Edge (Chromium) headless | — |
