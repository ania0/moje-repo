import random

koszyczek = ['a','b','d','y','czy','z','s','w','pepsi','cola']

random.shuffle(koszyczek)

def generujTeamy(lista):
    random.shuffle(lista)
    polowa = len(lista)//2
    team1 = lista[0 : polowa]
    team2 = lista[polowa :]
    
    return team1, team2

print ('Wynik to:', generujTeamy( [1,2,3,4,5,6,7,8,9,0] ))
print ('Typ wyniku to:', type (generujTeamy( [1,2,3,4,5,6,7,8,9,0] ))) 