#! /usr/bin/env python
# -*- coding: utf-8 -*-

def convert_from_show_to_set(input_text):
    output_text = ''
    indent = ''
    for line in input_text.splitlines():
        if line == '':
            output_text += '\n'
        elif line[-1] == '{':
            output_text += indent + 'edit ' + line[:-1].strip() + '\n'
            indent += ' ' * 4
        elif line[-1] == ';':
            output_text += indent + 'set  ' + line[:-1].strip() + '\n'
        elif line[-1] == '}':
            indent = indent[:-4]
            output_text += indent + 'up\n'
        elif '; ## SECRET-DATA' in line:
            # ignore sentence of "## SECRET-DATA"
            output_text += indent + 'set ' + line.strip('; ## SECRET-DATA') + '\n'
        else:
            output_text += line + '\n'
    return output_text

def convert_from_set_to_show(input_text):

    # Implement later
    pass

    # You need to define all of JUNOS sentences.
    # It difficult to find defference a variable and an invariable sentence,
    # for example "set interfaces fe-0/0/0 unit 0 family inet address 192.107.1.230/24"
