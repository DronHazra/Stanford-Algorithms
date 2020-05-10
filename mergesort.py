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
