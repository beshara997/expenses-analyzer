from main import totals_by_category, top_expenses, monthly_summary

SAMPLE = [
    {"date": "2026-10-01", "amount": 100.0, "category": "food", "note": "a"},
    {"date": "2026-10-02", "amount": 50.0, "category": "food", "note": "b"},
    {"date": "2026-11-01", "amount": 30.0, "category": "bills", "note": "c"},
]


def test_totals_by_category():
    assert totals_by_category(SAMPLE) == {"food": 150.0, "bills": 30.0}


def test_top_expenses():
    assert top_expenses(SAMPLE, 1)[0]["amount"] == 100.0


def test_monthly_summary():
    assert monthly_summary(SAMPLE) == {"2026-10": 150.0, "2026-11": 30.0}