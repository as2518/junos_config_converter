#! /usr/bin/env python
# -*- coding: utf-8 -*-

from convert_config import convert_from_set_to_show

file = open('sample_input_set.txt', 'r')
input_text = file.read()
file.close()

output_text = convert_from_set_to_show( input_text )

file2 = open ('sample_output_set.txt', 'w')
file2.write( output_text )
file2.close
