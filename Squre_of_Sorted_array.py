# Squre of Sorted array

def Sortedsquares(arr):

    size = len(arr)
    neg = []
    pos = []

    # Separate negative & positive numbers from the array & add this into neg & pos array respectively

    for i in arr:
        if i < 0:
            neg.append(i)
        else:
            pos.append(i)

    # Case 1 : If no -ve numbers in array (all +ve)

    if len(neg) == 0:
            return [x * x for x in pos]
            
    # Case 2 : If no +ve numbers in array (all -ve)

    if len(pos) == 0:
        return [x * x for x in neg][::-1]
        
    # Case 3: If both -ve and +ve numbers exists

    neg = [x*x for x in neg][::-1]
    pos = [x*x for x in pos]
    n = len(neg)
    m = len(pos)
    res = []

    # Take two pointers i & j, initially pointed at 0

    i=j=0

    while (i < n and j < m):

        if neg[i] < pos[j]:
            res.append(neg[i])
            i += 1
        else:
            res.append(pos[j])
            j += 1

    while i < n:
        res.append(neg[i])
        i += 1
    while j < m:
        res.append(pos[j])
        j += 1

    return res


arr = [-4, -1, 0, 3, 10]
print(Sortedsquares(arr))   # Expected: [0, 1, 9, 16, 100]

arr2 = [-7, -3, -1]
print(Sortedsquares(arr2))  # Expected: [1, 9, 49]

arr3 = [1, 2, 5]
print(Sortedsquares(arr3))  # Expected: [1, 4, 25]
