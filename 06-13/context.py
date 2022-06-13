import time
# context management (ale zatím pomocí finally)

f = open("output.txt", "w")

try:
    text = f.write("Ahoj")
    #raise ZeroDivisionError
except ZeroDivisionError:
    print("Chyba!!!")
finally:
    print("Tohle se stane vždycky, ať už je chyba nebo ne")
    f.close()

