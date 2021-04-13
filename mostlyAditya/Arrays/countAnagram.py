def countAnagram(arr,pattern):
    windowSize = len(pattern)

    newDict=dict()
    count=0
    for i in pattern:

        if i in newDict:
            newDict[i]+=1
        else:
            newDict[i] = 1
    print(newDict)
    distinctLetters = len(newDict)
    i=0
    j=0
    for j in range(0,len(arr)):
        if arr[j] in newDict:
            newDict[arr[j]]-=1
            if newDict[arr[j]]==0:
                distinctLetters-=1
        
        if j-i+1==windowSize:
            if distinctLetters==0:
                count+=1
            if arr[i] in newDict:
                if newDict[arr[i]]==0:
                    distinctLetters+=1
                    newDict[arr[i]]+=1
            i+=1
        j+=1
    return count

pattern='aaba'
text='aabaabaa'
print(countAnagram(text,pattern))