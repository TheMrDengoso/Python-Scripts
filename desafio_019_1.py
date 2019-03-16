import random
a = str(input("Digite o 1º nome: "))
b = str(input("Digite o 2º nome: "))
c = str(input("Digite o 3º nome: "))
d = str(input("Digite o 4º nome: "))

s = random.randint(1,4)
if(s==1):
    print("O nome escolhido foi: {}".format(a))
elif(s==2):
    print("O nome escolhido foi: {}".format(b))
elif(s==3):
    print("O nome escolhido foi: {}".format(c))
else:
    print("O nome escolhido foi {}".format(d))