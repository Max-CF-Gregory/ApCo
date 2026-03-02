acres = int(input())
if acres < 50:
    subsidy = acres*5
    print(10+subsidy)
else:
    rounded_acres = round(acres, -1)
    if rounded_acres > acres:
        rounded_acres-=10
    rounded_acres/=10
    print(int(rounded_acres*45))