import subprocess
import os


# Задача.
# Есть встроенная утилита sips для mac, которая сжимает фотографии,
# и есть папка «Source» с фотографиями. Каждую фотографию нужно
# уменьшить до 200px в ширину (высота меняется пропорционально).
# Нужно для каждой фотографии запустить программу и результат работы
# положить в папку «Result».
# Обратите внимание, что папки «Result» у пользователя нет и
# программа будет запущена несколько раз.
# Пример (sips):
# sips --resampleWidth 200 input.jpg

# Алгоритм выполнения ДЗ
# Получить путь до файлов в директории "Source"
# Получили путь до папки с результатами 'Result'
# Получить список всех файлов в папке "Source".
# C помощью команды cp скопировать все файлы из "Source" в папку Result для последующего монтажа
# при этом проверить есть ли папка Result, если нет, то создать ее.
# Получить список всех файлов в папке Result с полными путями до каждого файла.
# Обработать фото с помощью команды ['sips', '--resampleWidth', '200', "полный путь до файла с расширением"]


def make_the_full_path(names_lst, some_path):
    """Функция получает на вход список имен файлов
    и путь до директории. Создает список полных путей
    до каждого файла файла из списка names_lst.
    """

    files_path_list = []
    for name in names_lst:
        files_path_list.append(os.path.join(some_path, name))
    return files_path_list


def copy_all_photos(files_name_lst, path1, path2):
    """Функция производит копирование всех файлов
    из path1 в path2, если директории по path2 нет,
    то она будет создана.
    """

    files_path_list = make_the_full_path(files_name_lst, path1) # Получили список файлов с полными путями до них
    print('Список файлов для копирования: {0}'.format(files_path_list))
    # print('Папка в конце path2: ', os.path.split(path2)[1])
    for file in files_path_list:
        if os.path.exists(path2):
            subprocess.call(['cp', file, path2])
        else:
            subprocess.call(['mkdir', os.path.split(path2)[1]])
            subprocess.call(['cp', file, path2])
    print('Копирование файлов в директорию {0} завершено.'.format(os.path.split(path2)[1]))


def reduce_size_all_photos(lst, some_path):
    """ Функция получает список файлов для
    обработки и путь до них. Далее для каждого
    файла вызывается функция reduce_photo(),
    которая и производит изменение размера
    файла."""

    files_path_list = make_the_full_path(lst, some_path)  # Получили список файлов с полными путями до них
    for file in files_path_list:
        subprocess.call(['sips', '--resampleWidth', '200', file])  # Функция уменьшающая фотографию до 200px в ширину


def get_all_photos_in_dir(some_path):
    """Функция возвращает список всех файлов,
    которые имеются по переданной директории
    some_path.
    """

    return os.listdir(some_path)


def get_path(folder_name):
    """Функция получает на вход название папки и строит до нее путь,
    с условием, что эта папка лежит в той же директории, что
    и запускаемый файл.
    """

    return os.path.join(os.path.dirname(os.path.abspath(__file__)), folder_name)


if __name__ == '__main__':
    print('********** START PROGRAMM **********')
    print('Программа уменьшит фото до 200px в ширину.')
    migrations_path = get_path('Source')  # Получили путь до фото в папке Source
    result_path = get_path('Result')  # Получили путь до папки с результатами
    all_photos_in_dir = get_all_photos_in_dir(migrations_path)  # Получили список всех фото в передаваемой директории
    copy_all_photos(all_photos_in_dir, migrations_path, result_path)  # Скопируем все фото в папку Result
    reduce_size_all_photos(all_photos_in_dir, result_path)  # Уменьшили все фото в директории result_path ('Result')
    print('********** END PROGRAMM **********')
