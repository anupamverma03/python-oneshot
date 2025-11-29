with open(r"C:\VS Code\.vscode\python oneshot\nums.txt", "r") as f:
    count = 0
    data = f.read()

    #by using loops for getting nums as int

    # print(data)
    # nums = ""
    # for i in range(len(data)):
    #     if(data[i] == "," or data[i] == "\n"): # separates nums based on comma  and \n char
    #         if(nums.strip()):
    #             print(int(nums)) # misses the last integer in text file
    #             if(int(nums)%2 == 0):
    #                 count += 1
    #         nums = ""
    #     else:
    #         nums += data[i]
    # print(count)

    # by using a list of nums by split function

    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1
    print(count)