from helper.printformatter import pt


@pt
def write_file(src_file):
    # w -> rewrite the file, create if the file doesn't exist (all existing data wiped out)
    # x -> create new file and write. error if it's already exist
    # will returns FileExistsError
    # a -> append, create new file if doesn't exist.

    file = open(src_file, 'w+')
    print("writing : ", end="")
    for i in range(10):
        print(i, end="...")
        file.write(f'This is line #{i}\r\n')
    print("done writing!")
    file.close()


@pt
def read_file(src_file):
    # read with readlines, read and readline
    file = open(src_file, 'r')
    print(
        f"""
        File Info:
        file mode \t\t: {file.mode}
        file readable \t: {file.readable()}
        file writeable\t: {file.writable()}
        """
    )

    # reading file : once read, it cannot be read again with other method.
    print("--- line by line ---")
    content_list = file.readlines()  # read everything and returns as list
    print(content_list)
    for content in content_list:
        print(content, end="")
    file.close()

    print("--- all content ---")
    file = open(src_file, 'r')
    content_all = file.read()  # read everything in string
    print(content_all)
    file.close()

    print("--- read one line ---")
    file = open(src_file, 'r')
    content_line = file.readline()  # read single line in string
    print(content_line)
    file.close()


def main():
    target_file = '../resources/filehandling_ref_1.txt'
    write_file(target_file)
    read_file(target_file)


if __name__ == '__main__':
    main()
