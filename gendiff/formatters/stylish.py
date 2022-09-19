INTEND_PER_LEVEL = 4
SIGNS_LENGTH = 2


def body_stylish(diffs, level=1):
    result = []
    indent = calculate_indent(level)

    for key, value in diffs.items():
        match value['entry_type']:

            case 'add':
                result.append(build_entry(
                    key, diffs[key]['value'], '+', level))

            case 'delete':
                result.append(build_entry(
                    key, diffs[key]['value'], '-', level))

            case 'change':
                result.append(build_entry(
                    key, diffs[key]['old_value'], '-', level))
                result.append(build_entry(
                    key, diffs[key]['new_value'], '+', level))

            case 'stay':
                result.append(build_entry(
                    key, diffs[key]['value'], ' ', level))

            case 'nested':
                result.extend([f"{indent}{' '} {key}: {{",
                               body_stylish(diffs[key]['children'], level + 1),
                               f"{indent}  }}"])

    return '\n'.join(result)


def calculate_indent(level):
    return ' ' * (level * INTEND_PER_LEVEL - SIGNS_LENGTH)


def convert_item_to_stylish(item):
    match item:
        case None:
            return 'null'
        case bool():
            return str(item).lower()
        case _:
            return str(item)


def build_entry(key, value, sign, level):
    result = []
    indent = calculate_indent(level)
    level += 1

    if type(value) is dict:
        result.extend([f"{indent}{sign} {key}: {{",
                       build_dict_entry(value, level),
                       f"{indent}  }}"])
    else:
        result.append(f"{indent}{sign} {key}: "
                      f"{convert_item_to_stylish(value)}")
    return '\n'.join(result)


def build_dict_entry(dict_value, level):
    result = []
    for key, value in dict_value.items():
        result.append(build_entry(key, value, ' ', level))
    return '\n'.join(result)


def stylish_format(diffs):
    body_output = body_stylish(diffs)
    return f"{{\n{body_output}\n}}" if body_output else '{}'
