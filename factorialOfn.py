n = int(input("Enter a num: "))
prod = 1
for i in range(n, 1, -1):
    prod *= i
print(prod)