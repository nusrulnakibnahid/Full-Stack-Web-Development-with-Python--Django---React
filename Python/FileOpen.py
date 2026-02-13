
f = open("demofile.txt","r")

print(f.read())


# File Write 

newFile = open("index.html", "a")

newFile.write("<h1> Hello World </h1>")

print(newFile.read())




# Delete File

import os
os.remove("index.html")

# create a folder then delete it
os.mkdir("myfolder")
os.rmdir("myfolder")
