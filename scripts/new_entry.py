#!/usr/bin/python3

import os
from datetime import datetime


def create_entry(folder, timestamp=None, title=None, filename=None, category=''):

    try:
        os.makedirs(folder)
    except:
        pass

    if timestamp is None:
        timestamp = datetime.now().strftime("%Y-%m-%d")
    if title is None:
        title = \
            datetime.strptime(timestamp, "%Y-%m-%d").strftime("%A %d %B, %Y")
    if filename is None:
        filepath = os.path.join(folder, title + '.md')
    else:
        filepath = os.path.join(folder, filename + '.md')
    if os.path.exists(filepath):
        return filepath
    
    meta =  "Title:          {}\n"
    meta += "Authors:        Darren Hoyland\n"
    meta += "Date:           {}\n"
    meta += "Tags:           \n"
    meta += "HeaderImage:    \n"
    meta += "Category:       {}\n"
    meta += "Publish:        True\n"
    meta += "\n\n"
    meta = meta.format(title, timestamp, category)        
    
    with open(filepath, 'w') as op:
        op.write(meta)       
    
    return filepath
