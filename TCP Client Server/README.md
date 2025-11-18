# 🟩 TCP Client-Server || Konfigurasi Step by Step

Apabila anda ingin langsung mencoba *source code* saya, bisa langsung ambil saja dengan menggunakan langkah-langkah berikut:

**📎Clone Repository**

Pastikan anda sudah pernah menginstall `git` sebelumnya. Jalankan perintah berikut pada terminal:

```bash
git clone https://github.com/RockHead07/UDP-TCP-Client-Server.git
```

Kemudian masuk direktori UDP nya:

```bash
cd UDP-TCP-Client-Server/TCP\ Client\ Server
```

### 📂 Struktur File

```arduino
TCP Client Server/
├── tcpServer.py
├── tcpClient.py
└── README.md
```

### ⚙️ Alat & Bahan

Pastikan anda sudah memiliki:
- `Python 3.x` terpasang atau *latest version*-nya pada device anda.
- Terminal / command prompt.
- (Opsional) IDE Tools, seperti VsCode untuk ngoding pemgoraman `Python` nya.

Untuk memastikan apakah `Python` sudah terinstall atau belum, gunakan perintah ini (pada terminal windows):

```bash
python --version
py --version
```

Apabila *output* nya menampilkan keluaran dari versi `Python` itu sendiri, maka artinya `Python` sudah terinstall di perangkat mu.

### TCP Server

Langkah pertama adalah membuat dan menjalankan *TCP Server*. Berbeda dengan *UDP*, protokol *TCP* bersifat *connection-oriented*, sehingga *client* harus melakukan proses *handshake* terlebih dahulu sebelum mengirim data.

Berikut *code program* ***TCP Server***:

```Python

```

Cara menjalankan *code program* diatas, yang pertama buka terminal pada direktori projek yang kalian kerjakan, lalu jalankan perintah berikut di terminal:

```bash
python tcpServer.py
```

### TCP Client

Setelah ***TCP Server*** siap, selanjutnya membuat *client* untuk mengirim pesan dan menerima balasan respon dari *server*.

Berikut *code program* ***TCP Client***:

```python

```

Setelah *code program* client selesai dibuat, jalankan *client* dengan membuka terminal baru (*biarkan terminal pada bagian server tetap aktif*), lalu jalankan perintah berikut:

```bash
python tcpClient.py
```

Jika berhasil, maka *client* akan mengirimkan pesan ke server, menerima respon, dan menampilkan hasilnya pada terminal. 

### 📤 Output

Berikut, contoh keluaran *output* nya ketika program dijalankan:

#### Output pada *terminal* Server

```bash
UDP server up and listening on
Pesan dari Client: "b'Hello UDP Server'"
IP address Client: "('127.0.0.1', 62341)"
```

#### Output pada *terminal* Client

```bash
Respon dari server: "Selamat datang di UDP Server"
```

# ✨ Kesimpulan

Dari konfigurasi *UDP Client-Server* ini, dapat kita simpulkan bahwa komunikasi yang menggunakan protokol *UDP* berjalan dengan konsep *connectionless*, yang dimana *client* dapat langsung mengirimkan data ke server tanpa perlu melakukan proses *handshake* terlebih dahulu. Server hanya perlu mendengarkan pada IP & port tertentu, kemudian menrima pesan dan mengirimkan balasnnya.
