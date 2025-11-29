f = open(r"C:\VS Code\.vscode\python oneshot\demo.txt", "r")
data = f.read() # reads entire data 
print(data)
print(type(data)) # pointer in the file is at the end

line1 = f.readline() # prints enpmty space because dur to read() command 
                     # it shifts cursor to the end
print(line1)

f.close()

f = open(r"C:\VS Code\.vscode\python oneshot\demo.txt", "r+")
f.write("Hola") # moves cursor to the end
f.seek(0) # moves cursor to the begining
data = f.read()
print(data)
f.close()