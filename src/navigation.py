import os
import sys

def listFiles(path): #Lists the contents of your current directory
    try: 
        dirList = os.listdir(path)
        return dirList
    except FileNotFoundError:
        print(f"Could not find directory {path}\n")
        return None 
    except Exception as e:
        print(f"An error occurred: {e}") 
        return None 

def currentDir(): #Returnes the system path
    #path = sys.path[0] #Sets the path to the program folder
    path = os.path.expanduser("~") #Sets the path to the users home folder
    return path

def navigateForward(path,folder): #returns the path to a sub directory of the current path
    folder = folder[2:].replace(" ", "")
    path += f'\\{folder}'
    return path

def navigateBackward(path): #returns the path to the parent directory of the current path
    return path.rpartition(f'\\')[0]