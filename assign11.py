import re

file = open("actualdata.txt")
x=list()
for line in file:
     y = re.findall('[0-9]+',line)
     x = x+y

sum=0
for z in x:
    sum = sum + int(z)

print(sum)
