F=[]
f1=1
f2=1
F.append(f1)
F.append(f2)
#print(F)
for i in range(1,24):
    j=F[i-1]+F[i]
    F.append(j)
print(F,len(F))
print()
print(f'Q1:sum={sum(F)}')
print()

D=[]
for i in range(1,len(F)):
    d=F[i]/F[i-1]
    D.append(d)
print(D,len(D))
print()
print(f'Q2:sum={sum(D)}')
print()

print("Q3:")
k=1
for i in range(5):
    for j in range(i+1):
        print(k,end=" ")
        k+=1
    print()
    
"""
i=0
    j=0
        k=1
        
i=1
    j=0     j=1
        k=2     k=3

"""

    
    
    
    
    