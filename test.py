f= open("SIC.txt",'r')
word = f.readlines()
temp = []
titlename = ["Loc","title","code","explain"]
temp.insert(0,titlename)
loc=0
for i in word:
    temp1 = i.strip('\n')
    temp.append(temp1.split('\t'))
for num in range(1,len(temp)):
    if len(temp[num])<=1:
        continue
    elif temp[num][0]=='.':
        continue
    elif(temp[num][1]=='START'):
        loc = int(temp[num][2],16)
        temp[num].insert(0,"{:X}".format(loc))
        continue
    elif(temp[num][1]=='WORD'):
        temp[num].insert(0,"{:X}".format(loc))
        loc+=3
        continue
    elif(temp[num][1]=='RESW'):
        temp[num].insert(0,"{:X}".format(loc))
        loc= loc + (3*int(temp[num][3],16))
        continue
    elif(temp[num][1]=='RESB'):
        temp[num].insert(0,"{:X}".format(loc))
        loc+=int(temp[num][3])
        continue
    elif(temp[num][1]=='BYTE'):
        temp[num].insert(0,"{:X}".format(loc))
        temp1 = temp[num][3].split('\'')
        if temp1[0]=='C':
            loc += len(temp1[1])
        elif temp1[0]=='X':
            loc += int(len(temp1[1])/2)
        continue
    else:
        temp[num].insert(0,"{:X}".format(loc))
        loc += 3

f.close()
with open('outputfile.txt','w') as f:
    for num in range(0,len(temp)):
        for output in temp[num]:
            f.write(output+'\t')
        f.write('\n')
