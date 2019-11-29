# -*- coding: utf-8 -*-
#! python3.8
import dominate 
from dominate.tags import *
import pdfkit
import re

n = open('reverse-dick.txt','r')
novel = n.read()

sectioned = novel.split("\n\n")

chapters = novel.split("CHAPTER")

chapterHeadings = re.compile(r"^CHAPTER.+\.$")
removeChapterHeadings = re.compile(r".+<p>CHAPTER\s\d+\.\s\w*\.</p>")

doc = dominate.document(title='The Whale: Dick Moby')
with doc.head: 
    style("body {background-color: white; color: black; font-size: 25pt; margin-top: 2.5cm; margin-bottom: 2.5cm; margin-left: 2.5cm; margin-right: 2.5cm;}")
    
with doc: 
    
    h1("The Whale: Dick Moby")
    h2("by Mark Sample")
    p()
    h3("A NaNoGenMo Novel")
    
    for s in sectioned:
        if chapterHeadings.match(s):
            h3(s)
        else:
            p(s)
            
    
pdfkit.from_string(str(doc.render()), 'dickmoby.pdf')

print(doc)

len(novel.split(" "))

# pdfkit.from_file('reverse-dick.txt', 'out.pdf')