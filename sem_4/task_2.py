def sorted_unique_symbols(text: str) -> list[str]:
    return list(sorted(set(text), key=id))

print(sorted_unique_symbols("Текст выравнивается по правому краю так, чтобы у самого длинного"))