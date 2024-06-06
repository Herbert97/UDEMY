#metodos de las listas
myset={1,2,3,4,5}
yourset={4,5,6,7,8,9,10}
#saca la diferencia entre listas
print(myset.difference(yourset))
#descarta el valor de la lista
#print(myset.discard(5))
#print(myset)
#actualzia los valores de la lista con los de la otra lista
#print(myset.difference_update(yourset))
#print(myset)
#obtiene la interseccion de las listas
#print(myset.intersection(yourset))
#comprueba si tiene valores compartidos entre listas.
#print(myset.isdisjoint(yourset))
#comprueba la union entre las listas.
#print(myset.union(yourset))
#comprueba si es un subset de la lista
print(myset.issubset(yourset))
#comprueba si una lista engloba los valores de la otra.
print(yourset.issuperset(myset))