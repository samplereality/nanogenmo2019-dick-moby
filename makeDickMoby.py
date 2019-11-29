# -*- coding: utf-8 -*-
import re
import io
from nltk.tokenize import sent_tokenize

with io.open("moby-ready-to-reverse.txt", "r", encoding="utf-8") as f:
     raw = f.read()
     f.close()

novel = ''

normal = sent_tokenize(raw)

normal.reverse()
output = ' '.join(normal)

output = re.sub(r"<P>", r"\n\n", output)

fixChapters = re.compile(r"(\.)(.+\w*\..)(\n\n)(CHAPTER.\d+\.)", re.MULTILINE)

output = fixChapters.sub(r"\n\n\4\2\n\n", output)

novel = output.encode("utf-8")

n = open("reverse-dick.txt","w")
n.write(novel)
n.close()