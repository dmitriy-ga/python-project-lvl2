def convert_item_to_plain(item):
    match item:
        case None:
            return 'null'
        case bool() | int():
            return str(item).lower()
        case str():
            return f"'{item}'"
        case dict():
            return '[complex value]'


def plain_format(diffs, working_directory=''):
    result = []
    for key, value in diffs.items():
        path = f'{working_directory}.{key}' if working_directory else key
        match value['entry_type']:

            case 'add':
                added_value = convert_item_to_plain(diffs[key]['value'])
                result.append(
                    f"Property '{path}' was added with value: {added_value}")

            case 'delete':
                result.append(f"Property '{path}' was removed")

            case 'change':
                old_value = convert_item_to_plain(diffs[key]['old_value'])
                new_value = convert_item_to_plain(diffs[key]['new_value'])
                result.append(f"Property '{path}' was updated. "
                              f"From {old_value} to {new_value}")

            case 'nested':
                result.append(plain_format(diffs[key]['children'], path))

    return '\n'.join(result)
