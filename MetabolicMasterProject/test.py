with open("populate_bcm.py") as fp:
    for i, line in enumerate(fp):
        if "\xe2" in line:
            print i, repr(line)
