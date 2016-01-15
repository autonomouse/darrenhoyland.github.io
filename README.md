# PyQuo
Static site generator and/or journal using markdown.

PyQuo is written in Python3 and uses markdown to generate a collection of html pages that can be used as a static blog or a offline journal.

## Quickstart

To begin, you can run the "`new_personal_entry.py`" example script provided in the scripts directory as follows:

`./scripts/new_personal_entry.py` which will generate a file in the 'markdown' directory with the necessary metadata already pre-populated. Alternatively, you can, of course, do this manually  and add a file to the 'markdown' directory. There you can fill out the metadata at the beginning of the file, such as this:

Title:          First post!
Authors:        Darren Hoyland
Date:           2015-12-21
Tags:           Meta
HeaderImage:
Category:       Blog
Publish:        True

You can then leave a space and fill out the rest of the file with [markdown syntax](http://daringfireball.net/projects/markdown/syntax).

The source directory ('markdown' in the example, above) can be changed by editing the properties.json. You can also change the root from '/', used for websites hosted on a server, to 'file:///home/path/to/local/directory', which is useful if you wish to use PyQuo as a private journal.

If you wish to generate a website and are looking for a way to host it, one option is to add your website address to the CNAME file and follow the instructions [here](https://pages.github.com/).

To generate your site, run `./scripts/generate_website.py` and an index.html page will be generated, along with each entry in its individual category.
