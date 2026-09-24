nome = input("Digite seu nome completo: ")

print("Analisando seu nome...")

print("Seu nome em maiúscula é {}".format(nome.upper()))
print("Seu nome em minúscula é {}".format(nome.lower()))
print("Seu nome tem ao todo {} letras".format(len(nome.replace(" ", ""))))

primeiro_nome = nome.split()

print("Seu primeiro nome é {} e ele tem {} letras".format(primeiro_nome[0], len(primeiro_nome[0])))