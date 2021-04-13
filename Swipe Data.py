fileA_read = "C:/Dhruv/projects/fileA.txt"
fileB_write= "C:/Dhruv/projects/fileB.txt"
fileB_read= "C:/Dhruv/projects/fileB.txt"
fileA_write = "C:/Dhruv/projects/fileA.txt"



fileA = open(fileA_read, "r")
dataA = fileA.read()
fileA.close()

fileB = open(fileB_read, "r")
dataB = fileB.read()
fileB.close()

with open(fileB_write,"w") as file:
    file.write(dataA)
print("completed")

with open(fileA_write,"w") as file:
    file.write(dataB)
print("completed")



