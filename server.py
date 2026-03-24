from socket import *
from constCS import *

HOST = '0.0.0.0'
s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
(conn, addr) = s.accept()
while True:
    option = conn.recv(1024)
    if not option: break
    option = bytes.decode(option).strip()
    print(option)
    data = conn.recv(1024)
    if not data: break
    text = bytes.decode(data).strip()
    print(text)
    if option == "1":
        result = text.upper()
    elif option == "2":
        result = f"*{text}*"
    else:
        result = "Servidor encerrado..."
    response = result
    conn.send(str.encode(response))
conn.close()