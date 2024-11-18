import os
import sys
from fileHandling import readFileTypes
from logg import defaultLogger

#Declares the path the files will be sorted into
parentDirectory = sys.path[0].rpartition("\\")[0] + "\\Sorted_Files"

@defaultLogger
def createNewDirectory(path):
    try:
        os.mkdir(path)
        folder = path.rpartition("\\")[2]
        #print(f"Directory {path} created successfully")
        result = f'Directory "{folder}" created successfully'
    except FileExistsError:
        #print(f"Directory {path} already exists")
        result = f"Directory {path} already exists"
    except PermissionError:
        #print(f"Permission denied: Unable to create {path}")
        result = f"Permission denied: Unable to create {path}"
    except Exception as e:
        #print(f"An error occurred: {e}")
        result = f"An error occurred: {e}"
    print(result)
    return result

def fetchFileName(fileType):
    fileTypes = readFileTypes()
    if fileTypes != None:
        for f in fileTypes:
            if f[0] == fileType:
                return parentDirectory + f"\\{f[1]}"
    return parentDirectory + f"\\{fileType}"
    
def assignDirectory(fileType):
    path = fetchFileName(fileType)
    if os.path.isdir(path) == False:
        createNewDirectory(path)
    return path

@defaultLogger
def moveFile(filePath):
    #Checks that the user isn't trying to sort the program files
    if filePath.rpartition("\\")[0] != sys.path[0] and filePath != sys.path[0].rpartition("\\")[0] and filePath != sys.path[0].rpartition("\\")[0] + "\\Sorted_Files":

        fileType = filePath.rpartition(".")[2] #Finds the file extension
        fileName = filePath.rpartition("\\")[2] #Finds the file name
        newFilePath = assignDirectory(fileType) + f"\\{fileName}" #Creates the new path the file will be moved to
        
        try: 
            os.replace(filePath, newFilePath)
            #print(f"File {fileName} moved successfully to {newFilePath}\n")
            result = f'File "{fileName}" moved successfully to "{newFilePath}"\n'
        except FileExistsError:
            #print(f"File {fileName} already exists")
            result = f"File {fileName} already exists"
        except PermissionError:
            #print(f"Permission denied could not move file: {fileName}")
            result = f"Permission denied could not move file: {fileName}"
        except FileNotFoundError:
            #print(f"Could not find file: {fileName}")
            result = f"Could not find file: {fileName}"
        except Exception as e:
            #print(f"An error occurred: {e}")
            result = f"An error occurred: {e}"
        print(result)
        return result
    else:
        print("Dude, dont sort the programfiles\n")
        return


def findFiles(path):
    os.chdir(path) #Changes the working directory to the directory the user selected
    files = []
    for f in os.listdir(path):
        if os.path.isfile(f):
            files.append(os.path.join(path,f))
    return files

def moveFiles(files):
    for i in files:
        moveFile(i)

if os.path.isdir(parentDirectory) == False:
    createNewDirectory(parentDirectory)