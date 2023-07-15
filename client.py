import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1",55555))
data = s.recv(1024)
print(f"Message is: {data.decode()}")