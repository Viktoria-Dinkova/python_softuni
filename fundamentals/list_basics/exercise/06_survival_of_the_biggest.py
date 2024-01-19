# Write a program that receives a list of integer numbers (separated by a single space) and a number n.
# The number n represents the count of numbers to remove from the list.
# You should remove the smallest ones, and then, you should print all the numbers that are left in the list,
# separated by a comma and a space ", ".

inlist = list(map(int,input().split()))
cuted_numbers = int(input())

outlist = inlist.copy()

outlist.sort()
outlist = outlist[:cuted_numbers]
for num in outlist:
    inlist.remove(num)

outlist = map(str, inlist)

print(', '.join(outlist))