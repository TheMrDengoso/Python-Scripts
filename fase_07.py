n1 = int(input("Digite um valor: "))
n2 = int(input("Digite o outro valor: "))
s=n1+n2
d=n1/n2
m=n1*n2
r=n1%n2
di=n1//n2

print("A soma é {}\nDivisão é {:.2f}\nProduto é {}\nO resto é {}\nDivisão inteira é {}".format(s, d, m, r, di))