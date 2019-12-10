import sys
import argparse

def change_variable_name(source_file_path, old_name, new_name):
    #new_name = wild_card_resolver(new_name, old_name)
    new_name = wild_card_resolver(new_name, "Hello")
    print(new_name)

def change_function_name(source_file_path, old_name, new_name):
    print("We good function anme")
    
def wild_card_resolver(raw_str, master_str):
    resolved_str = ""
    if len(raw_str) > 0:
        index = 0
        if raw_str[0] == '%':
            resolved_str = master_str + raw_str[1:len(raw_str)]
            index += 1
        if raw_str[len(raw_str)-1] == '%':
            resolved_str = resolved_str[0:len(resolved_str)-1] + master_str
    # for c in raw_str:
        # print(c)
    return resolved_str
    
def file_reader():
    print("write to file")
    
def file_writer():
    print("write to file")
    
def file_backup():
    print("backup to tmp folder")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Initiate a variable name change on a source file, support wildcard in variable name manipulation.')
    parser.add_argument('--variable', dest='change_variable_name',  action='store_const', const=change_variable_name, help='Convert the binary value to decimal')
    parser.add_argument('--function', dest='change_function_name',  action='store_const', const=change_function_name, help='Convert the decimal value to binary')
    parser.add_argument('source_file_path', help='The value to convert')
    parser.add_argument('type', help='The value to convert')
    parser.add_argument('new_name', help='The value to convert')
    
    args = parser.parse_args()
    if args.change_variable_name:
        args.change_variable_name(args.source_file_path, args.type, args.new_name)
    elif args.change_function_name:
        args.change_function_name(args.source_file_path, args.type, args.new_name)