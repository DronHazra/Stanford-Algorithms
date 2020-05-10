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
    

def quick_sort(a, l, r):
    if l < r:
        pivot = partition(a, l, r)
        quick_sort(a, l, pivot - 1)
        quick_sort(a, pivot + 1, r)

test = [0, 1, 4, 12, 14, 156, 12, 1, 0]
print(test)
quick_sort(test, 0, len(test) - 1)
print(test)