from random import randint 
import random

#zona, seção e eleitores
zona_eleito = [372, 2, 374, 376, 375, 381, 253, 352, 371, 418]
zona_urna = random.choice(zona_eleito)

secao_eleito = randint(0, 600)

total_eleitores = 2064850

eleitore_votos = randint(200000, 2064850)

urna_cod = randint(0,100)

eleitor1 = randint(1, 7)
eleitor2 = randint(1, 7)

if (eleitor1 > 4):
    eleitor1 = ['B','N']
    elemento = random.choice(eleitor1)
else:
    elemento = ''

if (eleitor2 > 4):
    eleitor2 = ['B','N']
    elemento2 = random.choice(eleitor2)
else:
    eleitor2 = ''

print(eleitor1,elemento)