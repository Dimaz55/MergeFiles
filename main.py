def sort_files_by_size(file_list):
    content_list = []  # Список с содержимым файлов + заголовок
    for file in file_list:
        line_counter = 0
        content = ''
        with open(file, encoding='utf-8') as f:
            for line in f:
                line_counter += 1
                content += line
            content_list.append([f.name, line_counter, content])
    content_list.sort(key=lambda x: x[1])  # Сортировка по кол-ву строк
    return content_list


def merge_list_in_file(sorted_list, file):
    with open(file, 'w', encoding='utf-8', ) as f:
        for element in sorted_list:
            for line in element:
                f.write(str(line) + '\n')
    return None


def main():
    file_list = ['1.txt', '2.txt', '3.txt']
    sorted_list = sort_files_by_size(file_list)
    merged_file = 'merged.txt'
    merge_list_in_file(sorted_list, merged_file)


if __name__ == '__main__':
    main()
