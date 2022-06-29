import os
from random import choice
from time import sleep

#Limpar a Tela
def linha():
    print('=' * 40)

#Limpar Tela (VSCODE)    
def limparTela():
    os.system('cls')

#Menu com as opções de jogadas
def menu():
    print(f'''Escolha uma das opções abaixo para jogar.
{"=" * 40}
                [1] Pedra
                [2] Papel
                [3] Tesoura
{"=" * 40}''')
    
#O usuario deve escolher uma das 3 opçoes
def escolha():
    opcoes_disponiveis = ['1', '2', '3']
    nomes_jogadas = ['Pedra', 'Papel', 'Tesoura']
    escolha = input('Sua jogada: ').strip()
    linha()
    while True:
        if escolha not in opcoes_disponiveis:
            escolha = input('Opção inválida, por favor digite um número entre 1 e 3: ').strip()
            linha()
        else:
            break
    for i, x in enumerate(opcoes_disponiveis):
        if x == escolha:
            print('Você escolheu:', nomes_jogadas[i]) 
            linha()
            escolha = int(escolha)
            return escolha

#Estrutura condicional de vitória ou derrota.
def partida(jogador1, jogador2):
    #Jogador 1 = Pedra x Jogadas do Computador
    if jogador1 == 1 and jogador2 == 1:
        print('Pedra x Pedra')
        print('Empate.')
    elif jogador1 == 1 and jogador2 == 2:
        print('Pedra x Papel')
        print('Você ganhou.')
    elif jogador1 == 1 and jogador2 == 3:
        print('Pedra x Tesoura')
        print('Você Perdeu.')
    #Jogador 1 = Papel x Jogadas do Computador
    if jogador1 == 2 and jogador2 == 1:
        print('Papel x Pedra')
        print('Você ganhou.')
    elif jogador1 == 2 and jogador2 == 2:
        print('Papel x Papel')
        print('Empate.')
    elif jogador1 == 2 and jogador2 == 3:
        print('Papel x Tesoura')
        print('Você Perdeu.')
    #Jogador 1 = Tesoura x Jogadas do Computador
    if jogador1 == 3 and jogador2 == 1:
        print('Tesoura x Pedra')
        print('Você Perdeu.')
    elif jogador1 == 3 and jogador2 == 2:
        print('Tesoura x Papel')
        print('Você ganhou.')
    elif jogador1 == 3 and jogador2 == 3:
        print('Tesoura x Tesoura')
        print('Empate.')

#Grito de guerra (rsrs)
def inicio():
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PÔ')
    sleep(0.5)
    linha()
 
#Inicio do Jogo
while True:
    limparTela()
    menu()
    opcoes_disponiveis = [1, 2, 3]
    jogada_usuario = escolha()
    jogada_maquina = choice(opcoes_disponiveis)
    
    inicio()
    partida(jogada_usuario, jogada_maquina)
    
    opcoes_jogar_novamente = ['S', 'N']
    jogar_novamente = input('Quer jogar novamente? [S/N]: ').upper()
    
    while jogar_novamente not in opcoes_jogar_novamente:
        jogar_novamente = input('Comando inválido, digite uma opção válida. [S/N]: ').upper()
    if jogar_novamente == 'N':
        linha()
        print('Encerrando...')
        sleep(2)
        break
    else:
        pass
        linha()

