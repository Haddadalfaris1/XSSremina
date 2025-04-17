* XSSRemina - Pemindai Kerentanan Cross-Site-Scripting

XSSRemina adalah pemindai kerentanan XSS (Cross-Site Scripting) canggih yang dirancang untuk peneliti keamanan dan penguji penetrasi. Alat ini menguji aplikasi web terhadap berbagai muatan XSS, termasuk teknik bypass tingkat lanjut.

** Fitur
- Beberapa payload XSS termasuk teknik dasar, lanjutan, dan teknik pengaburan
- Pemindaian serentak dengan threading untuk hasil yang lebih cepat
- Rotasi User-Agent secara acak untuk menghindari deteksi
- Payload kelas profesional untuk pengujian yang komprehensif

** Instalasi di Kali Linux

1. Klon repositori ini:

git clone https://github.com/yourusername/XSSRemina.git


2. Navigasi ke direktori proyek:

cd XSSRemina


3. Instal dependensi yang diperlukan:

pip3 install requests fake-useragent


4. Jalankan pemindai:

python3 xssremina.py


** Penggunaan
1. Jalankan skrip
2. Masukkan URL target saat diminta (sertakan parameter, misalnya, `https://example.com/page?param=`)
3. Alat ini akan secara otomatis menguji semua payload dan laporan kerentanan

** Contoh

python3 xssremina.py
[*] Tempel URL yang ingin di-scan (https://example.com/page?param=): https://vulnerable-site.com/search?q=testss 
[!] XSS Vulnerability Found: https://vulnerable-site.com/search?q=testss<svg><script>alert('PriaJomblo')</script></svg>


** Penafian
Alat ini hanya untuk tujuan edukasi dan pengujian penetrasi resmi. Pengembang tidak bertanggung jawab atas penyalahgunaan perangkat lunak ini.

Selamat berburu! 🚀

# xssremina.py - XSS Vulnerability Scanner
# XSSremina # Cross-Site-Scripting
