#!/usr/bin/python3

import os
from datetime import datetime


def create_entry(folder, timestamp='', title='', filename=None, category='',
                 name='', tags='', header_image='', categories='', 
                 publish_bool='True', content=''):

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
    
    meta =  "Title:          {title}\n"
    meta += "Authors:        {name}\n"
    meta += "Date:           {date}\n"
    meta += "Tags:           {tags}\n"
    meta += "HeaderImage:    {header_image}\n"
    meta += "Category:       {categories}\n"
    meta += "Publish:        {publish_bool}\n"
    meta += "\n\n"
    meta = meta.format(title=title, name=name, date=timestamp, tags=tags, 
                       header_image=header_image, categories=categories, 
                       publish_bool=publish_bool)        
    
    with open(filepath, 'w') as op:
        op.write(meta)
        op.write('\n')
        op.write(content)       
    
    return filepath
