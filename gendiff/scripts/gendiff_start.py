import argparse
from gendiff.gendiff_generator import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument("-f", "--format", help='set format of output',
                        choices=('stylish', 'plain', 'json'),
                        default='stylish')
    args = parser.parse_args()
    file1 = args.first_file
    file2 = args.second_file
    style = args.format
    generate_diff(file1, file2, style)


if __name__ == '__main__':
    main()
