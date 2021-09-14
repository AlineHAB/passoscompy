#ALINE HENRIQUE ALVES BARROS - 476684 - Ciência da computação
import turtle
from math import sqrt
from math import atan
from math import degrees


print("****************")
print("VAMOS DESENHAR")
print("****************")
    
    
#DESENHO  1 - (RÊTANGULO)
def Retangulo(caneta, lar, alt):            #DADOS DO 1 OBJETO  - RETANGULO
    #ENTRADAS
    lar = int(input('Digite a largura das linhas: '))   
    alt = int(input('Digite a altura: '))

    for i in range(2):                      #LAÇO PARA INICIO DE DESENHO
        caneta.down()
        caneta.begin_fill()
        caneta.forward(lar)
        caneta.left(90)
        caneta.forward(alt)
        caneta.left(90)
        caneta.end_fill()
        caneta.penup()
    return (lar, alt)                       #RETORNO  E FIM DE DESENHO 1

#DESENHO 2 - (POLIGONOREG)
def Poligonoreg(caneta,lado,nLados):        #DADOS DO 2 OBJETO - POLIGONOREG
    #ENTRADAS
    lado = int(input("lado: "))
    nLados = int(input("N passos: "))

    caneta.begin_fill()                
    for i in range(nLados):                 #LAÇO PARA INICIO DE DESENHO
        caneta.down()
        caneta.forward(lado)
        caneta.left(360/nLados)
    caneta.end_fill()
    caneta.penup()
    return (lado, nLados)                   #RETORNO E FIM DE DESENHO 2


#DESENHO 3 - (CIRCULO)
def circulo(caneta, raio):                  #DADOS DO OBJETO 3 - CIRCULO
    #ENTRADAS
    raio = int(input("Raio do Circulo: "))

    for i in range(1):                      #LAÇO PARA INICIO DE DESENHO
        caneta.goto(-150,150)
        caneta.down()
        caneta.begin_fill()
        caneta.circle(raio)
        caneta.end_fill()
        caneta.penup()
    return (caneta, raio)                   #RETORNO E FIM DESENHO 3


#DESENHO 4 TRIANGULO RETANGULO
#calculando a hipotenusa
def hipotenusa(cateto1, cateto2):           #retornando valores de uma hipotenusa (h²=a²+b²)
    return sqrt(cateto1 ** 2 + cateto2 ** 2) 

#caracteristicas e entrada de usuario para valores
def trianguloReg(caneta, cateto1, cateto2): #DADOS DO OBJETO 4 - TRIANGULO RETANGULO
    #ENTRADA
    cateto1 = int(input("cateto1: "))
    cateto2 = int(input("cateto2: "))

    caneta.goto(150,-150)                   #INCIO DE DESENH0
    caneta.down()
    caneta.begin_fill()
    origem = caneta.position()
    caneta.forward(cateto1)
    caneta.left(90)
    caneta.forward(cateto2)
    caneta.left(180)                    

    angulo = degrees(atan(cateto1 / cateto2))
    caneta.right(angulo)
    h = hipotenusa(cateto1, cateto2)
    caneta.forward(h)
    caneta.end_fill()
    caneta.penup()                          #FIM DE DESENHO

    return (cateto1, cateto2)               #RETORNO E FIM DE DESENHO 4



#FUNÇÃO PARA GUARDAR OS PARAMETROS EM TUPLAS
def mostrarTabela(tabela):
    print("\n")
    print("------TABELA DE PARAMETROS------")
    for reg in tabela: 
        (lar, alt) = reg
        print(f" {lar} | {alt}")
    print("--------------------------------")
    print("\n")


registro = []                               #LISTA PARA GUARDAR PARAMETROS DE DESENHOS


#CARACTERISTICAS DA MINHA JANELA
janela = turtle.Screen()
janela.setup(600,600)
janela.bgcolor("Grey")

#1 retangulo - VARIAVEL REFERENTE 
ret = turtle.Turtle()
ret.pensize(3)
ret.color("Black")
ret.fillcolor("Blue")
ret.penup()

#2 PoligonoREG - VARIAVEL REFERENTE
pol = turtle.Turtle()
pol.pensize(3)
pol.color("Black")
pol.fillcolor("Green")
pol.penup()

#3 circulo - VARIAVEL REFERENTE
cir = turtle.Turtle() 
cir.pensize(3)
cir.color("Black")
cir.fillcolor("Pink")
cir.penup()

#4 trianguloRETANG - VARIAVEL REFERENTE 
tr = turtle.Turtle()
tr.pensize(3)
tr.color("Black")
tr.fillcolor("Orange")
tr.penup()


#MENU INICAL DE OPÇÕES
# 6 - POSSIBILIDADES

while True:
    print('**Menu**')       
    print('[0] Sair')                       #SAIR 
    print('[1] retângulo ')                 # DESENHO 1
    print('[2] poligonoReg')                # DESENHO 2
    print('[3] circulo')                    # DESENHO 3
    print('[4] trianguloRet')               # DESENHO 4
    print('[5] Mostrar')                    # MOSTRAR PARAMETROS
           

    opcao = int(input('Opção: '))           #COMEÇO DE LOOP
    if (opcao == 0):
        break
    elif(opcao == 1): 
        ret.goto(150,150)                   #POSIÇÃO DE OBJETO 1
        registro.append(Retangulo(ret, lar = 0, alt = 0))         #chamando a função de desenho retangulo
                    
    elif(opcao == 2):
        pol.goto(-150,-150)                 #POSIÇÃO DE OBJETO 2
        registro.append(Poligonoreg(pol, lado = 0, nLados = 0 ))

    elif(opcao == 3): 
        
        registro.append(circulo(cir, raio = 0))                     #chamando a função de desenhar o circulo

    elif(opcao == 4):

        registro.append(trianguloReg(tr, cateto1 = 50, cateto2 = 50)) #CHAMANDO A FUNÇÃO DE DESENHO CIRCULO

    elif(opcao == 5):
        mostrarTabela(registro)             #OPÇÃO DE MOSTRAR 

    else:
        print('Opção inexistente')          #fim

janela.exitonclick()