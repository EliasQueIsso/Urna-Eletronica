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

controle = 3

#roda eternamente
while True:
#apresente os candidatos
    print("*"*20)
    print(f'TOTAL CANDIDATO 1: {voto_c1}{os.linesep}TOTAL CANDIDATO 2: {voto_c2}')
    print(f'TOTAL CANDIDATO 3: {voto_c3}{os.linesep}TOTAL CANDIDATO 4: {voto_c4}')
    print(f'TOTAL ANULADO: {voto_nulo}{os.linesep}TOTAL BRANCO: {voto_branco}')
    print("*"*20)
#votar prefeito ou vereador
    votar = 1
#permita votar
    def votarPrefeito():
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
        

    def votarVereador():
        try:
            Voto=str(input(f'Escolha seu voto a Vereador:{os.linesep} 1 - Candidato 1{os.linesep} 2 - Candidato 2{os.linesep} 3 - Candidato 3{os.linesep} 4 - Candidato 4{os.linesep} B - Voto em Branco{os.linesep} N - Voto Nulo{os.linesep}Seu voto:'))
            if Voto == '1':
                voto_v1 += 1
            elif Voto == '2':
                voto_v2 += 1
            elif Voto == '3':
                voto_v3 += 1 
            elif Voto== '4':
                voto_v4 += 1
            elif Voto == 'B':
                voto_branco += 1
            elif Voto == 'N':
                voto_nulo += 1
            else:
                print("Voto inválaido")
                pass
        except:
            print("Digite uma opção válida, tente novamente")            
#loop
