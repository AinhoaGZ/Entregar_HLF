
#from variables import *

# Función de tocado o undido

def esta_hundido(tablero,x,y):
    ''' Con esta función queremos saber si el disparo acertado que hemos hecho ha sido tocado o hundido.
        Vemos si tenemos en cada eje X e Y más 'O's que si hay alguno nos dirá tocado y si no se cumple quiere decir que está hundido.  
    '''
    hundido = True
    #N
    if x > 0 and tablero[x-1, y] == "O":
        hundido = False
    #S
    elif x < 9 and tablero[x+1, y] == "O":
        hundido = False
    #W
    elif y > 0 and tablero[x, y-1] == "O":
        hundido = False
    #E
    elif y < 9 and tablero[x, y+1] == "O":
        hundido = False
    return hundido
    

# Función para pintar agua alrededor del barco

def pinta_aguas(tablero,x,y):
    '''Comprobar si el barco es horizontal o vertical (el de uno lo tratará como horizontal).
    Si el barco es vertival voy comprobando hacia abajo hasta encontrar agua o el borde del tablero. Entonces pinto de agua 
    (si no es el borde del tablero) esa coordenada xmax y me la guardo; hago lo mismo pero hacia arriba y guardo xmin. 
    Teniendo ese rango (xmin, xmax), itero y pinto ambos lados de agua.
    En el caso horizontal sigue el mismo principio.  
    '''
    vertical = False
    # Mirar arriba y abajo
    if x > 0 and tablero[x-1, y] == "X":
        vertical = True
    if x < 9 and tablero[x+1, y] == "X":
        vertical = True
    if vertical:
        # Bajo todo
        while x<9 and tablero[x, y] == "X":
            x +=1
        xmax = x # guardo valor max
        if tablero[x,y] != "X":
         tablero[x,y] = "-" #pinto el del sur
        # Subo todo
        x -=1
        while x>0 and tablero[x, y] == "X":
            x -=1
        xmin = x # guardo valor min
        if tablero[x,y] != "X":
         tablero[x,y] = "-" # pinto el del norte
        # Pintar aguas W
        if y>0:
            for w in range(xmin, xmax+1):
             tablero[w,y-1] = "-"
        # pintar aguas E
        if y<9:
            for w in range(xmin, xmax+1):
             tablero[w,y+1] = "-"
    else:
        # Derecha todo
        while y<9 and tablero[x, y] == "X":
            y +=1
        ymax = y # guardo valor max
        if tablero[x,y] != "X":
         tablero[x,y] = "-" # pinto el el este
        # Izquierda todo
        y -=1
        while y>0 and tablero[x, y] == "X":
            y -=1
        ymin = y # guardo valor min
        if tablero[x,y] != "X":
         tablero[x,y] = "-" # pinto el del oeste
        # Pintar aguas N
        if x>0:
            for w in range(ymin, ymax+1):
             tablero[x-1,w] = "-"
        # Pintar aguas S
        if x<9:
            for w in range(ymin, ymax+1):
             tablero[x+1,w] = "-"