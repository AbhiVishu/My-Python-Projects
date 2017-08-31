from collections import Counter
def frequency(l):
    count =0
    count1 =0
    l.sort()
    #print (l)
    set1 = set(l)
    #print (set1)
    element = []
    element.extend(set1)
    element.sort()
    #print (element)
    c = Counter(l)
    s = [c[i] for i in range(min(c),max(c)+1)]
    #print (s)
    freqList = []
    for i in s:
        if(i != 0):
            freqList.append(i)

    #print (freqList)
    minList = []
    maxList = []
    minimumFreq = min(freqList)
    maximumFreq = max(freqList)
    if(minimumFreq == maximumFreq):
        minList = maxList
    for i in range(0, len(freqList)):
        if(freqList[i] == minimumFreq):
            minList.append(element[i])
        elif(freqList[i] == maximumFreq):
            maxList.append(element[i])

    return (minList, maxList)


def onehop(relation):
    lis = []

    for a,b in relation:
        for c,d in relation:
            if(b==c and a!=d):
                ans = tuple([a,d])
                lis.append(ans)
    for i in range(len(lis)-1):
        for j in range(len(lis)-1):
            if(lis[i]==lis[j] and i!=j):
                del lis[j]
    lis.sort()

    return(lis)
