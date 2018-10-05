
"""
prime.py - massa de dados para o Tableau

"""

def so(pp):
    s=0
    for c in pp[:]:
        s+=int(c)
    if s > 9:
        return(so(str(s)))
    return str(s)

def pr(pp):
    for d in range(2,pp-1):
        #print(d,pp/d,int(pp/d))
        if ((pp/d) - int(pp/d) == 0.0):
            return 0
    return 1

#fatorar: colocar o numero em produto de numeros primos(forma fatorada)
def fatorar(x):          #simulado-> fatorar(6)
    A=[]                 #A=[]
    for y in range(2,x): #for y in range(2,6): y=[2,3,4,5]
        while x%y==0:    #enquanto resto da divisao 6/y for 0:
            x=x/y        #x=6/y-> 6/2,6/3,6/4,6/5-> 6/3=3 e 3/3=1, por isso usar while.
            A.append(y)  #A=[6/2,6/3,3/3]=[3,2,1]
    if sum(A)==0:        #se x fosse numero primo, a sua forma fatoriada seria ele mesmo.
        A.append(x)      #se sum(A)==0 i.e, x%y nunca é 0, entao x é primo
    return A             #retorna lista [3,2,1]
def str0(pp):
    while len(pp) < 3:
        pp = "0" + pp
    return " " + pp

def tost(pp):
    ret = "" 
    for um in pp:
        ret += str0(str(um))
    return  ret

def makereg5(p1,p2,p3,p4,p5):
    horizon = [2,3,5,7,11]
    r=1
    for i in range(p1):
        r = r * horizon[0]
    for i in range(p2):
        r = r * horizon[1]
    for i in range(p3):
        r = r * horizon[2]
    for i in range(p4):
        r = r * horizon[3]
    for i in range(p5):
        r = r * horizon[4]
    return r

primes = []
anterior = 0
for ii in range(3,100):
    if(pr(ii)==1):
        primes.append(ii)
        anterior = ii

for ca in primes:
    print(tost(fatorar(ca-1)[::-1]), ca)

print(makereg5(1,1,1,1,1))
print(makereg5(1,1,1,0,0))
print(makereg5(192,168,0,1,0))


