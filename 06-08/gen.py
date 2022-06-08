def my_generator():
    seznam = [1,2,3,4,5]
    for i in seznam:
        yield i * i


for cislo in my_generator():
    print(cislo)




    


