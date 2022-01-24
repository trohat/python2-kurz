
def count(muj_list):
    a,b,c = muj_list
    sum_numbers = (a[0] * a[1]) + (b[0] * b[1]) + (c[0] * c[1])
    return sum_numbers

#print(count(muj_oblibeny_list))

#x = dict(muj_oblibeny_list)

muj_oblibeny_list = [([5,6], 2), 
                     (3, 7), 
                     (9, 5),
                     (5, 6)]

soucet = 0
for a, b in muj_oblibeny_list:
    soucet += a * b
print(soucet)

