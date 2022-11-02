import os
import sys
import winreg as reg

cwd = os.getcwd()

python_exe = sys.executable

key_path = r"Directory" + os.sep + r"Background" + os.sep + r"shell" + os.sep + r"Organiser"

key = reg.CreateKeyEx(reg.HKEY_CLASSES_ROOT, key_path)

reg.SetValue(key, '', reg.REG_SZ, 'Pa&ste With Directories')

key1 = reg.CreateKeyEx(key, r"command")

reg.SetValue(key1, '', reg.REG_SZ, python_exe + ' ' + f'"{cwd}{os.sep}paste_with_directory.py"')