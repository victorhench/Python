distancia = float(input("Qual a distância da sua viagem?: "))

if distancia > 200:
    preco = distancia * 0.45
    print("Você está prestes a começar uma viagem de{}Km.".format(distancia))
    print("E o preço da sua passagem será de R${:.2f}".format(preco))
else:
    preco = distancia * 0.50
    print("Você está prestes a começar uma viagem de{}Km.".format(distancia))
    print("E o preço da sua passagem será de R${:.2f}".format(preco))