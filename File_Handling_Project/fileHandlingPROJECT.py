from pathlib import Path
import os

def readfileandfolder():
    path = Path('')
    items = list(path.rglob('*'))

    for i,items in enumerate(items):
        print(f" {i+1} : {items} ")


def createfile():
    try:
        readfileandfolder()
        name = input("Enter your File Name : ")
        p = Path(name)
        if not p.exists():# and p.is_file():
            with open(p,"w") as fs:
            
             data = input("what do you want to write in this file :- ")
             fs.write(data)
            print(F"FILE CREATED SUCCESSFULLY ")
        else:
            print("This File already Exists ")

    except Exception as err:
        print(f"An Error Occured as {err}")

def readfile():
   try:
    readfileandfolder()
    name= input("which file you want to read :- ")
    p= Path(name)
    if p.exists() and p.is_file():
        with open(p,'r') as fs:
            data = fs.read()
            print(data)
        
            print(" Readed Successfully ")
    else:
        print("The File does not exist ")
   
   except Exception as err:
      print(f"An Error Occured as {err}")

def updatefile():
   try:
    readfileandfolder()
    name= input("which file you want to update :- ")
    p= Path(name)
    if p.exists() and p.is_file():
        print("press 1 for changing the name for your file")
        print("pess 2 for overwriting the data of your file")
        print("press 3 for appending some data in your file ")

        res= int (input(" tell your response : "))
        if res==1:
            name2 = input("tell your new file name : ")
            p2= Path(name2)
            p.rename(p2)
        if res==2:
            with open(p,'w') as fs:
                data=input("what you want to write , this will overwrite the data : ")
                fs.write(data)
        if res==3:
            with open(p,'a') as fs:
                data=input("what you want to append : ")
                fs.write(" " +data)
         
   except Exception as err:
      print(f" An Error Occured as { err }")
      
def deletefile():
   try:
    readfileandfolder()
    name=input("which file you want to delete :- ")
    p=Path(name)
    if p.exists() and p.is_file():
        os.remove(p)
        print("File removes Successfully ")
    else:
        print("No such file exists")
   except Exception as err:
      print(f"An Error Occured as {err}")

print("Press 1 for Creating a File")
print("Press 2 for Reading a File")
print("Press 3 for Updating a File")
print("Press 4 for Deleting a File")

check=int(input("Enter your response : "))
if check ==1:
    createfile()

if check == 2:
   readfile()

if check == 3:
   updatefile()

if check == 4:
   deletefile()
