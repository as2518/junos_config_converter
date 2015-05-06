# junos_config_converter
This script converts junos configuration to 'set / edit ' style or ' show configuration' style.

How to use
----------
This tool is very simple to use.


The input is Junos script of 'show configuration' style.

```
system {
    host-name R1;
    time-zone Asia/Tokyo;
    root-authentication {
        encrypted-password "$1$9kcwd00g$YDqr8sBMaAh8SOCjQ2f4b0"; ## SECRET-DATA
    }
}
interfaces {
    fe-0/0/0 {
        unit 0 {
            family inet {
                address 192.168.1.1/24;
            }
        }
    }
}
```

This is sample program.

```python
from convert_config import convert_from_show_to_set

output_text = convert_from_show_to_set( input_text )
```


The converted output file .
```
edit system
    set  host-name R1
    set  time-zone Asia/Tokyo
    edit root-authentication
        set encrypted-password "$1$9kcwd00g$YDqr8sBMaAh8SOCjQ2f4b0"
    up
up
edit interfaces
    edit fe-0/0/0
        edit unit 0
            edit family inet
                set  address 192.168.1.1/24
            up
        up
    up
up
```


If you want to know the detial samle code, you should see sample/sample_from_shwo_to_set.py.


Current Status
--------------
We implement only situation which convert script from 'show configration style' to 'set/edit style'.
If you need conversion from 'set/edit style' to 'show configration style', you should define all of JUNOS configuration architecture and implement the function of 'convert_from_set_to_show'.

# blog
Posted technical blog in Qiita (In Japanese).
http://qiita.com/taijijiji/items/d83ca9d57b711d1e6afb#%E9%96%8B%E7%99%BA%E7%8A%B6%E6%B3%81
