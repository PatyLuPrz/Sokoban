import Movimientos as F
import Sokoban as M
Var=0
f=1
c=1
x=0
y=0

if Mapa[5][3]=="5":
    Var=2
elif Mapa[5][1]=="5":
    Var=1
elif Mapa[3][2]=="5":
    Var=3

if Var==1:
    Nivel='Nivel01.ap'
elif Var==2:
    Nivel='Nivel02.ap'
elif Var==3:
    Nivel='Nivel03.ap'
    
file=open(Nivel,'r')
Mapa=[]
for row in file.readlines():
    linea=[]
    for c in row:
        linea.append(c)
    linea.pop()
    Mapa.append(linea)

M.Movimientos(x,y,f,c,Mapa)

