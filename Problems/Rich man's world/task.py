money = float(input())
year = 0
while money <= 700000:
    money = money + money * 0.071
    year += 1
print(year)