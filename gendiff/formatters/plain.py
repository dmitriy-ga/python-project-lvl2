from gendiff import constants


def convert_item_to_plain(item):
    match item:
        case None:
            return constants.NULL

        case bool() | int():
            return str(item).lower()

        case str():
            return f"'{item}'"

        case dict():
            return constants.COMPLEX_VALUE


def plain_format(generated_diffs, working_directory=''):
    changes_list = []
    for key, value in generated_diffs.items():
        path = f'{working_directory}.{key}' if working_directory else key
        match value['entry_type']:

            case constants.ADD:
                added_value = convert_item_to_plain(
                    generated_diffs[key]['value']
                )
                changes_list.append(
                    f"Property '{path}' was added with value: {added_value}"
                )

            case constants.DELETE:
                changes_list.append(f"Property '{path}' was removed")

            case constants.CHANGE:
                old_value = convert_item_to_plain(
                    generated_diffs[key]['old_value']
                )
                new_value = convert_item_to_plain(
                    generated_diffs[key]['new_value']
                )
                changes_list.append(f"Property '{path}' was updated. "
                                    f"From {old_value} to {new_value}"
                                    )

            case constants.NESTED:
                changes_list.append(
                    plain_format(generated_diffs[key]['children'], path)
                )

    return '\n'.join(changes_list)
