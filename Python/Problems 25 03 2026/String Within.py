string = str(input("String: "))
within = str(input("Within: "))
lenminus = len(string)-len(within)+1
count = 0

for i in range(lenminus):
    if string[i:(i+len(within))] == within:
        count+=1

print(count)