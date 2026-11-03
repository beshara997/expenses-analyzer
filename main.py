import argparse
import csv
from collections import defaultdict


def load_expenses(path):
    expenses = []
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            expenses.append({
                "date": row["date"].strip(),
                "amount": float(row["amount"]),
                "category": row["category"].strip().lower(),
                "note": row["note"].strip(),
            })
    return expenses


def totals_by_category(expenses):
    totals = defaultdict(float)
    for e in expenses:
        totals[e["category"]] += e["amount"]
    return dict(totals)


def top_expenses(expenses, n=5):
    return sorted(expenses, key=lambda e: e["amount"], reverse=True)[:n]


def monthly_summary(expenses):
    months = defaultdict(float)
    for e in expenses:
        months[e["date"][:7]] += e["amount"]
    return dict(sorted(months.items()))


def main():
    parser = argparse.ArgumentParser(description="Analyze a CSV file of expenses.")
    parser.add_argument("file", help="path to the CSV file")
    parser.add_argument("--top", type=int, default=5, help="how many top expenses to show")
    args = parser.parse_args()

    expenses = load_expenses(args.file)

    print("Total per category:")
    totals = totals_by_category(expenses)
    for category, total in sorted(totals.items(), key=lambda x: x[1], reverse=True):
        print(f"  {category}: {total:.2f}")

    print(f"\nTop {args.top} expenses:")
    for e in top_expenses(expenses, args.top):
        print(f"  {e['amount']:.2f}  {e['date']}  {e['category']}  {e['note']}")

    print("\nMonthly summary:")
    for month, total in monthly_summary(expenses).items():
        print(f"  {month}: {total:.2f}")


if __name__ == "__main__":
    main()