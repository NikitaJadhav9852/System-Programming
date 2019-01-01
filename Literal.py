import re
from Symbol import *
from tabulate import tabulate
OP=['mov','add','sub','div','mul','cmp','inc','dec']

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

def Hex(str1):
    ls1=[]
    ls2=[]
    for i in str1:
        a = hex(ord(i))
        ls1.append(a)
    for j in ls1:
        ls2.append(j[2:])
        str1 = ''.join(ls2)
#    print(str1)
    ls1=[]
    ls2=[]
    return str1

lst1=fileReading("fact.asm")
#print("File1",lst1)
def ConvertToHex(n):
    w=''
    w = hex(int(n))
    return w[2:]

LitHex = []
LitNm = []

for hh in Value:
	if(int(len(hh))>0):
		h = Hex(hh)
		LitHex.append(h)
		LitNm.append(hh)

j=0
for i in range(len(lst1)):
    if len(lst1[i])>=2:
        l1 = list(lst1[i][1].split(','))
        if len(l1)>=2:
            if l1[1].isdigit():
                LitHex.append(ConvertToHex(l1[1]))
                LitNm.append(l1[1])
#print(LitHex)
#print(LitNm)
FinalList1= [[LitNm[i],LitHex[i]] for i in range(len(LitNm))]
f2 = open('Literal','w')
f2.write(tabulate(FinalList1))
