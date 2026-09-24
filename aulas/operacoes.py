n1 = int(input("Um valor: "))
n2 = int(input("Outro Valor: "))

# n1 e n2 são variáveis inteiras que recebem os valores digitados pelo usuário.
# O int() transforma os valores recebidos pelo input() em números inteiros.

print("A soma vale: {}".format(n1 + n2))

# O print() exibe uma informação na tela.
# O .format() permite inserir o resultado de uma operação dentro do texto, ou uma variavel.
# Nesse caso, n1 + n2 calcula a soma dos dois valores.

print("A multiplicação vale: {}".format(n1 * n2))

# Nesse caso, n1 * n2 calcula a multiplicação dos dois valores.

print("A divisão vale: {}".format(n1 / n2))

# Nesse caso, n1 / n2 calcula a divisão dos dois valores.
# O operador / sempre realiza uma divisão comum, podendo gerar casas decimais.

print("A divisão inteira vale: {}".format(n1 // n2))

# Nesse caso, n1 // n2 realiza uma divisão inteira.
# O resultado não considera a parte decimal.

print("A exponenciação vale: {}".format(n1 ** n2))

# Nesse caso, n1 ** n2 realiza a exponenciação.
# O primeiro número é elevado à potência do segundo número.