import json


def stylish(item):
    styled_dict = json.dumps(item, indent=4, separators=('', ': '))
    styled_dict = styled_dict.replace('"', '')
    print(styled_dict)
    return styled_dict


def style_formatting(item, style='stylish'):
    match style:
        case 'stylish':
            return stylish(item)
