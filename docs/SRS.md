# SRS — Software Requirements Specification

> Revisi implementasi (31 Oktober 2026): pengguna mempertahankan satu `index.html` dengan lima section dan tanpa header. Rujukan lima HTML/router fetch/header di bagian lain adalah rancangan awal, bukan klaim runtime saat ini. Kontrak pengganti dan pengecualian dicatat di `CHANGES.md`; model benang terbaru mengikat pada §5.9 PRD / §10.3 SRS. Hasil QA lama bukan bukti versi baru.


## Sandi Leluhur: Mesin Biner Pertama

**Website Kompetisi Web Design TECHTOPIA Vol. 2 (Tingkat Nasional)**

| Atribut | Nilai |
| :---- | :---- |
| Versi | 1.1 (Final, disinkronkan dengan desain final) |
| Tanggal | 23 Oktober 2026 |
| Dokumen Induk | `BRD.md`, `PRD.md` |
| Tech Stack | Static HTML, CSS manual (design tokens), Vanilla JavaScript, GSAP + ScrollTrigger via CDN |
| Sumber Perubahan | Desain final (`MAIN.jpg`), redesign hero, Benang Sepanjang Situs, penyelarasan copy |

### Riwayat Revisi

| Versi | Tanggal | Perubahan Utama |
|---|---|---|
| 1.0 | 9 Okt 2026 | Spesifikasi awal (5 bagian) |
| 1.1 | 23 Okt 2026 | Struktur dirapikan menjadi §1–§15 agar sesuai rujukan BRD/PRD; keputusan **CSS manual** menggantikan Tailwind CDN (§3); *classic script* menggantikan ES module (§3); header persisten dengan indikator langkah (§5); Booting Sequence baru (§6); readout biner baru berisi hex, kerapatan, dan koordinat kursor (§8); skema `localStorage` bervers dan ID/checksum nyata (§8.4); aturan kejujuran konten pada Sertifikat (§9); Benang Sepanjang Situs (§10.3); halaman Kredit dan manifest atribusi (§15); lampiran kerangka HTML dan selisih terhadap 1.0 |

---

## 1. Pendahuluan

### 1.1 Tujuan
Dokumen ini mendefinisikan spesifikasi rekayasa perangkat lunak untuk "Sandi Leluhur". Mengingat batasan TECHTOPIA Vol. 2, sistem dibangun **tanpa** framework JavaScript modern (React/Vue), **tanpa** proses *build* (SSG/bundler), dan beroperasi sepenuhnya di sisi klien (*client-side*).

### 1.2 Konvensi
- **HARUS** = wajib (setara *Must*), **SEBAIKNYA** = dianjurkan (*Should*), **DAPAT** = opsional (*Could*).
- Rujukan `BR-xx` mengacu ke BRD §8; `US-xxx` mengacu ke PRD §4.
- Teks antarmuka yang dikutip dalam dokumen ini mengikuti **Kamus Salin Final** di PRD §7.1.

### 1.3 Keputusan Penting yang Berubah dari Versi 1.0

| # | Keputusan | Versi 1.0 | Versi 1.1 | Alasan ringkas |
|---|---|---|---|---|
| K-1 | Kerangka CSS | Tailwind via CDN | **CSS manual + `tokens.css`** | Lihat §3.1. Selaras dengan BRD §9 |
| K-2 | Pemuatan JS | IIFE atau ES module | **Classic script + IIFE**, satu namespace `window.SL` | ES module gagal di `file://` (BRD R-03) |
| K-3 | Header | Tidak dispesifikasikan | **Persisten di luar `<main>`**, disinkronkan oleh router | Desain final memuat indikator langkah dan label monograf |
| K-4 | Benang | Tidak ada | **`#thread-layer` persisten** (SVG + GSAP) | Konsep "satu benang sepanjang situs" |
| K-5 | ID dan checksum | Contoh statis | **FNV-1a 32-bit**, dihitung dari matriks | Semua angka di UI harus nyata (BR-14) |
| K-6 | Skema `localStorage` | Tanpa versi | **`version: 2`** + validasi | Ketahanan terhadap data rusak |
| K-7 | Umur kartu jejak | "≈ 700 ms" | **≈ 1,4 dtk total**, dihapus saat memudar selesai | Menyelaraskan dengan PRD §5.1 |

---

## 2. Arsitektur Sistem & Struktur Direktori

### 2.1 Arsitektur Aplikasi
Pendekatan *Static Multi-page* yang ditingkatkan menjadi *Single Page Application* (SPA) ilusi memakai Vanilla JavaScript (`fetch` dan `History API`). Tidak ada komunikasi ke server *backend* maupun *database*.

**Lapisan global** (berada di luar `<main>`, tidak diganti saat pindah halaman):

| Lapisan | Elemen | Catatan |
|---|---|---|
| Skip link | `a.skip-link` | Selalu pertama dalam urutan tab |
| Header | `header.site-header` | Disinkronkan router (§5.4) |
| Benang | `#thread-layer` | Persisten; hanya `ScrollTrigger`-nya dibuat ulang (§10.3) |
| Progres muat | `#nav-progress` | Garis Merah Saga di tepi atas |
| Footer | `footer.site-footer` | Nada (`void` atau `paper`) disinkronkan router |
| Wilayah pengumuman | `#sr-status` (`aria-live="polite"`) | Mengumumkan "Halaman … dimuat" |

**Lapisan halaman** (diganti router): hanya `<main id="konten">`.

### 2.2 Struktur Direktori

```
/sandi-leluhur
 ├── index.html            (Beranda: Boot + Menenun Waktu)
 ├── arsip.html            (Arsip Sandi)
 ├── playground.html       (Playground Biner)
 ├── dampak.html           (Dampak: Sertifikat)
 ├── kredit.html           (Kurasi & Kredit)
 ├── README.md             (daftar periksa kepatuhan + sinkronisasi shell)
 ├── /docs                 (BRD.md, PRD.md, SRS.md)
 ├── /assets
 │    ├── /img             (foto kartu jejak 8–12 buah, WebP/JPEG ≤ 60 KB)
 │    ├── /fonts           (Anton, PlayfairDisplay roman+italic, JetBrainsMono; .woff2 subset Latin)
 │    ├── /svg             (loom-exploded.svg, seal.svg, thread-fiber.svg)
 │    └── /data            (credits.json = manifest atribusi, §15)
 ├── /css
 │    ├── tokens.css       (CSS custom properties: warna, tipografi, spasi, garis, gerak)
 │    ├── base.css         (reset, tipografi dasar, fokus, skip link)
 │    ├── components.css   (tombol, label bracket, tag artefak, siku kuningan, sel grid, header, footer)
 │    ├── pages.css        (gaya per halaman, dikelompokkan per `[data-page]`)
 │    └── motion.css       (transisi, kelas `.is-exiting`, `no-gsap`, `prefers-reduced-motion`)
 └── /js
      ├── /core
      │    ├── namespace.js   (membuat window.SL, util `on()`/`off()`, daftar disposer)
      │    ├── storage.js     (localStorage/sessionStorage aman + fallback memori)
      │    ├── router.js      (SPA ilusi)
      │    ├── transition.js  (fade-out/fade-in)
      │    └── header.js      (sinkronisasi header, indikator langkah, nada)
      ├── /features
      │    ├── boot-sequence.js
      │    ├── cursor-trail.js
      │    ├── thread.js
      │    ├── exploded-view.js
      │    ├── weave-grid.js
      │    └── certificate.js
      └── main.js          (entry point: inisialisasi inti, registri halaman)
```

Halaman Kredit tidak memiliki modul fitur khusus (konten statis dan tautan unduh manifest).

### 2.3 Pustaka Eksternal
Kepatuhan mutlak: library UI dan proses *build* dilarang.

| Pustaka | Versi | Sumber | Catatan |
|---|---|---|---|
| GSAP Core | 3.12.x (di-*pin*, mis. `3.12.5`) | cdnjs/jsDelivr | Atribut `integrity` (SRI) dan `crossorigin="anonymous"` wajib; isi hash dari halaman resmi CDN |
| GSAP ScrollTrigger | sama dengan Core | cdnjs/jsDelivr | Dimuat setelah Core |
| Font | — | **Self-host** di `/assets/fonts` | `woff2`, subset Latin, `font-display: swap`, lisensi SIL OFL (verifikasi akhir) |

**Tidak dipakai (dan tidak boleh ditambahkan):** Tailwind, Bootstrap, jQuery, Three.js/WebGL, plugin GSAP tambahan (MorphSVG, MotionPath, dll.), library canvas atau ekspor gambar (mis. html2canvas).

Manipulasi DOM: 100% Vanilla JavaScript.

---

## 3. Keputusan Teknologi

### 3.1 CSS Manual dengan Design Tokens (menggantikan Tailwind CDN)
Versi 1.0 memilih Tailwind via skrip CDN. Versi 1.1 mengganti dengan CSS manual karena:

1. **Keterbacaan kode.** Juri teknis membaca *View Source*. Kelas utilitas panjang menyulitkan audit "kode asli".
2. **Performa.** Tailwind via skrip CDN mengompilasi di peramban saat runtime dan menambah beban serta potensi FOUC. Dokumentasi resmi Tailwind menyebut pendekatan ini ditujukan untuk pengembangan, bukan produksi. Ini berbenturan dengan target Lighthouse (BRD OBJ-03).
3. **Kesesuaian dengan BRD §9.** BRD sudah menyatakan "CSS ditulis manual dengan design tokens".
4. **Desain final memiliki kosakata komponen khusus** (label bracket, siku kuningan, status strip) yang lebih rapi sebagai komponen CSS bernama.

Konsekuensi: berkas `/css` bertambah menjadi lima (lihat §2.2). Aturan penamaan: **BEM-lite** (`.blok`, `.blok__elemen`, `.blok--varian`), satu `:root` sumber kebenaran untuk nilai (`tokens.css`).

> **Perlu konfirmasi tim.** Bila tim tetap memilih Tailwind, ubah §2.3, §3.1, §4, dan BRD §9, serta tambahkan Tailwind ke manifest pustaka (§15.4).

### 3.2 Classic Script, Bukan ES Module
`<script type="module">` tidak berjalan pada `file://` karena kebijakan CORS peramban. Karena juri dapat membuka ZIP secara lokal (BRD R-03), seluruh JS ditulis sebagai *classic script* berformat IIFE dengan **satu** namespace global:

```js
/**
 * Namespace tunggal proyek. Seluruh modul mendaftar di sini.
 * @namespace SL
 */
window.SL = window.SL || {};
```

Urutan `<script defer>` pada setiap halaman: GSAP, ScrollTrigger, `namespace.js`, `storage.js`, `transition.js`, `header.js`, `router.js`, `features/*.js`, `main.js`.

### 3.3 Benang: SVG + GSAP, Bukan Three.js
Three.js tidak ada dalam daftar pustaka yang diizinkan (BRD §9), berat (± 600 KB atau lebih), dan versi modernnya hanya berupa ES module. Benang dibuat sebagai SVG buatan sendiri dan digerakkan GSAP ScrollTrigger (§10.3).

### 3.4 ID dan Checksum
Web Crypto (`crypto.subtle`) tidak dipakai agar tetap berjalan sinkron dan bebas dari syarat *secure context*. Hash memakai **FNV-1a 32-bit** (§8.4). UI **tidak boleh** menyebut SHA-256, BLAKE2, enkripsi, atau "terverifikasi" kecuali benar-benar diimplementasikan.

---

## 4. Design Tokens & Komponen

### 4.1 `css/tokens.css`

```css
/**
 * Token desain Sandi Leluhur. Satu-satunya tempat nilai mentah didefinisikan.
 */
:root {
  /* Warna inti (BRD §6.3) */
  --c-void:      #0D0D0D;  /* Hitam Arang: hero, garis tebal */
  --c-ivory:     #F5F2EB;  /* Putih Gading: Beranda Scroll 2 */
  --c-paper:     #FCF9F2;  /* Kertas Arsip: Arsip, Playground, Dampak, Kredit */
  --c-red:       #D91604;  /* Merah Saga: aksi, tipografi ekspresif */
  --c-brass:     #C4A661;  /* Emas Kuningan: dekoratif (garis, siku, ❖) */
  --c-brass-ink: #8C6E2E;  /* Tinta Kuningan: teks informatif di atas paper/ivory */
  --c-concrete:  #A6A6A6;  /* Abu Beton: teks kode, HANYA di atas void */
  --c-ash:       #6C6B67;  /* Abu Tinta: teks sekunder di atas paper/ivory */

  /* Tipografi */
  --f-display: "Anton", Impact, "Arial Narrow Bold", sans-serif;
  --f-serif:   "Playfair Display", Georgia, "Times New Roman", serif;
  --f-mono:    "JetBrains Mono", ui-monospace, "SFMono-Regular", Menlo, monospace;

  --fs-hero:  clamp(2.5rem, 11vw, 9rem);    /* manifesto Booting */
  --fs-h1:    clamp(2.25rem, 7vw, 5rem);    /* judul halaman (Anton) */
  --fs-h2:    clamp(1.5rem, 3.2vw, 2.5rem); /* subjudul Serif */
  --fs-body:  1rem;                         /* 16 px; 18 px mulai 900 px */
  --fs-label: 0.6875rem;                    /* 11 px, mono kapital */
  --ls-label: 0.12em;
  --lh-body:  1.7;

  /* Spasi: skala 8 px */
  --s-1: 8px;  --s-2: 16px; --s-3: 24px; --s-4: 32px; --s-5: 40px;
  --s-6: 48px; --s-7: 56px; --s-12: 96px; --s-15: 120px; --s-25: 200px;
  --margin-x: 24px;
  --section-y: 96px;

  /* Garis dan bayangan */
  --line-hair: 1px;
  --line-bold: 4px;
  --shadow-hard: 4px 4px 0 var(--c-void);  /* tanpa blur */

  /* Gerak (BRD §7.3) */
  --t-exit: 280ms;
  --t-enter: 420ms;
  --ease: cubic-bezier(.2, .7, .2, 1);

  /* Lapisan (z-index) */
  --z-thread: 1;
  --z-content: 2;
  --z-header: 100;
  --z-progress: 900;
}

@media (min-width: 900px) {
  :root { --margin-x: 120px; --section-y: 200px; --fs-body: 1.125rem; }
}
```

> Nilai `--c-paper`, `--c-brass-ink`, dan `--c-ash` diukur dari desain final. `--c-brass-ink` mencapai ≈ 4,55 : 1 di atas Paper (batas tipis). Untuk teks ≤ 12 px **SEBAIKNYA** memakai `#7A5C14` (≈ 5,9 : 1).

### 4.2 Aturan Warna (ringkasan matriks BRD §6.3)

| Kebutuhan | Pakai | Jangan |
|---|---|---|
| Teks bacaan di atas paper/ivory | `--c-void` | `--c-concrete` (≈ 2,2 : 1) |
| Teks sekunder di atas paper/ivory | `--c-ash` (≈ 5,1 : 1) | `--c-concrete` |
| Label kuningan informatif di atas paper/ivory | `--c-brass-ink` | `--c-brass` (≈ 2,1 : 1) |
| Garis, siku, ❖, hairline | `--c-brass` | Membawa informasi |
| Teks kode di atas void | `--c-concrete`, `--c-ivory` | — |
| Teks Merah Saga di atas void | Hanya ≥ 24 px | Teks biasa |
| Latar hero | `--c-void` | — |

### 4.3 Komponen

| Komponen | Kelas | Spesifikasi |
|---|---|---|
| Tombol utama | `.btn--primary` | Latar Merah Saga, teks Ivory, Mono kapital, tinggi ≥ 56 px, `--shadow-hard`, sudut 0 px. **Maksimal satu per layar** |
| Tombol sekunder | `.btn--outline` | Garis 2 px Void, latar transparan |
| Tautan teks | `.link` | Garis bawah 1 px |
| Label bracket | `.label` | Mono kapital 11 px, `letter-spacing: .12em`, format `[ LABEL // SUBLABEL ]` |
| Tag artefak | `.tag` | Garis 1 px kuningan, teks `--c-brass-ink` |
| Siku kuningan | `.frame` | Empat siku (`::before`, `::after`, dan dua elemen) 12 px garis 1 px `--c-brass` |
| Hairline | `.rule` | `border-top: 1px solid var(--c-brass)` |
| Pemisah ❖ | `.sep` | Glyph ❖ `aria-hidden="true"` |
| Status strip | `.status-strip` | Mono 11 px; isi **harus nyata** (§4.6) |
| Sel grid | `.cell` | Persegi, min 24 × 24 px, glyph `0`/`1` |

### 4.4 Tata Letak dan Spasi
- Grid 12 kolom; margin sisi `--margin-x`; teks rata kiri.
- Jarak antar-elemen memakai skala 8 px. Elemen terkait rapat (16 px), kelompok tak terkait berjauhan (≥ 96 px desktop).
- Minimal ≈ 40% area layar hero dan narasi dibiarkan kosong.
- **Anggaran ornamen:** kosakata ornamen dibatasi pada siku kuningan, hairline kuningan, label bracket, ❖, dan satu segel per layar. Dilarang pola latar (batik/tumpal), bingkai ganda/tripel, bayangan lembut, gradien besar.

### 4.5 Header Global dan Indikator Langkah

```html
<header class="site-header" data-tone="void">
  <a class="site-header__logo" href="index.html" aria-label="Sandi Leluhur, ke Beranda">SL<span class="cursor" aria-hidden="true"></span></a>
  <ol class="steps" aria-label="Langkah perjalanan">
    <li data-step="1">Temukan</li><li data-step="2">Pahami</li>
    <li data-step="3">Tenun</li><li data-step="4">Lestarikan</li>
  </ol>
  <nav aria-label="Utama">
    <a href="index.html">BERANDA</a>
    <a href="arsip.html">ARSIP</a>
    <a href="playground.html">PLAYGROUND</a>
    <a href="dampak.html">DAMPAK</a>
    <a href="kredit.html">KREDIT</a>
  </nav>
  <a class="btn--outline" href="playground.html" data-cta="header">MULAI MENENUN</a>
</header>
```

Aturan:
- Label menu **kanonik**: BERANDA · ARSIP · PLAYGROUND · DAMPAK · KREDIT (sama dengan nama berkas).
- Tautan aktif memakai `aria-current="page"` dan garis bawah Merah Saga.
- Indikator langkah: langkah aktif Merah Saga; di halaman Kredit disembunyikan.
- `data-cta="header"` disembunyikan di Playground dan Dampak.
- **Tidak ada ikon profil/akun** (bertentangan dengan non-goal "tanpa akun").
- Mobile (< 900 px): logo + tombol `MULAI MENENUN` + tombol menu; menu layar penuh berisi lima tautan besar. Tombol aksi **tetap terlihat di luar menu**.

### 4.6 Status Strip (Dampak dan Kredit)
Status strip hanya boleh memuat nilai nyata:

| Kolom desain | Sumber nilai |
|---|---|
| `SYS_NORMAL` / `SYS_LITE` | `NORMAL` bila GSAP termuat dan storage tersedia; `LITE` bila memakai *fallback* |
| `CHKSUM: 0x....` | 16 bit rendah FNV-1a matriks tersimpan; `—` bila belum ada motif |
| `LOC: 07°15'S 112°45'E` | **Dihapus** (koordinat tidak punya makna fungsional) |
| Hitungan berkas, status | Hanya bila sesuai kenyataan (mis. jumlah baris tabel atribusi) |

---

## 5. Router SPA, Transisi & Header Persisten

### 5.1 Mekanisme (`core/router.js`)
Meng-intercept klik pada `<a href>` internal.

**Syarat intersepsi:** tautan satu *origin*, bukan `target="_blank"`, bukan `download`, tanpa tombol pengubah (Ctrl/Cmd/Shift/Alt), bukan sekadar anchor `#`, dan `location.protocol` **bukan** `file:`.

**Transisi lintas halaman:**
1. `e.preventDefault()`.
2. Batalkan navigasi sebelumnya (`AbortController`); navigasi terakhir menang.
3. Tambahkan `is-exiting` pada `<main>` (fade-out 280 ms) **paralel** dengan `fetch(url)`.
4. Tunggu keduanya selesai. Ekstrak `<main>`, `<title>`, dan atribut `<body>` dengan `DOMParser`.
5. Panggil `destroy()` modul halaman lama (§11).
6. Ganti isi `<main>`, perbarui `document.title`.
7. `history.pushState({ url }, '', url)`.
8. Sinkronkan shell: `SL.header.sync(doc.body.dataset)` (§5.4) dan `SL.thread.setScene(...)` (§10.3).
9. `init()` modul halaman baru, hapus `is-exiting` (fade-in 420 ms, pergeseran `y` 12–16 px).
10. Pindahkan fokus ke `<h1>` (`tabindex="-1"`), gulir ke atas, isi `#sr-status`.

```js
/**
 * Router SPA ilusi.
 * @module core/router
 */
(function (SL) {
  'use strict';
  var cache = new Map();   // url -> teks HTML (cache sesi)
  var controller = null;   // AbortController navigasi berjalan

  /** @param {MouseEvent} e */
  function onClick(e) {
    var a = e.target.closest('a[href]');
    if (!a || !isInternal(a, e)) return;
    e.preventDefault();
    go(a.href, { push: true });
  }

  /**
   * Pindah halaman dengan transisi.
   * @param {string} url
   * @param {{push:boolean}} opt
   */
  function go(url, opt) {
    if (controller) controller.abort();
    controller = new AbortController();
    return SL.transition.out()
      .then(function () { return fetchPage(url, controller.signal); })
      .then(function (doc) { swap(doc, url, opt); })
      .catch(function (err) {
        if (err.name === 'AbortError') return;
        location.assign(url);           // fallback normal
      });
  }

  SL.router = { init: init, destroy: destroy, go: go };
})(window.SL = window.SL || {});
```

**Fallback pengamanan:** pada `file://` atau `fetch()` gagal (koneksi/CORS), router membatalkan intersepsi dan navigasi browser berjalan normal. Pada `file://` router tidak dipasang sama sekali.

### 5.2 Registri Halaman (`main.js`)

Modul halaman didaftarkan berdasarkan `data-page` pada `<body>`:

| `data-page` | Modul `init()` |
|---|---|
| `home` | `bootSequence`, `cursorTrail` |
| `arsip` | `explodedView` |
| `playground` | `weaveGrid` |
| `dampak` | `certificate` |
| `kredit` | — |

`SL.thread` dan `SL.header` **bukan** modul halaman: keduanya hidup selama sesi.

### 5.3 Transisi (`core/transition.js`) dan Anti White Flash
- `html` dan `body` berlatar **Void Black**; fade melewati hitam (efek tirai), bukan putih.
- Semua CSS dimuat di setiap halaman sejak awal (tanpa FOUC).
- `min-height` pada `<main>` dijaga untuk mencegah *layout shift*.
- `prefers-reduced-motion`: pergantian cepat (≤ 100 ms), tanpa pergeseran `y`.
- Indikator progres: bila muat > 150 ms, `#nav-progress` tampil.

### 5.4 Sinkronisasi Header (`core/header.js`)
Setiap HTML menyatakan statusnya pada `<body>`:

```html
<body data-page="playground" data-step="3" data-monograf="03" data-tone="paper">
```

`SL.header.sync(data)` melakukan:
1. `aria-current="page"` pada tautan yang cocok dengan `data-page`.
2. Menandai langkah aktif dari `data-step` (`0` = sembunyikan indikator).
3. Mengisi label monograf (`NO. 0X`) bila elemen ada.
4. Menyembunyikan/menampilkan `data-cta="header"` (disembunyikan pada `playground` dan `dampak`).
5. Mengatur `data-tone` header dan footer (`void` atau `paper`).

**Nada header per bagian.** Pada Beranda, header berada di atas dua bagian berbeda (Void lalu Ivory). `IntersectionObserver` pada elemen `[data-tone]` di bawah header mengubah `data-tone` header saat bagian berganti, sehingga teks header selalu kontras.

Pemetaan halaman:

| Halaman | `data-step` | `data-monograf` |
|---|---|---|
| Beranda | 1 | 01 |
| Arsip | 2 | 02 |
| Playground | 3 | 03 |
| Dampak | 4 | 04 |
| Kredit | 0 | 05 |

### 5.5 Kondisi Tepi

| Kondisi | Perilaku |
|---|---|
| `fetch()` gagal | `location.assign(url)` |
| Klik berturut-turut | Navigasi terakhir menang (`AbortController`) |
| *Back/forward* | `popstate` → transisi yang sama, gulir ke atas |
| `file://` | Router tidak dipasang |
| Tautan eksternal | Tidak diintersepsi; `rel="noopener noreferrer"` bila `target="_blank"` |
| JS gagal | `<a href>` asli tetap bekerja; header/footer sudah ada di tiap HTML |
| Prefetch (SEBAIKNYA) | `pointerenter`/`touchstart` mengisi `cache` |

---

## 6. Booting Sequence (`features/boot-sequence.js`)

### 6.1 Susunan Layar (Desktop 1440)
Latar Void. Kolom kiri (≈ 58–70%) berisi teks, kolom kanan (≈ 22–32%) dialokasikan untuk **benang** (§10.3).

| Urutan | Elemen | Isi final |
|---|---|---|
| 1 | Log terminal (2–3 baris, Mono, Concrete) | `> memuat sandi_leluhur.bin` / `> status: siap_` + kursor berkedip |
| 2 | **Judul** (Anton, Merah Saga, 4 baris) | `KOMPUTER` / `PERTAMA` / `DITENUN,` / `BUKAN DITULIS` |
| 3 | **Subjudul** (Playfair italic, Ivory, ≤ 3 baris) | "Naik atau turun. Satu atau nol. Pada helai lungsi, leluhur kita menyimpan sebuah bahasa, jauh sebelum ada layar." |
| 4 | **Aksi utama** | Tombol Merah Saga `MULAI MENENUN →` (tautan ke `playground.html`) |
| 5 | Baris kredibilitas (Mono kecil, hairline kuningan di atasnya) | `TECHTOPIA VOL. 2 · PUSAKA  \|  Kartu berlubang Jacquard, ≈ 1804` |
| 6 | Petunjuk gulir | `GULIR ↓` |

Jarak: judul → subjudul 48 px, subjudul → tombol 56 px (desktop). Semua elemen di atas **harus** muat di dalam 100 `svh` pada 1440 × 900.

### 6.2 Urutan dan Waktu (Aturan 5 Detik)
Judul, subjudul, dan tombol adalah **HTML nyata** yang ada sejak *first paint*. Efek hanya menyembunyikan lalu menyingkapnya.

| t (ms) | Peristiwa |
|---|---|
| 0 | Header, latar, dan kolom benang tampil |
| 0–600 | Baris terminal diketik (18 ms/karakter) |
| 400–1400 | Judul disingkap **per baris** (topeng `translateY` 100% → 0, jeda 120 ms antar-baris). **Bukan** efek ketik per karakter |
| 1400–1900 | Subjudul memudar masuk |
| 1900–2300 | Tombol aksi memudar masuk |
| ≤ 3000 | Semua tuntas (batas keras) |

**Pengaman.** `<head>` memuat satu baris inline yang mengganti kelas `no-js` menjadi `js` pada `<html>` (`document.documentElement.classList.replace('no-js', 'js')`). CSS hanya menyembunyikan elemen saat `.js` aktif, dan memuat animasi *failsafe* yang memaksa elemen tampil setelah 3 detik bila JS gagal:

```css
.js .boot [data-reveal] { opacity: 0; animation: boot-failsafe 0s 3s forwards; }
@keyframes boot-failsafe { to { opacity: 1; } }
```

### 6.3 Perilaku
- **Sekali per sesi:** `sessionStorage['sl_boot_seen']`. Kunjungan berikutnya dalam sesi menampilkan keadaan akhir langsung.
- **Lewati (SEBAIKNYA):** tautan teks kecil `LEWATI` dan tombol `Esc` menampilkan keadaan akhir seketika. (Belum ada di mock; lihat PRD Lampiran A.)
- **`prefers-reduced-motion`:** seluruh teks statis, tanpa efek ketik atau singkap.
- **Peralihan ke Scroll 2:** potongan keras dengan hairline kuningan; `data-tone` header berganti (§5.4). Efek *wipe* digerakkan scroll bersifat opsional (DAPAT).
- **LCP:** elemen LCP adalah teks judul (bukan gambar). CLS = 0.

---

## 7. Interactive Cursor Trail & Input Sentuh (`features/cursor-trail.js`)

### 7.1 Susunan Zona (Desktop 1440)
Latar Ivory, tinggi minimal `100svh`, hairline kuningan di tepi atas.

| Elemen | Isi final |
|---|---|
| Judul (Playfair, tengah atas) | "Gerakkan kursormu, tenun masa lalu ke masa depan." |
| Petunjuk (Mono, di bawah judul) | `GERAKKAN KURSOR DI AREA INI` (sentuh: `KETUK ATAU SERET DI AREA INI`) |
| Kiri | "Masa Lalu" (Playfair italic) + keterangan `serat · pamor · benang emas` |
| Kanan | "Masa Depan" (Playfair roman) + keterangan `kode · biner · mesin` |
| Tengah | Kanvas kosong untuk jejak (lebar bebas ≥ 600 px) |
| Strip bawah | Mono kecil: `SANDI LELUHUR // EDISI ARSIP PRESERVASI` (kiri) dan `KODIFIKASI BINER NUSANTARA` (kanan) |

> **Catatan.** Teks `1440 × 900 MUSEUM SPEC` pada mock adalah sisa prompt dan **tidak boleh** dibawa ke produksi.

Kartu pada mock masih berupa blok abu/hitam; produksi memakai foto close-up nyata (8–12 buah).

### 7.2 Logika
- **Event:** *Pointer Events* untuk semua jenis input (`pointermove`, `pointerdown`). Atribut `touch-action: pan-y` pada zona agar guliran vertikal tetap berjalan sementara seret horizontal menghasilkan jejak.
- **Throttle jarak:** `Math.hypot(dx, dy)`; kartu baru disisipkan bila jarak dari kartu terakhir melebihi **80 px** (desktop) atau **56 px** (sentuh). Pemrosesan dibatasi lewat `requestAnimationFrame` (satu proses per frame).
- **Tap-to-Stamp:** `pointerdown` bertipe sentuh menaruh satu kartu di titik ketukan.
- **Siklus kartu (≈ 1,4 dtk):** muncul 250 ms (`scale` 0,6 → 1, `opacity` 0 → 1, rotasi acak ±7°), tahan 450 ms, memudar 700 ms, lalu `element.remove()`.
- **Batas node aktif:** desktop **12**, mobile **8**. Bila terlampaui, node paling tua dihapus paksa sebelum node baru disisipkan.
- **Ukuran kartu:** ≈ 180 × 240 px (desktop), ≈ 120 × 160 px (sentuh).
- **Z-index:** bertambah, kartu baru di atas.
- Lapisan jejak: `aria-hidden="true"`, `pointer-events: none`, `<img alt="" draggable="false" decoding="async">`.

```js
/**
 * Cursor Trail "Menenun Waktu".
 * @module features/cursor-trail
 */
(function (SL) {
  'use strict';
  var nodes = [];          // kartu aktif, urut dari tertua
  var last = { x: 0, y: 0 };
  var pending = null;      // posisi pointer terbaru untuk rAF
  var raf = 0;
  var disposers = [];

  function onMove(e) {
    if (e.pointerType === 'touch' && !e.isPrimary) return;
    pending = { x: e.clientX, y: e.clientY };
    if (!raf) raf = requestAnimationFrame(flush);
  }

  function flush() {
    raf = 0;
    if (!pending) return;
    var min = SL.isTouch() ? 56 : 80;
    if (Math.hypot(pending.x - last.x, pending.y - last.y) >= min) {
      spawn(pending.x, pending.y);
      last = pending;
    }
    pending = null;
  }

  function init(zone) { /* pasang listener lewat SL.on() dan simpan disposer */ }
  function destroy() {
    cancelAnimationFrame(raf);
    nodes.forEach(function (n) { n.remove(); });
    nodes.length = 0;
    disposers.forEach(function (off) { off(); });
    disposers.length = 0;
  }

  SL.cursorTrail = { init: init, destroy: destroy };
})(window.SL = window.SL || {});
```

### 7.3 Kondisi Tepi

| Kondisi | Perilaku |
|---|---|
| `prefers-reduced-motion` | Tanpa jejak animatif; klik/ketuk menampilkan satu kartu statis yang diganti pada interaksi berikutnya |
| Gambar gagal dimuat (`error`) | Kartu dilewati; tidak ada ikon rusak |
| GSAP gagal | Fallback CSS: transisi `opacity` dasar |
| Tab tidak aktif (`visibilitychange`) | Tidak ada kartu baru |
| Pindah halaman | `destroy()` membersihkan kartu, listener, rAF |

---

## 8. Playground Biner (`features/weave-grid.js`)

### 8.1 Susunan Layar (Desktop 1440)
Latar Paper. Dua kolom dengan garis pemisah tipis.

**Kolom kiri (≈ 55%)**

| Elemen | Isi final |
|---|---|
| Eyebrow (label) | `KODIFIKASI BINER ❖ PRIMER TENUN • MATRIKS 144-BIT` |
| Judul (Anton) | `PROGRAM MOTIFMU` |
| Subjudul (Playfair italic) | "0 = benang turun (pakan terbenam), 1 = benang naik (lungsi timbul) — rekonstruksi geometri songket biner." |
| Kepala kanvas | `KANVAS BINER 12×12` + tag `BENANG EMAS`, kanan: `KURSOR: X:06 Y:04` |
| Penggaris kolom | `01`–`12` di atas grid; kolom aktif ditebalkan |
| Grid 12 × 12 | Bingkai siku kuningan; label baris `01`–`12` di kiri |
| Legenda | "Klik sel matriks untuk mengubah orientasi lungsi emas (1) dan pakan terbenam (0)." |

**Kolom kanan (≈ 35%)**

| Blok | Isi |
|---|---|
| Kurasi singkat | `[ KURATORIAL // KORPUS 03 ]`, judul "Petunjuk Penenun & Arsip Register", satu paragraf pengantar |
| Readout biner | Judul `BARIS · SEKUENS (PAKAN)` dan `HEX DUMP`; 12 baris (lihat §8.3); baris aktif disorot |
| Ringkasan | `BENANG NAIK (1): 72` · `BENANG TURUN (0): 72` · `KERAPATAN: 50.0%` |
| Transformasi matriks | `TENUN`, `BERSIHKAN`, `BALIK`, `ACAK` (lihat §8.5) |
| Pemilik | Label `NAMA PENJAGA (OPSIONAL)` + kolom isian; contoh isian: `Contoh: Dewi Lestari` |
| Aksi utama | Tombol Merah Saga `[ SIMPAN & LIHAT SERTIFIKAT → ]` |
| Baris kepercayaan | "Gratis · tanpa akun · motif tersimpan di perangkatmu saja" |

### 8.2 Struktur Data dan Render
Kanvas direpresentasikan sebagai matriks 2 dimensi, contoh `var motif = [[0,1,0],[1,0,1]];`.

- Grid memakai satu elemen `role="grid"` dengan `n × n` tombol (`<button role="gridcell">`) dan **satu** pendengar peristiwa (delegasi).
- Klik/ketuk mengubah satu sel (0 ↔ 1), memperbarui array, menukar kelas `cell--on` (Merah Saga + glyph Ivory), dan memperbarui **hanya** sel serta baris readout yang berubah (tanpa render ulang penuh).
- Sel mati: latar Void + glyph Concrete. Sel aktif: latar Merah Saga + glyph Ivory. Status **tidak** dibawa oleh warna saja (glyph `0`/`1`).
- `aria-label` per sel: "Baris 3, kolom 5, 1, benang naik".

### 8.3 Readout Biner

Untuk setiap baris `r` (1-indeks, dua digit):

```
R03 | 001100001100 | 4            0x30C
 │        │          │              │
 │        │          │              └ hex = parseInt(bits, 2) → huruf besar, lebar ceil(n/4)
 │        │          └ jumlah benang naik pada baris
 │        └ string biner baris
 └ label baris
```

Rumus ringkasan:
- `naik = jumlah semua sel 1`, `turun = n² − naik`.
- `kerapatan = naik / n² × 100`, satu desimal, format `50.0%`.
- **Baris aktif** (sorot Kuningan di sisi kiri + teks tebal): baris sel yang terakhir difokus atau diubah.
- **`KURSOR: X:kk Y:bb`**: kolom dan baris sel yang sedang di-*hover* atau memiliki fokus keyboard (dua digit, 1-indeks). Menampilkan `—` bila tidak ada.

### 8.4 Penyimpanan (`localStorage`) dan Identitas Motif

**Key:** `sandi_leluhur_data`

**Payload (versi 2):**

```json
{
  "version": 2,
  "metadata": {
    "namaPenenun": "Pengunjung",
    "tanggal": "2026-10-23T14:30:00Z",
    "idTerminal": "SL-9A3F1B"
  },
  "gridSize": 12,
  "matriksBiner": [
    [0,1,1,0,0,1,1,0,0,0,1,0],
    [1,0,0,1,1,0,0,1,0,0,0,1]
  ]
}
```

(Contoh hanya memperlihatkan dua baris; payload sebenarnya memuat `gridSize` baris.)

**Validasi saat membaca:** `version === 2`; `gridSize ∈ {8, 12, 16}`; matriks berukuran `gridSize × gridSize`; setiap sel `0` atau `1`; `namaPenenun` string. Bila salah satu gagal, data **diabaikan** dan aplikasi mulai kosong tanpa galat.

**Nama penenun:** dipangkas (*trim*), maksimum 32 karakter, karakter kontrol dibuang, kosong menjadi `Pengunjung`. Selalu ditulis ke DOM dengan `textContent` (bukan `innerHTML`).

**Identitas yang diturunkan (nyata, bukan statis):**

```js
/**
 * Hash FNV-1a 32-bit.
 * @param {string} str
 * @returns {number} bilangan tak bertanda 32-bit
 */
function fnv1a(str) {
  var h = 0x811c9dc5;
  for (var i = 0; i < str.length; i++) {
    h ^= str.charCodeAt(i);
    h = Math.imul(h, 0x01000193) >>> 0;
  }
  return h >>> 0;
}

// Contoh: input = baris-baris matriks digabung, dipisah "|"
// hex8 = fnv1a(input).toString(16).toUpperCase().padStart(8, '0')
// hex6 = hex8.slice(-6)
//   idTerminal   = 'SL-' + hex6              // mis. SL-9A3F1B
//   nomorPiagam  = 'PUSAKA-' + tahun + '-' + hex6
//   kodeMotif    = '0x' + hex6
//   checksum16   = '0x' + hex8.slice(-4)     // untuk status strip
```

Pola yang sama menghasilkan ID yang sama (ID adalah "turunan pola").

**Penulisan:** didebounce 300 ms dan di-*flush* pada `pagehide` serta sebelum navigasi router. Seluruh `localStorage` dibungkus `try...catch` (Mode Incognito dapat memblokir). Bila gagal, status disimpan di `SL.memory` (RAM). Karena SPA tidak memuat ulang halaman, motif tetap sampai ke Dampak walau storage gagal; bila halaman di-*refresh*, data hilang dan **banner informatif** ditampilkan (PRD US-511).

### 8.5 Interaksi dan Kontrol

| Input | Perilaku |
|---|---|
| Klik/ketuk | Ubah satu sel |
| Seret | Melukis banyak sel dengan nilai = kebalikan sel pertama yang disentuh; `pointerdown` memanggil `setPointerCapture`, `pointermove` memakai `document.elementFromPoint` |
| Sentuh | `touch-action: none` hanya pada grid; di luar grid halaman tetap menggulir |
| Keyboard | Roving `tabindex`; panah memindahkan fokus; `Home`/`End` ke awal/akhir baris; `Spasi`/`Enter` mengubah sel; `Ctrl/Cmd+Z` Undo, `Ctrl/Cmd+Shift+Z` Redo |

**Tombol pada mock:** `TENUN`, `BERSIHKAN`, `BALIK`, `ACAK` (prioritas SEBAIKNYA). `CERMIN`, `UNDO/REDO`, dan `PRESET` **belum ada di mock**; spesifikasinya dipertahankan (PRD US-504, US-505) dan perlu ditambahkan ke desain atau diturunkan ke DAPAT.

- **TENUN:** menyorot baris demi baris dengan jeda 120 ms; `prefers-reduced-motion` menampilkan semuanya sekaligus; dibatalkan pada `destroy()`.
- **BALIK:** `1 − nilai` untuk semua sel. **BERSIHKAN:** semua `0`. **ACAK:** peluang 0,5 per sel. **CERMIN** (SEBAIKNYA): cerminkan sisi kiri ke kanan.
- **Riwayat Undo/Redo:** maksimum 50 langkah, menyimpan salinan matriks.
- Ukuran grid 8 / 12 / 16 (DAPAT; mock hanya 12). Lebar hex mengikuti `ceil(n/4)`.
- Sel minimum 24 × 24 px (WCAG 2.2, 2.5.8).

### 8.6 Aksi Utama
Tombol `SIMPAN & LIHAT SERTIFIKAT →`: membaca nama, menulis storage secara sinkron, lalu `SL.router.go('dampak.html')`.

### 8.7 Kondisi Tepi

| Kondisi | Perilaku |
|---|---|
| Pertama kali | Grid kosong + legenda "0 = benang turun, 1 = benang naik" |
| Kembali berkunjung | Motif dipulihkan |
| `localStorage` tidak tersedia | Banner informatif; sesi berjalan di RAM |
| Data rusak | Diabaikan |
| Mobile (< 900 px) | Judul ringkas → grid persegi lebar penuh → panel kontrol (tombol ≥ 48 px) → readout |

---

## 9. Dampak & Sertifikat (`features/certificate.js`)

### 9.1 Susunan Layar (Desktop 1440)
Latar Paper. Dari atas ke bawah:

1. **Strip katalog:** `SANDI LELUHUR | Katalog Monolitik Komputasi Biner Nusantara` (kiri); tag `KORPUS ED-01` dan `© 2026 PRESERVASI TERBUKA` (kanan).
2. **Header** global (§4.5) dan **status strip** (§4.6).
3. **Eyebrow:** `[ EPILOG // PIAGAM PENJAGA PUSAKA ] :: [ NO. PUSAKA-2026-9A3F1B ]` dan satu kalimat pengantar.
4. **Dua kolom:** kiri kartu sertifikat (≈ 2/3), kanan kolom aksi (≈ 1/3).
5. **Footer** (§15.5).

### 9.2 Komposisi Kartu Sertifikat
Kartu pos kuno bertemu terminal: bingkai garis 4 px Void, bayangan keras, satu segel kuningan.

| Zona | Isi final |
|---|---|
| Kepala | `KODEKS PRESERVASI NUSANTARA` (kiri) dan `LEMBAR PIAGAM DIGITAL` (kanan) |
| Nomor | `NO. PIAGAM: PUSAKA-2026-9A3F1B // STATUS: DIBUAT UNTUKMU` |
| Judul | `PENJAGA PUSAKA` (Anton) |
| Kutipan | "Dengan ini menenun masa lalu ke masa depan." |
| Blok motif | Tag `[ BLOK: MATRIKS-SONGKET-12 ]`, `ASAL INSPIRASI: [diisi dari mitra nyata]`, `KODE MOTIF: 0x9A3F1B // SANDI LELUHUR` |
| Perangko | Matriks motif pengguna (piksel Merah Saga/putih), keterangan `POS PUSAKA 7500 // IDR`, tulisan `ARSIP BINER` |
| Cap pos | Bulat, tanggal format Indonesia (mis. `9 OKT 2026`) |
| Terminal (Void) | `TERMINAL REKAMAN // NODE: PERANGKAT-INI`, `NAMA PENJAGA`, `ID MOTIF`, `MOTIF BINER` (tiga baris pertama), `CHECKSUM (FNV-1A): 0x…` |
| Kaki | Segel `SL 2026`, `[ SANDI LELUHUR · TECHTOPIA VOL. 2 ]`, "Dirancang oleh [Nama Tim]", dan catatan "Piagam simbolis, bukan dokumen resmi." |

**Kolom aksi (kanan):**
1. Tombol Merah Saga `[ DUKUNG PENGRAJIN → ]` dan baris mitra: `Mitra Pengrajin: [Nama Mitra], [Daerah]`.
2. Tiga tombol garis: `UNDUH PNG`, `BAGIKAN SERTIFIKAT`, `TENUN ULANG (PLAYGROUND)`.
3. Ringkasan nyata: `MOTIF: 12 × 12 · 72 NAIK · 72 TURUN`, `TERSIMPAN: DI PERANGKAT INI`, `CHECKSUM 0x9A3F1B`.

### 9.3 Aturan Kejujuran Konten (mengikat)
Bagian berikut pada mock **tidak boleh** dibawa ke kode karena menyatakan sesuatu yang tidak benar atau tidak ada:

| Pada mock | Masalah | Pengganti |
|---|---|---|
| `PUSAKA.GOV`, `OTORITAS SERTIFIKASI TINGKAT I`, `DIREKTORAT MESIN BINER PERTAMA`, `KODEKS NASIONAL PUSAKA DIGITAL`, `ARSIP NASIONAL INDONESIA` | Menyiratkan afiliasi pemerintah/lembaga yang tidak ada | Nama proyek dan tim |
| `RESMI TEROTENTIKASI`, `KONTRAK RESMI LEMBAR SAH` | Klaim keabsahan | "Dibuat untukmu", "Piagam simbolis" |
| `ENKRIPSI: AKTIF [BLAKE2B]`, `HASH SHA-256`, `ENKRIPSI FISIK AKTIF` | Tidak diimplementasikan | Checksum FNV-1a yang benar-benar dihitung |
| `TERPERMANENKAN (IMMUTABLE)`, `KONSENSUS ARSIP`, `TERDESENTRALISASI` | Data ada di `localStorage` dan dapat diubah | Ringkasan motif dan lokasi simpan nyata |
| `99.98% VERIFIKASI`, `1.048.576 OKTET` | Angka tidak bersumber | Dihapus atau diganti nilai terukur (§15.5) |
| `LOKASI FISIK: TUBAN / SILUNGKANG`, mitra "Komunitas Penenun … Tuban & Silungkang" | Organisasi/tempat belum divalidasi (BRD D-02) | Isi dengan mitra nyata atau hapus |
| Nama motif (`PUCUK REBUNG`, `ITIK PULANG PATANG`, `KANCANG BAPATOLA`) pada pola 12-bit buatan pengguna | Menyiratkan pola itu adalah motif tradisional asli | Hapus, atau tampilkan hanya setelah divalidasi kurator (PRD Q-04) |
| `LOC: 07°15'S 112°45'E`, `© 2024` | Tanpa makna / tahun keliru | Hapus; gunakan `© 2026` |

### 9.4 Ekspor PNG dan Bagikan
Tanpa library eksternal. Render ulang kartu pada `<canvas>` 2D:

1. Tunggu `document.fonts.ready` (Anton, Playfair, JetBrains Mono harus siap).
2. Kanvas 1520 × 960 px (2×). Gambar latar, bingkai, teks, matriks perangko (kotak piksel), cap pos (lingkaran + teks), blok terminal.
3. `canvas.toBlob()` → `URL.createObjectURL` → `<a download="penjaga-pusaka-SL-9A3F1B.png">` → `revokeObjectURL`.
4. **Bagikan:** bila `navigator.canShare({files:[file]})` tersedia, panggil `navigator.share`; bila tidak, tawarkan unduh PNG.

### 9.5 Kondisi Tepi

| Kondisi | Perilaku |
|---|---|
| Ada motif valid | Render sertifikat |
| Tidak ada motif / data rusak | **State kosong**: judul `PIAGAMMU MENUNGGU MOTIF PERTAMAMU`, satu kalimat, tombol `MULAI MENENUN →` ke Playground (mock belum ada; PRD Lampiran A) |
| Font gagal | Sertifikat tetap dirender dengan font cadangan |
| Ekspor gagal | Pesan jelas; tombol tetap dapat dicoba ulang |
| Tautan mitra masih `[…]` | **Gerbang rilis gagal** (SRS §13.4) |
| CTA UMKM | `target="_blank" rel="noopener noreferrer"` |

---

## 10. Animasi GSAP: Exploded View, Reverse Time-Scroll, dan Benang

### 10.1 Dasar
- GSAP Core + ScrollTrigger via CDN dengan versi di-*pin* dan SRI (§2.3).
- Bila GSAP tidak termuat, `<html>` mendapat kelas `no-gsap`; CSS memberi transisi dasar dan konten tetap terbaca (PRD US-903).
- `prefers-reduced-motion`: tidak ada *pin* maupun *scrub*; konten tampil statis berurutan.
- Semua `ScrollTrigger` diberi `id` agar dapat dibersihkan terarah (§11).

### 10.2 Arsip Sandi: Exploded View + Reverse Time-Scroll (`features/exploded-view.js`)

**Susunan layar (Desktop 1440).** Latar Paper. Kiri: SVG alat tenun terurai di dalam bingkai siku kuningan. Kanan:

| Urutan | Isi final |
|---|---|
| Judul (Anton, Merah Saga) | `LUNGSI = 0 / 1` (berganti sesuai bagian aktif; lihat tabel di bawah) |
| Paragraf (Playfair, 18 px) | "Benang lungsi yang terangkat membentuk logika biner murni: status '1' saat terangkat dan '0' saat diturunkan. Dari selang-seling inilah barisan tenun dieksekusi baris demi baris layaknya *punched card* sebelum era komputasi modern." |
| Register (Mono) | `REGISTER BINER // [ 1 0 1 1 0 0 1 0 ] · 8-BIT PER BARIS WEFT` |
| Tahun (Anton raksasa) | `1804` |
| Keterangan tahun (Mono) | `≈ 1804 · KARTU BERLUBANG JACQUARD` |
| Aksi utama | `UJI LOGIKA DI PLAYGROUND →` |

> Pada mock keterangan tahun berbunyi "… JACQUARD & MESIN TENUN GEDOGAN". Gedogan jauh lebih tua dari 1804, sehingga gabungan itu menyesatkan. Pisahkan atau hapus bagian gedogan.

**Struktur SVG** (`assets/svg/loom-exploded.svg`, disisipkan inline agar dapat dianimasikan):

| Grup | `id` | Label pada mock |
|---|---|---|
| Penggulung lungsi | `penggulung-lungsi` | `PENGGULUNG LUNGSI` |
| Sisir | `sisir` | `SISIR (REED)` |
| Lungsi | `lungsi` | `LUNGSI (WARP)` (garis Merah Saga) |
| Gulungan kain | `gulungan-kain` | `GULUNGAN KAIN` |

**Bagian aktif dan teks.** Empat bagian bergantian pada ambang progres 0 / 0,25 / 0,5 / 0,75. Setiap bagian memiliki judul Anton, satu paragraf, dan padanan biner. Keempat teks ada di DOM; yang tidak aktif disembunyikan secara visual dengan kelas, **bukan** `display:none` pada konten yang perlu dibaca *screen reader*.

**ScrollTrigger:**

```js
var tl = gsap.timeline({
  scrollTrigger: {
    id: 'exploded',
    trigger: '#arsip-stage',
    start: 'top top',
    end: '+=300%',
    pin: true,
    scrub: 1,
    onUpdate: function (self) { updateYear(self.progress); setPart(self.progress); }
  }
});
tl.to('#sisir',            { x: 120, y: -80, rotation: -6 }, 0)
  .to('#penggulung-lungsi',{ x: -100, y: -60 }, 0)
  .to('#gulungan-kain',    { x: 90, y: 90 }, 0);
```

**Reverse Time-Scroll.** Teks tahun memanipulasi `textContent` berdasar proksi persen scroll:

```js
function updateYear(p) {
  year.textContent = Math.round(gsap.utils.interpolate(2026, 1804, p));
}
```

Rentang 2026 → 1804 sesuai desain final. Penanda yang lebih dalam (mis. "tenun tradisional Nusantara") hanya dipakai bila kurator menetapkannya (PRD Q-04). Seluruh tahun ditandai `≈` (perkiraan). Teks statis `<span class="sr-only">Perkiraan tahun 1804</span>` disediakan untuk pembaca layar; angka animasi diberi `aria-hidden="true"`.

**Mobile (< 900 px):** komposisi vertikal, ilustrasi di atas dan teks di bawah, label tidak saling menumpuk, interaksi cukup dengan scroll.

### 10.3 Benang Sepanjang Situs (`features/thread.js`)

Lapisan `#thread-layer` tetap di luar `<main>`. Serat adalah persediaan yang berkurang sampai tuntas; bukan ujung lepas. Implementasi satu HTML/lima section dipertahankan sesuai keputusan pengguna, tanpa mengembalikan header atau lima berkas HTML.

Urutan kanonik: `home` (section `beranda`), `arsip`, `playground`, `dampak`, `kredit`. Model:

```text
siteProgress = (indeksSection + progresGulirSection) / 5
seratTersisa = 1 - siteProgress
posisiSimpulY = 0.85 × tinggiLapisan × seratTersisa
```

Progres lokal dihitung antara posisi atas section aktif dan posisi atas section berikutnya. Untuk Kredit, batas akhirnya adalah dasar dokumen yang dapat digulir, termasuk footer. Nilai dijepit 0..1. Batas diperbarui sesudah pin Arsip, font, perubahan piagam dan resize diukur ulang. Perhitungan berasal dari DOM/posisi gulir; reload, hash langsung dan file lokal tidak memerlukan state sesi.

| Section | Indeks | Rentang siteProgress | Posisi simpul (fraksi tinggi lapisan) |
|---|---|---|---|
| Beranda | 0 | 0..0,2 | 0,85..0,68 |
| Arsip | 1 | 0,2..0,4 | 0,68..0,51 |
| Playground | 2 | 0,4..0,6 | 0,51..0,34 |
| Dampak | 3 | 0,6..0,8 | 0,34..0,17 |
| Kredit | 4 | 0,8..1 | 0,17..0 |

Batas interval menyambung persis: `(i + 1)/5 = ((i + 1) + 0)/5`. Simpul bergerak ke atas (Y berkurang). Navigasi melompat nonberurutan dan back/forward diperhalus selama 600 ms; gulir biasa reversibel. Router hanya memakai API publik `SL.thread.setScene(indeks)`; API ini bukan penyimpan state wajib dan tidak mengubah posisi gulir.

Saat `seratTersisa <= 0.04`, serat terakhir ditarik habis dan simpul keluar layar dengan fade/translate paling lama 300 ms. Hanya kolom biner dan keterangan Mono `SELESAI DITENUN` yang tertinggal. Keterangan dekoratif tersembunyi dari pembaca layar dan baru dihapus lagi setelah `seratTersisa > 0.08`, sehingga ambang tidak berkedip. Menggulir naik mengembalikan serat dan simpul.

Jika dokumen akhir tidak bisa digulir (`scrollHeight <= innerHeight + 8`), penyelesaian berbasis waktu dimulai 1,5 detik setelah konten siap. Preferensi reduced-motion tidak memakai tween: tampilkan posisi aktual secara statis, termasuk keadaan habis saat sudah di dasar Kredit.

SVG digambar dalam piksel lapisan agar digit tidak terdistorsi. Klip hanya berlaku pada serat, bukan seluruh SVG. Digit memakai bit motif tersimpan (event `sl:motif` memperbaruinya) atau pola bawaan; 56 desktop/24 mobile, sekitar 60 node SVG, tanpa filter dan tanpa `will-change` permanen. Label dapat berupa node HTML di lapisan yang sama. Lapisan `aria-hidden`, `pointer-events:none`, tidak menangkap fokus. Lebar hero dan ruang konten tetap seperti desain awal.

`init()` idempoten; `destroy()` melepas listener, rAF, timer, interpolasi, node buatan dan referensi. Modul memakai scroll native + rAF sehingga tidak membuat ScrollTrigger sendiri; trigger fitur lain tetap dimiliki fiturnya. Tanpa JS/GSAP/ScrollTrigger, lapisan disembunyikan dan konten tetap dapat dipakai. Atribut rentang benang per halaman tidak dipakai lagi.

---

## 11. Manajemen Memori & Siklus Hidup

Berhubung perpindahan halaman tidak memicu *refresh* penuh, memori dikelola manual.

### 11.1 Kontrak Modul
Setiap modul fitur mengekspor `init()` dan `destroy()`. Router memanggil `destroy()` modul halaman lama **sebelum** mengganti `<main>`, lalu `init()` modul halaman baru setelahnya.

### 11.2 Daftar Sumber Daya dan Pelepasannya

| Modul | Sumber daya | Dilepas dengan |
|---|---|---|
| `cursor-trail` | Listener `pointermove`/`pointerdown`, rAF, node `<img>`, `visibilitychange` | `off()`, `cancelAnimationFrame`, `remove()` semua node |
| `boot-sequence` | Timeline GSAP, interval/timeout ketik | `timeline.kill()`, `clearTimeout` |
| `exploded-view` | `ScrollTrigger` (id `exploded`), timeline | `ScrollTrigger.getById('exploded').kill()`, `timeline.kill()` |
| `weave-grid` | Delegasi listener grid, `keydown`, timer `TENUN`, debounce simpan | `off()`, `clearInterval`, `flush()` lalu `clearTimeout` |
| `certificate` | `ObjectURL`, kanvas sementara | `URL.revokeObjectURL`, buang referensi kanvas |
| `thread` | `ScrollTrigger` (id `thread`), tween `state` | **Tidak** di-destroy saat pindah halaman; hanya `setScene()` |

### 11.3 Pembantu Listener (`core/namespace.js`)

```js
/**
 * Pasang listener dan kembalikan fungsi pelepasnya.
 * @param {EventTarget} el
 * @param {string} type
 * @param {Function} fn
 * @param {object} [opts]
 * @returns {Function} off
 */
SL.on = function (el, type, fn, opts) {
  el.addEventListener(type, fn, opts);
  return function off() { el.removeEventListener(type, fn, opts); };
};
```

### 11.4 Prosedur Uji
1. Buka DevTools → Memory → *Heap snapshot* baseline.
2. Lakukan 20 perpindahan halaman antar kelima halaman dan gerakkan kursor 5 menit di Beranda.
3. Ambil snapshot kedua: **nol *detached DOM node*** dan heap stabil.
4. Konsol: `getEventListeners(document)` dan pada elemen zona kembali ke jumlah baseline.
5. `ScrollTrigger.getAll()` hanya berisi `thread` (+ `exploded` di Arsip).

---

## 12. Responsif, Mobile-First & Aksesibilitas

### 12.1 Strategi Responsif
- CSS **mobile-first**: basis 320 px, peningkatan lewat `min-width`. Titik patah: 480, 768, **900** (tata letak dua kolom), 1200, 1440.
- Tipografi raksasa memakai `clamp()` (§4.1). Pada 320 px kata terpanjang manifesto (`BUKAN DITULIS`) harus muat tanpa *horizontal scroll*.
- Tinggi hero memakai `100svh`/`dvh` dengan *fallback* `vh`; *safe-area* dihormati (`env(safe-area-inset-*)`, `viewport-fit=cover`).
- Efek hover hanya di `@media (hover: hover) and (pointer: fine)`.

### 12.2 Perilaku Mobile per Halaman

| Halaman | Perilaku |
|---|---|
| Beranda | Benang menjadi garis tipis di tepi kanan; layar pertama hanya berisi judul, subjudul, tombol; Trail → Tap-to-Stamp dan Swipe-to-Weave |
| Arsip | Komposisi vertikal; label tidak menumpuk |
| Playground | Grid di atas, panel kontrol di bawah (tombol ≥ 48 px), readout paling bawah |
| Dampak | Kartu lebar penuh, kolom aksi di bawahnya |
| Kredit | Satu kolom; garis waktu menjadi bagian setelah catatan kurasi; tabel atribusi dapat digulir horizontal **di dalam wadahnya sendiri** (`overflow-x:auto`) |

> Mock final baru tersedia untuk desktop. Versi mobile mengikuti aturan di atas dan perlu mock tersendiri (PRD Lampiran A).

### 12.3 Target Sentuh
Navigasi/tombol utama ≥ 44 × 44 px (CTA 48–56 px); sel grid ≥ 24 × 24 px.

### 12.4 Aksesibilitas
1. **Semantik:** landmark `header/nav/main/footer`, satu `<h1>` per halaman, `lang="id"`.
2. **Skip link** ke `#konten`; fokus terlihat (outline ≥ 2 px kontras tinggi); urutan tab logis.
3. **Navigasi SPA:** fokus dipindah ke `<h1>`, `document.title` diperbarui, `#sr-status` diumumkan.
4. **Grid:** `role="grid"`, roving `tabindex`, `aria-label` per sel (§8.2).
5. **Dekoratif disembunyikan:** `#thread-layer`, lapisan jejak, ❖, ornamen, dan status strip dekoratif memakai `aria-hidden="true"`.
6. **Kontras:** ikuti §4.2 dan BRD §6.3; informasi tidak dibawa warna saja.
7. **Ukuran teks:** bacaan 16–18 px; label Mono kapital **minimal 11 px**.
8. **`prefers-reduced-motion`:** nonaktifkan efek ketik, pin/scrub, jejak, dan benang animatif; sediakan padanan statis.
9. **Kontrol timer/animasi:** efek otomatis ≤ 5 detik atau dapat dilewati.

### 12.5 Ketahanan
Konten inti adalah HTML nyata sehingga tetap terbaca tanpa JS atau CDN. `localStorage` bersifat opsional.

---

## 13. Kepatuhan Lomba & Standar Kode

### 13.1 Standar Kode
1. **Format transparan:** seluruh HTML, CSS, dan JS **tidak diminifikasi** dan berkomentar (JSDoc untuk JS; komentar bagian pada CSS).
2. **Anti-kompilasi:** tanpa Vite, Webpack, SSG, Sass, atau transpiler.
3. **Lingkup eksekusi:** setiap modul dibungkus **IIFE** dan hanya mendaftar pada `window.SL` (§3.2); tidak ada variabel global lain.
4. **Aksesibilitas awal:** komponen interaktif memakai `tabindex="0"`, `aria-label`, dan merespons `keyup` `Enter`/`Space` bila bukan elemen `<button>` asli (utamakan elemen semantik asli).
5. **Konvensi:** `camelCase` untuk fungsi dan variabel, `SCREAMING_SNAKE` untuk konstanta, BEM-lite untuk CSS, berkas JS satu tanggung jawab.

### 13.2 Daftar Periksa Kepatuhan Aturan (BRD §9)

| Aturan | Cara verifikasi |
|---|---|
| Static HTML/CSS/Vanilla JS, ≤ 10 HTML | `ls *.html` = 5 |
| Tanpa React/Vue/Svelte/Angular/Node | Tidak ada `package.json`, `node_modules` |
| Tanpa UI library instan, website builder | Pencarian pada kode dan `<head>` |
| Tanpa minify/obfuscate | Buka berkas; periksa baris panjang tanpa spasi |
| Hanya GSAP + ScrollTrigger via CDN | Periksa semua `<script src>` |
| Navigasi `fetch()` + `pushState()` tanpa white flash | Uji manual §14 |
| Cursor Trail dan Grid murni DOM | Tinjau `cursor-trail.js`, `weave-grid.js` |
| State via `localStorage` | Tinjau `storage.js` |
| Mobile-first | `min-width` pada media query |
| Tanpa proses build | Tidak ada konfigurasi bundler |

### 13.3 Artefak Terlarang
`package.json`, `node_modules/`, `vite.config.*`, `webpack.config.*`, berkas `*.min.js`/`*.min.css` **di dalam folder proyek** (berkas minified milik pustaka CDN pihak ketiga tidak termasuk), `tailwind.config.*`, import `three`, jQuery.

### 13.4 Gerbang Rilis: Pencarian Sisa Placeholder dan Klaim Palsu
Perintah yang harus **tidak menghasilkan temuan** sebelum pengumpulan:

```bash
grep -rniE "MUSEUM SPEC|PUSAKA\.GOV|© ?2024|lorem|TODO|FIXME|Nama Mitra|\[isi" --include="*.html" --include="*.css" --include="*.js" --include="*.json" .
grep -rniE "BLAKE2B|SHA-256|IMMUTABLE|TERDESENTRALISASI|ARSIP NASIONAL INDONESIA|OTORITAS SERTIFIKASI" --include="*.html" --include="*.js" .
```

Setiap angka pada UI harus berasal dari state nyata atau dihapus (BR-14).

### 13.5 Sinkronisasi Shell (BRD R-09)
Tanpa build, bagian berikut **identik** di kelima HTML dan dicek manual: skip link, header, `#thread-layer`, `#sr-status`, footer, urutan `<script>`. Daftar periksa tersedia di `README.md`; hanya `<main>`, `<title>`, dan atribut `<body>` yang boleh berbeda.

---

## 14. Matriks Uji Perangkat & QA

### 14.1 Matriks Lebar dan Perangkat

| Lebar | Contoh | Wajib |
|---|---|---|
| 320 | iPhone SE lama | Nol *horizontal scroll*, judul tidak terpotong |
| 360 | Android kecil | Idem |
| 390 | iPhone modern | Idem |
| 768 | Tablet potret | Tata letak sebelum 900 px |
| 1024 | Tablet lanskap/laptop kecil | Tata letak dua kolom |
| 1440 | Desktop (target mock) | Seluruh *above the fold* Beranda muat dalam 900 px tinggi |
| 1920 | Monitor lebar | Margin dan ruang kosong terjaga |

Peramban: dua versi terakhir Chrome, Edge, Firefox, Safari (desktop + mobile). Minimal satu uji pada ponsel nyata.

### 14.2 Skenario Uji

| Skenario | Lulus bila |
|---|---|
| Lighthouse mobile (simulasi) | Performance ≥ 85, Accessibility ≥ 95, Best Practices ≥ 95, SEO ≥ 90; LCP ≤ 2,5 dtk; CLS ≤ 0,1 |
| Uji 5 detik | 5 penguji dapat menyebut isi situs dan aksi utama setelah 5 detik di Beranda |
| Memori | Prosedur §11.4 lulus |
| Keyboard saja | Seluruh Playground dapat dioperasikan; fokus terlihat |
| `prefers-reduced-motion` | Tidak ada efek ketik/pin/scrub/jejak animatif |
| `file://` | Tautan bekerja (router nonaktif); semua halaman terbaca |
| Tanpa JS | Konten inti terbaca; judul/subjudul/tombol tampil (failsafe 3 dtk) |
| CDN diblokir | Kelas `no-gsap`; konten tetap terbaca |
| `localStorage` diblokir | Banner muncul; sesi tetap menyimpan di RAM; sertifikat tetap tampil dalam SPA |
| Koneksi lambat (Slow 3G) | Indikator progres muncul > 150 ms; tidak ada layar putih |
| Back/forward | URL dan konten sesuai; header tersinkron |
| Benang | ≥ 55 fps pada desktop menengah; tidak menunda render judul |

### 14.3 Uji Visual terhadap Desain Final
Bandingkan hasil dengan mock pada 1440 px untuk: ukuran dan baris judul, jarak judul → subjudul → tombol, proporsi dua kolom Playground, komposisi sertifikat, dan susunan halaman Kredit. Penyimpangan yang disengaja (§9.3, §5.4, PRD Lampiran A) dicatat di `README.md`.

---

## 15. Halaman Kurasi & Kredit

### 15.1 Susunan (Desktop 1440)
Latar Paper. Urutan:

1. Header global dan status strip (nilai nyata, §4.6).
2. **Hero** *Kredit*: label `[ KODE KATEGORI: KURATORIAL ]`, judul Anton `KURASI & KREDIT`, garis `ONTOLOGI TENUN & KOMPUTASI // SEKSI DOKUMENTASI`, kartu `INDEX STATUS` (hanya berisi hitungan nyata).
3. **Kolom utama (≈ 60%)**
   - **Seksi 01, Catatan Kurasi.** "Nalar Analogi & Batas Historis": menyatakan bahwa klaim manifesto adalah **analogi dan provokasi kuratorial**, bukan klaim keutamaan kronologis; menyebut Jacquard (1804) sebagai tonggak kartu berlubang; kutipan pembuka memakai **teks manifesto aktif**: "Komputer pertama ditenun, bukan ditulis." Disertai catatan penegasan (kotak bergaris Merah Saga di kiri).
   - **Seksi 03, Matriks Atribusi Arsip** (§15.3).
4. **Kolom samping (≈ 35%)**: **Seksi 02, Kontinuum Nalar Biner** (§15.2).
5. Footer (§15.5).

### 15.2 Garis Waktu (Kontinuum Nalar Biner)

| Penanda | Judul | Isi (arah) | Catatan |
|---|---|---|---|
| `≈ ABAD KE-8` | Tenun Gedogan Nusantara | Pengetahuan pola diturunkan lisan dan kinetik antargenerasi | **Mock menyebut "pola tertua tercatat di relief Candi Borobudur".** Klaim ini butuh sumber; bila tak ada, pakai rumusan netral di samping (PRD Q-04) |
| `1804` | Mesin Tenun Jacquard | Joseph Marie Jacquard (Lyon, Prancis) memperkenalkan pembacaan kartu berlubang untuk mengendalikan pola tenun secara otomatis | Terpakai pada Arsip |
| `1843` | Algoritma Pertama Ada Lovelace | Mesin Analitis Babbage dirancang memakai logika kartu gaya Jacquard; Lovelace menulis program yang sering disebut sebagai algoritma pertama | Rumusan "sering disebut" dipertahankan |
| `2026` | Sandi Leluhur: Repositori Pusaka | Situs statis terbuka yang merekonstruksi nalar komputasional tenun | **Hapus "terdesentralisasi"** (tidak benar) |

Setiap item memuat penanda `≈ perkiraan` bila relevan, **nama sumber**, dan tautan ke matriks atribusi.

### 15.3 Matriks Atribusi Arsip
Tabel statis dengan kolom: **Aset**, **Sumber**, **Lisensi** (chip). Minimal lima baris sesuai mock: foto makro serat, skematik alat tenun, matriks motif 12 × 12, tipografi (Anton, Playfair Display, JetBrains Mono: SIL OFL 1.1), dan foto pamor/keris. Pada mock, sumber seperti "Laboratorium Tekstil Tradisional Silungkang", "Balai Pelestarian Kebudayaan Wilayah X", dan "Komunitas Penenun Tuban & Sikek" masih placeholder: **wajib diganti sumber nyata** (BRD D-01, D-03, R-04). Baris "Skematik alat tenun (Domain Publik, Manuskrip Serat Centhini 1814)" perlu verifikasi.

Catatan hak moral di bawah tabel: "Semua karya penenun tetap melekat pada komunitas adat yang bersangkutan."

### 15.4 Manifest Atribusi (`assets/data/credits.json`)
Tombol `[ UNDUH MANIFEST (.JSON) ]` adalah tautan biasa: `<a href="assets/data/credits.json" download>`. Tidak memerlukan JS, dan bekerja pada `file://`.

```json
{
  "proyek": "Sandi Leluhur: Mesin Biner Pertama",
  "versi": "1.1",
  "diperbarui": "2026-10-23",
  "aset": [
    {
      "id": "A-01",
      "nama": "Foto makro serat lungsi",
      "kategori": "Foto",
      "sumber": "[isi sumber nyata]",
      "lisensi": "CC BY-SA 4.0",
      "tautan": "[isi]"
    }
  ],
  "pustaka": [
    { "nama": "GSAP", "versi": "3.12.5", "lisensi": "[verifikasi di situs resmi]", "tautan": "https://gsap.com" },
    { "nama": "GSAP ScrollTrigger", "versi": "3.12.5", "lisensi": "[verifikasi di situs resmi]", "tautan": "https://gsap.com" }
  ],
  "font": [
    { "nama": "Anton", "lisensi": "SIL OFL 1.1" },
    { "nama": "Playfair Display", "lisensi": "SIL OFL 1.1" },
    { "nama": "JetBrains Mono", "lisensi": "SIL OFL 1.1" }
  ]
}
```

**Aturan sinkron:** isi `credits.json` dan tabel HTML harus identik; dicek pada QA (§13.4, `[isi` tidak boleh tersisa).

### 15.5 Footer
Dua nada: **paper** (akhir Dampak) dan **void** (akhir Kredit). Isi:

| Elemen | Isi final |
|---|---|
| Wordmark | `SANDI LELUHUR` (Anton raksasa) |
| Deskripsi | "Eksplorasi kuratorial atas genealogi transmisi sinyal biner Nusantara. Melestarikan nalar komputasi aksara dan artefak ritmis peradaban leluhur melalui telemetri mesin preservasi." |
| Panel telemetri (nilai nyata) | `KLASIFIKASI: PUSAKA TEKNO-HISTORIK` · `BERKAS HTML: 5` · `PUSTAKA PIHAK KETIGA: 2 (GSAP · ScrollTrigger)` · `PROSES BUILD: TIDAK ADA` |
| Baris hukum | `© 2026 SANDI LELUHUR: MESIN BINER PERTAMA · TECHTOPIA VOL. 2` |
| Penanda kanan | `[ KODE TERBUKA TERBACA ]` · `TANPA BUILD` |

Nilai `KLASIFIKASI` dan baris dekoratif lain boleh tetap gaya "arsip", selama tidak menyatakan afiliasi atau kemampuan yang tidak ada.

---

## Lampiran A: Kerangka HTML Halaman

```html
<!DOCTYPE html>
<html lang="id" class="no-js" data-tone="void">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>Playground Biner · Sandi Leluhur</title>
  <meta name="description" content="Programkan motif tenunmu dalam 0 dan 1.">
  <link rel="preload" href="assets/fonts/Anton.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="css/tokens.css">
  <link rel="stylesheet" href="css/base.css">
  <link rel="stylesheet" href="css/components.css">
  <link rel="stylesheet" href="css/pages.css">
  <link rel="stylesheet" href="css/motion.css">
  <script>document.documentElement.classList.replace('no-js', 'js');</script>
</head>
<body data-page="playground" data-step="3" data-monograf="03" data-tone="paper">
  <a class="skip-link" href="#konten">Lewati ke konten</a>
  <header class="site-header"><!-- salinan identik di semua halaman (§4.5) --></header>
  <div id="nav-progress" aria-hidden="true"></div>
  <div id="thread-layer" aria-hidden="true"><!-- SVG benang (§10.3) --></div>
  <div id="sr-status" class="sr-only" aria-live="polite"></div>
  <main id="konten" tabindex="-1">
    <h1>Program motifmu</h1>
    <!-- konten halaman -->
  </main>
  <footer class="site-footer"><!-- salinan identik (§15.5) --></footer>

  <script defer src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"
          integrity="[isi SRI]" crossorigin="anonymous"></script>
  <script defer src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"
          integrity="[isi SRI]" crossorigin="anonymous"></script>
  <script defer src="js/core/namespace.js"></script>
  <script defer src="js/core/storage.js"></script>
  <script defer src="js/core/transition.js"></script>
  <script defer src="js/core/header.js"></script>
  <script defer src="js/core/router.js"></script>
  <script defer src="js/features/boot-sequence.js"></script>
  <script defer src="js/features/cursor-trail.js"></script>
  <script defer src="js/features/thread.js"></script>
  <script defer src="js/features/exploded-view.js"></script>
  <script defer src="js/features/weave-grid.js"></script>
  <script defer src="js/features/certificate.js"></script>
  <script defer src="js/main.js"></script>
</body>
</html>
```

> `*.min.js` di atas adalah berkas pustaka CDN pihak ketiga, bukan kode proyek. Kode proyek tetap tidak diminifikasi. Pastikan panitia menerima hal ini; jika ragu, tulis di README.

## Lampiran B: Daftar Atribut Data

| Atribut | Elemen | Nilai | Dibaca oleh |
|---|---|---|---|
| `data-page` | `<body>` | `home`, `arsip`, `playground`, `dampak`, `kredit` | router, header |
| `data-step` | `<body>` | `0`–`4` | header |
| `data-monograf` | `<body>` | `01`–`05` | header |
| `data-tone` | `<html>`, `<header>`, `<footer>`, bagian | `void`, `paper` | header, observer |
| `data-section` | `.page-section` | `beranda`, `arsip`, `playground`, `dampak`, `kredit` | router, thread |
| `data-cta="header"` | tautan header | — | header |
| `data-reveal` | elemen Boot | — | boot-sequence |
| `data-part` | kartu/bagian Arsip | `penggulung-lungsi`, `sisir`, `lungsi`, `gulungan-kain` | exploded-view |

## Lampiran C: Pemetaan Perubahan terhadap Versi 1.0

| SRS 1.0 | SRS 1.1 |
|---|---|
| §1 Pendahuluan | §1 (diperluas: konvensi, keputusan berubah) |
| §2.1–2.3 | §2.1–2.3 (header, benang, folder CSS/JS baru; Tailwind dihapus) |
| §3.1 SPA Router | §5.1–5.5 |
| §3.2 Manajemen Memori | §11 |
| §4.1 Cursor Trail | §7 |
| §4.2 Playground | §8 |
| §4.3 Exploded View | §10.2 |
| §5 Standar Kode | §13 |
| — | §3 (keputusan), §4 (token, komponen), §6 (Boot), §9 (Sertifikat), §10.3 (Benang), §12 (responsif, aksesibilitas), §14 (uji), §15 (Kredit) |
