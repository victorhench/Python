#um programa que calcula a área de uma parede e mostra quanto de tinta precisa para pintar a parede toda, sabendo que cada litro pinta 2m quadrados

altura = float(input("Quantos metros tem sua parede em altura?: "))
largura = float(input("E largura?: "))

area = largura * altura
tinta = 2

tintanec = area / tinta

print("quantidade de tinta necessaria para pintar a parede é: {}".format(tintanec))