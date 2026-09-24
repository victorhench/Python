vcarro = float(input("Qual a velocidade do seu carro?: "))
multa = 0

if vcarro > 80:
    excesso = vcarro - 80
    multa = excesso * 7
    print("MULTADO! Você excedeu o limite da via e terá que pagar R${:.2f}".format(multa))
print("Tenha um bom dia! dirija com segurança")