mmg=[['A','B','C','D','E','F','G','H','I','J'],
     ['K','L','M','N','O','P','Q','R','S','T'],
     ['U','V','W','X','Y','Z','a','b','c','d'],
     ['e','f','g','h','i','j','k','l','m','n'],
     ['o','p','q','r','s','t','u','v','w','x'],
     ['y','z','1','2','3','4','5','6','7','8'],
     ['9','0','!','@','#','$','%','^','&','*'],
     ['(',')','`','-','=','~','_','+','[',']'],
     ['\ ',';',"'",',','.','/','{','}','|',':'],
     ['"','<','>','?',' ','','','','','']]
mm=input()
l=[[[],[]],[[],[]]]
s=''
for i in range(0,len(mm),4):
    l[0][0].append(int(mm[i]))
for i in range(1,len(mm),4):
    l[0][1].append(int(mm[i]))
for i in range(2,len(mm),4):
    l[1][0].append(int(mm[i]))
for i in range(3,len(mm),4):
    l[1][1].append(int(mm[i]))
for i in range(len(l[0][0])):
    if l[0][0][i]==0 and l[1][0][i]==0:
        s+=mmg[l[0][1][i]-1][l[1][1][i]-1]
    elif l[0][0][i]==0:
        s+=mmg[l[0][1][i]-1][int(str(l[1][0][i])+str(l[1][1][i]))-1]
    elif l[1][0][i]==0:
        s+=mmg[int(str(l[0][0][i])+str(l[0][1][i]))-1][l[1][1][i]-1]
print(s)