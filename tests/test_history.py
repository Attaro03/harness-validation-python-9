
from app.history import CalculationHistory





def test_history_returns_entries_in_order():

    history = CalculationHistory()

    history.add_entry("sum: 5")

    history.add_entry("product: 20")

    assert history.all_entries() == ["sum: 5", "product: 20"]


def test_history_defensive_copy():

    history = CalculationHistory()

    history.add_entry("sum: 5")

    history.add_entry("product: 20")

    entries = history.all_entries()

    entries.append("injected")

    entries.clear()

    assert history.all_entries() == ["sum: 5", "product: 20"]

