
class Context:
    def __init__(self):
        pass

    def __enter__(self):
        print("Otevírám context managera")
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print("Zavírám context manažera...")
        if exc_type:
            print(exc_type, exc_value, exc_traceback)
        return True


with Context():
    print("tohle je uprostřed ... např. když zapisuji do souboru...")
    raise KeyError("tenhle klíč ve slovníku není")

