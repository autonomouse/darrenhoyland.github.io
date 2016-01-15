#!/usr/bin/python3

import os
from datetime import datetime


def create_entry(folder, timestamp=None, title=None, category=''):

    try:
        os.makedirs(folder)
    except:
        pass

    if timestamp is None:
        timestamp = datetime.now().strftime("%Y-%m-%d")
    if title is None:
        title = \
            datetime.strptime(timestamp, "%Y-%m-%d").strftime("%A %d %B, %Y")
    
    filename = os.path.join(folder, title + '.md')
    if os.path.exists(filename):
        return filename
    
    meta =  "Title:          {}\n"
    meta += "Authors:        Darren Hoyland\n"
    meta += "Date:           {}\n"
    meta += "Tags:           \n"
    meta += "HeaderImage:    \n"
    meta += "Category:       {}\n"
    meta += "Publish:        True\n"
    meta += "\n\n"
    meta = meta.format(title, timestamp, category)        
    
    with open(filename, 'w') as op:
        op.write(meta)       
    
    return filename
