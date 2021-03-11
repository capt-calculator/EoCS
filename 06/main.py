#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from hack_parser import Parser
from hack_code import Code
from symbol_table import SymbolTable


def translate_asm(file_name):
    
    parser = Parser(file_name+".asm")
    code = Code()
    symbol_table = SymbolTable()
    
    # first pass
    line_number = 0
    for line in parser.parse_file():
        if line['type'] == "C_COMMAND" or line['type'] == "A_COMMAND":
            line_number += 1
        if line['type'] == "L_COMMAND":
            symbol_table.add_entry(line['symbol'], line_number)
    
    # second pass
    with open(file_name+".hack", mode='x') as hack:
        ram_address = 16
        for line in parser.parse_file():
            
            if line['type'] == "L_COMMAND":
                continue
            
            if line['type'] == "A_COMMAND":
                try:
                    line['symbol'] = int(line['symbol'])
                except:
                    if symbol_table.contains(line['symbol']):
                        line['symbol'] = symbol_table.get_address(line['symbol'])
                    elif line['symbol'] == 'None':
                        continue
                    else:
                        symbol_table.add_entry(line['symbol'], ram_address)
                        line['symbol'] = symbol_table.get_address(line['symbol'])
                        ram_address += 1
    
            hack.write(code.translate_line(line))
    print("File translation complete.")
    
if __name__ == '__main__':
    translate_asm("./rect/Rect")
