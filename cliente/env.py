from io import open
from os import path

HOST_SERVIDOR:str = "127.0.0.1"
PUERTO_SERVIDOR:int = 6000
TAMANO_CARGA:int = 1024
if path.exists("config.txt"):
    l = open("config.txt","r").readlines()
    for s in l:
        if s.strip().startswith("#"):
            continue
        elif s.strip().upper().startswith("IP"):
            s:str = s.strip().split("=")[1]
            if s.strip().upper() == "LOCALHOST":
                HOST_SERVIDOR = s
            else:
                if not s.replace(".","").isdigit():
                    raise Exception("Dirección IP inválida: formato IP incorrecto.")
                i = s.split(".")
                if len(i) != 4:
                    raise Exception("Dirección IP inválida: formato IP incorrecto.")
                if (int(i[0]) > 255 or int(i[0]) < 0):
                    raise Exception("Dirección IP inválida: no se permiten segmentos mayores a 255 ni menores a 0.")
                elif (int(i[1]) > 255 or int(i[1]) < 0):
                    raise Exception("Dirección IP inválida: no se permiten segmentos mayores a 255 ni menores a 0.")
                elif (int(i[2]) > 255 or int(i[2]) < 0):
                    raise Exception("Dirección IP inválida: no se permiten segmentos mayores a 255 ni menores a 0.")
                elif (int(i[3]) > 255 or int(i[3]) < 0):
                    raise Exception("Dirección IP inválida: no se permiten segmentos mayores a 255 ni menores a 0.")
                HOST_SERVIDOR = s
        elif s.strip().upper().startswith("DNS"):
            HOST_SERVIDOR = s.strip().split("=")[1]
        elif s.strip().upper().startswith("PUERTO"):
            s:str = s.strip().split("=")[1]
            if s.isdigit() and (int(s) < 65535 or int(s) > 0):
                PUERTO_SERVIDOR = int(s)
            else:
                raise Exception("Puerto inválido: debe ser un número entre 0 y 65535.")
        elif s.strip().upper().startswith("CARGA"):
            s:str = s.strip().split("=")[1]
            if s.isdigit() and (int(s) > 1024):
                TAMANO_CARGA = int(s)
            else:
                raise Exception("Tamaño de Carga inválido: debe ser un número mayor o igual a 1024.")