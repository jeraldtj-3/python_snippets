
def insertion_sort(array):
    for curr_index in range(len(array)):
        current_value = array[curr_index]

        # previous pointer
        prev_index = curr_index-1
        while prev_index>=0 and current_value<array[prev_index]:
            array[prev_index+1] = array[prev_index]
            prev_index-=1
        array[prev_index+1] = current_value
    return array


