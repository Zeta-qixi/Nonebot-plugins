
import os
import random



def xxx(a):
    data = []
    with open('python\plugins\jrrp\jrrp.txt','a+') as f:
        f.seek(0)
        for line in f.readlines():
            eachdata = line.split()
            data.append(eachdata)
        f.close

    for i in range(len(data)):
        if a == data[i][0]:
            return(data[i][1])

    
    rd = random.randrange(100)
    with open('python\plugins\jrrp\jrrp.txt','a+') as f:
        f.write(a+' '+str(rd)+'\n')
    return(rd)


a = "3"
print(xxx(a))
