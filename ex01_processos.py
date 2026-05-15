#OP.PROC_01
#Declaração de variáveis

#Início

import platform
import subprocess

def so ():
    system: str = ''
    system = platform.system ()
    if (system == "Linux"):
        print ("O sistema operacional é o linux")

    elif (system == "Windows"):
        print ("O sistema operacional é o Windows")

    else:
        print ("O sistema operacional não foi reconhecido")
    return system

def abre_proc (processo):
    vetor_processo = []
    vetor_processo = processo.split (' ')
    print (vetor_processo)
    subprocess.run (vetor_processo)


def ler_processo (processo, software):
    saida: str = ''
    linha: str = ''
    vetor_processo = []

    linha = ' '
    vetor_processo = processo.split (' ')
    saida = subprocess.Popen (vetor_processo, stdout=subprocess.PIPE)
    linha = saida.stdout.readline().decode('utf-8', errors = 'ignore')

    if (software == "Linux"):
        while (linha != ''):
            if ('avg' in linha):
                partes = linha.split ('=')
                valores = partes [1].split ('/')
                avg = (valores [1].strip())
                print (f"avg = {avg} ms")
            linha = saida.stdout.readline().decode('utf-8', errors = 'ignore')

    elif (software == "Windows"):
        while (linha != ''):
            if ('Média' in linha.strip()):
                partes = linha.split ("Média =")
                media = (partes [1].strip())
                print (f"Média = {media}")
            linha = saida.stdout.readline().decode('cp850', errors = 'ignore')




def main ():
    processo: str = ''
    so_name = so ()
    if (so_name == "Windows"):
        processo = 'ping -4 -n 10 www.google.com.br'
    elif (so_name == "Linux"):
        processo = 'ping -4 -c 10 www.google.com.br'
    
    abre_proc (processo)

    ler_processo (processo, so_name)

if (__name__ == "__main__"):
    main ()

#Fim