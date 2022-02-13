import os

fpath = input("Enter the directory the file is in... ")

if "C:/" not in fpath:
    print("invalid directory. File must be in C:/")

if "C:/" in fpath:
    os.system("cd " + fpath)
    name = input("Enter file name...")
    newname = input("Enter new file name...")
    os.system("ren " + name + " " + newname)
    print("file renamed")

