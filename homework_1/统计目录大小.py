import os


def main():
    directory_name = input("Please the path of a directory: ")
    print(get_dir_size(directory_name))


def get_dir_size(dir1):
    size = os.path.getsize(dir1)
    dir_list = os.listdir(dir1)
    for file in dir_list:
        file1 = os.path.join(dir1, file)
        if os.path.isfile(file1):
            size = size + os.path.getsize(file1)
        if os.path.isdir(file1):
            size = size + get_dir_size(file1)
    return size


main()
