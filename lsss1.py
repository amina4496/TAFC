
def access_policy(F):
    M=[]
    print type(M)
    M[1][1]=[1]
    L[1]=F
    m=1
    d=1
    z=1
    while z!=0:
        z=0
        i=1
        while i<=m and z==0:
            if L[i]:
                z=i
            i=i+1
        if z!=0:
            Fz=L[z]
            m2=len(Fz)
            for i in range(m2):
                L2[i]=Fz[i]
            d2=2#threshold value of Fz
            M1,L1,m1,d1=M,L,m,d
            for i in range(1,z-1):
                L[i]=L1[i]
                for j in range(1,d1):
                    M[i][j]=M1[i][j]
                for j in range(d1+1,d1+d2-1):
                    M[i][j]=0
            for i in range(z,z+m2-1):
                L[i]=L2[i-z+1]
                for j in range(1,d1):
                    M[i][j]=M1[z][j]
                a=i-(z-1)
                x=a
                for j in range(d1+1,d1+d2-1):
                    M[i][j]=x
                    x=x*a%p
            for i in range(z+m2,m1+m2-1):
                L[i]=L1[i-m2+1]
                for j in range(1,d1):
                    M[i][j]=M1[i-m2+1][j]
                for j in range(d1+1,d1+d2-1):
                    M[i][j]=0
            m,d=m1+m2-1,d1+d2-1
l=["IT","Software","Hardware"]
b=["Maintenance","Manager"]
F=l or b
access_policy(F)
