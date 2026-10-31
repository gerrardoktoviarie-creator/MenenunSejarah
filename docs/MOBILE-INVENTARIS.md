# Inventaris mobile — Fase 0

Tanggal pengambilan: 31 Oktober 2026. Branch: `fitur/mobile-friendly`. Status: baseline dan rencana perlakuan, BUKAN implementasi mobile selesai. Kode produk/refactor yang sudah ada tidak diubah pada fase ini. Berhenti pada gerbang C.4 sampai pengguna membalas `lanjut`.

## Ruang lingkup dan metode

Runtime aktual satu `index.html` dengan lima `.page-section`: Beranda, Arsip, Playground, Dampak, Kredit. Tidak ada lima dokumen HTML atau header global. Screenshot bernama halaman di bawah adalah screenshot viewport pada awal section, bukan screenshot lima halaman terpisah atau bukti seluruh section sudah ditinjau visual.

- `qa-mobile/baseline.py`: Edge headless, reduced-motion, menunggu network idle dan font siap; enam lebar; 30 screenshot section dan enam JSON inventaris state kosong.
- `qa-mobile/extra-baseline.py`: enam inventaris state motif terisi melalui API penyimpanan aplikasi dalam profil browser sementara; enam screenshot Dampak; tiga screenshot hero pendek; Lighthouse mobile halaman gabungan.
- Terlihat ketat: ukuran positif, display/visibility/opacity elemen dan leluhur, irisan terhadap leluhur overflow, dan batas dokumen. Jalur nth-of-type + tag + 40 karakter teks menjadi kunci. Fungsi `INVENTORY` yang sama dipakai semua lebar.
- Daftar setiap elemen desktop: [ELEMEN-DESKTOP.md](qa-mobile/ELEMEN-DESKTOP.md), 992 kunci gabungan state kosong/terisi. Termasuk wadah, ornamen dan SVG, bukan 992 konten unik. State berbeda mengubah teks wadah sehingga kuncinya juga bisa berubah.
- JSON berisi key, section, rect, ukuran font, status interaktif/aria-hidden; lihat `qa-mobile/baseline/inventory-*.json`. Manifest SHA-256 kode produk ada di `source-sha256.json` untuk pemeriksaan lanjutan.

## Hasil baseline

| Lebar | Tinggi | Terlihat kosong | Terlihat motif terisi | Overflow dokumen | JS/konsol error / request gagal |
|---|---|---|---|---|---|
| 1440 | 900 | 692 | 824 | 0 px | 0 / 0 |
| 1280 | 900 | 692 | 824 | 0 px | 0 / 0 |
| 1024 | 900 | 692 | 824 | 0 px | 0 / 0 |
| 768 | 844 | 686 | 818 | 0 px | 0 / 0 |
| 390 | 844 | 640 | 772 | 0 px | 0 / 0 |
| 320 | 844 | 640 | 772 | 0 px | 0 / 0 |

Log error/request di tabel berasal dari run baseline state kosong. Run tambahan belum memasang pencatat error browser yang sama. Server pengujian mencatat satu reset koneksi WinError 10054 saat browser menutup koneksi; skrip tetap exit 0, bukan bukti galat JS aplikasi.

Body saat ini memakai `overflow-x:clip`. Probe terpisah mengganti hanya CSS runtime browser menjadi `visible`: overflow dokumen tetap 0 px di enam lebar pada state terisi/reduced-motion. Ini tidak membuktikan animasi normal dan semua posisi scroll bebas overflow; belum boleh menganggap clipping global sebagai solusi sah.

Perbandingan kunci state kosong terhadap 1440: 768 kehilangan 13 kunci, 390/320 kehilangan 59 kunci. Perubahan angka dekoratif benang/teks agregat bukan otomatis kehilangan konten. Pada ponsel, penggaris dan nomor baris Playground benar-benar tidak terlihat; kolom Lisensi Kredit berada di luar irisan wadah gulir, tetapi dapat dicapai dengan gulir lokal. Perbandingan final harus menelusuri wadah gulir/posisi scroll, bukan menganggap semua sel di luar irisan hilang permanen.

Lighthouse mobile, satu halaman gabungan: run pertama Performance 84, Accessibility 97, Best Practices 100, SEO 100; run ulang Performance 85, Accessibility 97, Best Practices 100, SEO 100. Laporan terakhir di `qa-mobile/baseline/lighthouse-mobile.json`. Performance dekat batas dan berubah antarrun; bukan bukti lima section masing-masing lulus atau perangkat fisik lancar.

Hero judul/subjudul/CTA berada dalam viewport pada 390×844 dan 360×640. Di 844×390, subjudul/CTA berada di bawah lipatan; itu diperbolehkan jika dapat digulir penuh. Pengujian ini reduced-motion, bukan bukti animasi selesai dalam tiga detik atau uji pemahaman lima detik dengan manusia.

## Inventaris perlakuan per section

Seluruh baris berstatus rencana kecuali yang tertulis baseline. Daftar atomik setiap elemen dirujuk di atas; tabel berikut mengelompokkan elemen berdasarkan perlakuan agar dapat ditinjau.

### Shell dan footer

| Elemen | Wujud desktop | Perlakuan mobile | Alasan | Status |
|---|---|---|---|---|
| Skip link, main, sr-status | Landmark/fokus dan pengumuman | Pertahankan, ukuran target/fokus tidak tertutup | Kontrak aksesibilitas | Baseline ada; uji fokus lanjutan |
| Header/menu/indikator/monograf | Tidak ada di runtime | Tidak membuat shell baru tanpa menyelaraskan konflik dokumen | Keputusan terdahulu satu HTML/tanpa header; desktop tidak berubah | Selisih dicatat di MOBILE-KEPUTUSAN |
| Nav progress | Garis fixed | Ubah ukuran/posisi dengan safe-area | Tidak menutupi konten | Rencana |
| Thread dan semua label | SVG persisten; jumlah digit responsif | Gutter 24/32 px, label vertikal ≥11 px; pertahankan siteProgress | Paritas label dan ruang konten | Rencana; digit boleh berkurang |
| Wordmark/deskripsi | Judul besar dan teks footer | Ubah ukuran, 1–2 baris, tumpuk | Cegah kata meluap | Rencana |
| Telemetri, hukum, penanda kanan | Baris/kolom | Wrap label dan nilai, tumpuk | Semua nilai tetap terbaca | Rencana |

### Beranda

| Elemen | Wujud desktop | Perlakuan mobile | Alasan | Status |
|---|---|---|---|---|
| Log dan kursor | Terminal 3 baris | Ukuran ≥11 px, wrap bila diperlukan | Semua log tetap ada | Baseline log 12 px |
| Manifesto empat baris | Anton dengan mask singkap | Ubah ukuran fluid; tetap empat baris; ukur kata terlebar | Hindari mengecilkan berdasar tinggi saja | Rencana; `pages.css:35–49` |
| Judul Playfair aktual | Saat ini berada di boot, bukan head trail | Relokasi visual hanya setelah paritas desktop dibuktikan | Copy/posisi aktual berbeda dari dokumen lama | Rencana; `index.html:46` |
| Lead, CTA, trust, kredibilitas, GULIR | Narasi dan aksi | Tumpuk; CTA penuh 56 px; trust bacaan ≥16 px | Trust sekarang 12 px | Rencana; `pages.css:55–119` |
| Petunjuk input | Dua span berbeda modality | Satu teks adaptif kemampuan input | Tidak ada informasi hover-only/DOM duplikat | Rencana; `index.html:67–70` |
| Masa Lalu/Depan dan keterangan | Label sisi kanvas | Pindah atas/bawah kanvas | Menyisakan zona sentuh | Rencana |
| Kanvas dan kartu jejak | Kartu dekoratif animatif | Ukuran 120×160/150×200, clamp posisi, overflow lokal clip | Pan-y tetap bekerja; tanpa membuang makna | Rencana; `cursor-trail.js:113–185` |
| Dua teks strip | Strip bawah | Wrap/tumpuk | Tidak terpotong | Rencana |
| Peta perjalanan lima tautan | Daftar judul/deskripsi/panah | Tumpuk/wrap tanpa menghapus deskripsi atau tautan | Elemen tambahan runtime tetap wajib | Rencana; `index.html:90–145` |

### Arsip

| Elemen | Wujud desktop | Perlakuan mobile | Alasan | Status |
|---|---|---|---|---|
| Ilustrasi empat bagian/bingkai | SVG berlabel | Sticky visual ≤34svh; bingkai tetap | Visual mendampingi empat langkah | Belum sticky |
| Empat label dan garis pemandu | Teks SVG berskala | Pindah ke HTML ≥11 px, posisi persen | Pada 320 label efektif diperkirakan ~6 px, bukan 22 px fisik | Rencana; `pages.css:501–520` |
| Empat marker navigasi | Tampil pada desktop staged | Tampilkan dalam alur mobile, tanpa tab/menyembunyikan artikel | Strict parity kontrol desktop | Rencana; `pages.css:537–542` |
| Empat judul/paragraf/register | Artikel, bergantian saat pin desktop | Semua mengalir normal, judul tanpa pecah kata | Tidak menyembunyikan langkah | Rencana |
| Tahun dan keterangan | Angka besar | Susunan ringkas di visual sticky, tetap counter | Muat pada tinggi pendek | Rencana |
| CTA/progres/benang | Aksi ke Playground/lapisan global | CTA setelah langkah akhir; progres tanpa pin | Desktop ≥900 pin tetap | Rencana; `exploded-view.js:69–130` |

### Playground

| Elemen | Wujud desktop | Perlakuan mobile | Alasan | Status |
|---|---|---|---|---|
| Heading/subjudul/strip/kursor | Head dan metadata | Ubah ukuran/wrap | Semua metadata tetap ada | Rencana |
| Grid 12×12/sel 0–1 | Sel minimum 24 px | Pertahankan ukuran minimum/keyboard/tap, glyph ≥11 px | Glyph kini minimum 10 px | Rencana; `components.css:312–328` |
| Penggaris kolom/nomor baris/bingkai | Terlihat desktop | Tampilkan, susun gutter atau wadah gulir editor lokal jika perlu | Kini hilang di bawah 480 | Gagal paritas baseline; `pages.css:737–740,930–975` |
| Legenda dan petunjuk | Bacaan kecil | Ukuran ≥16 px, tetap di alur | Legenda kini 14 px | Rencana |
| Readout 12 baris/hex/ringkasan | Panel terminal | Tumpuk, wrap terstruktur tanpa ellipsis | Semua nilai harus dicapai | Rencana |
| Tujuh kontrol dan empat preset | Panel tombol | Wrap; bilah kontrol sticky satu DOM | Mudah dijangkau tanpa duplikasi | Belum sticky |
| Nama/CTA/trust/error storage | Input/pesan/aksi | Input ≥16 px; trust/pesan ≥16 px | Hindari zoom iOS/teks kecil | Rencana |
| Benang | Disembunyikan di Playground <480 | Kembalikan dan reservasi gutter | Larangan mengurangi elemen | Rencana; `pages.css:924–928` |

### Dampak

| Elemen | Wujud desktop | Perlakuan mobile | Alasan | Status |
|---|---|---|---|---|
| State kosong | Judul/pesan/CTA | Tumpuk/ubah ukuran | Keadaan data bukan variasi viewport | Baseline difoto |
| State terisi: strip/nomor/identitas | Metadata aktual | Wrap hash/nomor dan tumpuk | Jangan potong identifier | Baseline tambahan enam lebar |
| Piagam/judul/kutipan/segel | Kartu berbatas | Ubah padding/ukuran fluid | Hindari nested min-width | Rencana |
| Motif/perangko/cap pos | Matriks dan tanggal | Tumpuk; motif tetap terbaca | Bukan piagam jadi satu gambar kecil | Rencana |
| Terminal/nama/ID/3 baris/checksum | Blok terminal | Wrap terstruktur; bacaan ≥16 px | Kode/pesan kini sebagian 12 px | Rencana |
| Catatan simbolis/tim | Teks kartu | Bacaan ≥16 px | Kini 14 px | Rencana |
| Dukung/mitra | Tombol dan pesan mitra | Sticky bawah satu elemen; pesan tetap | Mitra belum dikonfigurasi, tombol disabled bukan bug mobile | Rencana; `certificate.js:58–77` |
| Unduh/bagikan/tenun ulang/ringkasan | Kolom aksi | Tumpuk, wrap nilai, fokus tidak tertutup | Semua aksi dipertahankan | Rencana |

### Kredit

| Elemen | Wujud desktop | Perlakuan mobile | Alasan | Status |
|---|---|---|---|---|
| Hero/ontologi/index | Heading dan kartu hitungan | Ubah ukuran/wrap, tumpuk | Judul tanpa pecah kata | Rencana |
| Catatan kurasi/kutipan/penegasan | Narasi/kotak | Lebar bacaan ≤60ch, ≥16 px | Penegasan kini 14 px | Rencana |
| Matriks sembilan baris/3 kolom/chip | Tabel min-width 560 px | Wadah gulir lokal yang sudah ada; pastikan semua kolom terjangkau | Lisensi tidak masuk irisan awal ponsel tetapi bukan dihapus | Baseline; `pages.css:1465–1504` |
| Manifest JSON/hak moral | Tautan unduh dan teks | Pertahankan di alur, wrap | Tidak memerlukan library | Rencana |
| Empat tonggak/judul/ringkasan/sumber | Garis waktu | Tumpuk, teks bacaan/sumber ≥16 px | Ringkasan 14 px, tautan sumber 11 px | Rencana |
| Warna area terang/gelap | Override lokal hasil refactor | Jangan ubah pada fase mobile | Lindungi pekerjaan kontras terdahulu | Baseline; konflik dicatat |

## Risiko tertinggi dan batas bukti

1. Paritas saat ini gagal pada koordinat Playground dan label SVG terlalu kecil. Grid minimum ~303 px hampir menghabiskan viewport 320 sebelum ruler/gutter benang; perlu solusi layout nyata, bukan sel diperkecil atau clipping global.
2. Aturan header baru bertentangan dengan keputusan satu HTML/tanpa header dan desktop beku; jangan membangun ulang shell lama diam-diam.
3. Sticky Arsip/bilah aksi belum ada; leluhur overflow dan tinggi visual harus diuji agar sticky tidak putus/menutupi fokus.
4. CSS sejumlah bacaan 11–15 px, sel 10 px; label dekoratif tidak boleh dijadikan alasan mengecilkan bacaan.
5. Snapshot reduced-motion tidak membuktikan mode normal (pin, scrub, transform, animasi singkap), breakpoint teardown, font Safari, gesture fisik atau no-JS/no-GSAP. Itu wajib pada implementasi/QA berikutnya.
6. Inventaris tabel gulir perlu gabungan posisi scroll agar perbandingan strict tidak menghasilkan false positive kehilangan kolom; angka benang dan teks state dinamis perlu pengecualian terjelaskan, bukan dihapus dari audit.
7. Belum ada diff pixel/computed-style pascaperubahan; belum ada perubahan produk untuk dibandingkan. 39 screenshot adalah bukti baseline, bukan klaim desktop regresi lulus.

Gerbang C.4: menunggu `lanjut`. Tidak ada commit/refactor tambahan dilakukan pada fase ini; berkas untracked `console.log` dan `dom_headless.html` tidak disentuh.
