# File Organizer
This program lets you navigate directories and sort files based on filetype <br>
**NB!** Has this app has only been tested on a windows file system, but could in *theory* work on a Linux file system

## Installation instructions:
1. Clone the files from github
```bash
git clone https://github.com/AndreasBrygmann/FileOrganizer
```
2. Install the program
```bash
pip install .
```
3. Run the program
```bash
fileOrganizer
```


## User guide
### Navigation
Once the program starts, you will see a list of commands followed by the contents of the directory you are in. The program opens in your home folder by default

>You can type `help` at anytime to see a list of commands  <br>

>**Selecting directory**  
>If you want to enter a directory, type `cd` followed by the name of the directory. For example: `cd foldername`  

Note that whether or not you have a space between "cd" and the directory name doesn't matter. It works either way.  

>**Go to parent directory**  
>If you want to go up to the parent directory, type `back` or `b` and press enter.

Any time you move to a new directory the files and folders in that directory will be shown on screen   

>List the files and folders in your current direnctory by pressing `show` or `s`. <br>  

>You can also list only the files in your current direnctory by pressing `list` or `l`. <br>  

>Check the current directory and path by pressing `pwd` or `p`. <br>  



### Sorting
There are 2 ways of sorting files.

>**Sort all files in a directory**  
>By pressing `1` the program will sort every file in your current directory. <br>

>**Select a file for sorting**  
>If you want to select a specific file to sort, pressing `2` will give you a list of the files in the directory.  
>Press the corresponding number to sort a file.  <br>

The files will be sorted into folders named based on filetypes. The folders will be created in the directory the files are in.  

>**Quit program**  
>Quit the program by typing `quit` or `q` and press enter  

