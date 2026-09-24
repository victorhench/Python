import random

computador = random.randint(0,5)

print("Vou pensar em um numero entre 0 e 5. Tente advinhar...")
num = int(input("Em qual numero eu pensei?: "))

print("="*20)
print("Processando...")
print("="*20)

if num == computador:
    print("Parabéns! Conseguiu me vencer!")
else:
    print("Ganhei! Pensei no {} e você no {}".format(computador, num))