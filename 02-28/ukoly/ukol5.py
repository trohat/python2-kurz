#5 task:
# You have a text file. Calculate the number of words that
# begin with a character set by the user.

import re
#letter = input("Which letter are we looking for")
letter = "d"

regex_compile = re.compile(fr"\b{letter}\w*?\b")

with open ("cist.txt", "r") as reader:
    sum_of_leters = []
    for line in reader:
        regex_search = regex_compile.findall(line)
        #if len(regex_search) > 0 :
            #print(regex_search)
        for index in regex_search:
            sum_of_leters.append(index)
    print("The sum of my letters are:",len(sum_of_leters))
    print(sum_of_leters)