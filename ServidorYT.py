from FuncsServ import *
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread




####################################################################################################################################

def logg(client):
    User = client.recv(1024).decode("utf-8")
    Pass = client.recv(1024)
    return Log(User,Pass)

def cadd(client):
    User = client.recv(1024).decode("utf-8")
    Pass = client.recv(1024)
    Add(User,Pass)


#recebe a conexão de novos clientes e chama a thread para lidar efetivamente com as requisições
def accept_incoming_connections():
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s se conectou." % client_address)
        addresses[client] = client_address
        loger = client.recv(1024).decode("utf-8")
        if loger == "l":
            resp = logg(client)

            if resp == "s":
                client.send(resp.encode("utf-8"))
                Thread(target=handle_client, args=(client,)).start()
            elif resp == "n":
                client.send("Senha incorreta".encode("utf-8"))
        elif loger =="c":
            cadd(client)
            client.send("Cadastrado".encode("UTF-8"))
            Thread(target=handle_client, args=(client,)).start()

#Lida com as requisições do cliente e efetua os downloads das imagens e fotos
def handle_client(client):
    try :
        while True:

            param = client.recv(1024)
            param = param.decode("utf-8")
            print(param)
            url = Searh_YouTube(param)

            client.send(GetYTitle(url).encode("utf-8"))


            choice = client.recv(1024)
            choice = choice.decode("utf-8")


            if choice == "video":
                Download_YouTube(url)
                print('Conectado a {}'.format(ADDR))
                f = open('video.mp4', 'rb')
                l = f.read(1024)
                while l:
                    client.send(l)
                    l = f.read(1024)
                f.close()
                client.close()
            elif choice == "audio":
                Download_Youtube_Audio(url)
                print('Conectado a {}'.format(ADDR))
                f = open('audio.mp3', 'rb')
                l = f.read(1024)
                while l:
                    client.send(l)
                    l = f.read(1024)
                f.close()
                client.close()
    except:
        print('Conexão fechada!!!')

####################################################################################################################################

####################################################################################################################################
#Define os parâmetros da conexão e inicia o socket
clients = {}
addresses = {}

HOST = '127.0.0.1'
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)
####################################################################################################################################


if __name__ == "__main__":
    SERVER.listen(15)
    print('Servidor de arquivos disponível. Aguardando conexão do cliente ...')
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()





