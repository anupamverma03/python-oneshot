with open(r"C:\VS Code\.vscode\python oneshot\demo.txt", "r") as f:
    data = f.read()
    print(data)#automatically closes the file

with open(r"C:\VS Code\.vscode\python oneshot\demo.txt", "r+") as f:
    f.write("Hello") # writes new data
    data = f.read() # truncates all data in the file and replaces with new data
    print(data)