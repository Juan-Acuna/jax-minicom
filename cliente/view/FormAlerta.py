# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FormAlerta.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class FormAlerta(object):
    def setupUi(self, FormAlerta):
        if not FormAlerta.objectName():
            FormAlerta.setObjectName(u"FormAlerta")
        FormAlerta.setWindowModality(Qt.WindowModal)
        FormAlerta.setEnabled(True)
        FormAlerta.resize(396, 142)
        self.imgAlerta = QLabel(FormAlerta)
        self.imgAlerta.setObjectName(u"imgAlerta")
        self.imgAlerta.setGeometry(QRect(20, 0, 131, 131))
        self.gif = QMovie("./assets/alerta.gif")
        self.imgAlerta.setMovie(self.gif)
        #self.imgAlerta.setPixmap(QPixmap(u"./assets/alerta.gif"))
        self.imgAlerta.setScaledContents(True)
        self.lbAlerta = QLabel(FormAlerta)
        self.lbAlerta.setObjectName(u"lbAlerta")
        self.lbAlerta.setGeometry(QRect(160, 60, 231, 71))
        font = QFont()
        font.setPointSize(16)
        self.lbAlerta.setFont(font)
        self.lbAlerta.setAlignment(Qt.AlignCenter)
        self.lbUsuario = QLabel(FormAlerta)
        self.lbUsuario.setObjectName(u"lbUsuario")
        self.lbUsuario.setGeometry(QRect(160, 10, 231, 51))
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        font1.setWeight(75)
        self.lbUsuario.setFont(font1)
        self.lbUsuario.setAlignment(Qt.AlignCenter)

        self.retranslateUi(FormAlerta)

        QMetaObject.connectSlotsByName(FormAlerta)
    # setupUi

    def retranslateUi(self, FormAlerta):
        FormAlerta.setWindowTitle("")
        self.imgAlerta.setText("")
        self.lbAlerta.setText(QCoreApplication.translate("FormAlerta", u"ha enviado una alerta!", None))
        self.lbUsuario.setText(QCoreApplication.translate("FormAlerta", u"<usuario#00000>", None))
    # retranslateUi

