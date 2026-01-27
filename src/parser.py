import pandas
def load_transactions():
    csvFile = pandas.read_csv('data/transactions.csv')
    data_list = csvFile.to_dict(orient='records')
    return data_list