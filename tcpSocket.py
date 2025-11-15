import socket

targetHost = "www.google.com"
targertPort = 80

# Membuat socket 
client = socket.socket(socket.AF_inet, socket.SOCK_STREAM)
client.connect((targetHost, targertPort))  

client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# Menerima respon dari server
response = client.recv(4096)
print(response.decode())

client.close()