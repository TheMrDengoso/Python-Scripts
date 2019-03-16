import math
n = float(input("Digite o valor do ângulo desejado: "))
sen = math.sin(math.radians(n))
cos = math.cos(math.radians(n))
tag = math.tan(math.radians(n))
print("O Ângulo desejado foi: {} \nO seno dele é: {:.2f} \nO cosseno dele é: {:.2f} \nA tangente dele é: {:.2f}".format(n, sen, cos, tag))