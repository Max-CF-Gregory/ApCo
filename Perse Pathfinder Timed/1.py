mebibytes = float(input())
shortest_time = float(input())
bits = mebibytes*1024*1024*8
answer = int((bits/shortest_time))
if answer > bits/shortest_time:
    print(answer-1)
else:
    print(answer)