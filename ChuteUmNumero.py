import os 
from random import randint
os.system('cls')


def limparTela():
    os.system('cls')
    

def menu():
    print('=' * 40)
    print(f'{"CHUTE UM NÚMERO":^40}')
    print('=' * 40)


def validacao_numero():
    numero = input('Digite um número entre 1 a 10: ')  
    while True:
        numeros_disponiveis = [x for x in range(1, 11)]
        numero.strip()
        if numero.isnumeric() == False or numero.isalpha() == True or int(numero) not in numeros_disponiveis:
            numero = input('Opção inválida, digite um número inteiro entre 1 e 10: ')
            print('=' * 60) 
        else:
            break
    numero = int(numero)
    return numero
    

    print(f'Recorde atual de tentativas: {recorde}')
    print('=' * 40)
    
numero_tentativas = 1
recorde_tentativas = 0
identificador_partida = 0
numero_vitorias = 0
respostas_validas = ['s', 'n', 'S', 'N']
#O programa deve gerar um número aleatorio (1, 10) para o usuario atentar advinhar.
menu()
while True:
    if identificador_partida == 0:
        numero_aleatorio = randint(1, 10)
    else: pass
    #Chute um número.(Com validação)
    tentativa_usuario = validacao_numero()
    #Verificação de maior ou menor;
    if tentativa_usuario > numero_aleatorio:
        print('O número sorteado é menor...')
        print('=' * 40) 
        numero_tentativas += 1
        identificador_partida += 1
    elif tentativa_usuario < numero_aleatorio:
        print('O número sorteado é maior...')
        print('=' * 40) 
        numero_tentativas += 1
        identificador_partida += 1
    else:
        print('PARABÉNS!, você ganhou.')
        print(f'Você precisou de {numero_tentativas} tentativa(s).')
        numero_vitorias += 1
        print('=' * 40) 
        #Perguntar se quer continuar jogando.
        continuar = input('Quer continuar? [S/N]: ').upper()
        while continuar not in respostas_validas:
            continuar = input('Resposta inválida, digite [S/N]: ').upper()
        if continuar == 'N':
            limparTela()
            break
        else:
            identificador_partida = 0
            numero_tentativas = 1
            limparTela()
#Resultado final          
print('=' * 40)            
print(f'Número de vitórias: {numero_vitorias}')
print('=' * 40)


