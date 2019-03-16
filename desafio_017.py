import math
c1 = float(input("Digite o valor do cateto adjacente: "))
c2 = float(input("Digite o valor do cateto oposto: "))
ca = c1**2
co = c2**2
h = math.sqrt(ca+co)
print("O valor do cateto adjacente é: {} e ao quadrado é: {:.2f} \nO valor do cateto oposto é: {} e ao quadrado é: {:.2f}\nO valor da hipotenusa: {:.2f}".format(c1, ca, c2, co, h))