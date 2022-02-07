

from readline import insert_text


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
    def mergeSort(self):
        pass

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
output2 = sortclass.__main__(sort_method='insertion_sort') 
print(output2) 
