#o programa mostra quantos dolares a pesoa pode comprar

reais = float(input("Quanto de dinheiro em reais você tem?: "))

dolar = reais / 5.11

print("Você pode comprar US${:.2f} em dolares".format(dolar))