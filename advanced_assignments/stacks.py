# implementing stacks

class Stack:
    def __init__(self):
        self.items = [] 
    def is_empty(self):
        return self.items == [] 
    def push(self,item):
        self.items.append(item)  # append has o(1) 
    def pop(self):
        return self.items.pop()  # pop() has o(1)
    def peek(self):
        return self.items[len(self.items)-1] 
    def size (self):
        return len(self.items) 

# reversing string using stack 
def reverse_str(inpt_str):
    output_string = Stack() 
    for i in inpt_str:
        output_string.push(i) 

    final_string = ''
    for j in range(output_string.size()):
        final_string+= output_string.pop()
    print(final_string) 

# reversing the pop() and pushing operation 
# pop() will remove the first element 
# push() element will insert element at the first (beginning) position

class StackReverse:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items ==[] 
    def push(self,item):
        self.items.insert(0,item) 
    def pop(self):
        return self.items.pop(0) # pop(0) will remove the first item in the stack 
    def peek(self):
        return self.items[0] # peek() will return the first item 
    def size(self):
        return len(self.items) 
    
# implementing parenthesis checker function using stacks 
def par_checker(symbol_string):
    s = Stack()
    balanced = True 
    index = 0 
    while index<len(symbol_string) and balanced:
        symbol = symbol_string[index] 
        if symbol == "(":
            # adding the opening parenthesis to the stack 
            s.push(symbol)
        else:
            # if the stack is empty and we get a closing parenthesis then not balanced 
            if s.is_empty():
                balanced = False 
            else:
                # if the symbol is not opening parenthesis then pop() it from the stack if stack is not empty 
                s.pop() 
        index+=1 
    if balanced and s.is_empty():
        return True 
    else:
        return False 
    
        
# generalizing parenthesis checker using stacks 

def matches(open,close):
    opens = "([{"
    closes = ")]}"
    return opens.index(open) == closes.index(close) 


# creating a generalized parenthesis checker for "(),{},[]" 

def par_checker_gen(symbol_string):
    s = Stack() 
    balanced = True 
    index = 0 
    while index <len(symbol_string) and balanced:
        symbol = symbol_string[index] 
        if symbol in "([{":
            s.push(symbol) 
        else:
            if s.is_empty():
                balanced = False 
            else:
                # taking the opening bracket 
                top = s.pop() 
                # compare it with the first closing bracket 
                if not matches(top,symbol):
                    balanced = False 
        index+=1 
    if balanced and s.is_empty():
        return True 
    else:
        return False 


# has 2log(n) complexity 
def divide_by_2(dec_number):
    rem_stack = Stack() 
    while dec_number>0:
        rem = dec_number%2
        rem_stack.push(rem) 
        dec_number = dec_number//2 
    bin_string = ''
    while not rem_stack.is_empty():
        bin_string += str(rem_stack.pop())
    return bin_string


# more generalized version of converter wrt base 
def base_converter(dec_number,base):
    digits = '0123456789ABCDEF'
    rem_stack = Stack() 
    
    while dec_number>0:
        rem = dec_number%base 
        rem_stack.push(rem) 
        dec_number = dec_number//base 
        
    new_string = "" 
    while not rem_stack.is_empty():
        new_string+=digits[rem_stack.pop()]
    return new_string 
