import socket

def create_socket():
    try:
        global host 
        global port 
        global s   

        host = ""
        port = 9999
        s = socket.socket()

    except socket.error as msg:
        print("Socket creation error: " + str(msg))
#проверяем порт
def bind_socket():
    try:
        global host
        global port
        global s

        print("Binding the Port: " + str(port))

        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print("Socket creation error: " + str(msg) + "\n" + "Retrying...")
        bind_socket()

# принимаем сообщение от клиента, сервер может принять сколько угодно сообщений от клиентов
#можно ограничить цикл только двумя сообщениями от клиента
def socket_accept():
    
    while True:
     try:
        conn, address = s.accept()
        print("Connection : |" + " IP: " + address[0] + " | Port: " + str(address[1]))
        client_response = str(conn.recv(1024), "utf-8")
        #конвертация в число, в будущем нужна ф-я, которая будет 
        #принимать сообщения от клиентов и считать местонахождение телефона 
        num = bytes(str(int(client_response)),"ascii")
     except KeyboardInterrupt:
      conn.close()
      break
     else:
           print(client_response, end="\n")
           #print(num, end="")
    
  #еще должна быть ф-я, отвещающая за параметры обнаружения телефона как на клиенте
  
def main():
    create_socket()
    bind_socket()
    socket_accept()

main()

