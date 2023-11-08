def func():
    with (open('names.txt', 'r', encoding='UTF-8') as file_name,
          open('example.txt', 'r', encoding='UTF-8') as file_nums):
        data_names = file_name.readlines()
        data_nums = file_nums.readlines()

    data_names = list(map(lambda x: x.strip(), data_names))
    data_nums = [tuple(map(float, item.strip().split(' | '))) for item in data_nums]
    data_nums = [item[0]*item[1] for item in data_nums]
    max_len = max([len(data_names), len(data_nums)])
    result = []
    for i in range(max_len):
        row = ''
        if data_nums[i] < 0:
            row = f'{data_names[i].lower()} | {abs(data_nums[i])}'
        else:
            row = f'{data_names[i].upper()} | {round(data_nums[i],0)}'
        result.append(row)
    with open('result.txt', 'w', encoding='UTF-8') as file:
        file.write('\n'.join(result))