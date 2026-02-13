import os
import sys
import navigation as nav
import sorting as sort

#sys.path.insert(0, os.path.abspath(os.path.dirname(__file__))) #path file for installation

#Lists the files and folders in a directory
def showDirectory(path):
    listDir = nav.listFiles(path)
    if listDir != None:
        if not listDir:
            print(f"{path}\nThis folder is empty")
            return True
        else:
            #Removes dotfiles and prints files and folders
            cleanedListDir = []
            for i in listDir:
                if i[0] != '.':
                    cleanedListDir.append(i)
            print(f"Files and direcories in {path}:")
            print(cleanedListDir)
            print()
            return True
    else:
        return None

#Creates a numbered list of files in a directory for selecting a single file to sort  
def sortSingleFile(path):
    files = sort.findFiles(path)
    if not files:
        print("There are no files in this directory")
    else:
        print("Select a file to sort:")
        
        i = 0
        for f in files:
            print(f'Press "{i}" to sort {f}')
            i += 1
        selectedFile = int(input("\nEnter a number... ")) #User selects a file from the list
        if selectedFile >= 0 and selectedFile < len(files):
            sort.startSorting(files[selectedFile]) #The chosen file is passed to the sorting function
        else:
            print("Please type a valid number")

def help():
    print("\ntype 'cd' followed by the folder name to enter a folder")
    print("type 'back' or 'b' to go back one folder")
    print("Type 'show' or 's' to list files and folders in this folder")
    print("Type 'list' or 'l' to list files in this folder")
    print("Type 'pwd' or 'p' see the current directory")
    print("Type 'help' or 'h' to see a list of commands")
    print("Type '1' to sort every file in this folder")
    print("Type '2' select a file to sort")
    print("Type 'quit' or 'q' to exit\n")

#The main menu
def main(): 
    defaultPath = nav.defaultDir() #The default path is set in navigation.py
    currentPath = defaultPath
    print("\n***Welcome to the file sorter***\n")
    help()
    print(f'{currentPath}')

    run = True
    while run == True:
        selection = input("Type.. ") #input from user.

        if selection[:2] == "cd":
            currentPath = nav.navigateForward(currentPath,selection)
            showDirectory(currentPath)

        elif selection == "b" or selection == "back":
            currentPath = nav.navigateBackward(currentPath)
            showDirectory(currentPath)

        elif selection == "s" or selection == "show":
            showDirectory(currentPath)

        elif selection == "l"  or selection == "list":
            print(f"Files in {currentPath}:")
            for f in sort.findFiles(currentPath):
                print(f.rpartition(f'\\')[2])
            print()

        elif selection == "p" or selection == "pwd":
            print(f'{currentPath}')

        elif selection == "h" or selection == "help":
            help()
        
        elif selection == "1":
            files = sort.findFiles(currentPath)
            if not files:
                print("There are no files in this directory")
            else:
                print(f"\nvariable passed from: files\n{files}\n")
                sort.startSorting(currentPath, files)

        elif selection == "2":
            sortSingleFile(currentPath)
        
        elif selection == "q" or selection == "quit":
            run = False

        else:
            print(f'"{selection}" Is not a valid input. Type "help" to see commands\n')

main()