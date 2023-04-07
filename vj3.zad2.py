
def funkcija(N):
    suma=0
    broj=5
    for i in range(N):
        suma+=suma+(1/3)
    print(suma)

    for i in range(N):
            broj=broj-(1/3)
    print(broj)
funkcija(200)
funkcija(2000)