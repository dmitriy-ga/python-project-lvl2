from gendiff.formatters.plain import plain_format
from gendiff.formatters.stylish import stylish_format


def style_formatting(item, style='stylish'):
    match style:
        case 'stylish':
            return stylish_format(item)
        case 'plain':
            return plain_format(item)
