import parser
import categorizer

data_list = parser.load_transactions()
categorizer.add_category(data_list)
print(*data_list, sep='\n')
