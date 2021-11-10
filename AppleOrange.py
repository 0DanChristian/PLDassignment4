def pricelist():
    pple_price = 20
    rng_price = 25
    print(f"Our orange costs {rng_price} pesos and for our apple, it will only cost you {pple_price} pesos.")

def hmany():
    ppl_hmany = int(input("How many apples do you want? "))
    rng_hmany = int(input("How many orange do you want? "))
    return ppl_hmany, rng_hmany

def cal_(pple_price, rng_price, ppl_hmany, rng_hmany):
    ppl_ttl = pple_price * ppl_hmany
    rng_ttl = rng_price * rng_hmany
    cal_ = ppl_ttl + rng_ttl
    return cal_

def display(calculate):
    print(f"The total amount of your purchase is {calculate} pesos. ")

# 
# pricelist
ApplePrice, OrangePrice = pricelist()
# how many
apple, orange = hmany()
# calculte
calculate = cal_(pple_price, rng_price, apple, orange)
# output
display(calculate)



    