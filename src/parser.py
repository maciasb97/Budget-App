import pandas
csvFile = pandas.read_csv('data/transactions.csv')

data_list = csvFile.to_dict(orient='records')

for row in data_list:
    print(row)

