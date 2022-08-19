from collections import OrderedDict
import json


def generate_diff(file1, file2):

    def apply_change_symbols(dict_without_symbols, symbols):
        """Creates new dictionary with text before keys,
        when deletes old dictionary"""
        dict_with_symbols = {}
        for i in dict_without_symbols.keys():
            new_name = symbols + i
            dict_with_symbols[new_name] = dict_without_symbols[i]
        del dict_without_symbols
        return dict_with_symbols

    # Loading files to dictionaries
    dict1 = json.load(open(file1))
    dict2 = json.load(open(file2))

    # Dictionary of untouched items
    stays_without_symbols = dict(dict1.items() & dict2.items())
    stays = apply_change_symbols(stays_without_symbols, '  ')

    # Dictionary of deleted items
    deletes_without_symbols = dict(dict1.items() - dict2.items())
    deletes = apply_change_symbols(deletes_without_symbols, '- ')

    # Dictionary of added items
    adds_without_symbols = dict(dict2.items() - dict1.items())
    adds = apply_change_symbols(adds_without_symbols, '+ ')

    # Python dictionary with diffs
    diffs = OrderedDict(stays | deletes | adds)
    for name in sorted(diffs, key=lambda x: x.split()[-1]):
        diffs.move_to_end(name)
    # print(diffs)

    # JSON output with diffs
    new_json = json.dumps(diffs, indent=2)
    new_json = new_json.replace("\"", "")
    print(new_json)
