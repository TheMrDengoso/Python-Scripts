import random
a = str(input("Digite o 1º nome: "))
b = str(input("Digite o 2º nome: "))
c = str(input("Digite o 3º nome: "))
d = str(input("Digite o 4º nome: "))

lista=[a,b,c,d]
s=random.choice(lista)
print("O nome escolhido foi: {}".format(s))