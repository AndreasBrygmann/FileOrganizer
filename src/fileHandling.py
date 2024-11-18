import sys
from csv import reader

fileTypeFile = sys.path[0].rpartition("\\")[0] + "\\file_types.csv"

def readFileTypes():
    fileTypes = []
    try:
        with open(fileTypeFile, newline="\n") as file:
            fileReader = reader(file)
            for row in fileReader:
                fileTypes += [row]
    except Exception as e:
        print(f"An error occurred: {e}")
    return fileTypes
