"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
#num_int = input('Digite um número inteiro: ')
#if num_int.isnumeric():
#    num_int = int(num_int)
#    if num_int % 2 == 0:
#        print(f'O número {num_int} é Par')
#    else:
#        print(f'O número {num_int} é Ímpar')
#else:
#    print('O número digitado não é inteiro.') 

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
#entrada = input('Digite a hora em números inteiros: ')

#try:
    #hora = int(entrada)
    #if hora >= 0 and hora <= 11:
        #print('Bom dia')
    #elif hora >= 12 and hora <= 17:
        #print('Boa tarde')
    #elif hora >= 18 and hora <= 23:
        #print('Boa noite')
    #else:
        #print('Horário inválido')
#except:
    #print('Horário inválido')
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
primeiro_nome = input('Digite seu primeiro nome: ')

if len(primeiro_nome) <= 4:
    print('Seu nome é curto')
elif len(primeiro_nome) >= 5 and len(primeiro_nome) <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')