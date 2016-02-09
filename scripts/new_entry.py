#!/usr/bin/python3

import os
from datetime import datetime
from generate_website import get_properties

properties_file = "properties.json"


def create_entry(folder, timestamp=None, title=None, filename=None, 
                 categories='', name='', tags='', header_image='', 
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
        op.write(content)       
    
    return filepath

def get_editor():
    props_path = os.path.abspath(os.path.join(os.path.dirname(__file__),  
                                 '../' + properties_file))
    properties = get_properties(properties_file=props_path)
    return properties.get('text_editor', None)
