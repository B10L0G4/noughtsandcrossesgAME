import os # limpar tela 
import random # numeros aleatorios  
from colorama import Fore, Back , Style  # para cores e estilos de fonte 

JogarNovamente= "s"
jogadas = 0
quemJoga = 2 #1 = CPU e 2 = Jogador 
maxJogadas = 9
vit = "n" #(or False)
velha = [
    [" "," "," "], 
    [" "," "," "],
    [" "," "," "]
]
def tela(): # para contruir e limpar a tela  
    global velha 
    global jogadas 
    os.system("cls")
    print("    0   1   2")
    print("")
    print("0:  "+ velha [0][0] + " | " + velha [0][1] + " | " + velha [0][2])
    print("    -----------")
    print("1:  "+ velha [1][0] + " | " + velha [1][1] + " | " + velha [1][2])
    print("    -----------")
    print("2:  "+ velha [2][0] + " | " + velha [2][1] + " | " + velha [2][2])
    print("Jogadas: " + Fore.GREEN + str(jogadas) + Fore.RESET) #antes estava 

def JogadorJoga():
    global jogadas
    global quemJoga
    global vit
    global maxJogadas
    
    if  quemJoga == 2 and jogadas < maxJogadas:
        l = int(input("Linha..."))
        c = int(input("Coluna..."))
        try:
            while velha[l][c] != " ":
                l = int(input("Linha..."))
                c = int(input("Coluna..."))
            velha[l][c]="X"
            quemJoga = 1 #mudança teste 
            jogadas += 1
        except:
            print("linha e/ou coluna inválida ")

def cpuJoga():
    global jogadas
    global quemJoga
    global vit
    global maxJogadas
    
    if  quemJoga == 1 and jogadas < maxJogadas:
        l = random.randrange(0,3)
        c = random.randrange(0,3)
        while velha[l][c] != " ":
            l = random.randrange(0,3)
            c = random.randrange(0,3)
        velha[l][c]="O"
        jogadas += 1
        quemJoga = 2

def verificarVitoria():
    global velha 
    vitoria = "n"
    simbolos = ["X","O"]
    for s in simbolos:
        vitoria="n"
        #verificar vitoria em linha 
        il = ic = 0 #inicialização e leitura de matrizes (percorrendo matrizes)
        while il<3:
            soma = 0
            ic = 0
            while ic <3:
                if(velha[il][ic]==s):
                    soma+=1
                ic+=1
            if(soma==3):
                vitoria=s
                break    
            il+=1
        if(vitoria!="n"):
            break
        # Verificação de Colunas 
        il = ic = 0 
        while ic<3:
            soma = 0
            il = 0
            while il <3:
                if(velha[il][ic]==s):
                    soma+=1
                il+=1
            if(soma==3):
                vitoria=s
                break    
            ic+=1
        if(vitoria!="n"):
            break
        #verifica diagonal 1 
        soma = 0
        idig=0
        while idig<3:
            if (velha[idig][idig]==s):
                soma+=1
            idig+=1
            if(soma==3):
                vitoria=s
                break
        #verificA DIAGONAL 2
        soma = 0
        idigl=0
        idigc=2
        while idigc>=0:
            if(velha[idigl][idigc]==s):
                soma+=1
            idigl+=1
            idigc-=1
            if(soma==3):
                vitoria=s
                break
    return vitoria

def redefinir():
    global jogadas 
    global quemJoga 
    global maxJogadas 
    global vit 
    global velha 
    
    jogadas = 0
    quemJoga = 2 
    maxJogadas = 9
    vit = "n" 
    velha = [
        [" "," "," "], 
        [" "," "," "],
        [" "," "," "]
    ]

while(JogarNovamente=="s"):           
    while True:
        tela()
        JogadorJoga()
        cpuJoga()
        tela()
        vit=verificarVitoria()
        if(vit!="n")or(jogadas>=maxJogadas):
            print(Fore.RED + "Fim de Jogo" + Fore.YELLOW)
            break
    if (vit=="X" or vit=="O"):
        print("Resultado: Jogador " + vit + " venceu!")
    else:
        print("resultado: Empate")
    JogarNovamente=input(Fore.BLUE + "Jogar Novamente? [s/n]:" + Fore.RESET)
    redefinir() 
    
    

    
    
    
 
 
