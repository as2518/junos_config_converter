#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys
import datetime
from convert_config import convert_from_show_to_set

sys.path.append(os.getcwd())

file_input = open('sample_config_show.txt', 'r')
input_text = file_input.read()
file_input.close()

output_text = convert_from_show_to_set( input_text )

date_today = datetime.datetime.today()
date_today_str = date_today.strftime( '%Y%m%d_%H%M' )

file_output = open ('output' + date_today_str + '.txt', 'w')
file_output.write( output_text )
file_output.close
