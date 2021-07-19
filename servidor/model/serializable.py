from abc import ABC, abstractmethod

class Serializable(ABC):
    def json(self, a=0) -> str:
        return dictJson(vars(self),a)

def dictJson(x:dict, a0 = 0) -> str:
    j = "{"
    a0 += 1
    for k, v in x.items():
        j+="\n"
        for a in range(0,a0):
            j+="\t"
        if isinstance(v,str):
            j += "\"{}\":\"{}\",".format(k,v)
        if isinstance(v,int) or isinstance(v,float) or isinstance(v,bool):
            j += "\"{}\":{},".format(k,str(v).lower())
        elif isinstance(v,Serializable):
            j += "\"{}\":{},".format(k,v.json(a0))
        elif isinstance(v,list):
            j += "\"{}\":{},".format(k,toJson(v,a0))
        elif isinstance(v,dict):
            j += "\"{}\":{},".format(k,dictJson(v,a0))
    j = j[:-1]
    j+="\n"
    a0-=1
    for a in range(0,a0):
        j+="\t"
    j+="}"
    return j

def toJson(x:list,a0=0) -> str:
    j = ""
    j+="["
    a0 += 1
    for i in x:
        j+="\n"
        for a in range(0,a0):
            j+="\t"
        if isinstance(i,str):
            j += "\"{}\",".format(i)
        if isinstance(i,int) or isinstance(i,float) or isinstance(i,bool):
            j += "{},".format(str(i).lower())
        elif isinstance(i,Serializable):
            j += "{},".format(i.json(a0))
        elif isinstance(i,list) or isinstance(i,dict):
            j += "{},".format(toJson(i,a0))
    j = j[:-1]
    a0 -= 1
    j+="\n"
    for a in range(0,a0):
        j+="\t"
    j+="]"
    return j