#!/usr/bin/env python3

import uuid
from lxml import etree
from subprocess import Popen
from datetime import datetime
from new_entry import create_entry


target_location = '/home/darren/Documents/Darren_Personal/Diary_Blog_Lifestream/OriginalAutonomousewordpress.2008-03-19.xml'
export_location = 'markdown'

p = etree.XMLParser(huge_tree=True)
try:
    et = etree.parse(target_location, parser=p)
    doc = et.getroot()
except etree.XMLSyntaxError as e:
    msg = "Cannot read from XML file"
    raise(msg)

filenames = []
for item in doc.xpath('.//channel/item'):
    children = item.getchildren()
    title = children[0].text
    timestamp = children[2].text
    author = children[3].text
    tags = []
    idx = 4
    for child in children[idx:]:
        idx += 1
        
        if child.text is not None:
            tags.append(child)
        else:
            content = children[idx+2].text
            break
        
        if 'http' not in child.text:
            tags.append(child)
        else:
            content = children[idx+1].text
            break
    
    unique_tags = set([tag.text for tag in tags if 'http' not in tag.text and 
                       tag is not None])

    if len(content) < 5:
        continue 
    dtime = datetime.strptime(timestamp, "%a, %d %b %Y %H:%M:%S %z").strftime("%Y-%m-%d")
    filename = 'blog_' + dtime
    if filename in filenames:
        filename = filename + "_" + str(uuid.uuid4())
    else:
        filenames.append(filename)
    path_to_file = create_entry(folder=export_location, 
                                timestamp=dtime, 
                                title=title, 
                                filename=filename, 
                                name='Darren Hoyland', 
                                tags=", ".join(unique_tags), 
                                header_image='', 
                                categories='Blog',
                                publish_bool='True', 
                                content=content)
    print(path_to_file + " created.")

