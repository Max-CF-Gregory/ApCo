from matplotlib import pyplot as plt
from csv import DictReader

def get_data_from_file(file_name: str) -> list[dict]:
    with open(file_name,"r") as f:
        reader = list(DictReader(f))
    return reader

list_of_files = ["UK_public_spending.csv"]

data = get_data_from_file(list_of_files[0])

d = {k:[] for k in data[0].keys()}

ax = plt.subplot(1,1,1)

for row in data:
    for k in row.keys():
        if k == "year":
            d.get(k).append(row.get(k))
        try:
            d.get(k).append(float(row.get(k)))
        except ValueError:
            pass

for k in d.keys():
    if k != "year":
        yr = d.get("year")
        plt.plot(yr[(len(yr)-(len(d.get(k)))):], d.get(k), label=k)

ax.set_xticks(d.get("year")[::5])
ax.tick_params(axis="x", labelrotation=45)
plt.xlabel("Financial Year")
plt.ylabel("Expenditure £bn")
plt.legend()
plt.show()