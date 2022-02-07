from time import sleep

seconds = 0

while True:
    try:
        seconds += 1
        print(f"Už to bylo {seconds} sekund.")
        sleep(1)
    except KeyboardInterrupt:
        # reaguje na Ctrl + C
        print("Ha ha ha ha ha - tenhle program nejde ukončit!!")



