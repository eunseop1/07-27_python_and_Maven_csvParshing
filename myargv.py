import sys

sum = 0
for n in range(1, len(sys.argv)):
    sum += int(sys.argv[n])
print(sum)
