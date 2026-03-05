import datetime

# today = datetime.date.today()
# bday = datetime.date(2011, 5, 24)
#
# print(f"It has been {str(today-bday)[:-9]} since my birth")
#
# #Easy
# ts = datetime.date(1989, 12, 13)
# print(f"Taylor swift is {str(today-ts)[:-9]} old")
#
# #Med
# milestone = bday + datetime.timedelta(10000)
# print(f"I will spend my 10000th day on {milestone}")
#
# #Hard
# print(f"I was born on a {bday.strftime("%A")}")

today = datetime.date.today()
end = datetime.date(2026, 7, 2)

print(str(end-today)[:-9])

#extension
bday = datetime.date(2011, 5, 24)
year = int(today.strftime("%Y"))
for i in range(10):
    year += 1
    bday2 = datetime.date(year, 5, 24)
    print(f"{year}: {bday2.strftime("%A")}")