
"""
for i in range(len(a)):
    for j in range(i+1, len(a)):
        for k in range(j+1, len(a)):
            if a[i]+a[j]+a[k] == num:
                print(a[i], a[j], a[k])
"""

def Triplet_sum(a, num):
    for i in range(len(a)-2):
        l = i+1
        r = len(a)-1
        while l < r:
            sum = a[i] + a[l] + a[r]
            if sum == num:
                print(a[i], ',', a[l], ',', a[r])
            if sum > num:
                r = r - 1
            else:
                l = l + 1

a = [1, 5, 7, 8, 2, 3, 4, 9, 6]
num = 15
a = sorted(a)
print(a)
print(Triplet_sum(a, num))
    