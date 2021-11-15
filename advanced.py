# Knapsack problem, dynamic progamming


'''
Dynamic programming

- Recursion: Take a problem/function and write it where the function uses itself to solve the problem -> recompute computated values

- Memoization: Store a solution when solved, in a dict or array. Use the stored solution instead of re-running the function

- Bottom-up: flipping-around, starts at the base level and build up towards the problem you're trying to solve
'''


'''
Shares & Wallet(500$)
'''

items = [('share-1',20,0.18), ('share-2',30,0.21), ('share-3',50,0.14),('share-4',70,0.12),('share-5',60,0.8),('share-6',80,0.3)]
def dynamic_shares(items, capacity):
    '''
    Look at the capacity and split it up all the way to wallet size of 1$ then 2$,3$....
    Run this until you reach desired wallet capacity
    '''

    wallet = [0 for i in range(capacity+1)]
    for i in range(capacity+1):
        '''
        check for all shares that can fit in the wallet
        '''
        for j in range(len(items)):
            share_name,price,profit = items[j]
            if(price < i):
                wallet[i] = max(wallet[i], wallet[i-price]+ price*profit)

    return round(wallet[capacity])

print(dynamic_shares(items,500))