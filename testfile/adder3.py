import sys
sum = 0
while True:
    for line in sys.stdin: sum += int(line)
print(sum)