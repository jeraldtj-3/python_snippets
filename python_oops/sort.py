

class ArraySort():
    def __init__(self,input_array):
        self.input_array = input_array 

    # insertion sort function 
    def insertionSort(self):
        # Traverse through 1 to len(arr)
        for i in range(1, len(self.input_array)):    
            key = self.input_array[i]
            j = i-1
            while j >= 0 and key < self.input_array[j] :
                    self.input_array[j + 1] = self.input_array[j]
                    j -= 1
            self.input_array[j + 1] = key
        return self.input_array 
    
    # merge sort 
    def mergeSort(array):
        if len(array) > 1:

            #  r is the point where the array is divided into two subarrays
            r = len(array)//2
            L = array[:r]
            M = array[r:]

            # Sort the two halves
            L = mergeSort(L)
            M = mergeSort(M)

            i = j = k = 0

            # Until we reach either end of either L or M, pick larger among
            # elements L and M and place them in the correct position at A[p..r]
            while i < len(L) and j < len(M):
                if L[i] < M[j]:
                    array[k] = L[i]
                    i += 1
                else:
                    array[k] = M[j]
                    j += 1
                k += 1

            # When we run out of elements in either L or M,
            # pick up the remaining elements and put in A[p..r]
            while i < len(L):
                array[k] = L[i]
                i += 1
                k += 1

            while j < len(M):
                array[k] = M[j]
                j += 1
                k += 1
        return array
        

    def __main__(self, sort_method):
        if sort_method == 'insertion_sort':
            return self.insertion_sort(self.input_array) 
        elif sort_method == 'merge_sort':
            return self.merge_sort(self.input_array) 
        else:
            return "sort method parameter error" 



test = [234,215,353,3,58,3,-4,4,-2,0,2]
sortclass = ArraySort(test)
output = sortclass.insertionSort() 
print(output) 