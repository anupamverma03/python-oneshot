def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)
cities = ["Mumbai", "Ahemdabad", "Indore", "Bhopal", "Nagpur", "Hyderabad"]
idx = int(input("Enter a number: "))
print_list(cities, idx)