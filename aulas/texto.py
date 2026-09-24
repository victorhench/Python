frase1 = "Curso em Video Python"
frase2 = "Aprendendo Python"
frase3 = "Esta frase esta dividida"

frase_div = frase3.split()

print(frase1)

print(frase2)

print("="*20)
# Exibe as duas frases na tela


print(frase1.lower())

print(frase2.lower())

print("="*20)
# .lower() transforma todos os caracteres da string em letras minúsculas


print(frase1.upper())

print(frase2.upper())

print("="*20)
# .upper() transforma todos os caracteres da string em letras maiúsculas


print(frase1[3:13])

print(frase2[:12:2])

print("="*20)
# Os colchetes permitem acessar partes da string usando índices.
# [3:13] pega os caracteres do índice 3 até o 12.
# [:12:2] pega do início até o índice 11, pulando de 2 em 2 caracteres.


print(len(frase1))

print(len(frase2))

print("="*20)
# len() conta quantos caracteres existem dentro da string, incluindo os espaços.


print(frase1.replace(frase1, frase2))

print(frase2.replace(frase2, frase1))

print("="*20)
# .replace() substitui uma parte da string por outra.
# Neste caso, toda a frase1 é substituída pela frase2 e vice-versa.


print(frase1.replace(frase1, frase1.upper()))

print(frase2.replace(frase2, frase2.upper()))

print("="*20)
# .replace() também pode ser usado junto com .upper().
# Aqui, a frase original é substituída pela mesma frase, porém em letras maiúsculas.


print("Curso" in frase1)

print("Curso" in frase2)

print("="*20)
# O operador "in" verifica se determinado texto existe dentro da string.
# O resultado será True se encontrar e False se não encontrar.


print("Aprendendo" in frase1)

print("Aprendendo" in frase2)

print("="*20)
# Novamente usamos "in" para verificar se a palavra existe dentro de cada frase.


print(frase1.find("Curso"), frase1.find("Video"))

print(frase2.find("Aprendendo"), frase2.find("Python"))

print("="*20)
# .find() procura uma palavra ou trecho dentro da string e retorna o índice
# onde ele começa. Se não encontrar, retorna -1.


print(frase1.split())

print(frase2.split())

print(frase_div[0])

print(frase_div[2] [3])

print("="*20)
# .split() divide a string em partes, usando os espaços como separadores.
# O resultado é uma lista.
# Podemos acessar cada palavra da lista usando seus índices.
# frase_div[0] pega a primeira palavra.
# frase_div[2][3] pega o quarto caractere da terceira palavra.