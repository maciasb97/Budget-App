import parser
import categorizer
import analyzer

data_list = parser.load_transactions()
categorizer.add_category(data_list)
transaction_totals = analyzer.calculate(data_list)

print(*data_list, sep='\n')
