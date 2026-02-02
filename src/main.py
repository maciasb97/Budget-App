import parser
import categorizer
import analyzer
import exporter
import pandas as pd

data_list = parser.load_transactions()
categorizer.add_category(data_list)
transaction_totals = analyzer.calculate(data_list)
exporter.export_summary(transaction_totals)





