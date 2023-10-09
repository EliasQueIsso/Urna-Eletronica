from random import randint 
import random
import os

#Constantes prefeitos
voto_c1 = 0
voto_c2 = 0
voto_c3 = 0
voto_c4 = 0

#Constantes Vereadores
voto_v1 = 0
voto_v2 = 0
voto_v3 = 0
voto_v4 = 0

#Constante Branco e Nulo
voto_nulo = 0
voto_branco = 0
voto_Vnulo = 0
voto_Vbranco = 0

#zona, seção e eleitores
zona_eleito = [372, 2, 374, 376, 375, 381, 253, 352, 371, 418]
zona_urna = random.choice(zona_eleito)
secao_eleito = randint(0, 600)

#total de eleitores e eleitores por urna
total_eleitores = 2064850
total_por_zona = [282827, 255425, 255589, 247771, 242409, 224044, 209356, 200996, 198069, 196435]
total_urna = random.choice(total_por_zona)

#eleitores que foram votar
eleitore_votos = randint(200000, 2064850)

#código da urna
urna_cod = randint(0,100)

#eleitores
eleitor1 = randint(1, 7)
eleitor2 = randint(1, 7)
eleitorN = randint(1, 7)

if (eleitor1 > 4):
    eleitor1 = ['B','N']
    elemento = random.choice(eleitor1)
else:
    elemento = ''

if (eleitor2 > 4):
    eleitor2 = ['B','N']
    elemento2 = random.choice(eleitor2)
else:
    elemento2 = ''

if (eleitorN > 4):
    eleitorN = ['B','N']
    elementoN = random.choice(eleitorN)
else:
    elementoN = ''
#cabeçalho
print("/" + "*"*20 + "/")
print("/* Aluno: Elias de Souza Mendonça */")
print("/* TURMA: CC2A13 */")
print("/* Professora: Eliane */")
print("/" + "*"*20 + "/")

print("IDENTIFICAÇÃO DA URNA ELETRÔNICA\nIdentificação da Seção e Zona Eleitoral: " + str(zona_urna) + "\nTotal dos Eleitores: " + str(total_urna) + "\nCódigo de identificação da urna: " + str(urna_cod))

'''
print("VOTAÇÃO INDIVIDUAL\nEleitor 1\nVoto ao Candidato à Prefeitura: " + str(eleitor1) + elemento +"\nVoto ao Candidato à Vereador: " + str(eleitor1) + elemento + "\nEleitor 2\nVoto ao Candidato à Prefeitura: " + str(eleitor2) + elemento2 +"\nVoto ao Candidato à Vereador: " + str(eleitor2) + elemento2 + "\nEleitor N\nVoto ao Candidato à Prefeitura: " + str(eleitorN) + elementoN +"\nVoto ao Candidato à Vereador: " + str(eleitorN) + elementoN)
'''

while True:
#apresente os candidatos
    print("*"*20)
    print('PREFEITOS')
    print(f'TOTAL CANDIDATO 1: {voto_c1}{os.linesep}TOTAL CANDIDATO 2: {voto_c2}')
    print(f'TOTAL CANDIDATO 3: {voto_c3}{os.linesep}TOTAL CANDIDATO 4: {voto_c4}')
    print(f'TOTAL ANULADO: {voto_nulo}{os.linesep}TOTAL BRANCO: {voto_branco}')
    print("*"*20)
    print('VEREADORES')
    print(f'TOTAL CANDIDATO 1: {voto_v1}{os.linesep}TOTAL CANDIDATO 2: {voto_v2}')
    print(f'TOTAL CANDIDATO 3: {voto_v3}{os.linesep}TOTAL CANDIDATO 4: {voto_v4}')
    print(f'TOTAL ANULADO: {voto_Vnulo}{os.linesep}TOTAL BRANCO: {voto_Vbranco}')
    print("*"*20)
#permita votar
    try:
        voto=str(input(f'Escolha seu voto a Prefeito:{os.linesep} 1 - Candidato 1{os.linesep} 2 - Candidato 2{os.linesep} 3 - Candidato 3{os.linesep} 4 - Candidato 4{os.linesep} B - voto em Branco{os.linesep} N - voto Nulo{os.linesep}Seu voto:'))
        if voto == '1':
            voto_c1 += 1
        elif voto == '2':
            voto_c2 += 1
        elif voto == '3':
            voto_c3 += 1
        elif voto == '4':
            voto_c4 += 1 
        elif voto == 'B':
            voto_branco += 1
        elif voto == 'N':
            voto_nulo += 1
        else:
            print("Voto inválaido")
            pass
    except:
        print("Digite uma opção válida, tente novamente")
    
    try:
        voto=str(input(f'Escolha seu voto a Vereador:{os.linesep} 1 - Candidato 1{os.linesep} 2 - Candidato 2{os.linesep} 3 - Candidato 3{os.linesep} 4 - Candidato 4{os.linesep} B - voto em Branco{os.linesep} N - voto Nulo{os.linesep}Seu voto:'))
        if voto == '1':
            voto_v1 += 1
        elif voto == '2':
            voto_v2 += 1
        elif voto == '3':
            voto_v3 += 1 
        elif voto== '4':
            voto_v4 += 1
        elif voto == 'B':
            voto_Vbranco += 1
        elif voto == 'N':
            voto_Vnulo += 1
        else:
            print("voto inválaido")
            pass
    except:
        print("Digite uma opção válida, tente novamente")

