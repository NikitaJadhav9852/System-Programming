fr = open('occ.asm','r')
fw = open('macroTable','w')
fd =open('macroDef','w')
i=0
lst=[]
l=[]
mn=[]
p=[]
t=tuple()
end=[]
start=[]
for j in fr:
    i=i+1
    l =j.strip().split()
    t=(i,l)
    #print(t)
    if(len(t[1])==1):
            if(t[1][0]=='%endmacro'):
                end.append(t[0])
            if(t[1][0]=='%endmacro'):
                fd.write(j)
                continue
    if(len(t[1])>1):
        if(t[1][0]=='%macro'):
                #print(t[1][k])
            mn.append(t[1][1])
            p.append(t[1][2])
            start.append(t[0])
        if(t[1][0]=='section'):
            break
    fd.write("%s"%(j))
    if(len(t[1])==0):
        fd.write("%s"%(j))


#print(end)
#print(mn)
if(len(mn)>=2):
    for e in range(1,len(mn)-1):
        if(mn[e-1]==mn[e]):
            p[e-1]=p[e]
            end[e-1]=end[e]
            start[e-1]=start[e]
            del end[e]
            del start[e]
            del mn[e]
            del p[e]
#print(end)
#print(mn)
#print(p)
#print(start)
for w in range(len(mn)):
    fw.write('%d\t%s\t\t%d\t%s\t%s\n'%(w+1,mn[w],int(p[w]),start[w],end[w]))

