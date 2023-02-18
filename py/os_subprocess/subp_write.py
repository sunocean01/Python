import sys

lts = sys.argv[1]

with open("writein.txt",'w') as fp:
    for i in lts:
        fp.write(i)