"""
In this task we examine lists and all of their functionality
"""

'''
int_list = [16, 3, 500, 26, 42, 231, 9, 12, 741, 22, 401]
string_list = [ "Hello", "is", "it", "me", "you're", "looking", "for", "I", "am", "16", "going", "on", "17"]

longest_string = max(string_list, key=len)
print(f"The longest string is: {longest_string}")
    
average_of_int_list = sum(int_list) / len(int_list)
print(f"The average of the ints is: {average_of_int_list}")

print("Strs with lengths matching numbers in int_list:")
for i in string_list:
    if len(i) in int_list:
        print(i)

int_list = [x / 2 for x in int_list]
print(f"The halved int_list is: {int_list}")


l1 = ["M","a","x","G","r","e","g","o","r","y"]
l1.sort()
print(l1.pop(-3))
l2 = [2,4,0,5,2,0,1,1]
l3 = l1 + l2
l3.reverse()
while 0 in l3:
    l3.remove(0)
print(l3)

s4 = "aaaaabbbcccdddeeFfg"
# s4 = "aaaaaaaaaaaaaaa"
l4 = list(s4)

for i in l4:
    l4_val = i #l4_val saves the value of i
    l4_pos = l4.index(i) #l4_pos is the first appearance of i
    l4.remove(i)
    while l4_val in l4:
        l4.remove(l4_val)
    l4.insert(l4_pos, l4_val)
print(l4)
'''