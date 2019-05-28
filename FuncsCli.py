from hashlib import *
def codf(senha_normal):
    senha_codificada = sha256()
    senha_codificada.update(senha_normal.encode())
    senha_codificada = senha_codificada.digest()
    return (senha_codificada)