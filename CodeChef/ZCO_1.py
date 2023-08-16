budget_l = []

for _ in range(int(input("Enter n: "))):
    budget_l.append(int(input()))

rev_curr = 0
rev_l = []

for i in budget_l:
    rev_total = 0
    rev_curr = i
    for j in budget_l:
        if j <= rev_curr:
            rev_total += j
    rev_l.append(rev_total)


print(max(rev_l))
