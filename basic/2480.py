dice = list(map(int, input().split()))

dice.sort()
dice_set = set(dice)
money = 0

if len(dice_set) == 1:  # all same
    money = 10000 + dice[0]*1000
elif len(dice_set) == 2:    # two same
    money = 1000 + dice[1]*100
else:   # all different
    money = dice[2]*100

print(money)
