import urllib.request
import urllib.parse
import re
from pytube import *
import moviepy.editor as mp
from hashlib import *
import pickle

#recebe a string de busca, faz a busca e concatena a url padrão + o resultado da busca.
def Searh_YouTube(pesquisa):
    query_string = urllib.parse.urlencode({"search_query": pesquisa})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    url = ("http://www.youtube.com/watch?v=" + search_results[0])
    return url

#Efetua a busca com a url disponibilzada e enfim baixa o arquivo de video para a transferência
def Download_YouTube(url):
    yt = YouTube(url)
    print(yt.title)
    stream = yt.streams.first()
    stream.download(filename = "video")

#Efetua a busca com a url disponibilzada e enfim baixa o arquivo de audio, depois o converte para a transferência
def Download_Youtube_Audio(url):
    yt = YouTube(url)
    print(yt.title)
    stream = yt.streams.first()
    stream.download(filename = "audio")
    clip = mp.VideoFileClip("audio.mp4")
    clip.audio.write_audiofile("audio.mp3")


def GetYTitle(url):
    yt = YouTube(url)
    return str(yt.title)


###################################################################################


def Log(User,Senha):
    dicti = {}
    with open("usuarios.pickle", "rb") as lista_users:
        while True:
            try:
                dicti.update(pickle.load(lista_users))
            except EOFError:
                break
    if User in dicti:
        print(Senha == dicti[User])
        print(str(Senha) == dicti[User])
        if Senha == dicti[User]:
            return "s"
        else:
            return "n"


def Add(User,Senha):
    dict_tmp = {User: Senha}
    with open("usuarios.pickle", "ab") as lista_users:
        pickle.dump(dict_tmp,lista_users)






