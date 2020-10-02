def get_num_case():
    while True:
        #n is the number of test cases
        #T must be a positive interger
        n = int(input("Number of test case: "))
        if n > 0:
            break
    return n

def get_array(n, i):
    while True:
        arr = list(map(int,input("The array of numbers in case %d: "%(i+1)).split()))
        if len(arr) == n:
            break
    return arr

#prompt the number of cases from user
T = get_num_case()

#for the number of test cases, the program will re-run until it ran all the cases
for i in range(T):
    #get 2 input from user
    #n is the length of list, s is the sum we need to search
    #turn the 2 input into int by map(int, input().split()) 
    n = int(input("Length of array in case %d is: "%(i+1)))
    s = int(input("The subarray sum in case %d is: "%(i+1)))

    #get the array from user and change into int and put it in the list
    arr = get_array(n, i)

    #boolean to print if no subarray found
    subarray_found = False

    #iterate through the array
    for i in range(n):
        #for eg, [1,2,3,4,5]
        #we set the sum to arr[i], the fist sum is 1
        curr_sum = arr[i]

        #we need the second loop to iterate from (i+1) 
        # to the end of loop to find the sum
        j = i + 1
        #then we add the sum with the rest of array
        while j < n:
            curr_sum += arr[j]

            #if we find the location matches the sum, break and print
            if curr_sum == s:
                #because loops count from 0, so for human counting we add 1
                print("Sum of elements from %dnd position to %dth position is %d"%(i+1, j+1, curr_sum))
                subarray_found = True
                break
            j += 1
    if subarray_found == False:
        print("No subarray found")
