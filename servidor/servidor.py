from model.agente import Agente
from model.cargas import Carga, Instruccion, Mensaje, SerializadorCargas
import socket as sk
import threading
import env
import model.comandos as Cmd

servidor = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
servidor.bind((env.HOST_SERVIDOR, env.PUERTO_SERVIDOR))
servidor.listen(20)
print("Servidor iniciado en {}:{}".format(env.HOST_SERVIDOR,str(env.PUERTO_SERVIDOR)))

conectados:dict[str,Agente]={}

def mensaje_generico(texto:str, para:str = None) -> bytes:
    p = Carga.BROADCASTING
    if para != None:
        p = para
    return SerializadorCargas.serializar(Mensaje(env.NOMBRE_SERVIDOR,p,texto,True))
def instruccion_generica(instruccion:str, para:str = None) -> bytes:
    p = Carga.BROADCASTING
    if para != None:
        p = para
    return SerializadorCargas.serializar(Instruccion(env.NOMBRE_SERVIDOR,p,instruccion,True))

def broadcasting(carga:bytes, autor:str):
    for k, v in conectados.items():
        if k != autor:
            v.conexion().send(carga)

def check_mensajes(cliente:Agente):
    while True:
        try:
            a = cliente.conexion().recv(env.TAMANO_CARGA)
            carga:Carga = SerializadorCargas.deserializar(a)
            if carga.tipo_carga() == Carga.CARGA_TIPO_INSTRUCCION:
                cmds:list[str] = carga.comando().split(";")
                for cmd in cmds:
                    if cmd == Cmd.ALERTA:
                        broadcasting(a,carga.de())
            elif carga.tipo_carga() == Carga.CARGA_TIPO_MENSAJE:
                carga:Mensaje
                if carga.es_broadcast:
                    broadcasting(a, cliente.usuario())
                else:
                    conectados[carga.para()].conexion().send(a)
        except:
            conectados.pop(cliente.usuario())
            broadcasting(mensaje_generico("{} se ha desconectado".format(cliente.usuario()),Carga.BROADCASTING),cliente.usuario())
            cliente.conexion().close()
            break
def conexiones():
    while True:
        socketCliente, ip = servidor.accept()
        socketCliente.send(instruccion_generica("{};{}={}".format(Cmd.SEND_NOMBRE,Cmd.SET_SERVER,env.NOMBRE_SERVIDOR), ip[0]))
        ins:Instruccion
        try:
            ins = SerializadorCargas.deserializar(socketCliente.recv(env.TAMANO_CARGA))
        except:
            socketCliente.close()
            continue
        nombre = ins.comando().replace("nombre=","")
        cliente = Agente(nombre, ip[0])
        cliente.conexion(socketCliente)
        cliente.conexion().send(instruccion_generica("{}={},{};{}".format(Cmd.CONFIG,cliente.ip(),cliente.tag(),Cmd.CHAT_ON), cliente.usuario()))
        conectados[cliente.usuario()] = cliente
        print("{} se ha conectado con la IP:{}".format(cliente.usuario(), cliente.ip()))
        broadcasting(mensaje_generico("{} se unio al chat".format(cliente.usuario()),Carga.BROADCASTING),cliente.usuario())
        thread = threading.Thread(target=check_mensajes, args=(cliente,))
        thread.start()
conexiones()