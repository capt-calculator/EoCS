#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Code:
    
    def __init__(self):
        self.dest_mnemonic_dict = {
            'None': '000',
            'M': '001',
            'D': '010',
            'MD': '011',
            'A': '100',
            'AM': '101',
            'AD': '110',
            'AMD': '111'
            }
        
        self.comp_mnemonic_dict = {
            '0': '101010',
            '1': '111111',
            '-1': '111010',
            'D': '001100',
            'A': '110000',
            '!D': '001101',
            '!A': '110001',
            '-D': '001111',
            '-A': '110011',
            'D+1': '011111',
            'A+1': '110111',
            'D-1': '001110',
            'A-1': '110010',
            'D+A': '000010',
            'D-A': '010011',
            'A-D': '000111',
            'D&A': '000000',
            'D|A': '010101',
            'M': '110000',
            '!M': '110001',
            '-M': '110011',
            'M+1': '110111',
            'M-1': '110010',
            'D+M': '000010',
            'D-M': '010011',
            'M-D': '000111',
            'D&M': '000000',
            'D|M': '010101'
            }
        
        self.jump_mnemonic_dict = {
            'None': '000',
            'JGT': '001',
            'JEQ': '010',
            'JGE': '011',
            'JLT': '100',
            'JNE': '101',
            'JLE': '110',
            'JMP': '111'
            }

    def translate_dest(self, line):
        return(self.dest_mnemonic_dict[line['dest']])
    
    def translate_comp(self, line):
        a = 0
        if 'M' in line['comp']:
            a = 1
        return(str(a) + self.comp_mnemonic_dict[line['comp']])
        
    def translate_jump(self, line):
        return(str(self.jump_mnemonic_dict[line['jump']]))
    
    def translate_a(self, line):
        return(format(int(line['symbol']), '016b'))
        
    def translate_line(self, line):
        if line['type'] == "A_COMMAND":
            return(self.translate_a(line) + '\n')
        if line['type'] == "C_COMMAND":
            comp = self.translate_comp(line)
            dest = self.translate_dest(line)
            jump = self.translate_jump(line)
            return(str(111) + comp + dest + jump + '\n')
            
        