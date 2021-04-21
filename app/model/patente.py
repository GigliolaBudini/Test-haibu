from .abc import Abc
from math import floor


class Patente():
    def __init__(self):
        # Inicializacion de variable
        str_patente = ''
        patente = []
        id_patente = 0


    def llenar_num(self,num):
        if type(num) is not int:
            raise Exception('El parametro ingresado debe ser tipo int')

        lista = []
        str_id = str(num)

        for i in range(len(str_id)):
            lista.append(str_id[i])

        if (len(lista) < 3):
            for i in range(len(lista), 3):
                lista.insert(0,'0')

        return lista


    def crear_patente_ser(self, _id):
        if type(_id) is not int:
            raise Exception('El id debe ser de tipo entero')

        if not (0 <= _id <= (26**4)*1000):
            raise Exception('id fuera de rango')

        l_num = []
        l_letras = []
        num_let = 26

        for i in range(3,-1,-1):
            letra = floor(_id
                          / (((num_let**i)
                          *1000)
                          +1))

            if letra > 0:
                resto = letra * (( (num_let**i) *1000) +1)
                _id = _id - resto
                l_letras.append(Abc.abc[int(letra)].upper())
            else:
                l_letras.append(Abc.abc[int(letra)].upper())

        l_num = self.llenar_num(_id-1)
        self.patente = l_letras + l_num
        str_patente = ''

        for i in range(len(self.patente)):
            str_patente += self.patente[i]

        return str_patente
