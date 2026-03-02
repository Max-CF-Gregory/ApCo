from matplotlib import pyplot as plt

def get_results(f: str) -> list[int]:
    grlist = []
    with open(f, "r") as file:
        fr = file.readlines()
        for i in fr:
            grlist.append(int(i[:-1]))
    return grlist

def get_frequencies(results:list[int]) -> dict:
    gfdict = {}
    for i in range(0,37):
        gfdict.update({i:0})
    for i in results:
        gfdict.update({i:(gfdict.get(i)+1)})
    return gfdict

def show_frequency_graph(results_dict: dict):
    rouletteorder = [0,32,15,19,4,21,2,25,17,34,6,27,13,36,11,30,8,23,10,5,24,16,33,1,20,14,31,9,22,18,29,7,28,12,35,3,26]
    resultkeys, resultvals = list(results_dict.keys()), list(results_dict.values())
    nresultkeys, nresultvals = [], []
    for i in rouletteorder:
        nresultkeys.append(str(i))
        nresultvals.append(resultvals[i])
    plt.bar(nresultkeys, nresultvals)
    plt.xticks(rotation=270)
    plt.show()

l4 = get_results("roulette.txt")
d1 = (get_frequencies(l4))
print(d1)
show_frequency_graph(d1)

#Weighted area = approx 21:34