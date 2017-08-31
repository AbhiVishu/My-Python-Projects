list = [5,2,4,8,6,3,1,7,9]
def Demo(c):
    for i in range(len(list)):
        if list[i] == c:
            a = i
            return a

    else:
        a = -1
        return a;

b = Demo(33)
print(b)
