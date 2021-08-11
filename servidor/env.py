from io import open
from os import path, environ

HOST_SERVIDOR:str = "127.0.0.1"
PUERTO_SERVIDOR:int = 6000
TAMANO_CARGA:int = 1024
NOMBRE_SERVIDOR:str = "Servidor"

def validar_ip(ip:str) -> str:
    if ip.strip().startswith('%') and ip.strip().endswith('%'):
        return environ.get(ip.replace('%',''))
    elif ip.strip().startswith('%') or ip.strip().endswith('%'):
        raise Exception("Dirección IP inválida: formato de entrada incorrecto. Esperado: %VALOR%, Encontrado: {}".format(ip.strip()))
    elif ip.strip().upper() == "LOCALHOST":
        return ip
    else:
        if not ip.replace(".","").isdigit():
            raise Exception("Dirección IP inválida: formato IP incorrecto.")
        i = ip.split(".")
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
        return ip
def validar_dns(dns:str) -> str:
    if dns.strip().startswith('%') and dns.strip().endswith('%'):
        return environ.get(dns.replace('%',''))
    elif dns.strip().startswith('%') or dns.strip().endswith('%'):
        raise Exception("DNS Inválido: formato de entrada incorrecto. Esperado: %VALOR%, Encontrado: {}".format(dns.strip()))
    else:
        return dns
def validar_puerto(port:str) -> int:
    if port.strip().startswith('%') and port.strip().endswith('%'):
        return int(environ.get(port.replace('%','')))
    elif port.strip().startswith('%') or port.strip().endswith('%'):
        raise Exception("Puerto inválido: formato de entrada incorrecto. Esperado: %VALOR%, Encontrado: {}".format(port.strip()))
    elif port.isdigit() and (int(port) <= 65535 or int(port) > 0):
        return int(port)
    else:
        raise Exception("Puerto inválido: debe ser un número entre 0 y 65535.")
def validar_carga(peso:str) -> int:
    if peso.strip().startswith('%') and peso.strip().endswith('%'):
        return int(environ.get(peso.replace('%','')))
    elif peso.strip().startswith('%') or peso.strip().endswith('%'):
        raise Exception("Tamaño de Carga inválido: formato de entrada incorrecto. Esperado: %VALOR%, Encontrado: {}".format(peso.strip()))
    elif peso.isdigit() and (int(peso) >= 1024):
        return int(peso)
    else:
        raise Exception("Tamaño de Carga inválido: debe ser un número mayor o igual a 1024.")
def validar_nombre(nombre:str) -> str:
    if nombre.strip().startswith('%') and nombre.strip().endswith('%'):
        return environ.get(nombre.replace('%',''))
    elif nombre.strip().startswith('%') or nombre.strip().endswith('%'):
        raise Exception("Nombre de Servidor inválido: formato de entrada incorrecto. Esperado: %VALOR%, Encontrado: {}".format(nombre.strip()))
    else:
        return nombre.split("=")[1]

if path.exists("config.txt"):
    l = open("config.txt","r").readlines()
    for s in l:
        if s.strip().startswith("#"):
            continue
        elif s.strip().upper().startswith("IP"):
            s:str = s.strip().split("=")[1]
            HOST_SERVIDOR = validar_ip(s)
        elif s.strip().upper().startswith("DNS"):
            s:str = s.strip().split("=")[1]
            HOST_SERVIDOR = validar_dns(s)
        elif s.strip().upper().startswith("PUERTO"):
            s:str = s.strip().split("=")[1]
            PUERTO_SERVIDOR = validar_puerto(s)
        elif s.strip().upper().startswith("CARGA"):
            s:str = s.strip().split("=")[1]
            TAMANO_CARGA = validar_carga(s)
        elif s.strip().upper().startswith("NOMBRE"):
            s:str = s.strip().split("=")[1]
            NOMBRE_SERVIDOR = validar_nombre(s)
