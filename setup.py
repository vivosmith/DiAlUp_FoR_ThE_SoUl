import os
import shutil
from sys import platform
os.system("pip install playsound")

platform == "win32":
   shutil.copy("dialup.mp3", "C:\\Users\\"+os.getlogin().strip()+"\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup")
   shutil.copy("dialup.py", "C:\\Users\\"+os.getlogin().strip()+"\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup")

platform == "darwin":
   shutil.copy("dialup.py", "/System/Library/StartupItems")
   shutil.copy("dialup.mp3", "/System/Library/StartupItems")
platform == "linux"
   os.system("@reboot /linux/")
