import csv


def write_csv():

    with open('shares.csv', 'w') as f:
        # create the csv writer
        writer = csv.writer(f)
        header = ['share_name', 'price','profit']
        data = [
            ['share-1',20,18],
            ['share-2',30,21],
            ['share-3',50,14],
            ['share-4',70,12],
            ['share-5',60,8],
            ['share-6',80,3],
            ['share-7',22,1],
            ['share-8',26,23],
            ['share-9',48,9],
            ['share-10',34,17],
            ['share-11',42,27],
            ['share-12',110,13],
            ['share-13',38,11],
            ['share-14',14,7],
            ['share-15',18,25],
            ['share-16',8,17],
            ['share-17',4,20],
            ['share-18',10,15],
            ['share-19',24,10],
            ['share-20',114,5],
        ]
        # write a row to the csv file
        writer.writerow(header)
        # write rows to the csv file
        writer.writerows(data)


write_csv()