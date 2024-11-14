import navigation as nav
import sorting as sort

def showDirectory(path):
    listDir = nav.listFiles(path)
    if listDir != None:
        if not listDir:
            print(f"{path}\nThis folder is empty")
            return True
        else:
            print(f"Files and direcories in {path}:")
            print(listDir)
            print()
            return True
    else:
        return None
    
def sortSingleFile(path):
    print("Select a file to sort:")
    files = sort.findFiles(path)
    i = 0
    for f in files:
        print(f'Press "{i}" to sort {f}')
        i += 1
    selectedFile = int(input("\nEnter a number... "))
    if selectedFile >= 0 and selectedFile < len(files):
        sort.moveFile(files[selectedFile])
    else:
        print("Please type a valid number")

def main():
    defaultPath = nav.currentDir()
    currentPath = defaultPath

    print("\nWelcome to the file sorter")
    print("type 'cd' followed by the folder name to enter a folder")
    print("type 'b' to go back one folder")
    print("Type '1' to sort every file in this folder")
    print("Type '2' select a file to sort")
    print("Type '3' to list files in this folder")
    print("Type '9' to exit\n")

    run = True
    while run == True:
        #Checks that the directory is valid. If not, it navigates to the parent directory
        if showDirectory(currentPath) == None:
            currentPath = nav.navigateBackward(currentPath)
            showDirectory(currentPath)

        selection = input("Type.. ")

        if selection[:2] == "cd" or selection[:2] == "CD":
            currentPath = nav.navigateForward(currentPath,selection)

        elif selection == "b" or selection == "B":
            currentPath = nav.navigateBackward(currentPath)
        
        elif selection == "1":
            files = sort.findFiles(currentPath)
            sort.moveFiles(files)

        elif selection == "2":
            sortSingleFile(currentPath)

        elif selection == "3":
            print(f"Files in {currentPath}:")
            for f in sort.findFiles(currentPath):
                print(f.rpartition(f'\\')[2])
            print()
        
        elif selection == "9":
            run = False

        else:
            print("Please enter a valid input")

main()