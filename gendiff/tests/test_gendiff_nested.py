from gendiff.gendiff_generator import generate_diff


def test_nested_example():
    file1_json = 'gendiff/tests/fixtures/nested/file1.json'
    file2_json = 'gendiff/tests/fixtures/nested/file2.json'
    file1_yaml = 'gendiff/tests/fixtures/nested/file1.yaml'
    file2_yaml = 'gendiff/tests/fixtures/nested/file2.yaml'
    example = 'gendiff/tests/fixtures/nested/expect_nested.txt'

    with open(example) as file:
        data_example = ''.join(line for line in file)

    for file1, file2 in ((file1_json, file2_json), (file1_yaml, file2_yaml)):
        actual_example = generate_diff(file1, file2)
        assert data_example == actual_example


def test_nested_plain():
    file1_json = 'gendiff/tests/fixtures/nested/file1.json'
    file2_json = 'gendiff/tests/fixtures/nested/file2.json'
    file1_yaml = 'gendiff/tests/fixtures/nested/file1.yaml'
    file2_yaml = 'gendiff/tests/fixtures/nested/file2.yaml'
    example = 'gendiff/tests/fixtures/nested/nested_plain.txt'

    with open(example) as file:
        data_example = ''.join(line for line in file)

    for file1, file2 in ((file1_json, file2_json), (file1_yaml, file2_yaml)):
        actual_example = generate_diff(file1, file2, 'plain')
        assert data_example == actual_example
