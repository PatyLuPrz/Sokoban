print "0 -> Muneco \n 1 -> Caja \n 2 -> Meta \n 3 -> Pared \n 4 -> Camino" #Simbologia

Mapa=[[3,3,3,3,3,3,3],
      [3,4,4,4,4,4,3],
      [3,0,1,2,4,4,3],
      [3,4,4,2,1,4,3],
      [3,4,4,4,4,4,3],
      [3,3,3,3,3,3,3]] #Mapa

x=0
y=0
#Posicion del mono
f=1 #Columnas
c=2 #Filas
#Poicion de la meta
#meta 1
fm=3 #Columnas
cm=2 #Filas
#meta 2
fm1=3 #Columnas
cm1=3 #Filas

B=2
while True:
    for y in Mapa: #Para mostrar la matriz sin corchetes ni comas
        for x in y: 
            print x,
        print
    
    Mov = raw_input("A donde te quieres mover?\n")
    if Mov== "b" or Mov == "B":
        B=B+1
        if B%2==0:
            print "Desactivado"
        else:
            print "Activado"
    elif Mov == "d" or Mov == "D": #Para mover a la derecha
        if Mapa[c][f+1]==3 and B%2==0: #Cuando hay una pared
            print "Opps! Una pared :( El personaje no puede avanzar en esa direccion"
        elif Mapa[c][f+1]==1 and Mapa[c][f+2]==1 and B%2==0: #Cuando hay dos cajas juntas
            print "Opps! No puedes avanzar en esa direccion!"
        elif Mapa[c][f+1]==1 and Mapa[c][f+2]==3 and B%2==0: #Cuando empuja la caja y hay una pared
            print "Opps! No puedes avanzar en esa direccion!"
        elif Mapa[c][f+1]==6 and B%2==0:
            if Mapa[c][f+2]==4:
                    Mapa[c][f]=4 #Coloca un camino
                    f=f+1 #Avanza el mono
                    Mapa[c][f]=0 #Actualiza el mono
                    Mapa[c][f+1]=1
            else:
                print "Opps! Obstaculo"
        
        elif Mapa[c][f+1]==1 and B%2==0: #Para mover la caja
            if Mapa[c][f+2]==Mapa[cm][fm]:
                Mapa[c][f]=4 #Coloca un camino
                f=f+1 #Avanza el mono
                Mapa[c][f]=0 #Actualiza el mono
                Mapa[c][f+1]=6
            elif Mapa[c][f+2]==Mapa[cm1][fm1]:
                Mapa[c][f]=4 #Coloca un camino
                f=f+1 #Avanza el mono
                Mapa[c][f]=0 #Actualiza el mono
                Mapa[c][f+1]=6
            else:
                Mapa[c][f]=4 #Coloca un camino
                f=f+1 #Avanza el mono
                Mapa[c][f]=0 #Actualiza el mono
                Mapa[c][f+1]=1
        else:
            Mapa[c][f] = 4
            f=f+1
            Mapa[c][f] = 0
            if (Mapa[cm][fm]==4 or Mapa[cm1][fm1]==4) and B%2==0: #Para regresar la meta a su lugar
                Mapa[cm][fm]=2
            
    elif Mov == "a" or Mov == "A": #Para mover a la izquierda
        if Mapa[c][f-1]==3 and B%2==0: #Cuando hay una pared
            print "Opps! Una pared :( El personaje no puede avanzar en esa direccion"
        elif Mapa[c][f-1]==1 and Mapa[c][f-2]==1: #Cuando hay dos cajas juntas
            print "Opps! No puedes avanzar en esa direccion!"
        elif Mapa[c][f-1]==1 and Mapa[c][f-2]==3: #Cuando empuja la caja y hay una pared
            print "Opps! No puedes avanzar en esa direccion!"
        elif Mapa[c][f-1]==6 and B%2==0:
            if Mapa[c][f-2]==4:
                    Mapa[c][f]=4 #Coloca un camino
                    f=f-1 #Avanza el mono
                    Mapa[c][f]=0 #Actualiza el mono
                    Mapa[c][f-1]=1
            else:
                print "Opps! Obstaculo"
        elif Mapa[c][f-1]==1 and B%2==0: #Para mover la caja
            if Mapa[c][f-2]==Mapa[cm][fm]:
                Mapa[c][f]=4 #Coloca un camino
                f=f-1 #Avanza el mono
                Mapa[c][f]=0 #Actualiza el mono
                Mapa[c][f-1]=6
            elif Mapa[c][f-2]==Mapa[cm1][fm1]:
                Mapa[c][f]=4 #Coloca un camino
                f=f-1 #Avanza el mono
                Mapa[c][f]=0 #Actualiza el mono
                Mapa[c][f-1]=6
            else:
                Mapa[c][f]=4 #Coloca un camino
                f=f-1 #Avanza el mono
                Mapa[c][f]=0 #Actualiza el mono
                Mapa[c][f-1]=1
        else: #Solo para avanzar a la izquierda
            Mapa[c][f] = 4
            f=f-1
            Mapa[c][f] = 0
            if (Mapa[cm][fm]==4 or Mapa[cm1][fm1]==4) and B%2==0: #Para rgresar la meta a su lugar
                Mapa[cm][fm]=2







            
    elif Mov == "s" or Mov == "S": #Para mover para abajo
        if Mapa[c+1][f]==3 and B%2==0: #Cuando hay una pared
            print "Opps! Una pared :( El personaje no puede avanzar en esa direccion"
        elif (Mapa[c+1][f]==1 and Mapa[c+2][f]==1) and B%2==0: #Cuando hay dos cajas juntas
            print "Opps! No puedes avanzar en esa direccion!"
        elif (Mapa[c+1][f]==1 and Mapa[c+2][f]==3) and B%2==0: #Cuando empuja la caja y hay una pared
            print "Opps! No puedes avanzar en esa direccion!"
        elif Mapa[c+1][f]==6 and B%2==0:
            if Mapa[c+2][f]==4:
                    Mapa[c][f]=4 #Coloca un camino
                    c=c+1 #Avanza el mono
                    Mapa[c][f]=0 #Actualiza el mono
                    Mapa[c+1][f]=1
            else:
                print "Opps! Obstaculo"
        elif Mapa[c+1][f]==1 and B%2==0: #Para mover la caja
            if Mapa[c+2][f]==Mapa[cm][fm]:
                Mapa[c][f]=4 #Coloca un camino
                c=c+1 #Avanza el mono
                Mapa[c][f]=0 #Actualiza el mono
                Mapa[c+1][f]=6
            elif Mapa[c+2][f]==Mapa[cm1][fm1]:
                Mapa[c][f]=4 #Coloca un camino
                c=c+1 #Avanza el mono
                Mapa[c][f]=0 #Actualiza el mono
                Mapa[c+1][f]=6
            else:
                Mapa[c][f]=4 #Coloca un camino
                c=c+1 #Avanza el mono
                Mapa[c][f]=0 #Actualiza el mono
                Mapa[c+1][f]=1
        else: #Solo para avanzar a la derecha
            Mapa[c][f] = 4
            c=c+1
            Mapa[c][f] = 0
            if (Mapa[cm][fm]==4 and Mapa[cm1][fm1]==4) and B%2==0:  #Para rgresar la meta a su lugar
                Mapa[cm][fm]=2

    elif Mov == "w" or Mov == "W": #Para mover para arriba
        if Mapa[c-1][f]==3 and B%2==0: #Cuando hay una pared
            print "Opps! Una pared :( El personaje no puede avanzar en esa direccion"
        elif Mapa[c-1][f]==1 and Mapa[c-2][f]==1 and B%2==0: #Cuando hay dos cajas juntas
            print "Opps! No puedes avanzar en esa direccion!"
        elif Mapa[c-1][f]==1 and Mapa[c-2][f]==3 and B%2==0: #Cuando empuja la caja y hay una pared
            print "Opps! No puedes avanzar en esa direccion!"
        elif Mapa[c-1][f]==6 and B%2==0:
            if Mapa[c-2][f]==4:
                    Mapa[c][f]=4 #Coloca un camino
                    c=c-1 #Avanza el mono
                    Mapa[c][f]=0 #Actualiza el mono
                    Mapa[c-1][f]=1
            else:
                print "Opps! Obstaculo"
        elif Mapa[c-1][f]==1 and B%2==0: #Para mover la caja
            if Mapa[c-2][f]==Mapa[cm][fm]:
                Mapa[c][f]=4 #Coloca un camino
                c=c-1 #Avanza el mono
                Mapa[c][f]=0 #Actualiza el mono
                Mapa[c-1][f]=1
                Mapa[cm][fm]=6
            elif Mapa[c-2][f]==Mapa[cm1][fm1]:
                Mapa[c][f]=4 #Coloca un camino
                c=c-1 #Avanza el mono
                Mapa[c][f]=0 #Actualiza el mono
                Mapa[c-1][f]=1
                Mapa[cm1][fm1]=6
            else:
                Mapa[c][f]=4 #Coloca un camino
                c=c-1 #Avanza el mono
                Mapa[c][f]=0 #Actualiza el mono
                Mapa[c-1][f]=1
        else: #Solo para avanzar a la derecha
            Mapa[c][f] = 4
            c=c-1
            Mapa[c][f] = 0
            if (Mapa[cm][fm]==4 or Mapa[cm1][fm1]==4) and B%2==0: #Para rgresar la meta a su lugar
                Mapa[cm][fm]=2

    else:
        print "Opps! Tecla incorrecta"
        print "Intenta de nuevo"
    if Mapa[cm][fm]==6 and Mapa[cm1][fm1]==6:
        for y in Mapa: #Para mostrar la matriz sin corchetes ni comas
            for x in y: 
                print x,
            print
        print "Haz ganado!"
        break
