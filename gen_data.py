import csv

# generate some sample data
data = [
    {'date': '1-Jan-20', 'close': 100},
    {'date': '2-Jan-20', 'close': 110},
    {'date': '3-Jan-20', 'close': 105},
    {'date': '4-Jan-20', 'close': 130},
    {'date': '5-Jan-20', 'close': 115},
    {'date': '6-Jan-20', 'close': 125},
    {'date': '7-Jan-20', 'close': 145},
    {'date': '8-Jan-20', 'close': 140},
    {'date': '9-Jan-20', 'close': 155},
    {'date': '10-Jan-20', 'close': 150}
]

# write the data to a CSV file
with open('data.csv', 'w', newline='') as csvfile:
    fieldnames = ['date', 'close']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in data:
        writer.writerow(row)