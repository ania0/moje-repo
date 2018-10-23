#pobiera moduł random
import random

koszyczek = ['a','b','d','y','czy','z','s','w','pepsi','cola']
team1 = []
#len zwraca dlugosc listy
pojemnoscKoszyczka = len(koszyczek)
#// dzieli liczbe i zwraca liczbe calkowita
polowa = pojemnoscKoszyczka // 2

for liczba in range(polowa):
    losowyelement=random.choice(koszyczek)
    team1.append(losowyelement)
    koszyczek.remove(losowyelement)
print('Team 1:',team1)
print('Team 2:',koszyczek)
