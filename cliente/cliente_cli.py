from model.agente import Agente
import socket as sk
import threading
import env
from model.cargas import Carga, Instruccion, Alerta, Mensaje, SerializadorCargas
import time
username = input("Ingrese el username> ")

cliente:Agente = Agente(username)
cliente.conexion(sk.socket(sk.AF_INET, sk.SOCK_STREAM))
cliente.conexion().connect((env.HOST_SERVIDOR, env.PUERTO_SERVIDOR))

def mensaje_generico(texto:str, para:str = None) -> bytes:
    p = Carga.BROADCASTING
    if para != None:
        p = para
    return SerializadorCargas.serializar(Mensaje(cliente.usuario(),p,texto))
def instruccion_generico(instruccion:str) -> bytes:
    return SerializadorCargas.serializar(Instruccion(cliente.usuario(),env.HOST_SERVIDOR,instruccion))
def receive_mensaje():
    while True:
        try:
            a:bytes = cliente.conexion().recv(env.TAMANO_CARGA)
            carga = SerializadorCargas.deserializar(a)
            if carga.tipo_carga() == Carga.CARGA_TIPO_INSTRUCCION:
                cmds = carga.comando().split(";")
                for c in cmds:
                    if c.startswith("setip="):
                        cliente.ip(c.replace("setip=",""))
                    elif c.startswith("sendnombre"):
                        cliente.conexion().send(instruccion_generico("nombre={}".format(cliente.nombre())))
                    print(c)
            elif carga.tipo_carga() == Carga.CARGA_TIPO_MENSAJE:
                print("{}: {}".format(carga.de(),carga.contenido()))
        except:
            print("Ha ocurrido un error")
            cliente.conexion().close()
            break
def write_mensaje():
    while True:
        mensaje = input('Yo: ')
        cliente.conexion().send(mensaje_generico(mensaje,Carga.BROADCASTING))
rt = threading.Thread(target=receive_mensaje)
rt.start()
time.sleep(3)
wt = threading.Thread(target=write_mensaje)
wt.start()