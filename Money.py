# assignment 4
# do everything you did w your recent assignment
# but this time, w only one function

def hm_money():
    mmnt_money = int(input("Please enter the how much money you have: "))
    ppl_prc = int(input("Please enter the amount of apple you want to buy: "))
    return mmnt_money, ppl_prc

def result(Money, PriceApple):
    max_apple = Money // PriceApple
    change = Money  % PriceApple
    return max_apple, change

def output(max_apple, change):
    print(f"You can have {max_apple} apples and your change will be {change} pesos, thank you!.")

Money, PriceApple = hm_money()

max_apple, change = result(Money, PriceApple)

output(max_apple, change)


