"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""
nome = input('Digite seu nome: ')
idade = input('Digite a sua idade: ')

if nome and idade:
    print(f'seu nome é {nome} e você tem {idade} anos')
    print(f'seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print(f'seu nome contém espaços')
    else:
        print(f'seu nome NÃO contém espaços')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira Letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')
else:
    print('Desculpe, você deixou campos vazios.')