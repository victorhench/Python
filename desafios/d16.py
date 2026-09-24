import math

a = int(input("Digite o ângulo que deseja: "))

sen = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tan = math.tan(math.radians(a))

print("o angulo de {} tem o SENO de {:.2f}".format(a, sen))
print("o angulo de {} tem o COSSENO de {:.2f}".format(a, cos))
print("o angulo de {} tem a TANGENTE de {:.2f}".format(a, tan))