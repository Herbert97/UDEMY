# CALCULAR EL AREA DE UN TRIANGULO


 # entrada
#variables del costo
print('Calculando el costo de la impresion')

#se leen los datos separados por enter
print('Dame el peso de la piezas en gr: ')
peso = float(input())

print('dame el costo del filamento')
costo_del_filamento = float(input())

print('dame el tiempo de impresion en horas: ')
tiempo_impresion=float(input())

print('dame el costo de la mano de obra: ')
mano_de_obra= float(input())
#variables fijas estos valores pueden cambiar dependiendo del trabajo.
costo_kw_hrs = 0.81
watts_maquina = 0.35
ganancia= 0.4
mantenimiento=5
#Proceso
#costo del filamento por gr.
costo_por_gramos=(peso/1000)*costo_del_filamento
costo_energia= (tiempo_impresion*costo_kw_hrs*watts_maquina)
subtotal=(costo_por_gramos+costo_energia+mantenimiento+mano_de_obra)
total=(subtotal*(1+ganancia))

#Salida
print(f'Para una impresion 3d con un tiempo de: {tiempo_impresion} tiene un costo por gramos de: {costo_por_gramos}  con un costo de energia de: {costo_energia}el subtotal es de: {subtotal} dando un total por pieza de {total}')