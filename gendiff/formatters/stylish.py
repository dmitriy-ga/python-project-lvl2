from gendiff import constants

INTEND_PER_LEVEL = 4
SIGNS_LENGTH = 2


def form_body_stylish(generated_diffs, level=1):
    changes_list = []
    indent = calculate_indent(level)

    for key, value in generated_diffs.items():
        match value['entry_type']:

            case constants.ADD:
                changes_list.append(build_entry(
                    key, generated_diffs[key]['value'], '+', level))

            case constants.DELETE:
                changes_list.append(build_entry(
                    key, generated_diffs[key]['value'], '-', level))

            case constants.CHANGE:
                changes_list.append(build_entry(
                    key, generated_diffs[key]['old_value'], '-', level))
                changes_list.append(build_entry(
                    key, generated_diffs[key]['new_value'], '+', level))

            case constants.STAY:
                changes_list.append(build_entry(
                    key, generated_diffs[key]['value'], ' ', level))

            case constants.NESTED:
                nested_entry_body = form_body_stylish(
                    generated_diffs[key]['children'], level + 1
                )
                changes_list.extend([f"{indent}{' '} {key}: {{",
                                     nested_entry_body,
                                     f"{indent}  }}"])

    return '\n'.join(changes_list)


def calculate_indent(level):
    return ' ' * (level * INTEND_PER_LEVEL - SIGNS_LENGTH)


def convert_item_to_stylish(item):
    match item:
        case None:
            return constants.NULL

        case bool():
            return str(item).lower()

        case _:
            return str(item)


def build_entry(key, value, sign, level):
    entry = []
    indent = calculate_indent(level)
    level += 1

    if type(value) is dict:
        entry.extend([f"{indent}{sign} {key}: {{",
                      build_dict_entry(value, level),
                      f"{indent}  }}"])
    else:
        entry.append(f"{indent}{sign} {key}: "
                     f"{convert_item_to_stylish(value)}")
    return '\n'.join(entry)


def build_dict_entry(dict_value, level):
    dict_entry = []
    for key, value in dict_value.items():
        dict_entry.append(build_entry(key, value, ' ', level))
    return '\n'.join(dict_entry)


def stylish_format(generated_diffs):
    body_output = form_body_stylish(generated_diffs)
    return f"{{\n{body_output}\n}}" if body_output else '{}'
