import os
import sys

def listFiles(path):
    try: 
        dirList = os.listdir(path)
        return dirList
    except FileNotFoundError:
        print(f"Could not find directory {path}\n")
        return None 
    except Exception as e:
        print(f"An error occurred: {e}") 
        return None 

def currentDir():
    path = sys.path[0]
    return path

def navigateForward(path,folder):
    folder = folder[2:].replace(" ", "")
    path += f'\\{folder}'
    return path

def navigateBackward(path):
    return path.rpartition(f'\\')[0]