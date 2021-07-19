# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FormLogin.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class FormLogin(object):
    def setupUi(self, FormLogin):
        if not FormLogin.objectName():
            FormLogin.setObjectName(u"FormLogin")
        FormLogin.resize(360, 164)
        self.btnConectar = QPushButton(FormLogin)
        self.btnConectar.setObjectName(u"btnConectar")
        self.btnConectar.setEnabled(False)
        self.btnConectar.setGeometry(QRect(270, 130, 75, 23))
        self.btnConectar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnConectar.setFlat(False)
        self.btnCancelar = QPushButton(FormLogin)
        self.btnCancelar.setObjectName(u"btnCancelar")
        self.btnCancelar.setGeometry(QRect(190, 130, 75, 23))
        self.txtNombre = QLineEdit(FormLogin)
        self.txtNombre.setObjectName(u"txtNombre")
        self.txtNombre.setGeometry(QRect(120, 70, 113, 20))
        self.label = QLabel(FormLogin)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 341, 41))
        font = QFont()
        font.setPointSize(11)
        self.label.setFont(font)

        self.retranslateUi(FormLogin)

        QMetaObject.connectSlotsByName(FormLogin)
    # setupUi

    def retranslateUi(self, FormLogin):
        FormLogin.setWindowTitle(QCoreApplication.translate("FormLogin", u"Acceder", None))
        self.btnConectar.setText(QCoreApplication.translate("FormLogin", u"Conectar", None))
        self.btnCancelar.setText(QCoreApplication.translate("FormLogin", u"Cancelar", None))
        self.txtNombre.setPlaceholderText(QCoreApplication.translate("FormLogin", u"Nombre de usuario", None))
        self.label.setText(QCoreApplication.translate("FormLogin", u"Ingrese un nombre de usuario para conectarse", None))
    # retranslateUi

