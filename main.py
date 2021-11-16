def main():
    info = []
    file_list = ['1.txt', '2.txt', '3.txt']
    for file in file_list:
        line_counter = 0
        content = ''
        with open(file, encoding='utf-8') as f:
            for line in f:
                line_counter += 1
                content += line
            info.append([f.name, line_counter, content])
    info.sort(key=lambda x: x[1])

    with open('merged.txt', 'w', encoding='utf-8', ) as f:
        for el in info:
            f.write(el[0] + '\n' + str(el[1]) + '\n' + el[2] + '\n')


if __name__ == '__main__':
    main()
