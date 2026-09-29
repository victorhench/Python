sal = float(input("Qual é o salário do funcionário? R$: "))

if sal > 1250:
    novosal = sal + (sal * 0.10)
else:
    novosal = sal + (sal * 0.15)

print("Quem ganhava R${} agora recebe R${:.2f}".format(sal, novosal))