#!/usr/bin/python3

from subprocess import Popen
from datetime import datetime
from new_entry import create_entry

folder = 'markdown'
filename = 'blog_' + datetime.now().strftime("%Y-%m-%d")
path_to_file = create_entry(folder, filename=filename, category='Blog')

Popen(["gedit", path_to_file])
