# Catatan perubahan dan rencana verifikasi

## Lingkup yang disetujui

Pengguna meminta penyelesaian seluruh prompt, lalu secara eksplisit memilih mempertahankan satu `index.html` dengan lima section dan desain tanpa header. Karena itu tidak dibuat `arsip.html`, `playground.html`, `dampak.html`, atau `kredit.html`. Navigasi tetap anchor + pushState, bukan fetch. Semua berkas lama dipertahankan.

## Rencana pelaksanaan

1. Selesaikan audit seluruh sumber dan catat baseline serta konflik spesifikasi di AUDIT.md.
2. Rapikan core, fitur, CSS dan HTML dengan kontrak publik, hook DOM, skema storage v2 dan nilai visual tetap. Jalankan syntax dan regresi sebelum commit per topik.
3. Ganti rentang benang dengan progres lima section; serat habis, simpul hilang, label SELESAI DITENUN; reversibel, reduced-motion statis, fallback tanpa GSAP tersembunyi.
4. Sinkronkan SRS §10.3/Lampiran B dan PRD §5.9/US-1003; buat PANDUAN-KODE.md dan perbarui README.
5. Uji browser, baseline visual, 320–1920 px, grid, storage, trail, navigasi, reduced-motion, file, CDN gagal; ukur performa/memori dan Lighthouse bila dapat dijalankan. Catat batas pengukuran, tidak menyebut yang belum diuji sebagai lulus.

## Keputusan implementasi

- Indeks halaman pada model asli dipetakan ke `.page-section` berurutan: beranda, arsip, playground, dampak, kredit. Titik awal section menjadi batas interval progres; dasar dokumen menjadi akhir Kredit, termasuk footer. `data-page` pada lapisan benang diselaraskan ke section aktif; body tetap mengikuti markup asli. Perhitungan tidak bergantung pada riwayat sesi.
- Tanpa perubahan desain selain benang. Posisi simpul bergerak ke atas (nilai Y berkurang), bukan turun; prompt memakai dua istilah arah yang bertentangan.
- Lenis yang sudah ada dikeluarkan dari runtime untuk memenuhi batas hanya GSAP + ScrollTrigger; berkas kompatibilitas smooth-scroll tetap dipertahankan. Ini pengecualian kompatibilitas yang dicatat, bukan penambahan library.
- Pengujian “20 perpindahan halaman” diadaptasi ke 20 perpindahan section dan siklus init/destroy; jumlah trigger tidak dipaksa menjadi satu karena animasi section yang sudah ada harus tetap hidup. Yang diperiksa adalah jumlah stabil dan sumber daya benar-benar dilepas.
- Dua berkas tidak terlacak milik pengguna (`console.log`, `dom_headless.html`) tidak dihapus, diubah, atau dimasukkan commit. Dump HTML bukan sumber aplikasi.

## Keputusan yang menunggu manusia

- Buku panduan resmi TECHTOPIA Vol. 2 belum tersedia di repo dan belum ditemukan lewat pencarian web yang relevan. Izin/deklarasi AI, pengecualian minified CDN, kewajiban router fetch dan bobot penilaian harus dikonfirmasi panitia. Tidak ada klaim patuh resmi.
- Nama tim, nama/daerah/URL mitra, lisensi/sumber foto pengganti tekstur SVG dan kurasi sejarah sebelum 1804 harus diberikan tim. Tidak dikarang.
- Uji ponsel fisik, Safari/iOS, Firefox dan lima penguji untuk uji lima detik tetap memerlukan manusia/perangkat tersebut.

## Perubahan per berkas

| Berkas | Yang berubah dan alasan |
|---|---|
| js/core/namespace.js | Header tujuan/pemanggil; API helper yang sudah dipakai dipertahankan. |
| js/core/config.js | Header singkat; data tim/mitra tidak dikarang. |
| js/core/motion.js | Hapus konfigurasi Lenis tanpa pemakai; nilai animasi lain tetap. |
| js/core/storage.js | Cache RAM terbaru menang setelah quota/write gagal; pembacaan berhasil menyegarkan cache; available mencerminkan kegagalan aktual. Format v2/key/FNV-1a tetap. |
| js/core/router.js | Disposer/destroy, init idempoten, hash malformed aman, hormati target/download/modifier/file lokal; notifikasi indeks ke API thread. |
| js/core/smooth-scroll.js | Native wheel/touch dan tween anchor GSAP mengganti Lenis; interupsi pengguna/cleanup dan reduced-motion. Rasa wheel berbeda secara sengaja, bukan klaim kesetaraan100%. |
| js/core/header.js | API kompatibilitas inert karena header tidak ada/tidak dipanggil; berkas tidak dihapus. |
| js/features/weave-grid.js | Komentar mengapa/header, init/destroy aman berulang, banner persistensi aktual. Matriks12, algoritme, tombol dan copy tetap. |
| js/features/certificate.js | Init idempoten dan marker CTA partner dipertahankan untuk reinit. Perbaikan snapshot ekspor/fokus navigasi sedang diverifikasi terpisah. |
| js/features/boot-sequence.js | Header/JSDoc ringkas, guard init, cleanup/fallback tetap; timing visual tidak diubah. |
| js/features/cursor-trail.js | Generasi preload mencegah callback stale; timeline/listener milik kartu dilepas; rAF dan perubahan preferensi dibersihkan. |
| js/features/home-sections.js | ID trigger diagnostik deterministik, guard init, tween batch yang dibuat belakangan dimiliki konteks existing agar revert tuntas. |
| js/features/magnetic.js | Guard init dan quickTo tween dibunuh bersama listener saat cleanup. |
| js/features/exploded-view.js | Guard init, media query mengikutsertakan reduced-motion live, pin/scrub/state dibersihkan; parameter animasi normal tetap. |
| js/features/thread.js | Model progres lima section, digit motif live, penyelesaian/hysteresis/reversibilitas, fallback waktu, lifecycle terukur. Memakai native scroll+rAF, tidak menambah ScrollTrigger sendiri. |
| js/main.js | Hilangkan wrapper catch umum/pesan diagnostik startup, idempoten; teardown shell lengkap dan fitur urutan terbalik, resume bfcache, font callback diberi guard lifecycle. |
| css/tokens.css | Tambah token presisi nilai lama (termasuk optis/negatif/unitless), tanpa pembulatan/desain baru. |
| css/base.css | Urutan properti, token fokus/sr-only, komentar arsitektur diperbarui. |
| css/pages.css | Urutan properti dan literal menjadi token tepat; breakpoint/geometri tetap. |
| css/motion.css | Header/komentar dan token durasi; keyframe/reduced-motion tetap. |
| css/components.css | Clip serat terpisah, label selesai/shuttle/reduced-motion, hilangkan will-change permanen khusus benang. |
| index.html | Hapus dua baris CDN/SRI Lenis saja; copy/DOM/hook/urutan script lain tetap. |
| README.md | Hapus klaim header aktif, tautkan audit/panduan, tandai skor historis bukan QA terbaru. |
| docs/BRD.md | Catatan revisi arsitektur, tanpa menulis ulang aturan panitia. |
| docs/PRD.md | §5.9/US-1003 mengikuti progres/habis dan narasi SELESAI DITENUN; catatan satu HTML. |
| docs/SRS.md | §10.3 mengganti rentang dengan model progres; Lampiran B memakai data-section, contoh atribut rentang lama dilepas; catatan pengecualian arsitektur. |
| docs/DECISIONS.md | Keputusan pengganti Lenis/header/fetch lama dinyatakan di awal, sejarah dokumen tetap. |
| docs/AUDIT.md | Inventaris, tabel a–i/bukti awal, baseline, sepuluh prioritas dan pertanyaan manusia. |
| docs/PANDUAN-KODE.md | Alur data, tujuan/fungsi/jebakan tiap modul dan tiga pertanyaan juri beserta jawaban. |
| docs/CHANGES.md | Lingkup/persetujuan, perubahan per berkas, pengecualian dan status pengujian ini. |

## Pengecualian dan temuan ditahan

- Copy UI/index dan credits.json masih menyebut Lenis/tiga pustaka. Tidak diubah agar larangan perubahan copy tetap dipatuhi; tim perlu menyetujui koreksi kredit menjadi dua pustaka. README/panduan menjelaskan runtime yang sebenarnya.
- Kelas legacy Lenis/nav/steps tidak dihapus massal. Kelas dinamis diverifikasi lewat seluruh HTML/JS; mempertahankan sedikit CSS kompatibilitas lebih aman daripada menghapus berdasarkan asumsi nama.
- Payload storage8/16 valid secara skema, tetapi grid UI hanya12. Belum ada fitur konversi/konfirmasi baru; risiko penimpaan lewat penyimpanan UI dicatat untuk keputusan tim. Jangan menganggap migrasi ukuran teruji.
- Klaim ilustrasi orisinal/generatif berasal dari kredit repo; XML valid bukan bukti provenance. Lisensi GSAP resmi diperiksa (https://gsap.com/standard-license/), bukan MIT seperti istilah lama beberapa dokumen; kepatuhan distribusi/versi tetap perlu tim konfirmasi.
- Rujukan header/lima halaman/fetch di rancangan awal diberi catatan pengganti, tidak dimigrasikan diam-diam. Kalimat arah “turun” pada prompt ditafsirkan Y menurun/bergerak ke atas sesuai formula0,85→0.
- Target jumlah trigger hanya thread(+exploded) tidak berlaku pada satu dokumen dengan seluruh reveal hidup. Pemeriksaan adalah jumlah stabil, ID unik, cleanup total, bukan mematikan animasi untuk mengejar angka.

## Bagian 6 — warna teks Kurasi & Kredit

Cakupan runtime adalah `index.html#kredit`, bukan berkas kredit.html yang tidak ada. Pada audit browser tidak ditemukan teks putih/ivory di atas latar terang. Judul, isi, kutipan, index, sel tabel, chip dan tombol sudah mewarisi Void dari `.kredit`; tidak dipaksa hitam ulang. Empat label justru mewarisi aturan tema gelap body `[data-tone="void"] .label` sehingga Concrete tampil di Paper (2,32:1).

| Selektor yang diubah | Warna lama efektif | Warna baru | Alasan |
|---|---|---|---|
| `.kredit[data-tone="paper"] .label` (aturan lokal baru) | Concrete #A6A6A6 dari `[data-tone="void"] .label` | `var(--c-brass-ink)` #8C6E2E | Tema lokal Paper harus mengalahkan tema body Void; label informatif tetap kuningan, kontras 4,55:1. |

Tidak mengubah token, copy, ukuran, layout, background, footer/status strip/terminal, atau JS. Tidak memakai inline style/!important. Warna Ash dan Merah Saga dipertahankan.

Verifikasi nyata 31 Oktober 2026 (Edge headless):
- 320/390/768/1024/1440/1920 px × direct hash/reload dan router.go × atas/tengah/bawah =36 sampel. Sebelum:144 pelanggaran kontras (empat label berulang), sesudah:0; teks putih/ivory pada latar terang0; overflow body0; pageerror0.
- Rasio efektif Paper: Void18,48:1; Ash5,07:1; Brass Ink4,55:1; Merah Saga4,91:1. Pemindaian memperhitungkan ambang teks besar, background transparan melalui rantai leluhur dan warna RGB computed. Tidak merupakan audit gambar/lapisan pseudo kompleks di seluruh situs.
- Daftar computed color/background seluruh footer dan status strip identik sebelum/sesudah pada36 sampel. Tidak ada blok terminal dalam section Kredit; aturan terminal tidak disentuh.
- Screenshot sebelum/sesudah390 dan1440, atas/tengah/bawah tersedia di `C:/Users/Gerrad/AppData/Local/hermes/cache/scratch/kredit-colors/` (`before-*`, `after-*`); JSON berisi seluruh hasil teks.
- Simulasi zoom CSS200% pada viewport780px (ruang layout ekuivalen390): tidak ada overflow body,0 pelanggaran kontras. Uji stress390px dengan CSS zoom200% (ruang195px, di bawah minimum320) menunjukkan overflow; tidak diperbaiki karena akan membutuhkan perubahan layout yang dilarang. Zoom browser/perangkat fisik tetap perlu pemeriksaan manual.
- Lighthouse mobile Accessibility97 (target95 tercapai), exit0. Audit color-contrast keseluruhan dokumen masih melaporkan animasi Beranda di luar Kredit; tidak dinyatakan seluruh situs bebas masalah. Laporan `kredit-colors/lighthouse.json`.

## Bukti pengujian sampai saat ini

- Parent menjalankan ulang features12/12 dan thread24/24, exit0 di Edge pada31 Oktober2026. Uji thread mencakup posisi awal765px pada tinggi900, batas612/459/306/153, akhir0;56/24 digit;61/29 keturunan SVG; hysteresis, motif, reload, non-scroll fallback dan cleanup.
- Parent uji pagehide: seluruh ScrollTrigger0, router false setelah teardown. Ini uji lifecycle, bukan simulasi ponsel fisik/heap bebas bocor.
- Core:6 tes Node; browser375/1280, keyboard/undo/redo/simpan/navigasi/PNG1520×960 dilaporkan lulus oleh delegasi. Uji integrasi akhir masih berjalan.
- CSS: tinycss2 lima stylesheet tanpa parse error,11/11 SVG valid;467 elemen seluruh properti computed non-custom375/768/1280 tidak berbeda saat fase animasi disamakan. Perbandingan ini mengisolasi CSS refactor, bukan kesetaraan piksel seluruh animasi.
- Lighthouse/performa30detik/memori20navigasi/screenshot final: belum ada hasil final saat bagian ini ditulis; tidak dinyatakan lulus.

