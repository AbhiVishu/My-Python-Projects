def matched(s):

    count = 0
    a = False 

    for i in range(len(s)):
        if (inpStr[i] == '('):
            count = count + 1
        elif (inpStr[i] == ')' and count == 0):
            count = -1
            break
        elif (inpStr[i] == ')' and count != 0):
            count = count - 1
    if (count == 0):
        return True
    else:
        return False
            
inpStr = input()
ans = matched(inpStr)
print(ans)


        