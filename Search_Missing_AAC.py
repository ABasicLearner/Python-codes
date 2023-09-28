# a = [1, 2, 3, 5, 6, 7, 8]
# n = len(a)
# lb = 0
# ub = n-1
# while lb + 1 < ub:
#     mid = (ub + lb) // 2
#     if a[lb] - lb != a[mid] - mid:
#         ub = mid
#     elif a[ub] - ub != a[mid] - mid:
#         lb = mid
#     print(a[lb] + 1)

def SearchMissing(a, n):
    if a[0] != 1:
        return 1
    if a[n-1] != n:
        return n
    lb = 0
    ub = n
    while ub > lb:
        mid = (lb + ub) // 2
        if a[lb] - lb != a[mid] - mid:
            ub = mid
        elif a[ub] - ub != a[mid] - mid:
            lb = mid 
    return a[mid] + 1

a = [1, 2, 4, 5, 6, 7, 8, 9]
print(SearchMissing(a, len(a)))



    