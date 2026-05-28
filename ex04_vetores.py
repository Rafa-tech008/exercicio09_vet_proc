#OP.VET_LT02.4
#Declaração de variáveis

#Início

import random
def func_media (vetor):
    soma= 0
    med: float = 0
    for i in vetor:
        soma += i
    med= (soma / len (vetor))
    print (f"A média das notas do grupo, equivale a: {med: .2f}")


def func_calcm (vetor, media):
    for i in range (len(vetor)):
        if (vetor [i] >= media):
            print (f"O aluno {i+1} atingiu a média: {vetor [i]}")
        else:
            print (f"O aluno {i+1} não atingiu a média: {vetor [i]}")


def main ():
    vet = []
    media = 6.0
    tamanho = 30   
    num: int = 0

    for i in range (tamanho):
        num = (random.randint (0, 10))
        vet.append (num)
    
    

    func_calcm (vet, media)

    func_media (vet)


if (__name__ == "__main__"):
    main ()
