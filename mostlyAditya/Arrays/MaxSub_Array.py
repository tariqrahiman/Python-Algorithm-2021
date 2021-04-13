# Calculate the maximum sum of a subarray of partcular size in the array.
def max_subarray(arr,w_size):
    max_ans=-999
    k=len(arr)
    sum_size=0
    i=0
    j=0
    while j<k:
        
        sum_size+=arr[j]
        if j>=w_size-1:
            max_ans=max(sum_size,max_ans)  
            sum_size-=arr[i]
            i+=1
            
        j+=1
   
    return max_ans

arr=[1, 4, 2, 10, 2, 3, 1, 0, 20]
w_size=3
print(max_subarray(arr,w_size))
