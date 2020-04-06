import os

#File Handling

#Open a file

#open() function
path = "/Users/bobit/Desktop/pythonFiles/demo.txt"

#demo = open(path)
#print(demo.read())

#demo = open(path, "r")
#print(demo.read(5))

#readline()
#print(demo.readline())
#print(demo.readline())

#readlines
#print(demo.readlines())

#Loop concept

'''
demo = open(path, "r")
for x in demo:
    print(x)

'''

# close()
'''
demo = open(path, "r")
print(demo.read())
demo.close()

'''
path2 = "/Users/bobit/Desktop/pythonFiles/demo2.txt"

#append "a"
# write "w"
'''
demo2 = open(path, "a")
demo2.write("\nThis is new line in my file...!")
demo2.close()

#Open and read the file after appending
demo2 = open(path, "r")
print(demo2.read())
'''

#Delete file
#os.remove(path2)

''' 
if os.path.exists(path2):
    os.remove()
else:
    print("The file does not exist")

'''
#os.remove(path)
os.rmdir("/Users/bobit/Desktop/pythonFiles")