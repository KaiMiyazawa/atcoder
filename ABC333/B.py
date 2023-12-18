S = str(input())
T = str(input())

def func(lst):
    l = ["A", "B", "C", "D", "E",]
    for i in range(5):
        for j in range(5):
            if (lst[0] == l[i] and lst[1] == l[j]):
                return abs(i - j)
                
snum = func(S)
tnum = func(T)

if (snum == 1 or snum == 4):
    if (tnum == 1 or tnum == 4):
        print("Yes")
    else:
        print("No")
elif (tnum != 1 and tnum != 4):
    print("Yes")
else:
    print("No")
