# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FormPrincipal.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class FormPrincipal(object):
    def setupUi(self, FormPrincipal):
        if not FormPrincipal.objectName():
            FormPrincipal.setObjectName(u"FormPrincipal")
        FormPrincipal.resize(282, 192)
        self.btnAlerta = QPushButton(FormPrincipal)
        self.btnAlerta.setObjectName(u"btnAlerta")
        self.btnAlerta.setGeometry(QRect(90, 40, 101, 101))
        self.btnChat = QPushButton(FormPrincipal)
        self.btnChat.setObjectName(u"btnChat")
        self.btnChat.setGeometry(QRect(230, 160, 41, 23))
        self.btnDesconectar = QPushButton(FormPrincipal)
        self.btnDesconectar.setObjectName(u"btnDesconectar")
        self.btnDesconectar.setGeometry(QRect(10, 160, 81, 23))

        self.retranslateUi(FormPrincipal)

        QMetaObject.connectSlotsByName(FormPrincipal)
    # setupUi

    def retranslateUi(self, FormPrincipal):
        FormPrincipal.setWindowTitle(QCoreApplication.translate("FormPrincipal", u"Form", None))
        self.btnAlerta.setText("")
        self.btnChat.setText(QCoreApplication.translate("FormPrincipal", u"Chat", None))
        self.btnDesconectar.setText(QCoreApplication.translate("FormPrincipal", u"Desconectar", None))
    # retranslateUi

