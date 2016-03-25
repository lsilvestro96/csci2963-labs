"""
 Markdown.py
 0. just print whatever is passed in to stdin
 0. if filename passed in as a command line parameter, 
    then print file instead of stdin
 1. wrap input in paragraph tags
 2. convert single asterisk or underscore pairs to em tags
 3. convert double asterisk or underscore pairs to strong tags

"""

import fileinput
import re

def convertStrong(line):
  line = re.sub(r'\*\*(.*)\*\*', r'<strong>\1</strong>', line)
  line = re.sub(r'__(.*)__', r'<strong>\1</strong>', line)
  return line

def convertEm(line):
  line = re.sub(r'\*(.*)\*', r'<em>\1</em>', line)
  line = re.sub(r'_(.*)_', r'<em>\1</em>', line)
  return line

def convertH1(line):
  line = re.sub(r'#{1}(.*)',r'<h1>\1</h1>',line)
  return line

def convertH2(line):
  line = re.sub(r'#{2}(.*)',r'<h2>\1</h2>',line)
  return line

def convertH3(line):
  line = re.sub(r'#{3}(.*)',r'<h3>\1</h3>',line)
  return line

def convertBlock(line):
  line = re.sub(r'^>(.*)',r'    \1',line)
  return line

def linePeek(fileinput):
  pos = fileinput.tell()
  nextLine = f.readline()
  nextLine = nextLine.rstrip()
  fileinput.seek(pos)
  return nextLine

blockquote = False
for line in fileinput.input():
  line = line.rstrip()
  line = convertStrong(line)
  line = convertEm(line)
  line = convertH3(line)
  line = convertH2(line)
  line = convertH1(line)
  match = re.match(r'\>',line)
  if (match):
    if (not blockquote):
      blockquote = True
      print '<blockquote>'
  elif (blockquote):
    blockquote = False
    print '</blockquote>'

  line = convertBlock(line)
  if(re.match(r'(?!<h\d>)',line) and not blockquote):
    print '<p>' + line + '</p>'
  else:
    print line
  prevLine = line

if (blockquote):
  print '</blockquote>'
