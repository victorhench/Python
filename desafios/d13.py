#aluguel de carro

dias = int(input("Quantos dias você ficou com o carro?: "))
km = float(input("Quantos km rodados?: "))

totdia = dias * 60
totkm = km * 0.15

totp = totdia + totkm

print("O preço total a pagar pelo carro é: {:.2f}".format(totp))