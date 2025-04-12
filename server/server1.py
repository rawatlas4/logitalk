from socket import*#імпортуємо модуль
import threading
server = socket(AF_INET,SOCK_STREAM)#створюємо об'єкт сокет(сокстрим ето протокол афінет це сімейство ipv4)
server.bind(("localhost",12345))#прив'язуємо до певної адреси(локалхост) за допомогою бінд (2010 це порти)
server.setblocking(False)
server.listen(5)#скільки людей може обробляти сервер
clients = []
#--------------0------------------------------------
def recv_message():
    while 1:
        for vasya in clients:
            try:
                print(vasya.recv(1024).decode())
            except:
                pass    
threading.Thread(target=recv_message).start()
   


def otpravlyat():
    while 1:
        sms = input("->")
        for vasya in clients:
            vasya.send(sms.encode())        

threading.Thread(target=otpravlyat).start()

while 1:
    try:
        comunication , ip = server.accept()
        comunication.setblocking(False)
        print("Підключився кліент", ip)
        clients.append(comunication)
    except:
        pass