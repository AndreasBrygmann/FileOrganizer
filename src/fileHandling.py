import sys
from csv import reader

fileTypeFile = sys.path[0].rpartition("\\")[0] + "\\file_types.csv" #Looks for the file "file_types.csv" in the "fileorganizer" folder

#Reads filenames from the filetypes file
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
