from gendiff.gendiff_generator import generate_diff
import pytest

file1_json = 'gendiff/tests/fixtures/flat/file1.json'
file2_json = 'gendiff/tests/fixtures/flat/file2.json'
file1_yaml = 'gendiff/tests/fixtures/flat/file1.yaml'
file2_yaml = 'gendiff/tests/fixtures/flat/file2.yaml'


def test_flat_example():
    example = 'gendiff/tests/fixtures/flat/expect_example.txt'

    with open(example) as file:
        data_example = ''.join(line for line in file)

    for file1, file2 in ((file1_json, file2_json), (file1_yaml, file2_yaml)):
        actual_example = generate_diff(file1, file2)
        assert data_example == actual_example


def test_flat_one_empty():
    empty_json = 'gendiff/tests/fixtures/empty_file.json'
    empty_yaml = 'gendiff/tests/fixtures/empty_file.yaml'

    expect_one_empty1 = 'gendiff/tests/fixtures/flat/expect_one_empty1.txt'
    expect_one_empty2 = 'gendiff/tests/fixtures/flat/expect_one_empty2.txt'

    files_pairs1 = ((file1_json, empty_json), (file1_yaml, empty_yaml))
    files_pairs2 = ((empty_json, file2_json), (empty_yaml, file2_yaml))

    with open(expect_one_empty1) as file:
        data_one_empty1 = ''.join(line for line in file)
    with open(expect_one_empty2) as file:
        data_one_empty2 = ''.join(line for line in file)

    for file1, empty_file in files_pairs1:
        actual_one_empty1 = generate_diff(file1, empty_file)
        assert data_one_empty1 == actual_one_empty1

    for empty_file, file2 in files_pairs2:
        actual_one_empty2 = generate_diff(empty_file, file2)
        assert data_one_empty2 == actual_one_empty2


def test_flat_both_empty():
    empty_file = 'gendiff/tests/fixtures/empty_file.json'

    with open(empty_file) as file:
        data_both_empty = ''.join(line for line in file)

    actual_both_empty = generate_diff(empty_file, empty_file)
    assert data_both_empty == actual_both_empty


def test_unsupported_format():
    file_txt = 'gendiff/tests/fixtures/empty_file.txt'

    with pytest.raises(ValueError) as unknown_format_error:
        generate_diff(file_txt, file1_json)

    assert unknown_format_error.type == ValueError
    assert str(unknown_format_error.value) == 'Supported file format not found'


def test_unsupported_style():
    with pytest.raises(ValueError) as unknown_style_error:
        generate_diff(file1_json, file2_json, 'gangnam')

    assert unknown_style_error.type == ValueError
    assert str(unknown_style_error.value) == 'Style format not found'
