mmg=[['A','B','C','D','E'],
     ['F','G','H','I','J'],
     ['K','L','M','N','O'],
     ['P','Q','R','S','T'],
     ['U','V','W','X','Y']]
xx=input()
mm=''
for i in xx:
    for j in mmg:
        if i in j:
            mm+=str(j.index(i)+1)
            mm+=str(mmg.index(j)+1)
print(mm)