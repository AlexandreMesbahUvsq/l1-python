print("3"*"15") affiche une erreur car les int entre guillemets sont separes du block multiplication 
or on ne peut pas afficher la multiplication de deux chaines de caracteres.

ex 2:

origine=str(input("entrez un pays d'origine"))
destination=str(input("entrez un pays de destination"))
if origine=="france":
    if destination=="france":
        print("gratuit")
    elif destination=="estonie":
        print("0.3$/min")
    else : 
        print("consulter la brochure tarifaire")
if origine=="estonie":
    if destination=="france":
        print("0.7$/min")
    else : 
        print("consulter la brochure")
elif origine!="france" and origine!="estonie":
    print("consulter la brochure")


ex 3:
from math import*
a=int(input("entrer un entier"))
b=int(input("entrer un deuxieme entier"))
n=0
c=0
while(a!=b)