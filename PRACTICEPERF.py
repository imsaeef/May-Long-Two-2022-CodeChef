x = list(map(int, input().split()))
sol = 0
for item in x:
    if item>=10:
        sol+=1
print(sol)