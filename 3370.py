from math import floor
cipherList = ["0182002821959", "3092737753574", "3397137880489", "2339619796630", "2916903963593", "1986692232044"]
e = 3199957
num = 3832716017551
f = open("encryptDict.txt", "r")
conversion = {}
count = 1
for i in f:
    if len(str(count)) == 1:
        strCount = "0" + str(count)
    else:
        strCount = str(count)
    conversion[strCount] = i.strip()
    count += 1
count = 2
while True:
    if num%count == 0:
        p = count
        q = int(num/p)
        break
    else:
        count += 1
theta = (p-1)*(q-1)
high = theta
low = e
aList = [0, 1]
bList = [1, 0]
flag = False
while True:
    q = floor(high/low)
    r = high%low
    if flag:
        aList[0] -= bList[0]*q
        aList[1] -= bList[1]*q
        flag = False
    else:
        bList[0] -= aList[0]*q
        bList[1] -= aList[1]*q
        flag = True
    if r == 1:
        break
    else:
        high = low
        low = r
if flag:
    d = bList[1]%theta
else:
    d = aList[1]%theta
messageList = []
for i in cipherList:
    decipher = 1
    i1000000 = 1
    i10000 = 1
    i100 = 1
    for j in range(100):
        i100 = (i100*int(i))%num
    for j in range(100):
        i10000 = (i10000*i100)%num
    for j in range(100):
        i1000000 = (i1000000*i10000)%num
    for j in range(floor(d/1000000)):
        decipher = (decipher * i1000000)%num
    for j in range(floor((d%1000000)/10000)):
        decipher = (decipher * i10000)%num
    for j in range(floor((d%10000)/100)):
        decipher = (decipher * i100)%num
    for j in range(floor(d%100)):
        decipher = (decipher * int(i))%num
    if len(str(decipher))%2 == 1:
        messageList.append("0" + str(decipher))
    else:
        messageList.append(str(decipher))
decodeList = []
for i in messageList:
    decodeString = ""
    for j in range(int(len(i)/2)):
        if conversion[i[2*j] + i[(2*j)+1]] == "whitespace":
            decodeString = decodeString + " "
        else:
            decodeString = decodeString + conversion[i[2*j] + i[(2*j)+1]]
    decodeList.append(decodeString)
print(decodeList)
