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
python file_organizer.py
```

## User guide
### Navigation
Once the program starts, you will see a list of commands followed by the contents of the directory you are in.

If you want to enter a directory simply type "cd" followed by the name of the directory. For example:
```bash
cd foldername
```
Note that whether or not you have a space between "cd" and the directory name doesn't matter. It works either way.

If you want to go up to the parent directory simply type the letter "b" and press enter.

Any time you move to a new directory the files and folders in that directory will be shown on screen

### Sorting
There are 2 ways of sorting files.

By pressing "1" the program will sort every file in your current directory. The files will be moved to a folder called "Sorted_Files" in the directory of the code.

If you want to select which files to sort, pressing "2" will give you a list of the files in the directory. Press the corresponding number 2 sort a file.

You can also list the files in your current direnctory by pressing "3".

All sorted files are placed in the same folder as this program. This can be changed manually by entering "sorting.py" and changing the following line of code in line 6:

```python
parentDirectory = sys.path[0] + "\\Sorted_Files"
```
This can be changed to a custom path. 
For example:
```python
parentDirectory = "C:\\Users\\User\\Documents\\Sorted_Files"
```