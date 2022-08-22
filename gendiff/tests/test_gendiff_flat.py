from gendiff.gendiff_generator import generate_diff


def test_flat_example():
    file1 = 'gendiff/tests/fixtures/flat/file1.json'
    file2 = 'gendiff/tests/fixtures/flat/file2.json'
    example = 'gendiff/tests/fixtures/flat/expect_example.txt'

    with open(example) as file:
        data_example = ''.join(line for line in file)

    actual_example = generate_diff(file1, file2)
    assert data_example == actual_example


def test_flat_one_empty():
    empty_file = 'gendiff/tests/fixtures/empty_file.json'
    file1 = 'gendiff/tests/fixtures/flat/file1.json'
    file2 = 'gendiff/tests/fixtures/flat/file2.json'
    expect_one_empty1 = 'gendiff/tests/fixtures/flat/expect_one_empty1.txt'
    expect_one_empty2 = 'gendiff/tests/fixtures/flat/expect_one_empty2.txt'

    with open(expect_one_empty1) as file:
        data_one_empty1 = ''.join(line for line in file)
    with open(expect_one_empty2) as file:
        data_one_empty2 = ''.join(line for line in file)

    actual_one_empty1 = generate_diff(file1, empty_file)
    assert data_one_empty1 == actual_one_empty1

    actual_one_empty2 = generate_diff(empty_file, file2)
    assert data_one_empty2 == actual_one_empty2


def test_flat_both_empty():
    empty_file = 'gendiff/tests/fixtures/empty_file.json'

    with open(empty_file) as file:
        data_both_empty = ''.join(line for line in file)

    actual_both_empty = generate_diff(empty_file, empty_file)
    assert data_both_empty == actual_both_empty
