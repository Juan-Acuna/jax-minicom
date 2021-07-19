from .serializable import Serializable
import json as js

class Carga(Serializable):
    __tipo:int
    __serv:bool
    __de__:str
    __para__:str
    CARGA_TIPO_INSTRUCCION = 0
    CARGA_TIPO_MENSAJE = 1
    BROADCASTING = "broadcast"
    def __init__(self, tipo:int, de:str, para:str, ser:bool = False):
        self.__serv=ser
        self.__tipo=tipo
        self.__de__=de
        self.__para__=para
    def de(self) -> str:
        return self.__de__
    def para(self, para:str = None):
        if para == None:
            return self.__para__
        else:
            self.__para__ = para
    def es_broadcast(self) -> bool:
        return self.__para__ == Carga.BROADCASTING
    def tipo_carga(self) -> int:
        return self.__tipo
    def desde_servidor(self):
        return self.__serv

class Instruccion(Carga):
    __comando__:str
    def __init__(self, de:str, para:str, cmd:str, ser:bool = False):
        super().__init__(Carga.CARGA_TIPO_INSTRUCCION, de, para, ser)
        self.__comando__=cmd
    def comando(self) -> str:
        return self.__comando__

class Mensaje(Carga):
    __cont__:str
    def __init__(self, de:str, para:str, cont:str, ser:bool = False):
        super().__init__(Carga.CARGA_TIPO_MENSAJE, de, para, ser)
        self.__cont__=cont
    def contenido(self) -> str:
        return self.__cont__

class SerializadorCargas():
    def serializar(carga:Carga) -> bytes:
        return carga.json().encode("utf-8")
    def deserializar(json) -> Carga:
        j:dict[str,any] = js.loads(json)
        tipo:int = j['_Carga__tipo']
        de:str = j['__de__']
        para:str = j['__para__']
        serv:bool = j['_Carga__serv']
        if tipo == Carga.CARGA_TIPO_INSTRUCCION:
            return Instruccion(de, para, j['__comando__'], serv)
        elif tipo == Carga.CARGA_TIPO_MENSAJE:
            return Mensaje(de, para, j['__cont__'], serv)