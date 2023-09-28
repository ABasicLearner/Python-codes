def firstNonDuplicateLetter(a):
    n = []
    for i in range(len(a)):
        flag = 0
        if a[i] == a[-1]:
            flag = 1
        for j in range(i+1, len(a)):
            if a[i]==a[j]:
                flag = 1
                n.append(a[i])
            elif a[i] in n:
                flag = 1
        if flag == 0:
            return i+1
    return -1

a = 'statistics'
b = 'hackthegame'
c = 'aaa'
d = 'abcd'
e = 'aabcd'
f = 'aaaabcbdc'

print(firstNonDuplicateLetter(a))
print(firstNonDuplicateLetter(b))
print(firstNonDuplicateLetter(c))
print(firstNonDuplicateLetter(d))
print(firstNonDuplicateLetter(e))
print(firstNonDuplicateLetter(f))
