from socket  import *
from constCS import * #-

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT)) # connect to server (block until accepted)
option = input("Opção: ")
s.send(str.encode(option))
text = input("Texto: ")
s.send(str.encode(text))
response = s.recv(1024)
print(bytes.decode(response))
s.close()