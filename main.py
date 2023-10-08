import numpy as np
from funciones import *
from variables import *
import time

# Inicio del juego
print('''
       *** HUNDIR LA FLOTA v1.0 ***
       
    ''')
while not fin:
    if jugador:
        if vm == 0:
            fin = True
        else:
            print('Jugador: ' + str(20-vm) + '\t\t\t Máquina: ' + str(20-vj))
            print (tabo)
            # jugador dispara
            x = int(input('Introduzca coordenada x (0-9): '))
            y = int(input('Introduzca coordenada y (0-9): '))   
            
            if tabm[x, y] == "O":
                tabm[x, y] = "X"
                tabo[x, y] = "X"
                vm -= 1
                #print("\nHas acertado!")
                if esta_hundido(tabm,x,y):
                    print('\nHUNDIDO! :)')
                    pinta_aguas(tabo,x,y)
                    #pinta_aguas(tabm,x,y)
                else:
                    print('\nTocado')
                
            elif tabm[x, y] == " ":
                tabm[x, y] = "-"
                tabo[x, y] = "-"
                jugador = False
                print("\nAgua")
            elif tabm[x, y] == "X" or tabm[x, y] == "-":
                print("\nDisparo previamente realizado!")
            #print(tabo)
        time.sleep(1)
    else:
        if vj == 0:
            fin = True
        else:
            # máquina dispara
            print('La máquina dispara...')
            time.sleep(1)
            x = np.random.randint(0, 10)
            y = np.random.randint(0, 10)
            # evitar disparos previos
            while tabj[x, y] == "X" or tabj[x, y] == "-":
                x = np.random.randint(0, 10)
                y = np.random.randint(0, 10)
            if tabj[x, y] == "O":
                tabj[x, y] = "X"
                vj -= 1
                #print("\nLa máquina te ha dado!")
                if esta_hundido(tabj,x,y):
                    print('\t\t\t\t Hundido :(')
                    pinta_aguas(tabj,x,y)
                else:
                    print('\t\t\t\t Tocado :|')
            elif tabj[x, y] == " ":
                tabj[x, y] = "-"
                jugador = True
                print("\t\t\t\t Agua :)")
        time.sleep(1)
    print('\n')
    #print('Jugador: ' + str(20-vm) + '\t\t\t Máquina: ' + str(20-vj))
                
# Fin de juego
    # Mostrar resultados
print('\n\n')
if vm == 0:
    print('HAS GANADO!!!')
else:
    print('Has perdido la batalla')
print('\n\nFIN DE LA PARTIDA')