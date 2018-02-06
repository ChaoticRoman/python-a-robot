import datetime as dt
import random

hour = dt.timedelta(hours=1)
start, end = dt.datetime(2018, 1, 1), dt.datetime(2018, 2, 1)
missing_start, missing_end = dt.datetime(2018, 1, 4), dt.datetime(2018, 1, 6)
N = 200
format = '%Y-%m-%dT%H-%M-%SZ'
possibilities = ['0', '1']
filename = 'data.txt'

every_hour = []
current = start
while current < end:
    if current > missing_start and current < missing_end:
        current = missing_end
        continue
    every_hour.append(current)
    current += hour

random.seed()

sample = random.sample(every_hour, N)
sample = [d.strftime(format) for d in sample]

with open(filename, 'w') as f:
    for d in sample:
        f.write(d + ',' + random.choice(possibilities) + '\n')
