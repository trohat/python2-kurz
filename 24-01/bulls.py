pc = "4567"
user = "2567"

cows = 0 # černé v logiku
for x in range(4):
    if pc[x] == user[x]:
        print(f"Uhádnul jsi číslo {pc[x]} na pozici {x+1}")
        cows += 1

bulls = 0 # bílé v logiku (nevím jestli bulls nebo cows)
"""
for index, cislo in enumerate(user):
    if cislo in pc:
        print(f"Uhádnul jsi číslo {cislo}, které není na pozici {index+1}")
        bulls += 1
"""

#to samé bez enumerate
bulls = 0 # bílé v logiku (nevím jestli bulls nebo cows)
for cislo in user:
    if cislo in pc:
        print(f"Uhádnul jsi číslo {cislo}, a index nevíme")
        bulls += 1

