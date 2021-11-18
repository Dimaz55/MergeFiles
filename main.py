import os


def sort_files_by_size(file_list):
    content_list = []  # Список с содержимым файлов + заголовок
    if file_list:
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
    else:
        return None


def merge_list_in_file(sorted_list, file):
    """Записывает содержимое списка в файл"""
    with open(file, 'w', encoding='utf-8', ) as f:
        for element in sorted_list:
            for line in element:
                f.write(str(line) + '\n')
    return None


def get_file_list_to_parse(file_ext):
    """Возвращает список файлов с нужным расширением в текущем каталоге."""
    file_list = []
    with os.scandir() as files:
        for file in files:
            if file.name.endswith(file_ext):
                file_list.append(file.name)
    return file_list if len(file_list) > 0 else None


def main():
    input_file_extension = '.txt'  # расширение файлов для обработки
    output_file = 'merged.out'  # итоговый файл

    input_file_list = get_file_list_to_parse(input_file_extension)

    sorted_list = sort_files_by_size(input_file_list)

    merge_list_in_file(sorted_list, output_file)
    return None


if __name__ == '__main__':
    main()
