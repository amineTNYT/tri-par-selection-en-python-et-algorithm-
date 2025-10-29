from numpy import array
#sasir taille du tableau
def sasir():
    n=int(input("Donner le taille du tableau=:"))
    while not (3<=n<=5):
        n=int(input("Donner taille du tableau=:"))
    return n

#remplir un tableau
def remplir(t,n):
    for i in range(0,n):
        t[i]=int(input("t["+str(i)+"]=:"))
 
#tri d'un tableau        
def tri_bulle(t,n):
    for i in range(n-1):
        pMin=i
        for j in range(i+1,n):
            if t[j]<t[pMin]:
                pMin=j
        if i!=pMin:
            
            aux=t[i]
            t[i]=t[pMin]
            t[pMin]=aux
  
            
#afficher un tableau   
def afficher(t,n):
    for i in range(0,n):
        print(t[i],end="|")
   
 
#PP    
n=sasir()
t=array([int()]*n)
remplir(t,n)
#afficher le tableau avant le tri
print("le tableau avant le tri")

afficher(t,n)
print()
tri_bulle(t,n)
#afficher le tableau après le tri
print("le tableau aprés le tri")
afficher(t,n)
