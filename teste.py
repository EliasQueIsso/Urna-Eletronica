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
            print("voto inválaido")
            pass
    except:
        print("Digite uma opção válida, tente novamente")
    
    #apresente os candidatos
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