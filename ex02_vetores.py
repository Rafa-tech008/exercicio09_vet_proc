#OP.VET_LT02.2
#Declaração de variáveis

#Início

import random

def func_media (vetor):
    acum = 0
    med: float = 0.0
    for i in vetor:
        acum += i
    med = (acum / len(vetor))
    print (f"A média do vetor equivale a: {med: .2f}")


def func_tamanho (vetor):
    maior: int = 0
    menor: int = 0
    for i in vetor:
        if (maior < i):
            maior = i
        if (menor > i):
            menor = i
    print ("O maior número do vetor é igual a", maior)    
    print ("O menor número do vetor é igual a", menor)


def main ():
    vet = []
    numero: int = 0

    for i in range (100):
        numero = random.randint (0,150)
        vet.append (numero)

    func_tamanho (vet)

    func_media (vet)

if (__name__ == "__main__"):
    main ()
