from collections import Counter
def frequency(l):
    count =0
    count1 =0
    l.sort()
    print (l)
    c = Counter(l)
    s = [c[i] for i in xrange(min(c),max(c)+1)]
    print (s)
    setAns = set(s)
    print (setAns)


frequency([13,12,11,13,14,13,7,11,13,14,12,14,14])
