import csv
from icecream import ic
# import itertoolss
import yaml
import time
import timeit
import os


# The screen clear function

def screen():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')

def gen_shares_dict(csvfile):
    '''
    read a csvfile and return the shares into a dictionary
    '''
    shares_list = []
    shares_file = csv.DictReader(open(csvfile))

    for share in shares_file:
        
        if float(share['price']) > 0:
            share['profit'] = float(share['profit']) / 100
            share['price'] = float(share['price'])
            shares_list.append(share)

    return shares_list



def best_wallet(shares, csvfile):
    sorted_shares = sorted(shares, key=lambda k: k['profit'], reverse=True)
    budget = 500
    profit = 0
    wallet = []
    for share in sorted_shares:
        # If budget ever reaches 0 return the wallet
        if 0<= budget <=0.00:
            screen()
            print(f'\n\nYour whole budget of { 500 - budget } has been spent.\n\nIts profit is worth {profit}')
            break
        # reduce the budget amount by the share['price'] amount
        # until budget is between 0 and 0
        # or until the loop has ended
        else:
            #if budget is negative pass
            if budget - share['price'] > 0:
                budget = budget - share["price"]
                profit = profit + share['price'] * share['profit']
                wallet.append(share)
            else:
                pass

    # Print the wallet which is the closest to a budget of 5
    screen()
    print(f'''

    Shares To Buy:
        
{yaml.dump(wallet, allow_unicode=True, default_flow_style=False)}

    The best wallet for {csvfile} returns a profit of {profit} for a budget of {500 - budget}

        ''')


def start_program():
    screen()
    csvfile = input('\n***************************************\n  Welcome To The Optimized Algorithm  \n***************************************\n\nWhich CSV File would you like to use:\n\n   ')

    endloop = False

    while endloop == False:
        try:
            
            shares = gen_shares_dict(csvfile)
            # print(timeit.timeit(stmt='best_wallet()',setup='',timer=time.perf_counter,number=1,globals=globals())) 
            t = timeit.Timer(lambda: best_wallet(shares, csvfile))
            print(f'          Time To Run The Optimized Algorithm : {t.timeit(1)} seconds\n\n')
            endloop = True
        except FileNotFoundError:
            screen()
            print('\n File not found, please try again \n\n')
            print('*** File has to be in the same directory ***\n\n')
            csvfile = input('Which CSV File would you like to use: \n\n  ')
            screen()



start_program()