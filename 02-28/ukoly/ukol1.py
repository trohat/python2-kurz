#1 task:
# You have a text file. Create a new file and remove all bad
# words from it. The list of bad words is in another file.
import re
import string

string_for_regex = ""

with open ("First_task_filter.txt","r") as filter_list:
    for word in filter_list:
        string_for_regex += word[:-1] + "|"

string_for_regex = string_for_regex[:-1]
# odstraňuji poslední svislítko ( svislítko = |)

regex_compile = re.compile(fr"{string_for_regex}")

print(regex_compile)





"""
with open ("first_task.txt","r") as reader, open("First_task__without_bad.txt","w") as output, open ("First_task_filter.txt","w") as filter_list:
    list_to_check = []
    for word in reader: # read a text
        regex_search = regex_compile.findall(word) # find what i want from regex
        if len(regex_search) > 0: # check if list not empty
            words = " ".join(regex_search) # cut to words
            list_to_check.append(words) # send to the list , to check
            filter_list.write(words) # write to object filter_list
            filter_list.write("\n") # do the space
        my_split = word.split(" ") # creat a list of words
        #print(my_split)
        for letter in my_split: # read a list 
            if letter not in list_to_check : # check if letter have a bad word , if letter doesn`t have a bad word write to the another text
                print(list_to_check)
                output.write(letter) 
                output.write(" ")
"""