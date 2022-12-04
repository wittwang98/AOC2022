
items = [a.rstrip('\n') for a in (open("input.txt", 'r').readlines())]

matches = []
for a in items:
    duplicate = False
    for b in range(int(len(a)/2)):
        for i in a[0:int(len(a)/2)]:
            if not duplicate and i in a[b+int(len(a)/2)]:
                matches.append(i)
                duplicate = True
                break
sum = 0
for m in matches:
    if ord(m) < 91:
        sum += ord(m)-38
    else:
        sum += ord(m)-96
print(sum)

badges = []
for a in range(0,len(items), 3):
    rucksackMatches = []
    for i in items[a]:
            if i in items[a+1]:
                rucksackMatches.append(i)
            
    for r in rucksackMatches:
        if r in items[a+2]:
            badges.append(r)
            break
        
sum = 0
for m in badges:
    if ord(m) < 91:
        sum += ord(m)-38
    else:
        sum += ord(m)-96
print(sum)