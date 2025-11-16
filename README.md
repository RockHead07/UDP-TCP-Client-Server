<div align="center">

<h1> MATA KULIAH </h1>
<h3> PRAKTIKUM KONSEP JARINGAN</h3>

![Image](https://github.com/user-attachments/assets/3ad88b6e-7159-44a2-a004-c909b974a88c)

<h3> Dosen Pengampu: </h3>

**Mohammad Robihul Mufid S.ST., M.Tr.Kom**

<h3> Disusun Oleh: </h3> 

**Bagus Insan Pradana** D3 IT A **(3214521007)**

PROGRAM STUDI D3 TEKNIK INFORMATIKA DEPARTEMEN TEKNIK INFORMATIKA DAN KOMPUTER  
POLITEKNIK ELEKTRONIKA NEGERI SURABAYA  
**2025**

#

<div align="center">
     
![Repo Size](https://img.shields.io/github/repo-size/RockHead07/UDP-TCP-Client-Server)
![Last Commit](https://img.shields.io/github/last-commit/RockHead07/UDP-TCP-Client-Server)
![Language](https://img.shields.io/github/languages/top/RockHead07/UDP-TCP-Client-Server)

</div>

# UDP & TCP Client-Server

<div align="left">

Pada penugasan kali ini, diberikan perintah untuk mengerjakan praktikum konfigurasi **UDP & TCP Client-Server** menggunakan bahasa pemrograman `Python`.

Praktikum ini dikerjakan berdasarkan referensi dari beberapa video berikut:
</div>

<div align="center">

| UDP Client Socket | UDP Server Socket | TCP Client Server |
|------------------|-------------------|-------------------|
| [![Video 1](https://img.youtube.com/vi/bKfDS1lOSho/0.jpg)](https://www.youtube.com/watch?v=bKfDS1lOSho) | [![Video 2](https://img.youtube.com/vi/i1AOd7AQcok/0.jpg)](https://www.youtube.com/watch?v=i1AOd7AQcok) | [![Video 3](https://img.youtube.com/vi/GlVfVn17_ug/0.jpg)](https://www.youtube.com/watch?v=GlVfVn17_ug) |

</div>

<div align="left">

# 1. Tujuan Praktikum

Praktikum ini bertujuan agar mahasiswa dapat:
- Memahami perbedaan konsep **UDP** dan **TCP** dalam komunikasi jaringan.  
- Mampu membangun program **client-server** sederhana menggunakan Python.  
- Menguji proses pengiriman dan penerimaan data melalui socket.  
- Melihat proses koneksi dan komunikasi real-time antara client dan server.

# 2. Pendahuluan

Pada praktikum ini kita akan mempelajari dua protokol utama pada lapisan _Transport_, yaitu **UDP** (***User Datagram Protocol***) dan **TCP** (***Transmission Control Prtocol***). Keduanya digunakan untuk komunikasi antar *Client* dan *Server*, namun memiliki mekanisme yang berbeda.

**UDP** bersifat *connectionless*, tidak memerlukan *handshake*, dan mengirim data dengan cepat. Namun, tidak ada jaminan bahwa data akan sampai atau berurutan. Protokol ini banyak digunakan pada aplikasi *real-time* seperti game online, streaming, dan VoIP.

Dan bersifat sebaliknya, **TCP** bersifat *connection-oriented*, yang dimana protokol ini menggunakan *three-way handshake*, serta menjamin data terkirim dengan utuh & berurutan. TCP juga sering digunakan pada aplikasi yang membutuhkan keandalan seperti WB, email, dan transfer file.

# 3. Implementasi & Penjelasan Program

Untuk melakukan konfigurasi **TCP & UDP Client-Server**, digunakan bahasa pemrograman `Python` dengan memanfaatkan modul *socket*.  
Setiap implementasi dipisahkan ke dalam direktori yang berbeda agar lebih terstruktur dan mudah dipelajari.

Penjelasan langkah demi langkah dapat dilihat pada masing-masing bagian berikut:

## 🔗 Konfigurasi Client–Server

<div align="center">

> ### TCP Client–Server  
> [![TCP](https://img.shields.io/badge/TCP-Client--Server-0A84FF?style=for-the-badge&logo=python&logoColor=white)](https://github.com/RockHead07/UDP-TCP-Client-Server/tree/main/TCP%20Client%20Server)  
> Implementasi komunikasi berbasis **Transmission Control Protocol (TCP)** yang menyediakan koneksi *reliable*, menggunakan mekanisme *3-way handshake*, serta menjamin urutan data.

---

> ### UDP Client–Server  
> [![UDP](https://img.shields.io/badge/UDP-Client--Server-30D158?style=for-the-badge&logo=python&logoColor=white)](https://github.com/RockHead07/UDP-TCP-Client-Server/tree/main/UDP%20Client%20Server)  
> Konfigurasi komunikasi menggunakan **User Datagram Protocol (UDP)** yang menyediakan pengiriman data cepat, *connectionless*, dan cocok untuk aplikasi real-time.
