with open(r"C:\VS Code\.vscode\python oneshot\example1.txt", "r+") as f:
    data = f.read()
    new_data = data.replace("python", "java")
    print(new_data)
    f.seek(0) # move cursor to starting after reading file
    f.write(new_data) # write new data
    f.truncate() # truncate any leftover data
    f.seek(0) # move cursor to start
    data = f.read()
    print(data)

    if(new_data.find("learning") != -1): # check if a substring exists in the text
        print("found")
    else:
        print("not found")

    def check_for_line(): # check for line no of a substring
        word = "learning"
        data1 = True
        line_no = 1
        with open(r"C:\VS Code\.vscode\python oneshot\example1.txt", "r") as f:
            while data:
                data1 = f.readline()
                if(word in data1):
                    print(line_no)
                    return
                line_no += 1
        return -1

    check_for_line()