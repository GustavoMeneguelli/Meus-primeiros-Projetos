#Simulador de jogo de Dados usando Classes e Metódos
from random import randint
from time import sleep
import os


def LimparTela():
    os.system('cls')


def linha():
    print('=' * 40)


linha()
print(f"{'JOGO DE DADOS':^40}")

 
#Inicio da Classe 
class JogarDado:
    def __init__(self):
        self.numero_minimo = 1
        self.numero_maximo = 6
        self.mensagem = 'Quer jogar novamente? [S/N]: '
        self.vitorias_jogador = 0
        self.vitorias_maquina = 0
        self.partidas_empatadas = 0
        
        
    #Função para iniciar o Jogo   
    def Iniciar(self):
        self.jogada_usuario = randint(self.numero_minimo, self.numero_maximo)
        self.jogada_maquina = randint(self.numero_minimo, self.numero_maximo)
        linha()
        print('Iniciando o jogo...')
        linha()
        sleep(1)
        print(f'Você tirou... {self.jogada_usuario}')
        sleep(1)
        print(f'A maquina tirou... {self.jogada_maquina}')
        linha()
    
    
    #Função para Mostrar o Resultado da Partida
    def Resultado(self):
       if self.jogada_usuario > self.jogada_maquina:
           print('Parabéns, você venceu.')
           linha()
           self.vitorias_jogador += 1
       elif self.jogada_usuario == self.jogada_maquina:
           print('Partida empatada.')
           linha()
           self.partidas_empatadas += 1
       else:
           print('Você perdeu.')
           linha()
           self.vitorias_maquina += 1
    
    #Mostrar o Placar Final
    def Placar(self):
        print(f'{"Estatística das Partidas":^20}')
        linha()
        print(f'Quantidade de Vitórias: {self.vitorias_jogador}')
        print(f'Quantidade de Derrotas: {self.vitorias_maquina}')
        print(f'Partidas Empatadas: {self.partidas_empatadas}')
        linha()


    #Perguntar se o usuario quer jogar novamente.    
    def JogarNovamente(self):
        while True:
            resposta = input(self.mensagem).upper().strip()
            if resposta not in ['S', 'N']:
                print('Opção inválida, digite [S ou N]: ')
                linha()
            elif resposta == 'S':
                LimparTela()
                break
            else:
                linha()
                print('Encerrando o programa, obrigado por jogar. Até mais ;)')
                sleep(2)
                LimparTela()
                self.Placar()
                exit()


#Inicio do Jogo        
simulador = JogarDado()
while True:
    simulador.Iniciar()
    simulador.Resultado()
    simulador.JogarNovamente()

    
    
