# File Organizer
This program lets you navigate directories and sort files based on filetype
## Installation instructions:
1. Clone the files from github
```bash
git clone https://github.com/AndreasBrygmann/FileOrganizer
```
2. Install the program
```bash
pip install file_organizer 
```
3. Run the program
```bash
file_organizer
```

## User guide
### Navigation
Once the program starts, you will see a list of commands followed by the contents of the directory you are in. The program opens in your home folder by default

If you want to enter a directory, simply type "cd" followed by the name of the directory. For example:
```bash
cd foldername
```
(Note that whether or not you have a space between "cd" and the directory name doesn't matter. It works either way.)

If you want to go up to the parent directory, simply type the letter "b" and press enter.
```bash
b
```

Any time you move to a new directory the files and folders in that directory will be shown on screen

Quit the program by typing "q"
```bash
q
```

### Sorting
There are 2 ways of sorting files.

By pressing "1" the program will sort every file in your current directory.
```bash
1
```

If you want to select which files to sort, pressing "2" will give you a list of the files in the directory. Press the corresponding number to sort a file.
```bash
2
```

You can also list the files in your current direnctory by pressing "3".
```bash
3
```

The files will be sorted into folders named based on filetypes. The folders will be created in the directory the files where in.