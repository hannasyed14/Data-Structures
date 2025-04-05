'''
Hanna Syed, CSC 112, Project 3
'''

KEY = 0              # these are constants for easy reading
VALUE = 1

class HashMap:
    '''     Needs a good docstring here!'''

    def __init__(self, size=1000):
        self.size = size
        self.slots = [None]*size
        self.overflow = []
        slef.overflowCounters = [0] * self.size #Stage 2

    def get(self, key):
        where = self.hashme(key)
        if self.slots[where] == None:
            return None
        else:
            if self.slots[where][KEY] == key:
                return self.slots[where][VALUE]
            else:
                i = self.findInOverflow(key)
                if i == -1:
                    return "NOT FOUND"
                else:
                    return self.overflow[i][VALUE]

    def set(self, key, value):
        where = self.hashme(key)
        if self.slots[where] == None:
            self.slots[where] = [key,value]
        elif self.slots[where][KEY] == key:
            self.slots[where][VALUE] = value
        else:
            i = self.findInOverflow(key)
            if i == -1:
                self.overflow.append([key,value])
                self.overflowCounters[where] += 1  #added line: add 1 to array
            else:
                self.overflow[i][VALUE] = value
                

    def setPlus(self, key, value): #Stage 3
        where = self.hashme(key)
        if self.slots[where] == None:
            self.slots[where] = [key,value]
        elif self.slots[where][KEY] == key:
            self.slots[where][VALUE] += value
        else:
            i = self.findInOverflow(key)
            if i == -1:
                self.overflow.append([key,value])
                self.overflowCounters[where] += 1  #added line: add 1 to array
            else:
                self.overflow[i][VALUE] += value

                
    def delete(self, key): #Stage 3
        n = self.hashme(key)
        if self.slots[n][0] == key or self.slots[n] == None:
            k = self.findInOverflow(key)
            if k != -1 :
                self.slots[n] = self.overflow[k]
                del self.overflow[k]
            else:
                self.slots[n] = None
        else:
            print("Slot is empty")

    
    def deletetwo(self, key): #Extra Credit
        n = self.hashme(key)
        if self.slots[n][0] == key or self.slots[n] == None:
            if self.overflowCounters[n] > 0:
                k = self.findInOverflow(key)
                if k != -1 :
                    self.slots[n] = self.overflow[k]
                    del self.overflow[k]
                    self.overflowCounters[n] -= 1
                else:
                    self.slots[n] = None
            else:
                print("Not found in oveflow")               
        else:
            print("Slot is empty")
                
                
            
        

 # the following method is what they write

    def setAppend(self, key, value):
        where = self.hashme(key)
        if self.slots[where] == None:
            self.slots[where] = [key,str(value)]
        elif self.slots[where][KEY] == key:
            self.slots[where][VALUE] +="," + str( value)
        else:
            i = self.findInOverflow(key)
            if i == -1:
                self.overflow.append([key,str(value)])
            else:
                self.overflow[i][VALUE] += "," + str(value)

    def getKeys(self):
        returnlist = []
        for i in range(0,self.size):
            if self.slots[i] != None:
                returnlist += [self.slots[i][KEY]]
        for element in self.overflow:
            returnlist += [element[KEY]]
        return sorted(returnlist)

 #Stage 1
    def hashme(self,key):
        algo = 3
        if algo == 1: #original
            if len(key) == 0: return 0
            if len(key) == 1:
                return ord(key[0]) % self.size
            return (ord(key[0])+ord(key[1])) % self.size
        elif algo == 2: #adds up ords of all chars
            if len(key) == 0: return 0
            for ch in key: 
                totalord = sum(ord(char))
            return totalord % self.size
        elif algo == 3: #adds up ords *(position + 1) of all chars
            if len(key) == 0: return 0
            totalord = 0
            for n in range(len(key)):
                totalord += (n+1) * ord(key[n])
            return totalord % self.size
        else:
            print("Invalid Choice, 1-3")
           
            

    def findInOverflow(self, key):
        for i in range(0,len(self.overflow)):
            if self.overflow[i][KEY] == key:
                return i
        return -1

    def stats(self):
        numbusy = 0
        for i in range(0,len(self.slots)):
            if self.slots[i] != None:
                 numbusy+=1
            if self.overflowCounters > 0: #added line where overflow counter is greater than 0 
                print(f"Slot {i}: Has {self.overflowCounters[i]} overflows") #prints slot number and overflow count
        print(f"Number of slots that are busy: {numbusy} out of {len(self.slots)} total")
        ratio = numbusy / len(self.slots) * 100
        print(f"This is a ratio of {ratio:.2f}%")
        print(f"There are {len(self.overflow)} overflow slots")
        timeslarger = len(self.overflow) / self.size
        print(f"Overflow is {timeslarger:.2f} times larger than the main slots area")

    def display(self):
        print("size=", self.size)
        print("--------------------main table-------------------------")
        for i in range(0,self.size):
            print(i,"  ",str(self.slots[i]))

        print("\n-----------------overflow---------------------------")
        for i in range(0,len(self.overflow)):
            print(i,"  ",str(self.overflow[i]))
        print("\n")
