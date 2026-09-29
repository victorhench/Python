

altura = float(input("Quantos metros tem sua parede em altura?: "))
largura = float(input("E largura?: "))

area = largura * altura
tinta = 2

tintanec = area / tinta

print("quantidade de tinta necessaria para pintar a parede é: {}".format(tintanec))