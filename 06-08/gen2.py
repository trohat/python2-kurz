seznam = [1, 2, 3, 4, 5]


#druhé mocniny pomocí cyklu
novy_seznam = []

for i in seznam:
    novy_seznam.append(i * i)

#druhé mocniny pomocí list comprehension
novy_seznam2 = [i * i for i in seznam]

#druhé mocniny pomocí generator expression
novy_seznam2 = (i * i for i in seznam)

