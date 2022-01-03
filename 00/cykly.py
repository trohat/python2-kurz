"""
i = 0
print("Malá násobilka")
print("**************")

while i < 10:
    i = i + 1
    if napoj == "pivo":
        i = i + 1
    print("*******")
"""

#for i in range(10):
#    print(i, end=" ")

cislo = input("Zadej číslo, odstraním trojky a šestky: ")
"""
nove_cislo = ""

for cislice in cislo:
    if cislice != "3" and cislice != "6":
        nove_cislo = nove_cislo + cislice

print(nove_cislo)
    
"""
    
for i in cislo:
    if i == "3" or i == "6":
        continue
    print(i, end="")


for pismeno in "ahoj":
    print(pismeno)

for i in range(10):
    if i == 5:
        break
    print(i)
