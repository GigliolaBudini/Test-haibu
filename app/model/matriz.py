class Matriz():
    def __init__(self,r,c,z):
        self.r = r
        self.c = c
        self.z = z
        self.matriz = []

    def crear_matriz(self):
        if not (0 < self.z <= 1000000):
            raise Exception('Parametro z esta fuera de rango')
        if not type(self.r)==int and type(self.c)==int:  
            raise Exception('Los parametros z y c deben ser de tipo enteros')

        for i in range(1,self.r+1):
            if i == 1:
                num = self.z
            else:
               num = i + self.z -1

            fila = []
            for e in range(1,self.c+1):
                fila.append(num)

            self.matriz.append(fila)

    def sumar_matriz(self,x,y):
        if type(x) is not int and type(y) is not int:
            raise Exception('Los parametros deben ser tipo enteros')

        total = 0

        for i in range(y+1):
            for e in range(x+1):
                total += self.matriz[i][e]

        return total
