import csv
from icecream import ic
import itertools



def gen_shares_dict(csvfile):
    '''
    read a csvfile and return the shares into a dictionary
    '''
    shares_file = csv.DictReader(open(csvfile))
    shares_list = []

    for share in shares_file:
        shares_list.append(share)

    shares = {}

    for share in shares_list:
        share['profit'] = int(share['profit']) / 100
        share['price'] = int(share['price'])
        shares[f"{share['share_name']}"] = share
        share.pop('share_name')
    # print(shares)
    return shares




def wallet_value(shares_list):
    '''
    from a given shares_name list compares the share_names
    with the shares given from gen_shares_dict() function
    then returns a wallet = to 500

    - compute the whole value of a wallet
    - which is the sum of each share profit
    - also returns the exact cost and profit of the wallet

    a wallet is a list of share name
    example : ['share-3', 'share-1', 'share-13']
    '''
    profit = 0.0
    cost = 0
    share_names = []
    wallet= {'wallet_profit': profit,'wallet_cost':cost, 'share_names':share_names }
    for share_name in shares_list:
        share = shares[share_name]
        # if cost + share['price'] <= 500:
        cost = cost + share['price']
        profit = profit + share['price'] * share['profit']
        share_names.append(share_name)
        wallet = ({'wallet_profit': profit,'wallet_cost':cost, 'share_names':share_names })
    if cost <= 500:
        return wallet
    else:
        None




def best_wallet(shares):
    '''
    iterates over all the shares given in the argument
    returns the highest profit wallet for the price of 500
    '''
    wallets= []
    # print(shares)
    for x in range(len(shares)):
        # print(x)
        for wallet in itertools.combinations(shares, x):

            if wallet_value(wallet) is None:
                pass
            else:
                wallets.append(wallet_value(wallet))

    # print(wallets)
    wallets = sorted(wallets, key=lambda k: k['wallet_profit'], reverse=True)
    # ic(wallets)
    return wallets[0]



shares = gen_shares_dict('shares.csv')
wallet = best_wallet(shares)
ic(wallet)
# ic(shares)









