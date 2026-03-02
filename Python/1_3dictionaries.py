
# The below is starter code for the dictionary data structure


Mr_ONeills_fridge = {"eggs":1.5, "milk":1.89, "ketchup":2, "courgettes":3.5, "feta": 1.80}

#print(Mr_ONeills_fridge["courgettes"])
#print(Mr_ONeills_fridge.keys())

d1 = {}
d1.update(Mr_ONeills_fridge)

#print(d1[Mr_ONeills_fridge]["eggs"])
#print(d1["Mr_ONeills_fridge"].keys())
max_fridge = {"pizzabase":2.60, "fijiwater":2.30, "lucozade":1.95,"mozzarella":3.50,"monsterultra":1.65}
max_fridge.update({"babybell":3.99})
print(max(max_fridge.values()))
d1.update(max_fridge)
print(d1)

minprice = min(d1.values())
for i in d1:
    if d1.get(i) == minprice:
        print(i)