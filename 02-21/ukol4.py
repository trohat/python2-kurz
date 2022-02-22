
with open("carky.txt") as infile, open("output.txt", "w") as outfile:
    pis_hvezdicky = True
    for radek in infile:
        outfile.write(radek)
        if not radek.endswith(",\n") and pis_hvezdicky:
            outfile.write("**********\n")
            pis_hvezdicky = False


with open("output.txt") as file:
    print(file.read())

