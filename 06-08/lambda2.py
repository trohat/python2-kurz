seznam = [2, 5, 6, 7, 9]



novy_seznam = list(map(lambda x : x * x, seznam))

novy_seznam2 = list(filter(lambda x : x > 5, seznam))
#pro tyto dva případy je lepší list comprehension

seznamX = [(2, 6), (3, 13), (5, 9), (7, 3), (4 ,0)]

print(min(seznamX, key=lambda x : x[1]))

slova = ["jablko", "ananasasasa", "Eva", "Boris", "rajčátko", "paprika"]

print(sorted(slova, key=lambda s : s.lower()))
print(sorted(slova, key=len))

