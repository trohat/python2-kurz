
#1 First task:
# You have a text file. Create a new file where you should
# write all words consisting of at least seven letters found in the
# source file.

import re
regex_compile = re.compile(r"\w{7,}")

with open("input.txt","r") as reader, open("First_task__ready.txt","w") as output:
    for nove_jmeno in reader:
        regex_search = regex_compile.findall(nove_jmeno)
        print(regex_search)
        if len(regex_search) > 0:
            words = " ".join(regex_search)
            output.write(words)
            output.write("\n")