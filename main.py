from handler import Parser1 as ps1
from handler import Parser2 as ps2

with open("keylog.txt", "r") as f1:
    with open("output.txt", "w") as f2:
        file = [line.rstrip() for line in f1.readlines()]
        #f2.write(ps1(file, 0))
        f2.write(ps2(file))

f1.close()
f2.close()
