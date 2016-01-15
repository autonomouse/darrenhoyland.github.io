#!/usr/bin/python3

from subprocess import Popen
from datetime import datetime
from new_entry import create_entry

folder = '/home/darren/Repositories/Journals/Journal/markdown'
title = 'personal_' + datetime.now().strftime("%Y-%m-%d")
filename = create_entry(folder, title=title, category='Personal')

Popen(["gedit", filename])
