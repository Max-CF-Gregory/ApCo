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
    reddict, blackdict = {}, {}
    for i in range(1,37):
        if i in [15, 4, 2, 17, 6, 13, 11, 8, 10, 24, 33, 20, 31, 22, 29, 28, 35, 26]: blackdict[i] = results_dict[i]
        elif i in [32, 19, 21, 25, 34, 27, 36, 30, 23, 5, 16, 1, 14, 9, 18, 7, 12, 3 ]: reddict[i] = results_dict[i]
    resultkeys, resultvals = list(results_dict.keys()), list(results_dict.values())
    plt.bar(blackdict.keys(), blackdict.values(), color = "black")
    plt.bar(reddict.keys(), reddict.values(), color = "red")
    plt.bar(resultkeys[0], resultvals[0], color = "green")
    plt.show()

l4 = get_results("roulette.txt")
d1 = (get_frequencies(l4))
print(d1)
show_frequency_graph(d1)