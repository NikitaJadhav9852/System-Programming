from Symbol import *
from Literal import *
import re
from tabulate import tabulate
f3 = open('Inter','w')
def fileReading(filename):
    f=open(filename,"r")
    data=f.readlines()
    data1= map(lambda s: s.strip(),data)
    lst1=[]
    for ele in data1:
        lst=[]
        for j in ele.split():
            lst.append(j)
        lst1.append(lst)
    return lst1
reg=["eax","ecx","edx","ebx","esp","ebp","esi","edi"]
lst1=fileReading("fact.asm")
new = []
#print(labels)
def GenerateInter(str1):
    for i in range(len(str1)):
        for j in range(len(reg)):
            if reg[j]==str1[i]:
                str1[i]='R#'+str(j+1)
        for h in range(len(labels)):
            if labels[h]==str1[i]:
                str1[i]='S#'+str(h+1)
        for m in range(len(LitNm)):
            if LitNm[m]==str1[i]:
                str1[i]='L#'+str(m+1)
        for y in range(len(LineNo)):
            if LineNo[y]==str1[i]:
                str1[i]='S#'+str(y+1)
        if str1[i].find('[')>=0:
            p=str1[i][6:len(str1[i])-1]
            del str1[i]
            for u in range(len(LineNo)):
                if LineNo[u]==p:
                    s = 'dword[S#'+str(u+1)+']'
                    str1.append(s)
    f3.write(' '.join(str1))
    f3.write('\n')
#print("File1",lst1)
for i in lst1:
    if len(i)>=2:
        if i[1].find(',')>1:
            a1 = i[1].split(',')
            #print(a1)
            del i[1]
            i.append(a1[0])
            i.append(a1[1])
    #print(i)
    if len(i)==1:
        ind = i[0].find(':')
        if(i[0].find(':')>=0):
            #print(i[0])
            s = i[0][:ind]
            #print(s)
            del i[0]
            i.append(s)
    GenerateInter(i)
#print(i)
