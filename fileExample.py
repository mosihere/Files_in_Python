import os  # this module help us to create a folder path.

# For example we want full path of sth /home/mosihere/myProjects
# we can import os and then use os.path.join('home', 'mosihere', 'myProjects', 'python.py')
# the outpull will be --> /home/mosihere/myProjects/python.py

filePath = os.path.join('home', 'mosihere', 'myProjects', 'file.txt')
print(filePath)
print(os.getcwd())

# We have two kinda paths --> absolute / Relative
# absolute fike path always start from root and relative start from parrent directory
# we can use . and .. in relative path . means current direcotry and .. means parrent directory

print(os.path.abspath('file.txt'))
print('\n')

# Create a little program to calculate the size of all my python files in python tutorial directory
totalSize = 0 
for filename in os.listdir('/home/mosihere/myProjects/Python tutorial'):
    if not os.path.isfile(os.path.join('/home/mosihere/myProjects/Python tutorial', filename)):
        continue
    totalSize += os.path.getsize((os.path.join('/home/mosihere/myProjects/Python tutorial', filename)))

print(totalSize)
print('\n')


# File 
myFile = open('gitCommands.txt')

content = myFile.read()

print(content)

myFile.close()

# Tip --> using shelve module help us to save list, dictionaries and non-text data to a file and them re-open them in future in python program
import shelve
shelfFile = shelve.open('myShelfFile')
shelfFile['cat'] = ['Misha', 'Kisia', 'Kitty']
print(shelfFile['cat'])

# Shelve module can save python values in a binary File.
# shelve module has similar method as dictionary, for example .keys() .values()
myList = []
for k,v in shelfFile.items():
    print(k,v)
print('\n')

# Another Tricks --> shUtil module will help us to make a copy and rename that in python from one directory to another.
import shutil
createCoyp = shutil.copy('/home/mosihere/myProjects/Python tutorial/gitCommands.txt', '/home/mosihere/gitCopy.txt')
print(createCoyp)
# But now we wanna copy a whole directory not just a file 
# we have to use shutil.copytree(...)
# createCopyDirectory = shutil.copytree('/home/mosihere/myProjects/Python tutorial', '/home/mosihere/pythonCopy')

# we can move folder and files too with " shutil.move(..) "
# for rename a file or folder we have to use a small trick, which means we have to use shutil.move() and move it to the exact same place and use another name for it 
# rename = shutil.move(/home/mosihere/myProjects/Python tutorial/gitCommands.txt, /home/mosihere/myProjects/Python tutorial/GitCommands.txt)

# one way to delete a file is using os module and os.unlink() method.
# we can remove directory with os.rmdir(), but if we wanna do this we'll get an error
# we must use shutil.rmtree() and it will delete directory recursionally

# This methods for removing files and directories will delete them withoutt permission from whole system
# if we want to send them to recycle bin and then if we had a mistake, we restore them,
# we have to use third-party module(install with pip --> pip3 install send2trash ) named -> " send2trash "
# and send2trash has a function named send2trash
# send2trash.send2trash(/home/mosihere/myProjects/Python tutorial/gitCommands.txt)

# to walk in all directories and check files in them we can use os.walk()
checkingDirectories = os.walk('/home/mosihere/myProjects/Job')
for dirNames, subDirnames, filenames in checkingDirectories:
    print('The Directory is',dirNames)
    print('The SubFolder in',dirNames,'Are', subDirnames)
    print('The FileNames in',dirNames,'Are',filenames)
    print()

# Just remember when we use os.walks() it returns value in a for loop and that return three different values 
# 1- current folder we looking at 2- all of the subfolder inside current folder 3-  file in that folder and sub folders