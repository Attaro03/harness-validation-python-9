
class CalculationHistory:

    def __init__(self) -> None:

        self._entries: list[str] = []



    def add_entry(self, entry: str) -> None:

        self._entries.append(entry)



    def all_entries(self) -> list[str]:

        return list(self._entries)

