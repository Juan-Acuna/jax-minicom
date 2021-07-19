import socket
from PySide2 import QtWidgets
from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt
from view.FormLogin import FormLogin
from view.FormPrincipal import FormPrincipal
from view.FormChat import FormChat
from view.FormAlerta import FormAlerta
from model.cargas import Carga, Mensaje, Instruccion, SerializadorCargas
from model.agente import Agente
import env
from time import sleep
import model.comandos as cmd

class VentanaAlerta(QWidget, FormAlerta):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setGeometry(0, 0, 396, 142)
        self.setWindowOpacity(0)
        self.gif.start()
    def __aumentar_opacidad__(self):
        while True:
            if self.windowOpacity() >= 1:
                sleep(4)
                self.__disminuir_opacidad__()
                break
            self.setWindowOpacity(self.windowOpacity() + 0.050)
            self.update()
            sleep(0.05)
    def __disminuir_opacidad__(self):
        while True:
            if self.windowOpacity() <= 0:
                self.setVisible(False)
                break
            self.setWindowOpacity(self.windowOpacity() - 0.050)
            self.update()
            sleep(0.05)
    def mostrar_alerta(self, fuente:str):
        self.gif.setPaused(False)
        self.lbUsuario.setText(fuente)
        self.setVisible(True)
        self.__aumentar_opacidad__()
        self.gif.setPaused(True)

class VentanaLogin(QWidget, FormLogin):
    __cliente:Agente
    __siguiente:any
    __maestro:any
    def __init__(self, cliente:Agente, maestro):
        super().__init__()
        self.__cliente=cliente
        self.__maestro=maestro
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.btnConectar.clicked.connect(self.btnConectar_click)
        self.btnCancelar.clicked.connect(self.btnCancelar_click)
        self.txtNombre.textChanged.connect(self.txtNombre_text_changed)
    def agente(self) -> Agente:
        return self.__cliente
    def siguiente_ventana(self, ventana = None):
        if ventana == None:
            return self.__siguiente
        else:
            self.__siguiente=ventana
    def btnConectar_click(self):
        self.__cliente.nombre(self.txtNombre.text())
        if isinstance(self.__cliente.conexion(),socket.socket):
            self.__cliente.reiniciar_conexion()
        self.__cliente.conexion().connect((env.HOST_SERVIDOR, env.PUERTO_SERVIDOR))
        self.__maestro.activar_escucha()
        self.__siguiente.show()
        self.hide()
    def btnCancelar_click(self):
        self.close()
        self.destroy()
    def txtNombre_text_changed(self):
        nombre = self.txtNombre.text()
        if nombre != None and (len(nombre)>0):
            self.btnConectar.setEnabled(True)
        else:
            self.btnConectar.setEnabled(False)

class VentanaPrincipal(QWidget,FormPrincipal):
    __usuario:Agente
    __anterior:VentanaLogin
    __siguiente:any
    __master:any
    __alerta:VentanaAlerta
    def __init__(self, agente:Agente,master):
        super().__init__()
        self.__alerta=VentanaAlerta()
        self.__alerta.setObjectName(u"__alerta")
        self.__alerta.show()
        self.__alerta.setVisible(False)
        self.__alerta.update()
        self.__master=master
        self.__usuario=agente
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.btnAlerta.clicked.connect(self.btnAlerta_click)
        self.btnDesconectar.clicked.connect(self.btnDesconectar_click)
        self.btnChat.clicked.connect(self.btnChat_click)
    def mostrar_alerta(self, fuente:str):
        self.__alerta.mostrar_alerta(fuente)
    def anterior_ventana(self, anterior:VentanaLogin = None):
        if anterior == None:
            return self.__anterior
        else:
            self.__anterior=anterior
    def siguiente_ventana(self, ventana = None):
        if ventana == None:
            return self.__siguiente
        else:
            self.__siguiente=ventana
    def btnAlerta_click(self):
        self.btnAlerta.setEnabled(False)
        self.__master.alertar()
        self.__usuario.conexion().send(self.__alerta_generica())
        sleep(2)
        self.btnAlerta.setEnabled(True)
    def btnChat_click(self):
        self.__siguiente.show()
    def btnDesconectar_click(self):
        self.__usuario.conexion().close()
        self.__anterior.show()
        self.hide()
    def __alerta_generica(self) -> bytes:
        return SerializadorCargas.serializar(Instruccion(self.__usuario.usuario(),Carga.BROADCASTING,cmd.ALERTA))

class VentanaChat(QWidget, FormChat):
    __usuario:Agente
    __anterior:VentanaPrincipal
    def __init__(self, agente:Agente):
        super().__init__()
        self.__usuario=agente
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.btnEnviar.clicked.connect(self.btnEnviar_click)
        self.btnVolver.clicked.connect(self.btnVolver_click)
    def anterior_ventana(self, anterior:VentanaPrincipal = None):
        if anterior == None:
            return self.__anterior
        else:
            self.__anterior=anterior
    def btnEnviar_click(self):
        texto = self.txtInput.text()
        if texto != None and (len(texto)>0):
            self.__usuario.conexion().send(self.__mensaje_generico(self.txtInput.text(),Carga.BROADCASTING))
            self.txtChat.append("Yo: {}".format(self.txtInput.text()))
            self.txtInput.setText("")
    def mostrar_mensaje(self, msg:Mensaje):
        self.txtChat.append("<span>[{}]: {}</span>".format(msg.de(),msg.contenido()))
    def mostrar_servidor(self, msg:Mensaje):
        self.txtChat.append("<span><b>{}<b>: {}<span>".format(msg.de(),msg.contenido()))
    def mostrar_sistema(self, msg:str):
        self.txtChat.append("<hr style=\"border: 1px #ccc solid;width:80%;\"><center><span style=\"color:#ccc;\">{}</span></center>".format(msg))
    def btnVolver_click(self):
        self.__anterior.show()
        self.hide()
    def __instruccion_generica(self, instruccion:str) -> bytes:
        return SerializadorCargas.serializar(Instruccion(self.__usuario.usuario(),env.HOST_SERVIDOR,instruccion))
    def __mensaje_generico(self, texto:str, para:str = None) -> bytes:
        p = Carga.BROADCASTING
        if para != None:
            p = para
        return SerializadorCargas.serializar(Mensaje(self.__usuario.usuario(),p,texto))