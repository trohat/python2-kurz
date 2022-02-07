retezec = "ahoj"

while True:
    try:
        retezec = 2 * retezec
    except MemoryError:
        print("Došla paměť! :(")
        break


