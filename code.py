

price = int(input('What is Bitcoin price today?'))

hold = int(input('How much $ do you have?'))

def total(a, b):
    return a/b

print('You can buy',total(hold, price),'BTC')
