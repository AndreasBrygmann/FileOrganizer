import os
import sys
from fileHandling import readFileTypes
from logg import defaultLogger

#Declares the path the files will be sorted into
parentDirectory = sys.path[0].rpartition("\\")[0] + "\\Sorted_Files"

@defaultLogger
def createNewDirectory(path): #Creates a new directory
    try:
        os.mkdir(path)
        folder = path.rpartition("\\")[2]
        result = f'Directory "{folder}" created successfully'
    except FileExistsError:
        result = f"Directory {path} already exists"
    except PermissionError:
        result = f"Permission denied: Unable to create {path}"
    except Exception as e:
        result = f"An error occurred: {e}"
    print(result)
    return result

def fetchFileName(fileType): #Creates a folder name for a file
    fileTypes = readFileTypes() #Reads csv file containing file names
    if fileTypes != None: #If the file is missing, this step is skipped
        for f in fileTypes:
            if f[0] == fileType: #Checks if the file extension is in the csv file
                return parentDirectory + f"\\{f[1]}"
    return parentDirectory + f"\\{fileType}" #If the file extension wasn't in the csv file, or the file was missing, the folder is named after the file extension.
    
def assignDirectory(fileType): #Assigns a folder name for a file
    path = fetchFileName(fileType)
    if os.path.isdir(path) == False: #Checks if folder already exists
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
            result = f'File "{fileName}" moved successfully to "{newFilePath}"\n'
        except FileExistsError:
            result = f"File {fileName} already exists"
        except PermissionError:
            result = f"Permission denied could not move file: {fileName}"
        except FileNotFoundError:
            result = f"Could not find file: {fileName}"
        except Exception as e:
            result = f"An error occurred: {e}"
        print(result)
        return result
    else:
        print("Dude, dont sort the programfiles\n")
        return


def findFiles(path): #Returns a list of all the files in a directory
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