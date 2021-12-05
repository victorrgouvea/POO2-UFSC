'''Os métodos da classe "Series" implementam alguma series matemáticas.
   O valor atribuído aos métodos de mostrar a sequencia indica quantos valores vão ser 
   mostrados a partir do ínicio da sequência.
   Já um valor k atribuído aos outros métodos(fibonacci, fatorial, fibonarial) indica o
   k-ésimo valor da sequência.'''

class Series:

    def fibonacci(valor):
        if valor <= 2:
            return 1
        
        return Series.fibonacci(valor-1) + Series.fibonacci(valor-2)

    def sequencia_fibonacci(valor):
        lista = []
        for n in range(1, valor+1):
            lista.append(Series.fibonacci(n))

        return lista

    def fatorial(valor):
        if valor == 0:
            return 1

        return valor * Series.fatorial(valor-1)

    def sequencia_fatorial(valor):
        lista = []
        for n in range(valor+1):
            lista.append(Series.fatorial(n))

        return lista

    def fibonarial(valor):
        lista = Series.sequencia_fibonacci(valor)
        total = lista[0]
        for i in range(1, len(lista)):
            total = total * lista[i]

        return total

    def primo(numero):
        primo = True
        for n in range(2, numero):
            if (numero % n) == 0:
                primo = False
                break

        return primo

    def sequencia_primos(valor):
        primos = []
        counter = 2
        for _ in range(valor):
            while True:
                if Series.primo(counter):
                    primos.append(counter)
                    counter += 1
                    break
                counter += 1

        return primos
      

# Exemplos:
print(Series.fibonacci(5))
print(Series.sequencia_fibonacci(6))

print(Series.fatorial(4))
print(Series.sequencia_fatorial(4))

print(Series.fibonarial(3))

print(Series.sequencia_primos(6))