import socket as sk

class Agente():
    __nombre__:str
    __ip__:str
    __tag__:str
    __socket__:sk.socket
    def __init__(self, nombre:str):
        self.__nombre__ = nombre
        self.__tag__="99999"
    def nombre(self, nombre:str=None):
        if nombre == None:
            return self.__nombre__
        else:
            self.__nombre__ = nombre
    def usuario(self) -> str:
        return "{}#{}".format(self.__nombre__,self.__tag__)
    def config(self, ip, tag):
        self.__ip__=ip
        self.__tag__=tag
    def ip(self) -> str:
        return self.__ip__
    def tag(self) -> str:
        return self.__tag__
    def conexion(self, socket:sk.socket=None):
        if socket==None:
            return self.__socket__
        else:
            self.__socket__=socket
    def reiniciar_conexion(self):
        self.__socket__ = sk.socket(sk.AF_INET, sk.SOCK_STREAM)