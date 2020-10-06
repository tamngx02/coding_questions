# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

def calc_fib_fast(n):
    arr = []
    arr.append(0)
    arr.append(1)
    for i in range(2, n+1):
        arr.append(arr[i-1] + arr[i-2])
    
    print(arr)
    print("The length of %dth Fibonnaci is "%(n) + str(len(str(arr[-1]))))
    return arr[-1]

if __name__ == '__main__':
    n = int(input())
    print(calc_fib_fast(n))
