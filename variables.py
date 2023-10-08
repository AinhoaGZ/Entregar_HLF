import numpy as np

# VARIABLES
jugador = True
fin = False
vm = 20
vj = 20

# Tableros; usaremos el mismo para jugador y máquina
tablero = np.full((10,10), ' ')
tabj = tablero
tabm = tablero
tabo = np.full((10,10), ' ')

# Posicionar los barcos de manera fija para el jugador y la máquina
barco_1 = [(0,0),]
barco_2 = [(1,2),]
barco_3 = [(2,4),]
barco_4 = [(3,6),]
barco_5 = [(5,1), (6,1)]
barco_6 = [(9,1), (9,2)]
barco_7 = [(4,9), (5,9), (6,9)]
barco_8 = [(9,6), (9,7), (9,8)]
barco_9 = [(7,4), (7,5), (7,6), (7,7)]

lista_barcos = [barco_1, barco_2, barco_3, barco_4, barco_5, barco_6, barco_7, barco_8, barco_9]

for i in lista_barcos:
    for j in i:
        tablero[j] = 'O'