nome = 'Luiz Otavio'
altura = 1.80
peso = 95
imc = peso / (altura ** 2)  # IMC = peso / (altura * altura)

print(f'Luiz Otavio tem {altura:.2f} de altura, ')
print(f'pesa {peso} quilos e seu IMC é: \n{imc:.2f}' )


"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)


# Luiz Otavio tem 1.80 de altura,
# Pesa 95 quilos e seu IMC é
# 29.32