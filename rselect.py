from random import randint

def partition(a, l, r):
    p = randint(l, r)
    pivot = a[p]
    i = l+1
    a[l], a[p] = a[p], a[l]
    
    for j in range(l+1, r+1):
        if a[j] < pivot:
            a[j], a[i] = a[i], a[j]
            i += 1
    
    a[l], a[i-1] = a[i-1], a[l]
    return i - 1

def rselect(a, l, r, i):
    if l < r:
        pivot = partition(a, l, r)
        if pivot == i:
            return a[pivot]
        elif pivot > i:
            return rselect(a, l, pivot - 1, i)
        else:
            return rselect(a, pivot + 1, r, i)
    else:
        return a[r]

test = [0, 1, -1, 5]
print(test)
result = rselect(test, 0, len(test) - 1, 2)
print(result)