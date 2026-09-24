#pega um preço e mosra ele em desconto

preco = float(input("Quanto custa esse produto?: R$"))

novopreco = preco - (preco * 0.05)

print("O produto esta com desconto de 5%.")
print("Agora ele vai custar: {:.2f}".format(novopreco))