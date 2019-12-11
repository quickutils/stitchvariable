import sys
import argparse
import os
import datetime

backup_path =  "../"

class Ops:
    Unknown    = 0
    ParsingVar = 1

def change_variable_name(source_file_path, type, new_name):
    #new_name = wild_card_resolver(new_name, type)
    content = file_reader(source_file_path)
    
    variables_to_modify_actual = []
    variables_to_modify_value = []
    operation = Ops.Unknown
    line_ended = False
    last_token = ""
    previous_identifier = ""
    current_identifier = ""
    punctuations = "`¬!\"£$%^&*()_-=+\\|,<.>/?;:'@#~]}[{"
    for index in range(0, len(content) - 1):
        char = content[index]
        if char.isalnum():
            current_identifier += char
        elif char == ";" or char == "=":
            if operation == Ops.ParsingVar and not current_identifier == "":
                new_variable_name = wild_card_resolver(new_name, current_identifier)
                variables_to_modify_actual.append(current_identifier)
                variables_to_modify_value.append(new_variable_name)
            line_ended = True
            current_identifier = ""
            operation = Ops.Unknown
        else:
            if current_identifier != "":
                if previous_identifier == type and last_token not in punctuations:
                    operation = Ops.ParsingVar
                    new_variable_name = wild_card_resolver(new_name, current_identifier)
                    variables_to_modify_actual.append(current_identifier)
                    variables_to_modify_value.append(new_variable_name)
                elif operation == Ops.ParsingVar:
                    new_variable_name = wild_card_resolver(new_name, current_identifier)
                    variables_to_modify_actual.append(current_identifier)
                    variables_to_modify_value.append(new_variable_name)
            previous_identifier = current_identifier
            current_identifier = ""
            last_token =  char
            
    print(variables_to_modify_actual)
    print(variables_to_modify_value)
    
    #file_backup(os.path.basename(source_file_path), content)
    
def wild_card_resolver(raw_str, master_str):
    resolved_str = ""
    if len(raw_str) > 0:
        index = 0
        if raw_str[0] == '%':
            resolved_str = master_str + raw_str[1:len(raw_str)]
            index += 1
        if raw_str[len(raw_str)-1] == '%':
            resolved_str = resolved_str[0:len(resolved_str)-1] + master_str
    return resolved_str
    
def file_reader(source_file_path):
    if not os.path.isfile(source_file_path):
        print(source_file_path, "does not exist")
        exit(1)
    return open(source_file_path, "r").read()
    
def file_writer(source_file_path, content):
    f = open(source_file_path, "w+")
    f.write(content)
    f.close()
    
def file_backup(file_name, content):
    file_writer(os.path.realpath(backup_path) + os.sep + file_name + datetime.datetime.today().strftime('%m-%d-%Y') + ".java", content)
    
def screw_the_offside_rule():
    print(end='')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Initiate a variable name change on a source file, support wildcard in variable name manipulation.')
    parser.add_argument('source_file_path', help='The value to convert')
    parser.add_argument('type', help='The value to convert')
    parser.add_argument('new_name', help='The value to convert')
    
    args = parser.parse_args()
    change_variable_name(args.source_file_path, args.type, args.new_name)
    
    