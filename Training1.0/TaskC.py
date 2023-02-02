def remove_signs(line):
    return line.replace('-', '', line.count('-')).\
        replace('(', '', 1).replace(')', '', 1).replace('+', '', 1)

def split_number(number):
    if len(number) == 7:
        return {'code': '495', 'num': number}
    elif 10 <= len(number) <= 11:
        return {'code': number[-10: -7], 'num': number[-7:]}
    else:
        return {'code': '0', 'num': '0'}


new_number= split_number(remove_signs(input()))
existing_numbers = [split_number(remove_signs(input())) for _ in range(3)]
for j in range(3):
    if new_number['code'] == existing_numbers[j]['code']\
            and new_number['num'] == existing_numbers[j]['num']:
        print('YES')
    else:
        print('NO')
