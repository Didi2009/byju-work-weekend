import os
import sys

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

#path(source file)
source = 'main.txt'
#path(destination file)
dest = 'newfile.txt'

if os.rename(source, dest):
    print("Source path renamed to destination path successfully")