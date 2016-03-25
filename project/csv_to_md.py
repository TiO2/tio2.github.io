#!/usr/bin/env python

# from csv to md file


import csv,datetime

data = [line for line in csv.DictReader(open('csv_to_md.csv', 'rb'),quotechar='"', delimiter=',',skipinitialspace=True)]


for item in data:
    theFile = item['Title']
    with open('{}.csv'.format(theFile),'wb') as f:
        f.write('title: {}\n'.format(item['Title']))
        f.write('date: {}\n\n'.format(datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')))
        f.write('{}\n {}'.format(item['Company'],item['Description']))





