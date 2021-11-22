import csv
from icecream import ic
# import itertoolss
import yaml


def gen_shares_dict(csvfile):
    '''
    read a csvfile and return the shares into a dictionary
    '''
    shares_list = []
    shares_file = csv.DictReader(open(csvfile))

    for share in shares_file:
        
        share['profit'] = float(share['profit']) / 100
        share['price'] = float(share['price'])
        shares_list.append(share)
    return shares_list



def best_wallet(shares):
    sorted_shares = sorted(shares, key=lambda k: k['profit'], reverse=True)
    budget = 500
    profit = 0
    wallet = []
    for share in sorted_shares:
        # print(share['profit'])
        if budget - share['price'] < 0:
            result = print(
                    f'''e
The best wallet contains these shares:

{yaml.dump(wallet, allow_unicode=True, default_flow_style=False)}

It returns a profit of {profit} for a budget of {500 - budget}
                    ''')
            return result
        else:
            budget -= share["price"]
            profit = profit + share['price'] * share['profit']
            wallet.append(share)



csvfile = input('\n  Which csvfile to use: ')

endloop = False

while endloop == False:
    try:
        shares = gen_shares_dict(csvfile)
        wallet = best_wallet(shares)
        endloop = True
    except FileNotFoundError:
        print('\n File not found, please try again')
        print('** File has to be in the same directory **')
        csvfile = input('\n Which csvfile to use: \n')



        

