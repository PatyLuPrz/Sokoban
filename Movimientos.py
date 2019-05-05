def Der(f,c,Mapa):
    if Mapa[f][c]=='0' and Mapa[f][c+1]=='4':
        print "1-d"
        Mapa[f][c] = '4'
        Mapa[f][c+1] = '0'
    elif Mapa[f][c]=='0' and Mapa[f][c+1]=='1' and Mapa[f][c+2]=='4':
        print "2-d"
        Mapa[f][c] = '4'
        Mapa[f][c+1] = '0'
        Mapa[f][c+2] = '1'
    elif Mapa[f][c]=='0' and Mapa[f][c+1]=='1' and Mapa[f][c+2]=='2':
        print "3-d"
        Mapa[f][c] = '4'
        Mapa[f][c+1] = '0'
        Mapa[f][c+2] = '5'
    elif Mapa[f][c]=='0' and Mapa[f][c+1]=='2':
        print "4-d"
        Mapa[f][c]='4'
        Mapa[f][c+1]='6'
    elif Mapa[f][c]=='0' and Mapa[f][c+1]=='5' and Mapa[f][c+2]=='2':
        print "5-d"
        Mapa[f][c]='4'
        Mapa[f][c+1]='6'
        Mapa[f][c+2]='5'
    elif Mapa[f][c]=='6' and Mapa[f][c+1]=='2':
        print "6-d"
        Mapa[f][c]='2'
        Mapa[f][c+1]='6'
    elif Mapa[f][c]=='6' and Mapa[f][c+1]=='5' and Mapa[f][c+2]=='2':
        print "7-d"
        Mapa[f][c]='2'
        Mapa[f][c+1]='6'
        Mapa[f][c+2]='5'
    elif Mapa[f][c]=='6' and Mapa[f][c+1]=='5' and Mapa[f][c+2]=='4':
        print "8-d"
        Mapa[f][c]='2'
        Mapa[f][c+1]='6'
        Mapa[f][c+2]='1'
    elif Mapa[f][c]=='0' and Mapa[f][c+1]=='5' and Mapa[f][c+2]=='4':
        print "9-d"
        Mapa[f][c]='4'
        Mapa[f][c+1]='6'
        Mapa[f][c+2]='1'
    elif Mapa[f][c]=='6' and Mapa[f][c+1]=='4':
        print "10-d"
        Mapa[f][c]='2'
        Mapa[f][c+1]='0'
    elif Mapa[f][c]=='6' and Mapa[f][c+1]=='1' and Mapa[f][c+2]=='4':
        print "11-d"
        Mapa[f][c]='2'
        Mapa[f][c+1]='0'
        Mapa[f][c+2]='1'
    elif Mapa[f][c]=='6' and Mapa[f][c+1]=='1' and Mapa[f][c+2]=='2':
        print "12-d"
        Mapa[f][c]='2'
        Mapa[f][c+1]='0'
        Mapa[f][c+2]='5'
def Izq(f,c,Mapa):
    if Mapa[f][c]=='0' and Mapa[f][c-1]=='4':
        print "1-i"
        Mapa[f][c] = '4'
        Mapa[f][c-1] = '0'
    elif Mapa[f][c]=='0' and Mapa[f][c-1]=='1' and Mapa[f][c-2]=='4':
        print "2-i"
        Mapa[f][c] = '4'
        Mapa[f][c-1] = '0'
        Mapa[f][c-2] = '1'
    elif Mapa[f][c]=='0' and Mapa[f][c-1]=='1' and Mapa[f][c-2]=='2':
        print "3-i"
        Mapa[f][c] = '4'
        Mapa[f][c-1] = '0'
        Mapa[f][c-2] = '5'
    elif Mapa[f][c]=='0' and Mapa[f][c-1]=='2':
        print "4-i"
        Mapa[f][c]='4'
        Mapa[f][c-1]='6'
    elif Mapa[f][c]=='0' and Mapa[f][c-1]=='5' and Mapa[f][c-2]=='2':
        print "5-i"
        Mapa[f][c]='4'
        Mapa[f][c-1]='6'
        Mapa[f][c-2]='5'
    elif Mapa[f][c]=='6' and Mapa[f][c-1]=='2':
        print "6-i"
        Mapa[f][c]='2'
        Mapa[f][c-1]='6'
    elif Mapa[f][c]=='6' and Mapa[f][c-1]=='5' and Mapa[f][c-2]=='2':
        print "7-i"
        Mapa[f][c]='2'
        Mapa[f][c-1]='6'
        Mapa[f][c-2]='5'
    elif Mapa[f][c]=='6' and Mapa[f][c-1]=='5' and Mapa[f][c-2]=='4':
        print "8-i"
        Mapa[f][c]='2'
        Mapa[f][c-1]='6'
        Mapa[f][c-2]='1'
    elif Mapa[f][c]=='0' and Mapa[f][c-1]=='5' and Mapa[f][c-2]=='4':
        print "9-i"
        Mapa[f][c]='4'
        Mapa[f][c-1]='6'
        Mapa[f][c-2]='1'
    elif Mapa[f][c]=='6' and Mapa[f][c-1]=='4':
        print "10-i"
        Mapa[f][c]='2'
        Mapa[f][c-1]='0'
    elif Mapa[f][c]=='6' and Mapa[f][c-1]=='1' and Mapa[f][c-2]=='4':
        print "11-i"
        Mapa[f][c]='2'
        Mapa[f][c-1]='0'
        Mapa[f][c-2]='1'
    elif Mapa[f][c]=='6' and Mapa[f][c-1]=='1' and Mapa[f][c-2]=='2':
        print "12-i"
        Mapa[f][c]='2'
        Mapa[f][c-1]='0'
        Mapa[f][c-2]='5'
def Abj(f,c,Mapa):
    if Mapa[f][c]=='0' and Mapa[f+1][c]=='4':
        print "1-ab"
        Mapa[f][c] = '4'
        Mapa[f+1][c] = '0'
    elif Mapa[f][c]=='0' and Mapa[f+1][c]=='1' and Mapa[f+2][c]=='4':
        print "2-ab"
        Mapa[f][c] = '4'
        Mapa[f+1][c] = '0'
        Mapa[f+2][c] = '1'
    elif Mapa[f][c]=='0' and Mapa[f+1][c]=='1' and Mapa[f+2][c]=='2':
        print "3-ab"
        Mapa[f][c] = '4'
        Mapa[f+1][c] = '0'
        Mapa[f+2][c] = '5'
    elif Mapa[f][c]=='0' and Mapa[f+1][c]=='2':
        print "4-ab"
        Mapa[f][c]='4'
        Mapa[f+1][c]='6'
    elif Mapa[f][c]=='0' and Mapa[f+1][c]=='5' and Mapa[f+2][c]=='2':
        print "5-ab"
        Mapa[f][c]='4'
        Mapa[f+1][c]='6'
        Mapa[f+2][c]='5'
    elif Mapa[f][c]=='6' and Mapa[f+1][c]=='2':
        print "6-ab"
        Mapa[f][c]='2'
        Mapa[f+1][c]='6'
    elif Mapa[f][c]=='6' and Mapa[f+1][c]=='5' and Mapa[f+2][c]=='2':
        print "7-ab"
        Mapa[f][c]='2'
        Mapa[f+1][c]='6'
        Mapa[f+2][c]='5'
    elif Mapa[f][c]=='6' and Mapa[f+1][c]=='5' and Mapa[f+2][c]=='4':
        print "8-ab"
        Mapa[f][c]='2'
        Mapa[f+1][c]='6'
        Mapa[f+2][c]='1'
    elif Mapa[f][c]=='0' and Mapa[f+1][c]=='5' and Mapa[f+2][c]=='4':
        print "9-ab"
        Mapa[f][c]='4'
        Mapa[f+1][c]='6'
        Mapa[f+2][c]='1'
    elif Mapa[f][c]=='6' and Mapa[f+1][c]=='4':
        print "10-ab"
        Mapa[f][c]='2'
        Mapa[f+1][c]='0'
    elif Mapa[f][c]=='6' and Mapa[f+1][c]=='1' and Mapa[f+2][c]=='4':
        print "11-ab"
        Mapa[f][c]='2'
        Mapa[f+1][c]='0'
        Mapa[f+2][c]='1'
    elif Mapa[f][c]=='6' and Mapa[f+1][c]=='1' and Mapa[f+2][c]=='2':
        print "12-ab"
        Mapa[f][c]='2'
        Mapa[f+1][c]='0'
        Mapa[f+2][c]='5'
def Arb(f,c,Mapa):
    if Mapa[f][c]=='0' and Mapa[f-1][c]=='4':
        print "1-ar"
        Mapa[f][c] = '4'
        Mapa[f-1][c] = '0'
    elif Mapa[f][c]=='0' and Mapa[f-1][c]=='1' and Mapa[f-2][c]=='4':
        print "2-ar"
        Mapa[f][c] = '4'
        Mapa[f-1][c] = '0'
        Mapa[f-2][c] = '1'
    elif Mapa[f][c]=='0' and Mapa[f-1][c]=='1' and Mapa[f-2][c]=='2':
        print "3-ar"
        Mapa[f][c] = '4'
        Mapa[f-1][c] = '0'
        Mapa[f-2][c] = '5'
    elif Mapa[f][c]=='0' and Mapa[f-1][c]=='2':
        print "4-ar"
        Mapa[f][c]='4'
        Mapa[f-1][c]='6'
    elif Mapa[f][c]=='0' and Mapa[f-1][c]=='5' and Mapa[f-2][c]=='2':
        print "5-ar"
        Mapa[f][c]='4'
        Mapa[f-1][c]='6'
        Mapa[f-2][c]='5'
    elif Mapa[f][c]=='6' and Mapa[f-1][c]=='2':
        print "6-ar"
        Mapa[f][c]='2'
        Mapa[f-1][c]='6'
    elif Mapa[f][c]=='6' and Mapa[f-1][c]=='5' and Mapa[f-2][c]=='2':
        print "7-ar"
        Mapa[f][c]='2'
        Mapa[f-1][c]='6'
        Mapa[f-2][c]='5'
    elif Mapa[f][c]=='6' and Mapa[f-1][c]=='5' and Mapa[f-2][c]=='4':
        print "8-ar"
        Mapa[f][c]='2'
        Mapa[f-1][c]='6'
        Mapa[f-2][c]='1'
    elif Mapa[f][c]=='0' and Mapa[f-1][c]=='5' and Mapa[f-2][c]=='4':
        print "9-ar"
        Mapa[f][c]='4'
        Mapa[f-1][c]='6'
        Mapa[f-2][c]='1'
    elif Mapa[f][c]=='6' and Mapa[f-1][c]=='4':
        print "10-ar"
        Mapa[f][c]='2'
        Mapa[f-1][c]='0'
    elif Mapa[f][c]=='6' and Mapa[f-1][c]=='1' and Mapa[f-2][c]=='4':
        print "11-ar"
        Mapa[f][c]='2'
        Mapa[f-1][c]='0'
        Mapa[f-2][c]='1'
    elif Mapa[f][c]=='6' and Mapa[f-1][c]=='1' and Mapa[f-2][c]=='2':
        print "12-ar"
        Mapa[f][c]='2'
        Mapa[f-1][c]='0'
        Mapa[f-2][c]='5'



