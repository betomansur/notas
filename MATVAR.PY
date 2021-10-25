AV1 = 4.15
AV2 = 3.8
AV3 = 0
AV4 = 0
APS = 0 

mediak = (AV1+AV2+AV3)/3

media = AV1*0.15 + AV2*0.30 + AV3*0.25 + AV4*0.30
media2 = media*0.9 + APS*0.1


if mediak >= 6.5:
    print("Minha nota de MATVAR é :{0}".format(media))
    print("Dispensado da PF")
else:
    if media2 >= 5:
        print("Minha nota de MATVAR é :{0}".format(media2))
        print('APROVADO')
    else:
        print("Minha nota de MATVAR é :{0}".format(media2))
        print('REPROVADO')
