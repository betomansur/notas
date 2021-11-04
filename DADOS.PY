I=0
D=2.5
C=5
Cp=6
B=7
Bp=8
A=9
Ap=10


AV1 = 8.5
AV2 = 4
AV3 = 0
AV4 = 0
PROJ1 = D
PROJ2 = B
aps1 = 10
aps2 = 10
aps3 = 7.5
aps4 = 10
aps5 = 10
aps6 = 10
aps7 = 0
aps8 = 0
aps9 = 0

lista_aps = [aps1,aps2,aps3,aps4,aps5,aps6,aps7,aps8,aps9]

for aps in lista_aps:
    if aps< 8:
        lista_aps.remove(aps)
for aps in lista_aps:
    if aps< 8:
        lista_aps.remove(aps)
soma = 0
for aps in lista_aps:
    soma += aps
media_aps = soma/len(lista_aps)

NA = AV1*0.15+AV2*0.25+AV3*0.20+AV4*0.40

NP = media_aps*0.1 + PROJ1*0.45+PROJ2*0.45

if NP < 5:
    print("INSTA DP")

if NA < 5:
    print("INSTA DP")

NOTA = (NP+NA)/2

print("Minha nota de DADOS é :{0}".format(NOTA))
if NOTA >= 5:
    print('APROVADO')
else:
    print('REPROVADO')

