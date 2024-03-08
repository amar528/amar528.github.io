#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib
from urllib.request import urlopen

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def extract_urls(file_text):
    url_regex = r'GET\s+(.+)\s+HTTP'
    matches = re.findall(url_regex, file_text)

    if matches:
        return matches
    else:
        print('Error: failed to extract URL data')
        sys.exit(1)


def read_urls(filename):
    """Returns a list of the puzzle urls from the given log file,
    extracting the hostname from the filename itself.
    Screens out duplicate urls and returns the urls sorted into
    increasing order."""
    # +++your code here+++
    f = open(filename, 'rt', encoding='utf-8')
    file_text = f.read()
    extracted_urls = extract_urls(file_text)

    _idx = filename.index('_')
    _idx += 1
    server_part = filename[_idx:]
    print(f'Server: {server_part}')

    urls = []
    for _url in extracted_urls:
        item = server_part + _url
        if item not in urls:
            urls.append(item)

    return sorted(urls)

def download_images(img_urls, dest_dir):
    """Given the urls already in the correct order, downloads
    each image into the given directory.
    Gives the images local filenames img0, img1, and so on.
    Creates an index.html in the directory
    with an img tag to show each local image file.
    Creates the directory if necessary.
    """

    # +++your code here+++
    def do_get(url):
        try:
            ufile = urlopen(url)
            if ufile.info().get_content_type() == 'text/html':
                return ufile.read()
        except IOError:
            print('problem reading url:', url)
            sys.exit(1)


def main():
    args = sys.argv[1:]

    if not args:
        print('usage: [--todir dir] logfile ')
        sys.exit(1)

    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    img_urls = read_urls(args[0])

    if todir:
        download_images(img_urls, todir)
    else:
        print('\n'.join(img_urls))


if __name__ == '__main__':
    main()
