from .abc import Abc
from math import floor


class Patente():
    def __init__(self):
        # Inicializacion de variable
        str_patente = ''
        patente = []
        id_patente = 0


    def llenar_num(self,num):
        lista = []
        str_id = str(abs(num))

        for i in range(len(str_id)):
            lista.append(str_id[i])

        if (len(lista) < 3):
            for i in range(len(lista), 3):
                lista.insert(0,'0')

        return lista


    def crear_patente_ser(self, _id):
        assert type(_id)==int and _id>0

        l_num = []
        l_letras = []
        num_let = 26

        for i in range(3,-1,-1):
            letra = floor(_id
                          / (((num_let**i)
                             *1000)
                             +1))

            if letra > 0:
                resto = letra
                        * (((num_let**i)
                            *1000)
                            +1)
                _id = _id - resto
                l_letras.append(Abc.abc[letra])
            else:
                l_letras.append(Abc.abc[letra])

        l_num = self.llenar_num(_id-1)
        self.patente = l_letras + l_num
        str_patente = ''

        for i in range(len(self.patente)):
            str_patente += self.patente[i]

        return str_patente
