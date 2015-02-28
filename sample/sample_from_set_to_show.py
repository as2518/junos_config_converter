#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
sys.path.append(os.getcwd())

from convert_config import convert_from_set_to_show

file = open('./sample/sample_config_set.txt', 'r')
input_text = file.read()
file.close()

output_text = convert_from_set_to_show( input_text )

file2 = open ('./sample/output_set.txt', 'w')
file2.write( output_text )
file2.close
