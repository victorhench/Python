print("="*20)
print("ANALISADOR DE TRIANGULO")
print("="*20)

a = float(input("Digite o valor do primeiro segmento: "))
b = float(input("Digite o valor do segundo segmento: "))
c = float(input("Digite o valor do terceiros segmento: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("Os segmentos acima PODEM FORMAR um triangulo.")
else:
    print("Os segmentos acima NÃO PODEM FORMAR um triangulo")