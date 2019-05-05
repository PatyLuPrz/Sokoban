import Movimientos as F
file=open('Nivel01.ap','r')
Mapa=[] #lista
for row in file.readlines():  #Lee linea por linea
    linea=[] #lista dentro de la lista
    for c in row:
        linea.append(c) #concatena
    linea.pop() #quita salto de linea
    Mapa.append(linea) #concatena
f=1
c=1
x=0
y=0
bomba=True
#def Movimientos(x,y,f,c,Mapa):
while True:
    for y in Mapa: #Para mostrar la matriz sin corchetes ni comas
        for x in y: 
            print x,
        print
    Mov = raw_input("A donde te quieres mover?\n")
    if Mov == "b":
        while bomba==True:
            for y in Mapa:
                for x in y:
                    print x,
                print
            Mov = (raw_input("movimiento: "))
            if Mov == "d" :
                    Mapa[f][c] = '4'
                    Mapa[f][c+1] = '0'
                    c=c+1
            elif Mov == "a" :
                   Mapa[f][c] = '4'
                   Mapa[f][c-1] = '0'
                   c=c-1
            elif Mov == "w" :
                   Mapa[f][c] = '4'
                   Mapa[f-1][c] = '0'
                   f=f-1
            elif Mov == "s" :
                   Mapa[f][c] = '4'
                   Mapa[f][c+1] = '0'
                   f=f+1
            elif Mov == "b":
                bomba = False
    elif Mov == "d" or Mov=="D":
        print "D"
        F.Der(f,c,Mapa)
        c=c+1
    elif Mov == "a" or Mov=="A":
        print "A"
        F.Izq(f,c,Mapa)
        c=c-1
    elif Mov == "w" or Mov=="W":
        print "W"
        F.Arb(f,c,Mapa)
        f=f-1
    elif Mov == "s" or Mov=="S":
        print "S"
        F.Abj(f,c,Mapa)
        f=f+1
    else:
        print "Opps! Tecla incorrecta"
