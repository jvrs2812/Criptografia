from tqdm import tqdm
from time import sleep
from decimal import Decimal
from math import trunc

print ('='*85,'Codificando um texto','='*85)

#Pegando o texto contando os caracteres e tirando os espaços
n = 0
mult = 2
senha = str(input('Insira Seu Texto para  = '))
codigo = int(input('Insira o codigo para codificação = '))
codigo = codigo**codigo
senhalen = len(senha)
matrizA = []
matrizB = []
matrizResultante = []
matrizfinal = []
matrizfinalvdd = []
matrizTrocar = []
print ('='*85,'Inciando a Codificação','='*85)

#criando o progress bar
for i in tqdm(range(20)):
  sleep(0.05)
  pass

#criando as matrizes
while n<senhalen:
  if senha[n] == 'a':
    matrizResultante.append(1*codigo)
    pass
  if senha[n] == 'b':
    matrizResultante.append(2*codigo)
    pass
  if senha[n] == 'c':
    matrizResultante.append(3*codigo)
  if senha[n] == 'd':
    matrizResultante.append(4*codigo)
    pass
  if senha[n] == 'e':
    matrizResultante.append(5*codigo)
    pass
  if senha[n] == 'f':
    matrizResultante.append(6*codigo)
  if senha[n] == 'g':
    matrizResultante.append(7*codigo)
    pass
  if senha[n] == 'h':
    matrizResultante.append(8*codigo)
    pass
  if senha[n] == 'i':
    matrizResultante.append(9*codigo)
  if senha[n] == 'j':
    matrizResultante.append(10*codigo)
    pass
  if senha[n] == 'k':
    matrizResultante.append(11*codigo)
    pass
  if senha[n] == 'l':
    matrizResultante.append(12*codigo)
  if senha[n] == 'm':
    matrizResultante.append(13*codigo)
    pass
  if senha[n] == 'n':
    matrizResultante.append(14*codigo)
    pass
  if senha[n] == 'o':
    matrizResultante.append(15*codigo)
  if senha[n] == 'p':
    matrizResultante.append(16*codigo)
    pass
  if senha[n] == 'q':
    matrizResultante.append(17*codigo)
    pass
  if senha[n] == 'r':
    matrizResultante.append(18*codigo)
  if senha[n] == 's':
    matrizResultante.append(19*codigo)
    pass
  if senha[n] == 't':
    matrizResultante.append(20*codigo)
    pass
  if senha[n] == 'u':
    matrizResultante.append(21*codigo)
  if senha[n] == 'v':
    matrizResultante.append(22*codigo)
    pass
  if senha[n] == 'w':
    matrizResultante.append(23*codigo)
    pass
  if senha[n] == 'x':
    matrizResultante.append(24*codigo)
  if senha[n] == 'y':
    matrizResultante.append(25*codigo)
    pass
  if senha[n] == 'z':
    matrizResultante.append(26*codigo)
    pass
  if senha[n] == ' ':
    matrizResultante.append(27*codigo)
  n=n+1

#Verifica se a quantidade de numeros é impar
# Trocando a matriz de numeros para letras
##while n<len(matrizResultante):
##  matrizfinal.append(matrizResultante[n]**99)
##  n = n + 1

#trocando para letras
n = 0
while n<len(matrizResultante):
  if matrizResultante[n] == 1*codigo:
    matrizTrocar.append('a')
  if matrizResultante[n] == 2*codigo:
    matrizTrocar.append('b')
  if matrizResultante[n] == 3*codigo:
    matrizTrocar.append('c')
  if matrizResultante[n] == 4*codigo:
    matrizTrocar.append('d')
  if matrizResultante[n] == 5*codigo:
    matrizTrocar.append('e')
  if matrizResultante[n] == 6*codigo:
    matrizTrocar.append('f')
  if matrizResultante[n] == 7*codigo:
    matrizTrocar.append('g')
  if matrizResultante[n] == 8*codigo:
    matrizTrocar.append('h')
  if matrizResultante[n] == 9*codigo:
    matrizTrocar.append('i')
  if matrizResultante[n] == 10*codigo:
    matrizTrocar.append('j')
  if matrizResultante[n] == 11*codigo:
    matrizTrocar.append('k')
  if matrizResultante[n] == 12*codigo:
    matrizTrocar.append('l')
  if matrizResultante[n] == 13*codigo:
    matrizTrocar.append('m')
  if matrizResultante[n] == 14*codigo:
    matrizTrocar.append('n')
  if matrizResultante[n] == 15*codigo:
    matrizTrocar.append('o')
  if matrizResultante[n] == 16*codigo:
    matrizTrocar.append('p')
  if matrizResultante[n] == 17*codigo:
    matrizTrocar.append('q')
  if matrizResultante[n] == 18*codigo:
    matrizTrocar.append('r')
  if matrizResultante[n] == 19*codigo:
    matrizTrocar.append('s')
  if matrizResultante[n] == 20*codigo:
    matrizTrocar.append('t')
  if matrizResultante[n] == 21*codigo:
    matrizTrocar.append('u')
  if matrizResultante[n] == 22*codigo:
    matrizTrocar.append('v')
  if matrizResultante[n] == 23*codigo:
    matrizTrocar.append('w')
  if matrizResultante[n] == 24*codigo:
    matrizTrocar.append('x')
  if matrizResultante[n] == 25*codigo:
    matrizTrocar.append('y')
  if matrizResultante[n] == 26*codigo:
    matrizTrocar.append('z')
  if matrizResultante[n] == 27*codigo:
    matrizTrocar.append(' ')
  n = n+1

n = 0
# joga o valor descodificado para uma string
while n<1:
  finalCod= matrizTrocar[0]
  n+=1
  while n<len(matrizTrocar):
    finalCod += matrizTrocar[n]
    if n != len(matrizTrocar):
      n+=1
      exit
    else:
      exit
  exit
n = 0
# joga o valor codificado para uma string
sim = str(input('Deseja ver se codigo codificado [S/N] = '))

print('='*85,'Criando sua codificação','='*85)
#criando o progress bar
for i in tqdm(range(20)):
  sleep(0.05)
  pass
if sim.upper() == 'S': 
  while n<1:
    inicioCod= matrizResultante[0]
    n+=1
    while n<len(matrizResultante):
      inicioCod += matrizResultante[n]
      if n != len(matrizResultante):
        n+=1
        exit
      else:
        exit
    exit 
  print('Seu codigo codificado = ',inicioCod) 
