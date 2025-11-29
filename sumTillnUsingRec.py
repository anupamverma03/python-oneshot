def sum_tilln(num):
    if(num == 0):
        return 0
    return sum_tilln(num-1) + num
n = int(input("Enter a num: "))
sum = sum_tilln(n)
print(sum)
