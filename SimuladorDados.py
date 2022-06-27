#Exibir um valor de 1 até 6 sempre que rodar o programa.
from random import randint
from time import sleep
import os
   
placar_jogador = 0
placar_maquina = 0


def limparTela():
    os.system('cls')

def menu():
    print('=' * 20)
    print(f'{"JOGO DE DADOS":^20}')
    print('=' * 20)
    inicio_jogo = input('Pressione qualquer tecla para começar...')

def placar():
    print('=' * 20)
    print(f'{"Jogador"} {placar_jogador} x {placar_maquina} {"Maquina"}')
    print('=' * 20)

def linha():
    print('-=' * 20)

def validacao(reposta):
    respostas_validas = ['S', 'N', 's', 'n']
    while reposta not in respostas_validas:
        reposta = str(input('Opção inválida, digite [S/N]: ')).upper()
    return reposta.upper()
    
    
#Inicio do Jogo 
limparTela()
menu()   
while True:
    limparTela()
    #Gerando um número aleatório de 1 a 6 para os jogadores.
    numero_jogador = randint(1, 6)
    numero_maquina = randint(1, 6)
    placar()
    #Jogada do usuario
    print('Jogando o dado do jogador...')
    sleep(1)
    print(f'Resultado: {numero_jogador}')
    linha()

    #Jogada do computador
    print('Jogando o dado da maquina...')
    sleep(1)
    print(f'Resultado: {numero_maquina}')
    linha()

    #Estrutura Condicional do Vencedor 
    if numero_jogador > numero_maquina:
        print('O jogador venceu.')
        placar_jogador += 1
    elif numero_jogador == numero_maquina:
        print('Empate.')
    else:
        print('A maquina venceu.')
        placar_maquina += 1
        
    tentar_novamente = input('Quer jogar novamente? [S/N]: ').upper()
    resposta = validacao(tentar_novamente) 
    if resposta == 'N':
        print('Encerrando...')
         limparTela()
         placar()
        break
    else:
        pass

