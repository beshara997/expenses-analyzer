\# Expense Analyzer



A command-line tool that reads a CSV file of expenses and prints

the total per category, the top expenses, and a monthly summary.



\## Setup

python -m venv venv

venv\\Scripts\\activate

pip install -r requirements.txt



\## Usage

python main.py expenses.csv --top 5



\## CSV format

date,amount,category,note



\## Tests

pytest

