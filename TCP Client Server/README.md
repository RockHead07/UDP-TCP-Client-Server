# 🟩 TCP Client-Server || Konfigurasi Step by Step

> [!NOTE]
> ## ❕ Disclaimer  
> Seluruh langkah dan kode pada repository ini disusun berdasarkan materi dan video referensi yang diberikan oleh dosen.  
> Konten asli pada video tersebut bukan milik saya; seluruh hak cipta tetap pada pemilik resminya.  
> 
> 🔗 **Referensi Video:**  
> <div align="center">
>
> <a href="https://www.youtube.com/watch?v=GlVfVn17_ug">
>   <img src="https://img.youtube.com/vi/GlVfVn17_ug/0.jpg" width="270">
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
import socket  # Mengimpor library socket untuk komunikasi jaringan

# Mengecek apakah script dijalankan langsung (bukan diimport)
if __name__ == "__main__":
    ip = "127.0.0.1"       # IP server (localhost)
    port = 12345           # Port server untuk mendengarkan koneksi

    # Membuat socket TCP (SOCK_STREAM = TCP)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Mengikat server pada IP dan port
    server.bind((ip, port))

    # Memulai server untuk mendengarkan koneksi masuk
    # Angka 5 berarti maksimal 5 koneksi yang dapat masuk ke "antrian"
    server.listen(5)

    # Server terus berjalan dan menerima koneksi dari client
    while True:
        # Menerima koneksi dari client
        client, address = server.accept()

        # Menampilkan alamat client yang baru terhubung
        print(f"Connection from {address[0]}:{address[1]} has been established!")

        # Menerima data dari client (maks 1024 bytes)
        string = client.recv(1024)
        
        # Decode data dari bytes ke string UTF-8
        string = string.decode("utf-8")
        
        # Mengubah pesan menjadi huruf besar
        string = string.upper()

        # Mengirimkan balik (echo) ke client dalam bentuk bytes
        client.send(bytes(string, 'utf-8'))

        # Menutup koneksi dengan client
        client.close()
```

Cara menjalankan *code program* diatas, yang pertama buka terminal pada direktori projek yang kalian kerjakan, lalu jalankan perintah berikut di terminal:

```bash
python tcpServer.py
```

*Server* akan aktif dan menunggu koneksi dari *Client*.

### TCP Client

Setelah ***TCP Server*** siap, selanjutnya membuat *client* untuk mengirim pesan dan menerima balasan respon dari *server*.

Berikut *code program* ***TCP Client***:

```python
import socket  # Mengimpor library socket untuk komunikasi jaringan

# Mengecek apakah script dijalankan langsung
if __name__ == "__main__":
    ip = "127.0.0.1"     # IP server tujuan (localhost)
    port = 12345         # Port server tujuan

    # Membuat socket TCP (SOCK_STREAM berarti protokol TCP)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Melakukan koneksi ke server dengan IP dan port yang ditentukan
    server.connect((ip, port))
    
    # Meminta input dari user untuk dikirim ke server
    string = input("Enter a message to send to the server: ")

    # Mengirim pesan ke server dalam bentuk bytes
    server.send(bytes(string, 'utf-8'))

    # Menerima balasan dari server (maks 1024 bytes)
    buffer = server.recv(1024)

    # Mengubah data bytes menjadi string UTF-8
    buffer = buffer.decode("utf-8")

    # Menampilkan respon dari server
    print(f"Server response: {buffer}")
```

Setelah *code program* client selesai dibuat, jalankan *client* dengan membuka terminal baru (*biarkan terminal pada bagian server tetap aktif*), lalu jalankan perintah berikut:

```bash
python tcpClient.py
```

Jika berhasil, maka *client* akan memeberi kita opsi untuk mengirim pesan apapun, yang nantinya server mengembalikan ke versi huruf kapitalnya / **UPPERCASE** dari pesan tersebut.

### 📤 Output

Berikut, contoh keluaran *output* nya ketika program dijalankan:

#### Output pada *terminal* Server

```bash
Connection from 127.0.0.1:63789 has been established!
```

#### Output pada *terminal* Client

Apabila kita melakukan *input* pesannya seperti dibawah ini, akan dikembalikan menjadi huruf kapital semua.

```bash
Enter a message to send to the server: Indonesia
Server response: INDONESIA
```

# ✨ Kesimpulan

Dari konfigurasi *TCP Client-Server* ini, dapat kita simpulkan bahwa komunikasi yang menggunakan protokol *TDP* berjalan dengan konsep *connection-oriented*, yang dimana sebelum proses pengiriman data terjadi, *client* harus terlebih dahulu membuat koneksi (*three-way handshake*) ke server.

Hal ini membuat ***TCP*** lebih dapat diandalkan / *reliable* dibandingkan menggunakan ***UDP***, karena setiap data yang dikirim akan dijamin sampai dengan urutan yang benar. Server menerima pesan dari *client*, memprosesnya (mengubah menjadi huruf kapital), kemudian mengirimkan kembali ke client sebelum menutup koneksi.