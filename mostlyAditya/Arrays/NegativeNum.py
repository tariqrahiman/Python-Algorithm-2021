#The Sliding Window Solution
#Finding the first negative number in a subarray 
#and printing it or printing 0 instead if none found
def negativeNum(arr,windowSize):
    k=len(arr)
    j=0
    i=0
    negativeList=[]
    answerList=[]
    for j in range(0,k):
        if arr[j]<0:
            negativeList.append(arr[j])

        if j-i+1==windowSize:
            if len(negativeList)==0:
                answerList.append(0)
                
            else:
                answerList.append(negativeList[0])
                if arr[i]==negativeList[0]:
                    negativeLsist.pop(0)
            i+=1
        
    return answerList


arr=[12, -1, -7, 8, -15, 30, 16, 28]
windowSize=3
print(negativeNum(arr,windowSize))

'''
#Brute Force Solution
def negativeNum(arr,windowSize):
    k = len(arr)
    j=0
    for i in range(0,k-windowSize+1):
        j=i
        while j<windowSize+i:
            if arr[j]<0:
                print(arr[j])
                
                break
            j+=1
        if j==windowSize+i:
            print(0)

arr=[-8, 2, 3, -6, 10]
windowSize=2

negativeNum(arr,windowSize)'''