entered = 0.0
sequence = []

while entered < 1:
    entered = int(input("Enter starting value (integer): "))

sequence.append(entered)

while sequence[-1]!=1:
    n = sequence[-1]
    if n%2 == 0:
        sequence.append(int(n/2))
    else:
        sequence.append(int((3*n)+1))

print(sequence)
print(f"{len(sequence)} terms in sequence")
print(f"{max(sequence)} is the peak value")