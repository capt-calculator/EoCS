#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Parser:
    def __init__(self, file):
        self.file = file
        
    def get_command_type(self, line):
        if line[0] == "@":
            return("A_COMMAND")
        elif line[0] == "(":
            return("L_COMMAND")
        return("C_COMMAND")
            
    def get_symbol(self, line):
        at_location = line.find('@')
        open_paren = line.find("(")
        close_paren = line.find(")")
        if at_location != -1:
            return(line[at_location+1:])
        else:
            return(line[open_paren+1:close_paren])
        
    def get_dest(self, line):
        eq_location = line.find('=')
        if eq_location != -1:
            return(line[0:eq_location])   
        
    def get_comp(self, line):
        eq_location = line.find('=')
        if eq_location != -1:
            return(line[eq_location+1:])
        return(line[0])
        
    def get_jump(self, line):
        semi_location = line.find(';')
        if semi_location != -1:
            return(line[semi_location+1:])
        
    def parse_file(self):
        with open(self.file) as asm:
            for line in asm.readlines():
                if line == '\n':
                    continue
                if line[0:2] == '//':
                    continue
                line = line.strip()
                
                output = {
                    k:'None' for k in ['type', 'dest', 'comp', 'jump', 'symbol']
                }
                
                c_type = self.get_command_type(line)
                output['type'] = c_type
                
                if c_type == "C_COMMAND":
                    output['dest'] = str(self.get_dest(line))
                    output['comp'] = str(self.get_comp(line))
                    output['jump'] = str(self.get_jump(line))
                
                else:
                    output['symbol'] = self.get_symbol(line)
                    
                yield(output)