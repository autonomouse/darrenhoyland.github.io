#!/usr/bin/python3

from subprocess import Popen
from datetime import datetime
from new_entry import create_entry, get_editor

folder = 'markdown'
filename = 'personal_' + datetime.now().strftime("%Y-%m-%d")
path_to_file = create_entry(folder, filename=filename, categories='Personal')

text_editor = get_editor()
if text_editor is not None:
    Popen([text_editor, path_to_file])

