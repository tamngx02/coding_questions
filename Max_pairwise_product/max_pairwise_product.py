# python3
import random

def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product

def max_pairwise_product_fast(numbers):
    n = len(numbers)

    max_index1 = -1
    for i in range(n):
        if (max_index1 == -1) or (numbers[i] > numbers[max_index1]):
            max_index1 = i

    max_index2 = -1
    for j in range(n):
        if ((j != max_index1) and ((max_index2 == -1) or (numbers[j] > numbers[max_index2]))):
            max_index2 = j
    
    return numbers[max_index1] * numbers[max_index2]

if __name__ == '__main__':
    ''' Stress Test Begin
    while True:
        n = random.randint(2, 1002)
        print(n)
        a = []
        for i in range(n):
            a.append(random.randint(0, 10000))
        for i in range(n):
            print(a[i],end=" ")
        print()
        res1 = max_pairwise_product(a)
        res2 = max_pairwise_product_fast(a)
        if res1 != res2:
            print("Wrong answer " + str(res1) + " " + str(res2))
            break
        else:
            print("OK") '''

    input_n = int(input())
    input_array = input().split()
    if input_n != len(input_array):
        print("There must be %d numbers"%(input_n))
    else:
        input_numbers = [int(x) for x in input_array]
        print(max_pairwise_product_fast(input_numbers))

    
