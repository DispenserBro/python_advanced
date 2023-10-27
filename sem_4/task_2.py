def sorted_unique_symbols(text: str) -> list[int]:
    return list(sorted(map(ord, set(text)), reverse=True))

print(sorted_unique_symbols("Текст выравнивается по правому краю так, чтобы у самого длинного"))