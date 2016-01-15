#!/usr/bin/python3

from subprocess import Popen
from datetime import datetime
from new_entry import create_entry

folder = 'markdown'
filename = create_entry(folder, category='Blog')

Popen(["gedit", filename])
