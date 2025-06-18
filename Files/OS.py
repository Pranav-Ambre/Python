import os

a=os.listdir("Files/dir")
print(a)
print(os.getcwd())
print(os.path.exists("Files/dir"))
os.remove("Files/sample.txt")
os.rmdir("Files/xxx")