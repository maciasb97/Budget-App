import pandas as pd

def export_summary(balance_summary):
    revenue_sheet = pd.DataFrame(balance_summary['revenue'].items(), columns=['Category', 'Amount'])
    expense_sheet = pd.DataFrame(balance_summary['expenses'].items(), columns=['Category', 'Amount'])
    total_sheet = pd.DataFrame(balance_summary['totals'].items(), columns=['Metric', 'Amount'])

    csv_filename1 = 'reports/revenue_summary.csv'
    csv_filename2 = 'reports/expense_summary.csv'
    csv_filename3 = 'reports/total_summary.csv'

    revenue_sheet.to_csv(csv_filename1, index=False)
    expense_sheet.to_csv(csv_filename2, index=False)
    total_sheet.to_csv(csv_filename3, index=False)
    

