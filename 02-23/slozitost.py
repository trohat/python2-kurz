def jeden_ukon():
    3 + 4

def pet_ukonu():
    5 + 9
    9 - 3
    12 + 1
    2 * 7
    8 - 7

#člověk 1:
jeden_ukon()

#člověk 2:
pet_ukonu()

#1 nebo 5 úkonů = konstantní složitost

seznam = [ 2, 3, 5, 7]
# nevím jak je dlouhý
# N = délka seznamu

for x in seznam:
    jeden_ukon()

# složitost 1 * n = n

for x in seznam:
    pet_ukonu()

# složitost 5 * n = 5n

# n nebo 2n nebo 5n = lineární složitost

for x in seznam:
    pet_ukonu()

jeden_ukon()

#5 * n + 1 => 5n + 1 => 5n => n

for i in seznam:
    for j in seznam:
        jeden_ukon()

#n * n

for i in seznam:
    for j in seznam:
        pet_ukonu()

#5 * n * n => n * n => n^2

for i in seznam:
    for j in seznam:
        for k in seznam:
            pet_ukonu()

#5 * n * n * n => n * n * n => n^3

#5* n ^ 3 + 100 * n ^ 2 + 1000 * n + 10000000 = n ^ 3

# notace velkého O neboli Big Oh notation:
# seřazeny podle náročnosti
# O(1) = konstantní časová složitost - nejlepší
# O(log n) = logaritmická
# O(n) = lineární
# O(n ** 2) = kvadratická
# O(n ** 3) = mocninná
# O(n ** 4) = mocninná
# O(2 ** n) = exponenciální - nejhorší

# O( 3 * n ** 2 + 5) ==> O( n ** 2)