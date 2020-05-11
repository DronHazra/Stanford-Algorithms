def partition(a, l, r, p):
    pivot = a[p]
    i = l+1
    a[l], a[p] = a[p], a[l]
    
    for j in range(l+1, r+1):
        if a[j] < pivot:
            a[j], a[i] = a[i], a[j]
            i += 1
    
    a[l], a[i-1] = a[i-1], a[l]
    return i - 1

def merge(list_a, list_b):
    output = []
    i = 0
    j = 0
    for k in range(len(list_a) + len(list_b)):
        if i > len(list_a) - 1:
            output.append(list_b[j])
            j += 1
        elif j > len(list_b) - 1:
            output.append(list_a[i])
            i += 1
        elif list_a[i] < list_b[j]:
            output.append(list_a[i])
            i += 1
        else:
            output.append(list_b[j])
            j+= 1
    return output


def merge_sort(INPUT_LIST):
    n = len(INPUT_LIST)
    if len(INPUT_LIST) == 1:
        return INPUT_LIST
    else:
        list_a = INPUT_LIST[:round(n/2)]
        list_b = INPUT_LIST[round(n/2):]
        a = merge_sort(list_a)
        b = merge_sort(list_b)
        return merge(a, b)

def dselect(a, i):
    n = len(a)
    #Divide input list a into groups of 5, sort each, and find the median
    if n == 1:
        return a[0]
    c = []
    for k in range(n // 5):
        c.append(merge_sort(a[k*5:((k + 1)*5)])[2])
    #Get any remaining groups
    if n % 5 != 0:
        c.append(merge_sort(a[-(n % 5):])[(n % 5) // 2])
    
    p = dselect(c, len(c) // 2)
    j = partition(a, 0, len(a) - 1, a.index(p))
    if j == i:
        return a[j]
    if j > i:
        return dselect(a[:j], i)
    if j < i:
        return dselect(a[j+1:], i-j)

print(dselect([0, 1, 2, 3, 1, 7, 10, 9], 2))