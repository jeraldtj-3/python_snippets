
'''
given two arrays ar1, ar2 : ar1 has sufficient extra
space with 0s in order to be filled and sorted.
'''

def merge_sorted(ar1,ar2):

    j = len(ar2) -1
    i = len(ar1)- len(ar2) -1
    k = (i+j) -1

    while i>=0 and j>=0:
        if ar2[j]>ar1[i]:
            print(ar1)
            ar1[k] = ar2[j]
            ar2.remove(ar2[j])

            j = j-1
            k = k-1
        else:
            print(ar1)
            ar1[k] = ar1[i]
            i = i -1
            k = k-1

    if i == 0:
        ar1[:j] = ar2
    if j == 0:
        ar1[:i] = ar1

    return ar1

