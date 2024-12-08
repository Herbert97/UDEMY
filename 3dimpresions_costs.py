# CALCULAR EL AREA DE UN TRIANGULO


 # entrada
print('Calculando el costo de la impresion por gramos: ')
print('Dame el costo del kilogramo de filamento y la cantidad en gramos de filamento de la pieza: ')
base,altura = float(input()), float(input()) #se leen dos datos a la vez separados por enter
print('dame el tiempo de impresion: ')
tiempo_impresion=float(input())
#Proceso
area= base*altura /2
#Salida
print(f'Para un triangulo de base {base} y altura {altura} el area es {area}')