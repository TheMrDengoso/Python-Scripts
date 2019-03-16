s = float(input("Digite o valor do salário: "))
a = s*(15/100)
sf = s+a
print("O salário era no valor de R${:.2f} \nO novo salário é: R${:.2f} \nO aumento foi de R${:.2f}".format(s,sf,a))
