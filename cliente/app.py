from PySide2.QtWidgets import QApplication
from cliente import Cliente

if __name__=="__main__":
    app = QApplication()
    #app.setQuitOnLastWindowClosed(False)
    cliente = Cliente()
    window = cliente.login
    window.show()
    app.exec_()