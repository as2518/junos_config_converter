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

    '''
    output_text = ''
    indent = ''
    for line in input_text.splitlines():
        if line == '':
            output_text += '\n'
        elif 'edit' in line:
            #indent = line.rstrip('edit ')
            output_text +=  indent + line.lstrip('edit ') + '{\n'
        elif 'set' in line:
            output_text +=  indent + line.lstrip('set ') + ';\n'
        elif 'up' in line:
            output_text +=  indent + line.rstrip('up') + '}\n'
        else:
            output_text += line + '\n'
    return output_text
    '''
