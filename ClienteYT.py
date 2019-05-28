#Importação das bibliotecas do Tkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
#Bibliotecas para tratamento de imagens
import PIL
from PIL import Image,ImageTk
#Biblioteca de Socket
import socket
#Funcões criadas em outro arquivo apenas para fins de organização
from FuncsCli import  *

#função simples para popup de mensagens na tela, recebe como parâmetro a mensagem a ser disposta
def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    popup.configure(background="grey")
    label = ttk.Label(popup, text=msg, font=('Comic Sans MS', 14, 'bold italic'))
    label.configure(background="grey")
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.resizable(False,False)
    popup.mainloop()
#Efetua conexão com o host remoto
host = '127.0.0.1'
port = 33000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

#função para receber audio, usada apenas após a pesquisa
def Ad():
    s.send("audio".encode("utf-8"))
    RecebeAudio()


#função para receber video, usada apenas após a pesquisa
def Vd():
    s.send("video".encode("utf-8"))
    RecebeVideo()


#função para enviar a pesquisa para o servidor, como parametro, o servidor gerará a url do video a partir disso
def enviar_pesquisa():
    sendd = str(varfras.get())
    s.send(sendd.encode('utf-8'))
    global titulo
    titulo = s.recv(1024).decode("utf-8")
    vdti = titulo

#função que efetivamente recebe e concatena o arquivo
def RecebeVideo():
    with open(titulo + 'rcv.mp4', 'wb+') as f:
        while True:
            data = s.recv(1024)
            if not data:
                break
            f.write(data)
        f.close()
        s.close()
        print('Conexão encerrada.')
        root.destroy()
        popupmsg('Transferência completa!!!')

#função que efetivamente recebe e concatena o arquivo
def RecebeAudio():
    with open(titulo + 'rcv.mp3', 'wb+') as f:
        while True:
            data = s.recv(1024)
            if not data:
                break
            f.write(data)
        f.close()
        s.close()
        print('Conexão encerrada.')
        root.destroy()
        popupmsg('Transferência completa!!!')

def SendLog():

    s.send((ed1.get()).encode("utf-8"))
    s.send(codf((ed2.get())))
    resp = s.recv(1024).decode("utf-8")
    login.destroy()
    if resp == "s":
        callRoot()
    elif resp == "n":
        popupmsg("SENHA INCORRETA")
    else :
        popupmsg(resp)


def logar():
    s.send("l".encode("utf-8"))
    SendLog()

def cadastrar():
    s.send("c".encode("utf-8"))
    SendLog()
#BORING TKINTER
imagem = Image.open("thumb.jpg")
im2 = imagem.resize((350, 200),PIL.Image.ANTIALIAS)
im2.save("thumb.jpg")
im2 = 0
imagem = 0

root = Tk()
root.title = 'YOUTUBE DOWNLOADER'


varfras = StringVar()

mainframe = ttk.Frame(root)
search = ttk.Entry(mainframe,textvariable = varfras ,width = 30)


btn = ttk.Button(mainframe,command = enviar_pesquisa,text = "Pesquisar")
btn_audio = ttk.Button(mainframe,command = Ad,text = "Audio")
btn_video = ttk.Button(mainframe,command = Vd,text = "Video")
vdti = ""
imgFrame = ttk.Labelframe(mainframe,width = 350,height =200,text = vdti )




mainframe.grid(sticky=(N,W,E,S))


search.grid(row=0,column = 0,sticky = N,columnspan=2)


btn.grid(row=1,column = 0, sticky =S,columnspan=2)


imgFrame.grid(row=2,column = 0,columnspan = 2)


btn_audio.grid(row=3,column = 0, sticky =S)
btn_video.grid(row=3,column = 1, sticky =N)


canv = Canvas(imgFrame, width=350, height=200, bg='white')
canv.grid(row=2, column=3)

img = ImageTk.PhotoImage(Image.open("thumb.jpg"))  # PIL solution
canv.create_image(20, 20, anchor=NW, image=img)
root.resizable(False,False)
root.configure(background = "Grey")
root.wm_title("Zé Robert")
def callRoot():
    root.mainloop()


login = Tk ()

lb1 = Label (login, text = "Usuario: ")
lb2 = Label (login, text = "Senha: ")
usuario = StringVar
senha = StringVar
ed1 = Entry (login,textvariable = usuario)
ed2 = Entry (login, show="*", textvariable = senha)

bt1 = Button (login,command = logar, text = "Entrar")
bt2 = Button (login,command = cadastrar, text = "Cadastrar")

lb1.grid (row = 0, column = 0,columnspan=1)
lb2.grid (row = 1, column = 0,columnspan=1)

ed1.grid (row = 0, column = 1,columnspan=1)
ed2.grid (row = 1, column = 1,columnspan=1)

bt1.grid (row = 2, column = 0)
bt2.grid(row = 2, column = 1)

login.geometry("200x100+100+100")


#BORING TKINTER

while True :
    login.mainloop()


popupmsg("Recebido com sucesso! \n Obrigado por usar!")
