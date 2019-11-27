l=[]
attr=["IT","Ma","So","Ha","Mn"]
##attr=["IT","Maintenance","Software","Hardware","Manager"]
A,B,C,D,E=attr[0],attr[1],attr[2],attr[3],attr[4]
at=["A","B","C","D","E"]
F=(A and (B or C))
M,L,L2=[],[],[]
a=len(attr)
for i in range(a+1):
    t=[]
    for j in range(a+1):
        if i==0 and j==0:
            t.append(" ")
        elif j==0 and i>0:
            t.append(attr[i-1])
        elif i==0 and j>0:
            t.append(attr[j-1])
        else:
            t.append(" "+str(0))
    M.append(t)
for i in M:
    print i

M[1][1],m,d = 1,1,1
L.append(F)
z=1
while z!=0:
    z=0
    i=0
    while i<1 and z==0:
        if L[i]:
            z=i
        i=i+1
    if z!=0:
        fz=L[z]
        print fz
        m2=len(fz)
        
        print m2
        for ij in range(m2):
            L2.append(fz[ij])
        
        print L2
