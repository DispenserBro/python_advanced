def key_params(**kwargs):
    return {value if value.__hash__ else str(value): key for key, value in kwargs.items()}

print(hash(None))
# params = key_params(a=1, b='hello', c=[1, 2, 3], d={})
# print(params)
