from math import sqrt, floor

num = int(input("Digite um número: "))

raiz = sqrt(num)


print("A raiz de {} é {:.2f}".format(num, floor(raiz)))

# Existem duas formas principais de importar funcionalidades de uma biblioteca:

# import [nome da biblioteca]
# importa a biblioteca inteira
# exemplo:
# import math
# nesse caso, para usar a raiz quadrada, seria necessário escrever:
# raiz = math.sqrt(num)

# from [nome da biblioteca] import [funcionalidade]
# importa apenas a funcionalidade desejada da biblioteca
# exemplo:
# from math import sqrt
# nesse caso, podemos usar diretamente:
# raiz = sqrt(num)
# é possivel importar mais de uma função dessa forma também