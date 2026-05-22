#OP.PROC_2
#Declaração de variáveis

#Início

import platform
import subprocess


def mata_nome ():
    sys = os ()
    nome: str = '' 
    vet_comand = []   
    nome= str (input ("\n Digite o nome do processo: "))

    if (sys == "Linux"):
        comand = f'pkill -f {nome}'
        vet_comand = comand.split (' ')
        subprocess.run (vet_comand)       

    elif (sys == "Windows"):
        comand = f'TASKKILL /IM {nome}'
        vet_comand = comand.split (' ')
        subprocess.run (vet_comand)
    else:
        print ("Sistema não identificado")


def mata_pid ():
    sys = os ()
    pid: int = 0 
    vet_comand = []   
    pid= int (input ("\n Digite o PID do processo: "))

    if (sys == "Linux"):
        comand = f'kill -9 {pid}'
        vet_comand = comand.split (' ')
        subprocess.run (vet_comand)       

    elif (sys == "Windows"):
        comand = f'TASKKILL /PID {pid}'
        vet_comand = comand.split (' ')
        subprocess.run (vet_comand)

    else:
        print ("Sistema não identificado")


def proc_filhos (): 
    vet_proc = []
    sys = platform.system ()

    if (sys == "Linux"):
        proc = 'ps -ef'
        vet_proc = proc.split (' ')
        saida = subprocess.Popen (vet_proc,stdout = subprocess.PIPE)
        linha = saida.stdout.readline().decode ('utf-8', errors = 'ignore')
        while (linha != ''):
            print (linha)
            linha = saida.stdout.readline().decode ('utf-8', errors = 'ignore')

    elif (sys == 'Windows'):
        proc = 'TASKLIST /FO TABLE'
        vet_proc = proc.split (' ')
        saida = subprocess.Popen (vet_proc,stdout = subprocess.PIPE)
        linha = saida.stdout.readline().decode ('cp850', errors = 'ignore')
        while (linha != ''):
            print (linha)
            linha = saida.stdout.readline().decode ('cp850', errors = 'ignore')


def os ():
    sys = platform.system ()
    if (sys == "Linux"):
        print ("O sistema operacional é o Linux")
    elif (sys == "Windows"):
        print ("O sistema operacional é o Windows")
    else:
        print ("O sistema operacional não foi identificado")

    return sys


def main ():
    contador = 0
    menu: int = 0
    processo: str = ''

    while contador < 10000:
        print ("1- Processos, 2- Mata por pid, 3- Mata por nome, 9- Sair do loop")
        menu = int(input ("\n Digite a opção desejada: "))
        contador += 1
        if (menu == 1):
            sys = os ()
            proc_filhos ()
        elif (menu == 2):
            mata_pid ()
        elif (menu == 3):
            mata_nome()
        elif (menu == 9):
            break


if (__name__ == "__main__"):
    main ()