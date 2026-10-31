# Audit kualitas kode — sebelum refaktor

Tanggal: 31 Oktober 2026. Basis kode: `84b8cda`, branch `refactor/kode-bersih` dibuat dari `revisi-ui-menenun`.

Pengguna awalnya meminta berhenti seusai audit, lalu meminta seluruh prompt diselesaikan dan memilih mempertahankan satu HTML/desain sekarang. Audit ini mencatat keadaan awal, bukan mengklaim seluruh ketidaksesuaian harus diubah tanpa persetujuan.

## Cakupan dan metode

Inventaris sumber: 1 HTML aplikasi (`index.html`), 5 CSS, 16 JS, 1 SVG di assets/svg, 1 JSON di assets/data, 10 tekstur SVG di assets/img, README. Baca BRD/PRD/SRS; SRS §2–§5, §10, §11, §13 dan PRD §7.1 menjadi acuan. Pemeriksaan dibagi per kelompok berkas; nomor baris tabel merujuk versi sebelum perubahan.

`console.log` dan `dom_headless.html` adalah berkas tidak terlacak yang sudah ada sebelum tugas; bukan entry point aplikasi, tidak diubah/dihapus/disertakan commit. Berkas font biner tidak direfaktor. Dokumen historis docx/* bukan sumber kebenaran baru.

Kategori: a komentar; b penamaan; c rekayasa berlebih; d kode mati/sisa; e duplikasi; f CSS; g HTML; h copy; i perilaku/kepatuhan. Risiko adalah risiko perubahan yang diusulkan, bukan tingkat parah temuan. Temuan statis tidak otomatis membuktikan kebocoran heap.

## Tabel temuan awal

| Berkas | Baris awal | Kategori | Temuan dan bukti | Perbaikan yang diusulkan | Risiko perilaku |
|---|---|---|---|---|---|
| index.html; docs/SRS.md | 31,147; 68–75 | i | Lima halaman yang disebut SRS tidak ada; kelima bagian adalah section satu dokumen. | Pertahankan satu HTML sesuai keputusan pengguna; catat kontrak pengganti. | tinggi bila dimigrasikan; rendah untuk dokumentasi |
| js/core/router.js | 1–6,42–83 | i | Router hanya hash/pushState, bukan fetch + pergantian main. | Jangan migrasi diam-diam; dokumentasikan pengecualian arsitektur. | tinggi |
| index.html | 545–546 | i | Lenis adalah pustaka ketiga, bertentangan dengan batas GSAP/ST saja. DECISIONS §18 mengakui pengecualian lama. | Lepas CDN Lenis, pertahankan API scroll lewat fasilitas bawaan/GSAP. | sedang |
| js/core/header.js; index.html; js/main.js | 128–141;20–29;44–64 | d | Modul header masih dimuat, tetapi HTML header tidak ada dan init tidak dipanggil. | Pertahankan nama berkas, kurangi kode inert tanpa memasang header baru. | rendah |
| README.md | 51–53 | a | Menyatakan header scroll-spy hidup padahal sudah dihapus. | Jelaskan struktur tanpa header yang benar. | rendah |
| js/main.js | 2,51 | a | Header/Lenis dalam komentar tidak cocok runtime yang dituju. | Ringkas tujuan dan komentar sesuai lifecycle nyata. | rendah |
| js/features/thread.js | 211–212,36 | i | Body tidak punya data-thread-from/to, sehingga rentang default home dipakai seluruh situs. | Ganti dengan progres lima section yang dihitung dari posisi DOM/gulir. | tinggi (perubahan Bagian 2) |
| js/features/thread.js | 185–201 | d | setScene tidak dipanggil router saat ini. | Tetapkan API indeks section dan sambungkan router melalui API publik saja. | sedang |
| css/components.css | 460–464 | i | Clip-path di seluruh SVG memotong angka dan simpul bersama serat; angka di bawah simpul ikut hilang. | Clip hanya serat, angka tetap berada pada lapisan terpisah. | sedang (Bagian 2) |
| js/features/thread.js | 109–115,22 | h/i | Narasi Kredit sengaja belum selesai, bertentangan tujuan baru habis. | Hapus ujung lepas; SELESAI DITENUN dengan hysteresis .04/.08. | sedang (Bagian 2) |
| js/features/thread.js | 231–240 | i | Tiga disposer listener dibuang, destroy tidak membersihkan timer/rAF/listener. | Simpan disposer, batalkan timer/rAF dan lepaskan referensi saat destroy. | sedang |
| js/features/thread.js | 219–229 | i | Reduced-motion tidak membaca posisi scroll; baseline dasar dokumen front masih 85% tinggi. | Hitung posisi aktual tanpa tween pada init/scroll. | sedang |
| js/features/thread.js | 88,203–234 | i | Bit motif dibaca saat build saja; perubahan grid tidak memperbarui benang. | Dengarkan event sl:motif dan perbarui digit tanpa akumulasi node. | rendah |
| css/components.css | 486,491,496 | f | will-change permanen, termasuk transform digit yang tidak dianimasikan. | Hapus promosi permanen; ukur performa sesudahnya. | rendah |
| js/features/thread.js | 125 | i | Baseline 62 node SVG desktop (56 angka + grup/path/simpul); instruksi baru sekitar 60. | Batasi struktur tetap; jangan tambah node per frame. | rendah |
| js/features/home-sections.js | 78,91,99,112,134,178 | i | Banyak ScrollTrigger tanpa id. Baseline total 30 trigger, bukan thread saja. | Beri id diagnostik stabil; jumlah harus tetap setelah navigasi/lifecycle. Jangan matikan animasi yang ada agar memenuhi angka lama. | rendah |
| js/features/home-sections.js | 1–11 | a | Header komentar panjang merinci seluruh implementasi. | Ringkas menjadi tujuan dan pemanggil 1–3 baris. | rendah |
| js/features/weave-grid.js | 71,123,192,257,351 | a | Spanduk dekoratif; komentar kepala menyebut satu listener meskipun beberapa jenis event didelegasikan. | Komentar mengapa dan pemisahan fungsi bernama. | rendah |
| js/features/cursor-trail.js | 39–45 | i | Callback preload tidak dibatalkan saat destroy; hasil kunjungan lama bisa masuk daftar baru. | Ikat preload ke lifecycle dan buang callback saat dilepas. | sedang |
| js/features/cursor-trail.js | 75–77 | i | Timeline jejak tidak disimpan; killTweensOf(card) bukan kepemilikan timeline lengkap. | Simpan timeline per kartu lalu kill saat kartu dibuang/destroy. | sedang |
| js/features/magnetic.js | 18–20,32 | i | Disposer melepas listener, kepemilikan tween quickTo bergantung konteks GSAP. | Tegaskan pelepasan tween pada cleanup dan pertahankan matchMedia. | rendah |
| js/features/boot-sequence.js | 1–6,33,58 | a | Header panjang/JSDoc pada fungsi internal sepele dan label I-10 tanpa konteks. | Ringkas; pertahankan alasan quirk transform dan batas waktu boot. | rendah |
| js/main.js | 67–70 | i | pagehide membersihkan fitur saja; shell thread/smooth/router tertinggal. | Lifecycle shell simetris, reinit bfcache tanpa listener ganda. | sedang |
| README.md | 68–82 | a/i | Skor Lighthouse dan memori lama berasal dari arsitektur berbeda. | Pisahkan historis dan hasil eksekusi baru; jangan memindahkan klaim lama menjadi hasil sekarang. | rendah |
| docs/DECISIONS.md; docs/RELEASE-BLOCKERS.md | 18,39–42;10–11 | a/i | Keputusan Lenis/fallback dan rujukan HTML sudah tidak sesuai batas/struktur terbaru. | Tambahkan keputusan pengganti; jangan mengarang data mitra/sejarah. | rendah |

### Tambahan audit core, CSS, HTML dan aset

| Berkas | Baris awal | Kategori | Temuan dan bukti | Perbaikan yang diusulkan | Risiko perilaku |
|---|---|---|---|---|---|
| js/core/storage.js | 37–55,148–169 | i | setItem gagal setelah probe sukses tetapi read mengembalikan motif disk lama; probe VM mereproduksi nama lama, RAM baru. | Fallback per key ke RAM terbaru dan status persistensi aktual. | rendah |
| js/core/router.js | 19–24 | i | Heading pertama Dampak berada di state kosong yang disembunyikan saat piagam siap. | Pilih heading terlihat untuk fokus. | rendah |
| js/features/certificate.js | 216–283,337–343 | i | Ekspor menunggu font lalu membaca state global yang bisa berubah/destroy; callback masih mengakses root. | Snapshot data/identitas dan token lifecycle untuk hasil async. | sedang |
| js/features/certificate.js | 64–72 | i | CTA mitra mengganti marker sehingga init berikutnya tidak menemukan target. | Pertahankan data-partner dan rendering idempoten. | rendah |
| js/features/weave-grid.js; js/core/storage.js | 428–435;104–112 | i | Storage memvalidasi ukuran8/16 tetapi UI hanya memulihkan12; simpan bisa menimpa motif kompatibilitas. | Pertahankan data sampai tindakan matriks nyata; kebijakan konversi memerlukan keputusan. | sedang |
| js/core/router.js | 13–15 | i | decodeURIComponent hash malformed melempar URIError. | Tangkap pada batas decoding URL; abaikan hash tidak sah. | rendah |
| js/core/smooth-scroll.js | 15–29,49–55 | i | init dua kali menyisakan satu ticker Lenis setelah destroy. | Lifecycle idempoten dan pengganti tanpa Lenis. | sedang |
| css/base.css; css/pages.css | 177,210,235;28,76,462–537,754,760,829,1161 | f | Spasi optis/font/garis literal di luar token. | Ekstrak nilai tepat, jangan membulatkan atau mengubah font input menurut breakpoint. | sedang |
| css/tokens.css; css/pages.css; css/motion.css | 1–5 | a/f | Header panjang/pembatas dekoratif dan urutan deklarasi tidak konsisten. | Header ringkas, urutan layout-kotak-tipografi-visual-gerak tanpa mengacak shorthand. | rendah |
| css/base.css; css/components.css | aturan lenis/nav/steps | d | Kandidat kelas legacy tidak ditemukan markup aktif; state is-/word/trail/cell dibuat dinamis JS. | Jangan hapus berdasarkan nama saja; konservatif pertahankan kompatibilitas yang belum dibuktikan aman. | rendah |
| index.html; assets/data/credits.json | 482,532;46 | h | Setelah Lenis dilepas runtime, copy masih menyebut Lenis dan tiga pustaka. | Catat konflik, pertahankan copy karena larangan perubahan UI; keputusan tim diperlukan. | rendah |
| assets/img/tenun-01.svg..tenun-10.svg; assets/svg/favicon.svg | seluruh | i | 11 SVG valid XML, tidak ada script/referensi eksternal. | Tidak perlu refactor aset; provenance ilustrasi tetap klaim repo, bukan fakta independen. | rendah |
| assets/data/credits.json; assets/fonts/*OFL* | seluruh | h/i | Inventaris atribusi ada; tiga OFL cocok keluarga font, belum verifikasi provenance biner/upstream. | Pertahankan lisensi, konfirmasi sumber/mitra manusia. | rendah |

Penelusuran mencakup seluruh HTML/JS sebelum menyebut kandidat CSS tidak terpakai; tidak ada penghapusan massal kelas. Tidak ada abstraksi satu-pakai baru atau rename kontrak publik. Duplikasi kecil tidak otomatis diekstrak menjadi helper (ambang tiga pemakaian).

## Baseline nyata

Edge headless 156.0.4314.50, Playwright dijalankan di luar repo melalui uv; tidak ada package.json/node_modules/build baru.

- 10 screenshot viewport: lima SECTION, masing-masing 1440×900 dan 390×844. Bukan lima halaman yang tidak ada.
- Arsip di-pin menyebabkan tinggi desktop dokumen 12.369 px; mobile 12.288 px pada kondisi baseline. Geometry disimpan bersama gambar.
- Nol pageerror dan request gagal pada dua kunjungan baseline; console.info proyek dan console.table diagnostik tetap ada, bukan error.
- 320,360,390,768,1024,1440,1920 px: scrollWidth sama dengan innerWidth pada pemeriksaan root. Ini tidak membuktikan tidak ada clipping internal.
- Grid 144 sel; klik 0→1, keyboard panah+Spasi, drag empat sel, simpan payload v2/key tetap, piagam siap, back/forward hash bekerja.
- Jejak: 1 kartu setelah klik, 0 setelah 1,8 detik.
- Storage diblokir: tidak ada pageerror dalam smoke; belum membuktikan seluruh skenario quota.
- file://: router masih enabled=true (menyimpang spesifikasi awal).
- Tanpa GSAP: no-gsap=true tetapi lapisan thread masih block (harus disembunyikan sesuai acceptance baru).
- Reduced-motion dasar dokumen: front 612 px pada viewport720 px; membuktikan state belum mengikuti akhir situs.
- Syntax 16/16 JS lulus node --check.

Bukti: `C:/Users/Gerrad/AppData/Local/hermes/cache/scratch/menenun-audit-baseline/baseline.json`, `interactions.json`, gambar `beranda|arsip|playground|dampak|kredit-1440|390.png`.

## Pertanyaan dan batas kewenangan

Nama tim/mitra/kanal resmi, sumber sejarah sebelum1804, sumber foto dan lisensi aset memerlukan manusia. Panduan resmi lomba/aturan AI belum ditemukan; dokumen internal bukan bukti izin panitia. Tidak ada upaya menyamarkan asal kode, membuat kesalahan buatan atau memalsukan riwayat.

## Sepuluh temuan terpenting

1. Konflik satu HTML vs lima halaman; keputusan pengguna mempertahankan satu HTML.
2. Lenis melanggar batas pustaka baru.
3. Benang hanya memakai rentang home sepanjang dokumen.
4. Clip seluruh SVG menghilangkan digit yang seharusnya tersisa.
5. Lifecycle thread tidak melepas listener/timer.
6. Reduced-motion tidak mengikuti posisi akhir/reload.
7. Bit motif tidak disinkronkan setelah simpan.
8. Trigger tanpa id dan kriteria jumlah trigger lama tidak sesuai arsitektur.
9. Modul/header/README menyisakan kontrak yang sudah tidak hidup.
10. Hasil QA historis dan atribusi/mitra tidak boleh dianggap tervalidasi sekarang.

Perkiraan berkas terdampak: 20–25 sumber/dokumen, tanpa rename atau penghapusan berkas. Jumlah final akan dicatat dari diff Git, bukan perkiraan ini.
