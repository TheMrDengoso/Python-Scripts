km = float(input("Digite a quantidade de km percorridos: "))
dias = int(input("Digite a quantidade de dias: "))
km_r = km*0.15
dias_r = dias*60
t = km_r + dias_r
print("Você rodou {}km \nPreço por km's rodados: R${:.2f} \nDias que permaneceu com o carro: {} dias \nValor dos dias: R${} \nTotal a pagar: R${:.2f}".format(km, km_r, dias, dias_r, t))