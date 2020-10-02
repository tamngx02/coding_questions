def find_subarray(arr, n, sum): 
      
    # Initialize curr_sum as 
    # value of first element 
    # and starting point as 0  
    curr_sum = arr[0] 
    start = 0
  
    # Add elements one by  
    # one to curr_sum and  
    # if the curr_sum exceeds  
    # the sum, then remove  
    # starting element  
    i = 1
    while i <= n: 
          
        # If curr_sum exceeds 
        # the sum, then remove 
        # the starting elements 
        while curr_sum > sum and start < i-1: 
          
            curr_sum = curr_sum - arr[start] 
            start += 1
              
        # If curr_sum becomes 
        # equal to sum, then 
        # return true 
        if curr_sum == sum: 
            print(str(start+1) + " " + str(i))
            return 1
  
        # Add this element  
        # to curr_sum 
        if i < n: 
            curr_sum = curr_sum + arr[i] 
        i += 1
  
    # If we reach here,  
    # then no subarray 
    print ("-1") 
    return 0

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, s = list(map(int, input().split()))
        arr = [int(x) for x in input().split()]
        find_subarray(arr, n, s)

