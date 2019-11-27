
allattr=["IT","Software","Hardware","Maintenance","Office"]
attr=[["IT","Software","Hardware",2],["Maintenance",1]]
M=[]
print len(allattr)

##for i in range(0,len(allattr)):
##    t=[]
##    for j in range(0,len(allattr)+1):
##        if i==0 and j==0:
##            t.append(" ")
##        elif i==0 and j>0:
##            t.append(allattr[j-1])
##    if t:
##        M.append(t)
l=[]

for i in range(0,len(attr)):

    for j in range(0,len(attr[i])):
        if attr[i][j]==2 or attr[i][j]==1:
            pass
        else:
            l.append(attr[i][j])
a=0
b=0
print len(l)
print len(allattr)
for i in range(len(allattr)):
    t=[]
    for j in range(len(l)):
        if i==0 and j==0:
            t.append(" ")
        elif j==0 and i>0:
            t.append(l[b])
            b+=1
            print b
        elif i==0 and j>0:
            t.append(allattr[a])
            a+=1
            print a
        else:
            t.append("0")
    M.append(t)

for i in M:
    print i
