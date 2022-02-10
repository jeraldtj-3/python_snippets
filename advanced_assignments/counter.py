# creating a new dataype mylist which is a child class of list data type ( has all the funtionalities of list) 
class mylist(list):
    
    # this function will give the count of each unique element in a list 
    def counter(self):
        counts = dict.fromkeys(set(self))
        for key in counts:
            count = 0 
            for value in self:
                if key==value:
                    count+=1
            counts[key] = count 
        return counts 
    
    # top unique elements in the list which has high count
    # n is the parameter ( represents how many top ) 
    def most_common(self,n):
        output = []
        values = [] 
        counts = self.counter() 
        for i in counts.items():
            values.append(i[1])
            values.sort()
            values = values[::-1] 
        for i in counts.items():
            if i[1] in values[:n]:
                output.append((i[0],i[1]))
        return output

l = mylist(['thomaskutty', 'reethu','thomaskutty','reethu','thomaskutty','tony','maria','reethu','maria','reethu'])
print(l.counter())
print(l.most_common(n = 2))
