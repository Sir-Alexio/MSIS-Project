import socket

s = socket.socket() 
#ip сервера
host = '192.168.100.72' 
port = 9999
s.connect((host, port))
#передаю пока число, в будущем должна быть ф-я, которая обеспечивает
#связь телефона и компьютера и определяет параметры, которые будут передаваться на сервер
e = 565
es = str(e)
s.send(bytes(es, encoding="UTF-8"))

