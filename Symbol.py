import re
from tabulate import tabulate

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

lst1=fileReading("fact.asm")
#print("File1",lst1)

def CalculateAddress(ll):
    s =' '.join(ll)
    s = re.sub("'",'',s)
    s1 = list(s.split(','))
    s2= s1[0]
    s3=s1[1:]
    return (s,len(s2)+len(s3))
labels = []
LineNo = []
Section = []
DataType = []
DataSize = []
D = []
Addr = []
Value = []
txt1=[]

def SymbolTable(line,sec,dataT,dataS,defn,addr,val1):
    LineNo.append(line)
    Section.append(sec)
    DataType.append(dataT)
    DataSize.append(dataS)
    D.append(defn)
    Addr.append(addr)
    Value.append(val1)
def Hex(s1):
    ls1=[]
    ls2=[]
    a1 = ''
    for i in s1:
        a1 =hex(ord(i))
        ls1.append(a1)
    for r in ls1:
        d=i
        ls2.append(r[2:])
    final = ''.join(ls2)
    return(final)

sd=sb=0
DataHex=[]
for i in lst1:
    for j in i:
        if(j=="db"):
            ll=i[2:]
            #print(ll)
            val=CalculateAddress(ll)
            g=val[1]*1
            SymbolTable(i[0],'.data','db','1','D',sd,val[0])
            DataHex.append(Hex(val[0]))
            sd=sd+g
        if(j=="dd"):
            ll=i[2].split(',')
            g=len(ll)*4
            SymbolTable(i[0],'.data','dd','2','D',sd,' '.join(ll))
            sd=sd+g
            DataHex.append(Hex(''.join(ll)))
        if(j=="dq"):
            ll=i[2].split(',')
            g=len(ll)*8
            SymbolTable(i[0],'.data','dq','8','D',sd,' '.join(ll))
            sd=sd+g
            DataHex.append(Hex(''.join(ll)))
        if(j=="dw"):
            ll=i[2].split(',')
            g=len(ll)*16
            SymbolTable(i[0],'.data','dw','4','D',sd,' '.join(ll))
            sd=s+g
            DataHex.append(Hex(''.join(ll)))
        if j=="resb":
            ll=i[0]
            g=int(i[2])*1
            SymbolTable(i[0],'.bss','resb','1','D',sb,' '.join(ll))
            sb=sb+g
        if j=="resd":
            ll=i[0]
            g=int(i[2])*4
            SymbolTable(i[0],'.bss','resd','4','D',sb,' '.join(ll))
            sb=sb+g
        if j=="resq":
            ll=i[0]
            g=int(i[2])*8
            SymbolTable(i[0],'.bss','resq','8','D',sb,' '.join(ll))
            sb=sb+g
        if j=="resw":
            ll=i[0]
            g=int(i[2])*16
            SymbolTable(i[0],'.bss','resw','16','D',sb,' '.join(ll))
            sb=sb+g
        if j=='extern':
            j1 = i[1]
            SymbolTable(j1,'.text','-','-','D','-','')
            labels.append(i[1])
        index=j.find(':')
        if(index>0):
            txt = j[:index]
            SymbolTable(txt,'.text','-','-','D','-','')
            labels.append(txt)
        if j=='je' or j=='jz' or j=='jc' or j=='jne' or j=='jg' or j=='jl' or j=='jle' or j=='jge' or j=='jmp':
            txt1.append(i[1])

lab=labels[3:]
for i in range(len(lab)):
    for j in range(len(txt1)):
        if txt1[j]!=lab[i] :
            flag=0
        else:
            flag=1
            break
    if flag==0:
        SymbolTable(lab[i],'.text','-','-','UD','-','')
#headers=['LineNo','Section','DataType','Def/Not','Address','Value']
l1 = len(D)
for i in range(l1):
    for j in range(l1):
        if Value[i]==Value[j]:
            if D[i]=='D' and D[j]=='UD':
                D[i]='D'
            elif D[i]=='UD' and D[j]=='D':
                D[i]='D'
r = []
#print(len(Value))
for i in range(len(Value)):
    for j in range(i+1,len(Value)):
        if LineNo[i]==LineNo[j]:
            #print(j)
            r.append(j)

for i in range(len(r)):
    del LineNo[r[i]]
    del Section[r[i]]
    del DataType[r[i]]
    del DataSize[r[i]]
    del D[r[i]]
    del Value[r[i]]


FinalList= [[LineNo[i],Section[i],DataType[i],DataSize[i],D[i],Addr[i],Value[i]] for i in range(len(LineNo))]
f1 = open('SymbolTable','w')
f1.write(tabulate(FinalList))
#print(DataHex)
