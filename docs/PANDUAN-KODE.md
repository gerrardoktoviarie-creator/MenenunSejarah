# Panduan kode Sandi Leluhur

## Peta sistem

Situs adalah satu index.html dengan lima section. Classic script defer dimuat berurutan; setiap IIFE menerima window.SL. Tidak ada framework, bundler, ES module, backend atau data yang dikirim ke server. Router hanya mengubah hash/history dan menggulir. Shell benang/footer tetap di luar main. Header memang tidak dipasang; header.js dipertahankan sebagai kompatibilitas, bukan fitur tersembunyi.

Alur utama: main → smooth → fitur section → thread → pengukuran ScrollTrigger → router. Grid menyimpan motif melalui storage lalu mengirim sl:motif. Piagam dan digit benang membaca perubahan tersebut. pagehide melepas shell/fitur; pageshow.persisted memasang kembali untuk bfcache.

## js/core/namespace.js

Tujuan: utilitas lintas modul dan satu namespace. SL.on memasang event serta mengembalikan fungsi pelepas; SL.disposer mengumpulkannya. SL.inspect memeriksa hitungan listener, trigger, dan kartu. Preferensi media dibaca lewat fungsi bersama.

Jebakan: disposer hanya membantu bila nilai pengembaliannya disimpan dan flush dipanggil. Listener browser pihak ketiga tidak otomatis masuk penghitung ini.

Pertanyaan juri:
1. Mengapa satu global? Agar classic script dapat berbagi API tanpa framework dan tetap bekerja dari file lokal.
2. Apa bukti tidak bocor? Bandingkan hitungan sebelum/sesudah navigasi dan lifecycle, bukan menganggap helper otomatis menjamin semuanya.
3. Mengapa bukan ES module? Kontrak proyek dan fallback file lokal mensyaratkan classic IIFE.

## js/core/config.js

Tujuan: data tim/mitra di satu tempat. Nilai kosong memang belum diputuskan manusia; certificate membaca konfigurasi ini untuk CTA dukungan.

Jebakan: URL mitra bukan informasi yang boleh dibuat-buat. Ganti hanya dengan kanal resmi yang terverifikasi.

Pertanyaan juri:
1. Mengapa tombol dukungan bisa disabled? Belum ada mitra/kanal resmi terkonfirmasi.
2. Di mana data tim diubah? SL.config, bukan menyalin nama ke banyak handler.
3. Apakah ada pelacakan? Modul ini hanya data konfigurasi lokal.

## js/core/motion.js

Tujuan: durasi, easing, stagger dan ambang animasi bersama. homeSections, explodedView, magnetic dan fitur lain membaca nilai yang sama.

Jebakan: mengubah satu token bisa memengaruhi banyak section; perlakukan sebagai perubahan perilaku yang perlu regresi.

Pertanyaan juri:
1. Mengapa token gerak terpisah? Mencegah durasi/easing sejenis berbeda tanpa sengaja.
2. Apakah reduced-motion hanya lebih lambat? Tidak; animasi dekoratif dihilangkan atau dibuat statis.
3. Apakah GSAP wajib untuk konten? Tidak; HTML tetap tersedia tanpa library.

## js/core/storage.js

Tujuan: validasi payload versi2/key sandi_leluhur_data, fallback RAM, sanitasi nama dan identitas FNV-1a. writeMotif menyalin matriks; readMotif memeriksa bentuk/bit sebelum dipakai. readBits memasok pola benang.

Jebakan: storage bisa gagal setelah probe awal; RAM terbaru harus menang terhadap nilai disk lama. FNV-1a bukan kriptografi, tanda tangan, atau bukti kepemilikan.

Pertanyaan juri:
1. Apa makna bit? 1 lungsi naik, 0 turun; baris adalah satu pick.
2. Mengapa ID motif sama untuk pola sama? Hash diturunkan dari matriks yang diserialkan deterministik.
3. Bagaimana kalau penyimpanan diblokir? Interaksi memakai RAM; persistensi setelah tab ditutup tidak dijanjikan.

## js/core/smooth-scroll.js

Tujuan: API gulir bersama init/scrollTo/destroy. Wheel dan sentuh memakai browser; perpindahan anchor dapat dianimasikan oleh GSAP yang sudah diizinkan. Reduced-motion berpindah langsung.

Jebakan: input pengguna harus menghentikan tween, bukan melawan wheel. Lenis sudah dikeluarkan; rasa inersia wheel lama sengaja tidak dipertahankan karena batas pustaka.

Pertanyaan juri:
1. Mengapa tidak Lenis? Aturan teknis tugas membatasi GSAP dan ScrollTrigger saja.
2. Mengapa tidak ScrollToPlugin? Tidak menambah plugin; proxy angka menggerakkan window.scrollTo.
3. Apa yang dibersihkan? Tween aktif dan listener interupsi pengguna.

## js/core/router.js

Tujuan: anchor internal, pushState dan back/forward tanpa fetch. Target, modifier klik dan download dihormati. file:// memakai tautan biasa. Benang diberi tahu indeks tujuan lewat API publik.

Jebakan: hash tidak valid tidak boleh melempar URIError; fokus harus ke heading state yang terlihat, bukan h1 di panel hidden. Jangan mengklaim ini router fetch lima halaman.

Pertanyaan juri:
1. Mengapa tak ada white flash? DOM tidak diganti; browser hanya menggulir dokumen yang sama.
2. Bagaimana Back bekerja? Hash/history dipulihkan dan target digulir lagi.
3. Tanpa JS? Anchor HTML tetap punya tujuan nyata.

## js/core/header.js

Tujuan: menjaga nama berkas/API lama tanpa menghidupkan kembali header yang sudah dihapus dari desain.

Jebakan: jangan menyebut menu/indikator header aktif dalam presentasi. Navigasi yang masih ada berada di konten/footer.

Pertanyaan juri:
1. Mengapa berkas ada tetapi inert? Larangan menghapus/rename dan keputusan mempertahankan desain tanpa header.
2. Apakah ini bug menu? Tidak ada markup header yang dijanjikan runtime sekarang.
3. Boleh dihapus nanti? Perlu keputusan kontrak/berkas dan catatan perubahan terpisah.

## js/features/boot-sequence.js

Tujuan: menyingkap judul/log sekali per sesi. Log motif berasal dari storage, bukan teks keberhasilan palsu. Timeline GSAP atau jadwal fallback CSS; Escape/Lewati menyelesaikan urutan.

Jebakan: judul tetap HTML sejak awal; timer/timeline dibatalkan pada destroy. CSS failsafe membuat isi tidak selamanya tersembunyi.

Pertanyaan juri:
1. Mengapa sessionStorage? Agar boot tidak diputar setiap kembali ke situs dalam sesi sama.
2. Apa beda reduced-motion? Langsung keadaan akhir.
3. Mengapa bukan mengetik seluruh judul? Judul harus terbaca cepat dan tidak menghambat konten.

## js/features/cursor-trail.js

Tujuan: kartu tekstur tenun muncul mengikuti pointer/tap; jumlah aktif terbatas dan node dihapus setelah memudar. Koordinat dijepit agar tidak menutup teks. Reduced-motion memakai satu kartu statis.

Jebakan: preload asynchronous dan timeline harus dimiliki lifecycle; menghapus node saja tidak cukup untuk membatalkan callback.

Pertanyaan juri:
1. Mengapa DOM, bukan canvas? Batas fitur mewajibkan DOM dan jumlah kartu kecil.
2. Bagaimana ponsel? Tap menaruh kartu, gerak sentuh dibatasi jarak dan jumlah.
3. Apakah tekstur foto artefak? Bukan; kredit menyatakan ilustrasi generatif, bukan dokumentasi museum.

## js/features/home-sections.js

Tujuan: hero, judul bertopeng, reveal, daftar, mask, peta perjalanan, perubahan nada dan garis progres. matchMedia memiliki konteks animasi supaya destroy dapat mengembalikan gaya.

Jebakan: pin Arsip mengubah posisi pemicu lain. Callback batch yang membuat tween belakangan juga harus dibersihkan. Banyak trigger wajar pada satu halaman; yang berbahaya adalah jumlah terus bertambah setelah lifecycle.

Pertanyaan juri:
1. Mengapa banyak trigger? Elemen reveal/list memiliki batas gulir sendiri.
2. Bagaimana tanpa GSAP? Isi HTML tampil statis.
3. Mengapa memisah kata? Setiap kata dapat bergerak di balik mask tanpa mengubah isi kalimat.

## js/features/exploded-view.js

Tujuan: Arsip menguraikan penggulung, sisir dan gulungan kain; timeline dan teks bagian mengikuti progres yang sama. Desktop pin, mobile tanpa pin, reduced-motion statis.

Jebakan: label timeline harus sejajar pembagian partIndex; cleanup menghapus kelas state/pin. Tahun adalah narasi arsip, bukan tanggal penciptaan semua teknik tenun.

Pertanyaan juri:
1. Apa hubungan dengan biner? Pemilihan lungsi naik/turun digambarkan melalui bagian alat, bukan klaim bahwa komputer modern identik alat tenun.
2. Mengapa mobile tidak pin? Menjaga ruang baca dan kelancaran sentuh.
3. Mengapa tahun1804? Titik narasi Jacquard; sumber/kurasi sejarah lain tetap membutuhkan verifikasi tim.

## js/features/weave-grid.js

Tujuan: matriks12×12, klik/drag, roving tabindex, preset geometris, undo/redo, simulasi pick dan penyimpanan debounce. Pointer memilih nilai kebalikan sel pertama lalu melukis nilai sama selama satu gestur.

Jebakan: DOM bukan sumber matriks; sel/readout hanya proyeksi state. Storage menerima ukuran8/16 untuk kompatibilitas, sedangkan UI saat ini12; perilaku migrasi perlu dijelaskan dari batas implementasi yang dicatat CHANGES.

Pertanyaan juri:
1. Apa yang disimpan? Matriks biner, ukuran dan metadata pada skema versi2.
2. Bagaimana keyboard? Satu sel dalam tab order; panah memindahkan fokus, Spasi/Enter mengaktifkan.
3. Mengapa preset bukan nama motif adat? Bentuk geometris netral tidak mengklaim makna budaya yang belum dikurasi.

## js/features/certificate.js

Tujuan: mengubah motif tersimpan menjadi piagam lokal, identitas/checksum, PNG canvas dan share/download. Keadaan kosong dan siap sama-sama HTML. Perubahan sl:motif memperbarui piagam.

Jebakan: ekspor asynchronous harus memakai snapshot data saat klik dan mengabaikan callback setelah destroy. ObjectURL dicabut. Data mitra kosong tidak boleh menghasilkan URL karangan.

Pertanyaan juri:
1. Apakah piagam sertifikat resmi? Tidak, artefak pengalaman situs, bukan otoritas sertifikasi.
2. Mengapa menunggu font? Agar PNG memakai tipografi yang sama, bukan fallback yang kebetulan termuat dahulu.
3. Apakah data diunggah? Canvas/Blob dibuat lokal; share hanya lewat tindakan pengguna dan API browser.

## js/features/magnetic.js

Tujuan: tombol utama sedikit mengikuti pointer halus memakai quickTo; matchMedia mematikan pada sentuh/reduced-motion.

Jebakan: transform GSAP dan translate CSS dipisah agar hover/tekan tidak saling menimpa. Tween dan listener dilepas pada cleanup.

Pertanyaan juri:
1. Mengapa quickTo? Menggunakan ulang tween, bukan membuat animasi baru setiap pointermove.
2. Apakah fitur wajib untuk klik? Tidak, tombol HTML normal tetap berfungsi.
3. Mengapa tidak pada ponsel? Tidak ada hover presisi dan gerak dekoratif tak membantu sentuh.

## js/features/thread.js

Tujuan: persediaan benang berubah menjadi bit sepanjang lima section. Progress=(indeks+lokal)/5; serat tersisa=1-progress. Mulai85% tinggi lapisan dan habis di akhir Kredit. Penjelasan teknis/model terbaru ada SRS §10.3.

Jebakan: hanya serat diklip, bukan seluruh SVG. Ukuran interval harus menghitung pin/font/piagam. Ambang selesai4% dan pulih8% mencegah label berkedip. State dihitung dari posisi aktual, bukan cache sesi.

Pertanyaan juri:
1. Bagaimana sambungan antar-section? Akhir interval i sama dengan awal interval i+1 secara matematis.
2. Mengapa angka mencerminkan motif? readBits membaca matriks pengunjung saat tersedia, atau pola bawaan yang dinyatakan jelas.
3. Bagaimana gulir balik? Perhitungan reversibel; serat/simpul muncul lagi, tanpa menghapus motif tersimpan.

## js/main.js

Tujuan: urutan init/destroy shell dan fitur. start memasang modul dan mengukur ulang layout; suspend melepas router, benang, fitur dan scroll saat pagehide.

Jebakan: bfcache tidak memuat ulang script, sehingga pageshow.persisted perlu reinit tanpa listener ganda. Urutan teardown terbalik menjaga referensi DOM/pin sampai pemiliknya selesai.

Pertanyaan juri:
1. Mengapa inisialisasi fitur sebelum benang? Pin Arsip memengaruhi panjang interval benang.
2. Apakah error disembunyikan? Tidak; error internal muncul di browser, tidak dibungkus catch umum yang menutupi bug.
3. Apa bukti lifecycle? Uji pagehide/pageshow sintetis dan hitungan sumber daya; bukan klaim heap bebas bocor dari pembacaan kode saja.

## CSS, HTML dan aset

index.html memiliki konten/landmark/hook aksesibilitas. tokens.css menyimpan nilai desain; base.css reset/tipografi/fokus; components.css tombol/komponen/lapisan benang; pages.css tata letak section; motion.css keyframes/reduced-motion. Jangan rename class/id/data tanpa menelusuri CSS dan JS sekaligus. Gaya inline yang dibuat JS untuk koordinat/animasi bukan copy desain statis.

Aset SVG tekstur dan favicon diperiksa sebagai XML; credits.json adalah inventaris atribusi, bukan bukti kepemilikan independen. File OFL font harus ikut distribusi.

Pertanyaan juri:
1. Mengapa token? Menghindari warna/spasi berbeda tanpa alasan, tanpa membulatkan nilai desain yang sudah ada.
2. Bagaimana tanpa JS? Konten/anchor tetap HTML; lapisan dekoratif benang disembunyikan.
3. Apa yang masih perlu tim lakukan? Konfirmasi panduan lomba/AI, sumber sejarah/mitra/lisensi dan uji perangkat fisik; lihat CHANGES dan RELEASE-BLOCKERS.

## Cara menunjukkan pemahaman saat presentasi

Ubah satu sel, jelaskan matriks/readout, simpan, tunjukkan piagam dan digit benang. Tunjukkan navigasi Back, reduced-motion dan konten tanpa JS. Jalankan SL.inspect sebelum/sesudah beberapa siklus; jelaskan bahwa stabilnya hitungan bukan pengganti heap snapshot penuh. Sampaikan batasan sumber budaya dan penggunaan bantuan AI sesuai aturan panitia, bukan menyembunyikannya.
