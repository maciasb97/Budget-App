# Personal Finance & Budget Analyzer (Python)

A Python-based command-line application that analyzes personal financial transactions from a CSV file and generates category-based summaries and overall financial totals.

This project was built to strengthen Python fundamentals, data processing skills, and modular program design using a real-world use case.

---

## 📌 Features

- Import transactions from a CSV file
- Automatically categorize transactions based on description keywords
- Calculate:
    - Total income
    - Total expenses
    - Net savings
    - Per-category totals
- Export summary reports to CSV
- Modular, readable, and extendable codebase

---

## 🛠 Technologies Used

- Python 3
- pandas (CSV parsing & data handling)
- Standard Python libraries

---

## 📂 Project Structure

finance_tracker/
├── data/
│   └── transactions.csv
├── reports/
│   ├── expense_summary.csv
│   ├── revenue_summary.csv
│   └── total_summary.csv
├── src/
│   ├── main.py
│   ├── parser.py
│   ├── categorizer.py
│   ├── analyzer.py
│   └── exporter.py
├── README.md
└── requirements.txt

---

## 📄 Input Format

The input CSV should contain at least the following columns:

date,description,amount
2024-01-01,Paycheck,2500
2024-01-02,Groceries - Target,85.23
2024-01-03,Rent,1200
2024-01-05,Netflix,15.99
2024-01-06,Birthday Gift,300
2024-01-07,Electricity Bill,60.45

- Accepts positive amounts only as required for correct calculations of final totals
- "-" not required for descriptions, but helps visually seperate what the item/thing is to the category


---

## ▶️ How to Run

1. Clone the repository
2. Install dependencies:
    pip install -r requirements.txt
3. Place your transactions CSV in the data/ folder
4. Run the program:
    python src/main.py

Generated reports will be saved to the reports/ directory.

---

## 🧠 Key Concepts Demonstrated

- File I/O
- Data cleaning and validation
- Dictionaries and lists
- Functions and modular design
- Basic financial analysis logic
- Clean separation of responsibilities between modules

---

## 🚀 Future Improvements

- User-defined categories
- Date-based filtering (monthly/yearly)
- Visualization (charts/graphs)
- Export to additional formats (TXT, Excel)
- Web-based interface

---

## 👤 Author

Brandon Macias  
Bachelor’s in Computer & Information Science  
Associate’s in Business Administration

---