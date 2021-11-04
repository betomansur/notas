AV1 = 4.15
AV2 = 3.8
AV3 = 0
AV4 = 0
EF = 0
APS = 0

mediak = (AV1+AV2+AV3)/3

mp = AV1*0.15 + AV2*0.30 + AV3*0.25 + AV4*0.30
mi = mp*0.6 + 0.4*EF
m = 0.9*mi + 0.1*APS


if mp >= 6.5:
    print("Minha nota de MATVAR é :{0}".format(mp))
    print("Dispensado da PF")
else:
    if mi >= 5:
        print("Minha nota de MATVAR é :{0}".format(m))
        print('APROVADO')
    else:
        print("Minha nota de MATVAR é :{0}".format(mi))
        print('REPROVADO')
