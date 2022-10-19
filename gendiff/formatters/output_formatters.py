from gendiff.formatters.plain import plain_format
from gendiff.formatters.stylish import stylish_format
from gendiff.formatters.json import json_format
from gendiff import constants


def style_formatting(item, style):
    match style:
        case constants.STYLISH:
            return stylish_format(item)

        case constants.PLAIN:
            return plain_format(item)

        case constants.JSON:
            return json_format(item)
