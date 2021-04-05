class Item:
    #Takes the weght, value of the object. ind represents at which index the object is present 
    def __init__(self,wt,value,ind): 
        self.wt = wt
        self.value = value
        self.ind=ind
        self.ratio=value//wt
    def __lt__(self, other):
        '''
        __lt__ function allows us to sort based on certain criteria
        This compares the ratio of one object to another object
        '''
        return self.ratio < other.ratio
    
class Knapsack:
    @staticmethod
    def getMaxValue(wt,val,capacity):
        """
        This is a static method because it doesn't need any object arguement.
        """
        arr=[]
        for i in range(len(wt)):
            #Inserted objects in the array
            arr.append(Item(wt[i],val[i],i))
        #This sorts the object based on the condition of __lt__ menthod
        arr.sort(reverse=True) 
        
        totalValue=0
        for i in arr:
            curWeight=i.wt
            curVal=i.value
            if capacity >= curWeight:
                capacity -= curWeight
                totalValue+=curVal
            else:
                #Creating objectFrac for the last remaining object which needs to be added
                objectFrac=capacity/curWeight
                totalValue += objectFrac*curVal
                capacity = capacity-(objectFrac*curWeight)
                break
        return totalValue
    



wt = [10, 40, 20, 30]
val = [60, 40, 100, 120]
capacity = 50
maxValue = Knapsack.getMaxValue(wt, val, capacity)
print("Maximum value in Knapsack =", maxValue)       


    
    
