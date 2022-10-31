import pyperclip
import os
import shutil
import win32api



fileFullPath = pyperclip.paste().replace('"', '')

if os.path.exists(fileFullPath):
    fileDirectoriesWithoutRoot = os.sep.join(fileFullPath.split(os.sep)[1:-1])
    fileName = fileFullPath.split(os.sep)[-1]
    destinationPath = os.getcwd() + os.sep + fileDirectoriesWithoutRoot 

    if os.path.exists(destinationPath):
        pass
    else:
        os.makedirs(destinationPath)
    try:
        shutil.copy(fileFullPath, destinationPath + os.sep + fileName)
    except:
        win32api.MessageBox(0, 'Error While Pasting!', 'Error')


else:
    win32api.MessageBox(0, 'No File Select to Paste!', 'Error')

