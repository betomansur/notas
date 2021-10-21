import statistics as st
AV1 = 2.5
AV2 = 4.55
AV3 = 0
AV4 = 0
EX1 = 7.5
EX2 = 7.5
EX3 = 0
EX4 = 0
PROJ1 = 0
PROJ2 = 0


media_p = AV1+AV2+AV3+AV4
media_p = media_p/4

media_ex = EX1+EX2+EX3+EX4
media_ex = media_ex/4

coef = media_ex*0.05 + media_p*0.95


media = PROJ1*0.25+PROJ2*0.25 +  media_p*0.45 + media_ex*0.05


print("Minha nota de ACIONAS é :{0}".format(media))
if media >= 5:
    print('APROVADO')
else:
    print('REPROVADO')

print('Critérios de aprovação:')
proj = PROJ1 + PROJ2
proj = proj/2

if proj< 5:
    print("Media de projetos: NÃO")
else:
    print("Media de projetos: SIM")

if coef< 5:
    print("Coeficiente de aprovação: NÃO")
else:
    print("Coeficiente de aprovação: SIM")
