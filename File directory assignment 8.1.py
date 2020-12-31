import os

def getInput(): #function to get input from user
    global dir_name, file_name, user_name, phone_num, address
    dir_name = input("\nPlease enter the file directory: ")
    if dir_name[-1]== "?": #if file directory name contains punctuation symbols, print mssg:
        print("Directory name may not contain special characters. Please enter file directory with no punctuation symbols.")
        getInput()
    else:
        file_name = input("Enter file name: ")
        user_name = input("Enter user name: ")
        phone_num = input("Enter phone number: ")
        address = input("Enter address: ")

def dirCheck(): #function to validate directory
    checkDir = os.path.isdir(dir_name)
    print("\nChecking program log.")
    if checkDir == True: #if directory is found, print
        print("Directory validated successfully.")
        createFile()
    elif checkDir == False: #if directory is not found, create directory and file
        createDir()
        createFile()
    else: #if any other input print
        print("Error")


def createDir(): #function to create directory
    os.mkdir(dir_name)
    ("Directory successfully created.")

def createFile(): #function to create file and write data to file 
    os.chdir(dir_name)
    info = user_name + ", " + phone_num + ", " + address 
    file = open(file_name, "w")
    file.write(info)
    file.close()
    print("File sucessfully created.")

def fileRead(): #function to display file content
    file = open(file_name, "r")
    print("\nFile path: " + dir_name + "/" + file_name)
    print(file_name + "contents:\n")  #prints file contents

    for line in file:
        print(line, end='')
    file.close() 

def Run(): #function to run program as whole
    getInput()
    dirCheck()
    fileRead()

Run() #runs program


