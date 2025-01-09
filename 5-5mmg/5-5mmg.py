mmg=[['A','B','C','D','E'],
     ['F','G','H','I','J'],
     ['K','L','M','N','O'],
     ['P','Q','R','S','T'],
     ['U','V','W','X','Y']]
mm=input()
l=[[],[]]
s=''
for i in range(0,len(mm),2):
    l[0].append(int(mm[i]))
for i in range(1,len(mm),2):
    l[1].append(int(mm[i]))
for i in range(len(l[0])):
    s+=mmg[l[1][i]-1][l[0][i]-1]
print(s)



















































































' '#Not Space!
#supercalifragilisticexpialidocious