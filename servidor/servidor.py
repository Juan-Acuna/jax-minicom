from model.agente import Agente
from model.cargas import Carga, Instruccion, Mensaje, SerializadorCargas
import socket as sk
import threading
import env
import model.comandos as Cmd
import argparse

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Jax-minicom ligera aplicación de comunicación.",add_help=False)
    parser.add_argument("-?","--help","--ayuda",action="help",default=argparse.SUPPRESS,help="muestra las opciones disponibles de la aplicación")
    parser.add_argument("-n","--nombre",dest="nom",help="configura el nombre del servidor")
    parser.add_argument("-h","--host",dest="ip",help="configura la dirección ip del servidor")
    parser.add_argument("-d","--dns",dest="dns",help="configura la dirección DNS del servidor")
    parser.add_argument("-p","--port",dest="port",help="configura el puerto de conexión del servidor")
    parser.add_argument("-c","--carga",dest="peso",help="configura el tamaño de la carga")
    args = parser.parse_args()

    HOST_SERVIDOR:str = env.HOST_SERVIDOR
    PUERTO_SERVIDOR:int = env.PUERTO_SERVIDOR
    TAMANO_CARGA:int = env.TAMANO_CARGA
    NOMBRE_SERVIDOR:str = env.NOMBRE_SERVIDOR

    if args.ip:
        HOST_SERVIDOR:str = env.validar_ip(args.ip)
    if args.dns:
        HOST_SERVIDOR:str = env.validar_dns(args.dns)
    if args.port:
        PUERTO_SERVIDOR:int = env.validar_puerto(args.port)
    if args.peso:
        TAMANO_CARGA:int = env.validar_carga(args.peso)
    if args.nom:
        NOMBRE_SERVIDOR:str = env.validar_nombre(args.nom)

    servidor = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
    servidor.bind((HOST_SERVIDOR, PUERTO_SERVIDOR))
    servidor.listen(20)
    print("Servidor iniciado en {}:{}".format(HOST_SERVIDOR,str(PUERTO_SERVIDOR)))

    conectados:dict[str,Agente]={}

    def mensaje_generico(texto:str, para:str = None) -> bytes:
        p = Carga.BROADCASTING
        if para != None:
            p = para
        return SerializadorCargas.serializar(Mensaje(NOMBRE_SERVIDOR,p,texto,True))
    def instruccion_generica(instruccion:str, para:str = None) -> bytes:
        p = Carga.BROADCASTING
        if para != None:
            p = para
        return SerializadorCargas.serializar(Instruccion(NOMBRE_SERVIDOR,p,instruccion,True))

    def broadcasting(carga:bytes, autor:str):
        for k, v in conectados.items():
            if k != autor:
                v.conexion().send(carga)

    def check_mensajes(cliente:Agente):
        while True:
            try:
                a = cliente.conexion().recv(TAMANO_CARGA)
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
            socketCliente.send(instruccion_generica("{};{}={}".format(Cmd.SEND_NOMBRE,Cmd.SET_SERVER,NOMBRE_SERVIDOR), ip[0]))
            ins:Instruccion
            try:
                ins = SerializadorCargas.deserializar(socketCliente.recv(TAMANO_CARGA))
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