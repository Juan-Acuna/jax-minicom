from model.agente import Agente
import socket as sk
import threading
from env import TAMANO_CARGA
from model.cargas import Carga, Instruccion, Mensaje, SerializadorCargas
from ventanas import VentanaLogin, VentanaPrincipal, VentanaChat
import model.comandos as cmd
class Cliente():
    server:str
    agente:Agente
    login:VentanaLogin
    principal:VentanaPrincipal
    chat:VentanaChat
    escucha:threading.Thread
    def __init__(self):
        self.server="?"
        self.agente = Agente("?")
        self.login = VentanaLogin(self.agente,self)
        self.agente.conexion(sk.socket(sk.AF_INET, sk.SOCK_STREAM))
        self.principal = VentanaPrincipal(self.agente,self)
        self.chat = VentanaChat(self.agente)
        self.login.siguiente_ventana(self.principal)
        self.principal.siguiente_ventana(self.chat)
        self.principal.anterior_ventana(self.login)
        self.chat.anterior_ventana(self.principal)
        self.chat.txtInput.setEnabled(False)
    def __instruccion_generica(self, instruccion:str) -> bytes:
        return SerializadorCargas.serializar(Instruccion(self.agente.usuario(),self.server,instruccion))
    def activar_escucha(self):
        self.escucha = threading.Thread(target=self.__escuchar__)
        self.escucha.start()
    def alertar(self):
        self.chat.mostrar_sistema("Has enviado una alerta!")
    def __escuchar__(self):
        while True:
            a:bytes = self.agente.conexion().recv(TAMANO_CARGA)
            carga:Carga
            carga = SerializadorCargas.deserializar(a)
            if carga.tipo_carga() == Carga.CARGA_TIPO_INSTRUCCION:
                cmds = carga.comando().split(";")
                for c in cmds:
                    if c.startswith(cmd.CONFIG):
                        l = c.split("=")[1].split(",")
                        self.agente.config(l[0],l[1])
                    elif c.startswith(cmd.ALERTA):
                        self.chat.mostrar_sistema("{} Ha enviado una alerta!".format(carga.de()))
                        self.principal.mostrar_alerta(carga.de())
                    elif c.startswith(cmd.SEND_NOMBRE):
                        self.agente.conexion().send(self.__instruccion_generica("nombre={}".format(self.agente.nombre())))
                    elif c.startswith(cmd.CHAT_ON):
                        self.chat.txtInput.setEnabled(True)
                    elif c.startswith(cmd.CHAT_OFF):
                        self.chat.txtInput.setEnabled(False)
                    elif c.startswith(cmd.SET_SERVER):
                        self.server=c.split("=")
            elif carga.tipo_carga() == Carga.CARGA_TIPO_MENSAJE:
                carga:Mensaje
                if carga.desde_servidor():
                    self.chat.mostrar_servidor(carga)
                else:
                    self.chat.mostrar_mensaje(carga)
            '''try:
                a:bytes = self.agente.conexion().recv(TAMANO_CARGA)
                carga:Carga
                carga = SerializadorCargas.deserializar(a)
                if carga.tipo_carga() == Carga.CARGA_TIPO_INSTRUCCION:
                    cmds = carga.comando().split(";")
                    for c in cmds:
                        if c.startswith(cmd.SET_IP):
                            self.agente.ip(c.split("=")[1])
                        elif c.startswith(cmd.ALERTA):
                            self.chat.mostrar_sistema("{} Ha enviado una alerta!".format(carga.de()))
                        elif c.startswith(cmd.SEND_NOMBRE):
                            self.agente.conexion().send(self.__instruccion_generica("nombre={}".format(self.agente.nombre())))
                        elif c.startswith(cmd.CHAT_ON):
                            self.chat.txtInput.setEnabled(True)
                        elif c.startswith(cmd.CHAT_OFF):
                            self.chat.txtInput.setEnabled(False)
                        elif c.startswith(cmd.SET_SERVER):
                            self.server=c.split("=")
                elif carga.tipo_carga() == Carga.CARGA_TIPO_MENSAJE:
                    carga:Mensaje
                    if carga.desde_servidor():
                        self.chat.mostrar_servidor(carga)
                    else:
                        self.chat.mostrar_mensaje(carga)
            except:
                print("Ha ocurrido un error")
                self.agente.conexion().close()
                break'''

