import matplotlib.pyplot as plt
import numpy as np
import random as rad
import math

v=[]

def LogarithmFunction():
    lim=int(input('Introduceti limita inferioara a intervalului pe care doriti sa studiati functia: '))
    Lim=int(input('Introduceti limita superioara a intervalului pe care doriti studiati functia: '))
    answer=input('Introduceti baza logaritmului(in cazul in care veti lasa campul gol, logaritmul va fi calculat in baza e): ')
    if int(answer) < 0:
        print('Baza unui logaritm nu poate fi un numar negativ!')
    else:
        if len(answer) == 0:
            for i in range(lim,Lim+1):
                v.append(math.log(i))
        else:
            for i in range(lim,Lim+1):
                v.append(math.log(int(answer), i))

def ExponentialFunction():
    lim = int(input('Introduceti limita inferioara a intervalului pe care doriti sa studiati functia: '))
    Lim = int(input('Introduceti limita superioara a intervalului pe care doriti studiati functia: '))
    baza=input('Introduceti baza functiei exponentiale(in cazul in care nu veti mentiona, functia va fi calculata cu baza e): ')
    if len(baza) == 0:
        for i in range(lim,Lim+1):
            v.append(math.exp(i))
    else:
        for i in range(lim,Lim+1):
            v.append(int(baza)**i)

def HyperbolicSineFunction():
    lim = int(input('Introduceti limita inferioara a intervalului pe care doriti sa studiati functia: '))
    Lim = int(input('Introduceti limita superioara a intervalului pe care doriti studiati functia: '))
    for i in range(lim,Lim+1):
        v.append(math.sinh(i))

def HyperbolicCosineFunction():
    lim = int(input('Introduceti limita inferioara a intervalului pe care doriti sa studiati functia: '))
    Lim = int(input('Introduceti limita superioara a intervalului pe care doriti studiati functia: '))
    for i in range(lim,Lim+1):
        v.append(math.cosh(i))

def HyperbolicTangentFunction():
    lim = int(input('Introduceti limita inferioara a intervalului pe care doriti sa studiati functia: '))
    Lim = int(input('Introduceti limita superioara a intervalului pe care doriti studiati functia: '))
    for i in range(lim,Lim+1):
        v.append(math.tanh(i))

def AreaHyperbolicSineFunction():
    lim = int(input('Introduceti limita inferioara a intervalului pe care doriti sa studiati functia: '))
    Lim = int(input('Introduceti limita superioara a intervalului pe care doriti studiati functia: '))
    for i in range(lim,Lim+1):
        v.append(math.asinh(i))

def AreaHyperbolicCosineFunction():
    lim = int(input('Introduceti limita inferioara a intervalului pe care doriti sa studiati functia: '))
    Lim = int(input('Introduceti limita superioara a intervalului pe care doriti studiati functia: '))
    for i in range(lim,Lim+1):
        v.append(math.acosh(i))

def PowerFunction():
    lim = int(input('Introduceti limita inferioara a intervalului pe care doriti sa studiati functia: '))
    Lim = int(input('Introduceti limita superioara a intervalului pe care doriti studiati functia: '))
    power=input('Introduceti puterea parametrului functiei(in cazul in care nu veti introduce niciun numar, functia se va calcula la puterea 1 si va rezulta o functie de gradul 1): ')
    if len(power)==0:
        for i in range(lim,Lim+1):
            v.append(i)
    else:
        for i in range(lim,Lim+1):
            v.append(pow(i,int(power)))

def SineFunction():
    lim = int(input('Introduceti limita inferioara a intervalului pe care doriti sa studiati functia: '))
    Lim = int(input('Introduceti limita superioara a intervalului pe care doriti studiati functia: '))
    for i in range(lim,Lim+1):
        v.append(math.sin(i))

def CosineFunction():
    lim = int(input('Introduceti limita inferioara a intervalului pe care doriti sa studiati functia: '))
    Lim = int(input('Introduceti limita superioara a intervalului pe care doriti studiati functia: '))
    for i in range(lim,Lim+1):
        v.append(math.cos(i))

def TangentFunction():
    lim = int(input('Introduceti limita inferioara a intervalului pe care doriti sa studiati functia: '))
    Lim = int(input('Introduceti limita superioara a intervalului pe care doriti studiati functia: '))
    for i in range(lim,Lim+1):
        v.append(math.tan(i))

def CotangentFunction():
    lim = int(input('Introduceti limita inferioara a intervalului pe care doriti sa studiati functia: '))
    Lim = int(input('Introduceti limita superioara a intervalului pe care doriti studiati functia: '))
    for i in range(lim,Lim+1):
        v.append(1/math.tan(i))

def SquareRootFunction():
    lim = int(input('Introduceti limita inferioara a intervalului pe care doriti sa studiati functia: '))
    Lim = int(input('Introduceti limita superioara a intervalului pe care doriti studiati functia: '))
    for i in range(lim,Lim+1):
        v.append(math.sqrt(i))

def SawtoothWaveFunction():
    for i in range(0, int(2*math.pi+1)):
        if i>=0 and i<math.pi:
            v.append(i)
        elif i>=math.pi and i<=2*math.pi:
            v.append(i-2*math.pi)

def SquareWaveFunction():
    lim = int(input('Introduceti limita inferioara a intervalului pe care doriti sa studiati functia: '))
    Lim = int(input('Introduceti limita superioara a intervalului pe care doriti studiati functia: '))
    for i in range(lim,Lim+1):
        v.append(4*math.floor(i)-2*math.floor(2*i)+1)

def SigmaFunction():
    number=int(input('Introduceti numarul pentru calcularea functiei: '))
    power=int(input('Introduceti puterea la care doriti sa fie calculati divizorii: '))
    for i in range(1,number+1):
        if number%i==0:
            v.append(i**power)

SigmaFunction()
plt.plot(v)
plt.show()