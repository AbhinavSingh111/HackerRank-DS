class HashMap:
    def __init__(self):
        self.MAX=100
        self.arr=[[] for i in range(self.MAX)]
    
    def get_hash(self , key):
        h=0
        for i in key:
            h+=ord(i)
        return h%self.MAX

    def __setitem__(self, key , value):
        h = self.get_hash(key)
        self.arr[h]=value

    def __getitem__(self,key):
        h=self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h=self.get_hash(key)
        self.arr[h]=None



if __name__=="__main__":
    t = HashMap()
    print(t.get_hash('m'))
    t['march 9']=310
    t['march 8']=410
    t['march 7']=510
    t['march 6']=610
    t['march 5']=710
    t['march 4']=810

    t['march 3']=910

    print(t.arr)
    print(t['march 4'])





# chaining and collision handling



class HashMap:
    def __init__(self):
        self.MAX=10
        self.arr=[[] for i in range(self.MAX)]
    
    def get_hash(self , key):
        h=0
        for i in key:
            h+=ord(i)
        return h%self.MAX

    def __setitem__(self, key , val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0] == key:
                self.arr[h][idx] = (key,val)
                found = True
        if not found:
            self.arr[h].append((key,val))

    def __getitem__(self,key):
        h=self.get_hash(key)
        for elements in self.arr[h]:
            if elements[0]==key:
                return elements[1]


    def __delitem__(self, key):
        h=self.get_hash(key)
        for idex , elements in enumerate(self.arr[h]):
            if elements[0]==key:
                del self.arr[h][idex]



if __name__=="__main__":
    t = HashMap()
    print(t.get_hash('m'))
    t['march 9']=310
    t['march 17']=315
    t['march 8']=410
    t['march 7']=510
    t['march 6']=610
    t['march 5']=710
    t['march 4']=810
    t['march 4']=813

    t['march 3']=910

    print(t.arr)
    print(t['march 6'])
    t['march 6']=3550
    print(t['march 6']) 
    del t['march 17']       
    print(t.arr)




# exercise : 1 
# nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
# What was the average temperature in first week of Jan
# What was the maximum temperature in first 10 days of Jan
val = []
with open("nyc_weather.csv","r") as file:
    for line in file:
        tokens = line.split(',')
        try:
            val.append(int(tokens[1]))
        except:
            print("Invalid temperature . Ignore the row")
    print(sum(val[:7])/len(val[:7]))


# exercise : 2 
# nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
# What was the temperature on Jan 9?
# What was the temperature on Jan 4?
val = {}
with open("nyc_weather.csv","r") as file:
    for line in file:
        tokens = line.split(',')
        try:
            val[tokens[0]]=int(tokens[1])
        except:
            print("Invalid temperature . Ignore the row")
    print(val['Jan 9'])
    print(val['Jan 4'])
    
# exercise : 3 
# poem.txt Contains famous poem "Road not taken" by poet Robert Frost. You have to read this file in python and print every word and its count as show below. Think about the best data structure that you can use to solve this problem and figure out why you selected that specific data structure.
import string
val = {}
count=1
with open("poem.txt","r") as file:
    for line in file:
        line = line.strip(string.punctuation)
        line = line.strip('\n')
        for word in line.split(" "):
            word.strip('\n,')
            if word in val:
                val[word]=val[word]+1
            else:
                val[word]=count
    for w , c in val.items():
        print(w,":",c)

# exercise 4 : linear probing

class HashMap:
    def __init__(self):
        self.MAX=10
        self.arr=[[] for i in range(self.MAX)]
    
    def get_hash(self , key):
        h=0
        for i in key:
            h+=ord(i)
        return h%self.MAX

    def __setitem__(self, key , val):
        h = self.get_hash(key)
        if len(self.arr[h])!=0 and self.arr[h][0]==key:
            self.arr[h][1]=val
        elif len(self.arr[h])!=0:
            new_slot = self.get_new_slot(key)
            if new_slot==None:
                print("Hash Map full")
            else:
                self.arr[new_slot].append((key,val))
        else:
            self.arr[h].append((key,val))

    def get_new_slot(self,key):
        for i in range(self.MAX):
            g = (self.get_hash(key)+i)%self.MAX
            if len(self.arr[g])==0:
                break
        if g>10:
            return None
        else:
            return g
        

    def __getitem__(self,key):
        h=self.get_hash(key)
        for elements in self.arr[h]:
            if elements[0]==key:
                return elements
            else:
                for i in range(h+1,self.MAX):
                    if self.arr[i]==key:
                        break
                    elif len(self.arr[i]==0):
                        print("not found")





    def __delitem__(self, key):
        h=self.get_hash(key)
        for idex , elements in enumerate(self.arr[h]):
            if elements[0]==key:
                del self.arr[h][idex]



if __name__=="__main__":
    t = HashMap()
    t["march 6"] = 20
    t["march 17"] =  88
    print(t.arr)
    t["march 17"] = 29
    
    t["nov 1"] = 1
    t["march 33"] = 234
    t["april 1"]=87
    t["april 2"]=123
    t["april 3"]=234234
    t["april 4"]=91
    t["May 22"]=4
    t["May 7"]=47
    t["Jan 1"]=0
    print(t.arr)



class HashTable:  
    def __init__(self):
        self.MAX = 10 # I am keeping size very low to demonstrate linear probing easily but usually the size should be high
        self.arr = [None for i in range(self.MAX)]
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self, key):
        h = self.get_hash(key)
        if self.arr[h] is None:
            return
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            element = self.arr[prob_index]
            if element is None:
                return
            if element[0] == key:
                return element[1]
           
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        if self.arr[h] is None:
            self.arr[h] = (key,val)
        else:
            new_h = self.find_slot(key, h)
            self.arr[new_h] = (key,val)
        print(self.arr)
        
    def get_prob_range(self, index):
        return [*range(index, len(self.arr))] + [*range(0,index)]
    
    def find_slot(self, key, index):
        prob_range = self.get_prob_range(index)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return prob_index
            if self.arr[prob_index][0] == key:
                return prob_index
        raise Exception("Hashmap full")
        
    def __delitem__(self, key):
        h = self.get_hash(key)
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return # item not found so return. You can also throw exception
            if self.arr[prob_index][0] == key:
                self.arr[prob_index]=None
        print(self.arr)
  

if __name__=="__main__":
    t = HashTable()
    t["march 6"] = 20
    t["march 17"] =  88
    t["march 17"] = 29
    t["march 17"] = 29
    t["nov 1"] = 1
    t["march 33"] = 234
    t["march 33"] = 999
    t["april 1"]=87
    t["april 2"]=123
    t["april 3"]=234234
    t["april 4"]=91
    t["May 22"]=4
    t["May 7"]=47

    print(t.arr)
    


