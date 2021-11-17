data = 'word.txt'

with open(data) as f:
    line_num = 1
    for line in f:
        print('{}:{}'.format(line_num, line.strip()))


        line_num += 1