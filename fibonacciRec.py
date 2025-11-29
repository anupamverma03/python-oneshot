def fibo(n):
    if(n == 1 ):
        return 1
    if(n == 0):
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

n = int(input("Enter a num: "))
print(fibo(n))
    
    