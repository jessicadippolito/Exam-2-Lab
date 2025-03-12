def print_backwards(word):
    backwards = ''
    if len(word) == 0:
        return
    backwards += word[0]
    print_backwards(word[1:])
    print(backwards, end='')

def format_names(names):
    if len(names) == 1:
        if ',' in names[0]:
            return names[0]
        else:
            first, last = names[0].split(' ')
            return f'{last}, {first}'
    elif ',' in names[0]:
        return [names[0], format_names(names[1:])]
    else:
        first, last = names[0].split(' ')
        return [f'{last}, {first}', format_names(names[1:])]


def sum_a(data):
    total = 0
    for i in range (len(data)):
        for key in data[i]:
            if key=="a":
                total += data[i][key]
    return total

def process_list(nums):
    even_list = []
    odd_list = []
    processed = []
    for i in range (len(nums)):
        if i %2 ==0:
            even_list.append(nums[i])
        else:
            odd_list.append(nums[i])
    for j in range (len(even_list)):
        processed.append(str(even_list[j]))
    for k in range (len(odd_list)):
        processed.append(odd_list[k] * 10)
    return processed
