# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FormChat.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class FormChat(object):
    def setupUi(self, FormChat):
        if not FormChat.objectName():
            FormChat.setObjectName(u"FormChat")
        FormChat.resize(352, 432)
        self.txtChat = QTextBrowser(FormChat)
        self.txtChat.setObjectName(u"txtChat")
        self.txtChat.setEnabled(True)
        self.txtChat.setGeometry(QRect(10, 10, 331, 381))
        self.txtChat.setStyleSheet(u"border:1px #aaa solid;")
        self.btnEnviar = QPushButton(FormChat)
        self.btnEnviar.setObjectName(u"btnEnviar")
        self.btnEnviar.setGeometry(QRect(270, 400, 75, 23))
        self.btnVolver = QPushButton(FormChat)
        self.btnVolver.setObjectName(u"btnVolver")
        self.btnVolver.setGeometry(QRect(10, 400, 51, 23))
        self.txtInput = QLineEdit(FormChat)
        self.txtInput.setObjectName(u"txtInput")
        self.txtInput.setGeometry(QRect(70, 400, 191, 20))

        self.retranslateUi(FormChat)

        QMetaObject.connectSlotsByName(FormChat)
    # setupUi

    def retranslateUi(self, FormChat):
        FormChat.setWindowTitle(QCoreApplication.translate("FormChat", u"Chat", None))
        self.btnEnviar.setText(QCoreApplication.translate("FormChat", u"Enviar", None))
        self.btnVolver.setText(QCoreApplication.translate("FormChat", u"Volver", None))
    # retranslateUi

