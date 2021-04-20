class Matriz():
    def __init__(self,r,c,z):
        self.r = r
        self.c = c
        self.z = z
        self.matriz = []

    def crear_matriz(self):
        assert self.z > 0 and self.z < 1000000

        for i in range(1,self.r+1):
            if i == 1:
                n = self.z
            else:
              n = i + self.z -1

            fila = []
            for e in range(1,self.c+1):
                fila.append(n)

            self.matriz.append(fila)

    def sumar_matriz(self,x,y):
        total = 0

        for i in range(y+1):
            for e in range(x+1):
                total += self.matriz[i][e]

        return total
