# 🟩 UDP Client-Server || Konfigurasi Step by Step

> [!NOTE]
> ## ❕ Disclaimer  
> Seluruh langkah dan kode pada repository ini disusun berdasarkan materi dan video referensi yang diberikan oleh dosen.  
> Konten asli pada video tersebut bukan milik saya; seluruh hak cipta tetap pada pemilik resminya.  
> 
> 🔗 **Referensi Video:**  
> <div align="center">
>
> <a href="https://www.youtube.com/watch?v=bKfDS1lOSho">
>   <img src="https://img.youtube.com/vi/bKfDS1lOSho/0.jpg" width="270">
> </a>
>
> <a href="https://www.youtube.com/watch?v=i1AOd7AQcok">
>   <img src="https://img.youtube.com/vi/i1AOd7AQcok/0.jpg" width="270">
> </a>
>
> </div>


Apabila anda ingin langsung mencoba *source code* saya, bisa langsung ambil saja dengan menggunakan langkah-langkah berikut:

**📎Clone Repository**

Pastikan anda sudah pernah menginstall `git` sebelumnya. Jalankan perintah berikut pada terminal:

```bash
git clone https://github.com/RockHead07/UDP-TCP-Client-Server.git
```

Kemudian masuk direktori UDP nya:

```bash
cd UDP-TCP-Client-Server/UDP\ Client\ Server
```

### 📂 Struktur File

```arduino
UDP Client Server/
├── udpServer.py
├── udpClient.py
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

### UDP Server

Yang pertama kita lakukan, ialah membuat server dari *UDP* nya terlebih dahulu sebelum menjalankan *client*. Server ini nantinya berguna untuk menerima pesan dari *client* dan mengirimkan responnya kembali. 

Berikut *code program* ***UDP Server*** nya:

```Python
import socket  # Mengimpor library socket untuk komunikasi jaringan

# Konfigurasi server
localIP = "127.0.0.1"   # IP tempat server berjalan (localhost)
localPort = 9997        # Port yang digunakan server
buffer = 1024           # Ukuran maksimum data yang dapat diterima

# Membuat socket UDP
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Mengikat socket ke IP dan port sehingga server siap menerima data
serverSocket.bind((localIP, localPort))  # Menyalakan server UDP

print("UDP server up and listening on")

# Server terus-menerus mendengarkan pesan dari client
while True:
    data = serverSocket.recvfrom(buffer)  # Menerima data dari client
    pesan = data[0]                       # Bagian pertama berisi pesan
    ip_address = data[1]                  # Bagian kedua berisi alamat (IP, port) client

    # Menampilkan pesan dan alamat client ke terminal
    print("Pesan dari Client: \"{}\"".format(pesan))
    print("IP address Client: \"{}\"".format(ip_address))

    # Server membalas pesan ke client
    serverSocket.sendto(b"Selamat datang di UDP Server", ip_address)
```

Cara menjalankan *code program* diatas, yang pertama buka terminal pada direktori projek yang kalian kerjakan, lalu jalankan perintah berikut di terminal:

```bash
python udpServer.py
```

Maka, server akan aktif dan menunggu pesan dari *client*.

### UDP Client

Karena ***UDP Server*** telah dibuat, maka sekarang saatnya melakukan konfigurasi untuk ***UDP Client*** nya. *Client* ini akan bertugas untuk mengirim pesan ke server dan menunggu balasan dari *server*. Berikut *code program* nya:

```python
import socket  # Mengimpor library socket untuk komunikasi jaringan

# Konfigurasi target (alamat server tujuan)
target_host = "127.0.0.1"   # IP server (localhost)
target_port = 9997          # Port server yang digunakan untuk berkomunikasi

# Membuat socket UDP
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Mengirim data ke server (dalam bentuk bytes)
client.sendto(b"Hello UDP Server", (target_host, target_port))

# Menerima balasan dari server
data, address = client.recvfrom(4096)    # 4096 = ukuran maksimum data yang diterima

# Menampilkan balasan server ke terminal
print("Respon dari server: \"{}\"".format(data.decode()))

# Menutup koneksi socket client
client.close()
```

Setelah *code program* client selesai dibuat, jalankan *client* dengan membuka terminal baru (*biarkan terminal pada bagian server tetap aktif*), lalu jalankan perintah berikut:

```bash
python udpClient.py
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