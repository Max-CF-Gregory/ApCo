p1 = int(input())
p2 = int(input())
larger = max(p1, p2)
lesser = min(p1, p2)
if larger >= 11:
    print(2-(larger-lesser))
elif larger < 11 and larger-lesser>=2:
    print(11-larger)
else:
    print(11-larger+(larger-lesser))