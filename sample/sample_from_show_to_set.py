#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys
sys.path.append(os.getcwd())

from convert_config import convert_from_show_to_set

file = open('./sample/sample_config_show.txt', 'r')
input_text = file.read()
file.close()

output_text = convert_from_show_to_set( input_text )

file2 = open ('./sample/output_show.txt', 'w')
file2.write( output_text )
file2.close
