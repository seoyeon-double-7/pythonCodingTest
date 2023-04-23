key = []
b=20
d = 2
while(d <= b):
    if b % d == 0:
        key.append(d)
        b = b//d
    else:
        d+=1
answer = list(set(key))

print(answer)