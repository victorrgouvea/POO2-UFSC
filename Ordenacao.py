"""Universidade Federal de Santa Catarina.
   CTC - Centro Tecnologico - http://ctc.ufsc.br
   INE - Departamento de Informatica e Estatistica - http://inf.ufsc.br
"""

class Ordenacao():

    def __init__(self, array_para_ordenar):
        self.array_para_ordenar = array_para_ordenar 

    def ordena(self):
        for index in range(0, len(self.array_para_ordenar)):
            index_menor = index

            for proximo in range(index + 1, len(self.array_para_ordenar)):
                if self.array_para_ordenar[proximo] < self.array_para_ordenar[index_menor]:
                    index_menor = proximo

            self.array_para_ordenar[index], self.array_para_ordenar[index_menor] = self.array_para_ordenar[index_menor], self.array_para_ordenar[index]

    def toString(self):
        self.array_para_ordenar = ','.join(map(str, self.array_para_ordenar))

        return self.array_para_ordenar
        
'''
def main():
    array = [int(x) for x in input().split()]
    
    array_sort = Ordenacao(array)
    array_sort.ordena()

    print(array_sort.toString())

main()
'''
'''
        print('"', end='')
        print(self.array_para_ordenar[0], end='')
        for i in range(1, len(self.array_para_ordenar)):
            print(",%d" % self.array_para_ordenar[i], end='')
        print('"')
        '''