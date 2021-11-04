aps1 = 7.5
aps2 = 2
aps3 = 4.4
aps4 = 0
aps5 = 0
quiz1 = 2.2
quiz2 = 0
PI = 3.5
PF = 0

lista_aps = [aps1,aps2,aps3,aps4,aps5]

while len(lista_aps) != 3:
    lista_aps.remove(min(lista_aps))

media_aps = 0
for nota in lista_aps:
    media_aps+= nota
media_aps = media_aps/3

lista_quiz = [quiz1,quiz2]

media_quiz = max(lista_quiz)


NOTA = media_aps*0.2 + media_quiz*0.15 + PI*0.3 + PF*0.35

if aps1 and aps2 and aps3 and aps4 and aps5 != 0:
    NOTA += 0.3
elif aps1 and aps2 and aps3 and aps4 != 0:
    NOTA += 0.1
elif aps1 and aps2 and aps3 and aps5 != 0:
    NOTA += 0.1
elif aps1 and aps2 and aps5 and aps4 != 0:
    NOTA += 0.1
elif aps1 and aps5 and aps3 and aps4 != 0:
    NOTA += 0.1
elif aps5 and aps2 and aps3 and aps4 != 0:
    NOTA += 0.1



print("Minha nota de FISMOV é :{0}".format(NOTA))
if NOTA >= 5:
    print('APROVADO')
else:
    print('REPROVADO')

if (PI + PF)/2 < 5:
    print("DELTA")