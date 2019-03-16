v = float(input("Digite o valor do produto: "))
d = v*(5/100)
t = v-d
print("O Valor do produto com desconto é R${:.2f} \nO desconto foi de R${:.2f}".format(t, d))