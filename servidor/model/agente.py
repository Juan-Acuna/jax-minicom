import socket as sk

class Agente():
    __nombre__:str
    __ip__:str
    __tag__:str
    __socket__:sk.socket
    def __init__(self, nombre:str, ip:str):
        self.__nombre__ = nombre
        self.__ip__ = ip
        self.__setTag__(str(hash(self.__nombre__+self.__ip__))[2:7])
    def __setTag__(self, tag:str):
        self.__tag__=tag
    def usuario(self) -> str:
        return "{}#{}".format(self.__nombre__,self.__tag__)
    def ip(self) -> str:
        return self.__ip__
    def id(self):
        return self.__id
    def tag(self) -> str:
        return self.__tag__
    def conexion(self, socket:sk.socket=None):
        if socket==None:
            return self.__socket__
        else:
            self.__socket__=socket