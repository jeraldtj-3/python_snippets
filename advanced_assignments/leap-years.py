# finding the second largest number in an array 
def second_max(arr_):
    max_ = max(arr_) 
    arr_.remove(max_) 
    second_max = max(arr_)
    return second_max 

# checking whether a given ip is valid or not 
def check_ip(ip):
    test = []
    nums = range(0,255) 
    list_ip = ip.split('.')
    if len(list_ip)!=4:
        test.append(False)
    for i in list_ip:
        try:
            if len(i)>3:
                test.append(False) 
            for j in i:
                if int(j) not in nums:
                    test.append(False)
        except:
            test.append(False)
    if False in test:
        return False 
    else:
        return True

# checking whether an year is leap year or not 
def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%400 ==0: 
        leap = True 
    if year%100 !=0 and year%4 ==0:  
        leap = True
    return leap
