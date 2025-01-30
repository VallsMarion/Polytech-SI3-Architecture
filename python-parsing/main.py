import argparse

import contants
from opcodes_binary import get_binary
from utils import is_code, extract_instruction, split_params, convert_to_hex, is_label, get_type_of_param


def clean_file(input_file, output_file):
    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    # Créer un fichier de sortie et écrire les lignes nettoyées

    with open(output_file, 'w') as outfile:
        for line in lines:
            # Vérifier si la ligne commence par un '.' (il peut y avoir des espaces) et ne finit pas par ':'
            # ou qu'elle commence par run ou qu'elle est vide
            if line.strip().startswith('.') and not line.strip().endswith(':') or line.strip().startswith('run') or line.strip() == '':
                continue  # Ne pas écrire cette ligne dans le fichier de sortie
            else:
                outfile.write(line)

def parse_file(file_path, output_file):
    with open(output_file, 'w+') as output:
        output.write('v2.0 raw\n')
    index = 0
    decalage = 0
    with open(file_path, 'r') as file:
        # Read the file to index the labels
        instructions = []
        labels = []
        for line in file:
            if is_label(line):
                labels.append([(index - decalage), line[:len(line) - 2]])
                decalage = decalage + 1
            elif is_code(line):
                instructions.append(line)
            index = index + 1
        print(labels)
        print(instructions)
        for i in range(0, len(instructions)):
            instruction = instructions[i]
            print(instruction, end='')
            print('\tInstruction: ', extract_instruction(instruction))
            print('\tParameters: ', split_params(instruction))
            for param in split_params(instruction):
                print('\t\tType of param ' + param + ': ', get_type_of_param(param))
            print('\tBinary: ', get_binary(i, labels, instruction))
            print('\tHex: ', convert_to_hex(get_binary(i, labels, instruction)))
            print('\n')
            # put the hex in the output file
            with open(output_file, 'a') as output:
                hex = convert_to_hex(get_binary(i, labels, instruction))[2:].zfill(4)
                output.write(hex + ' ')

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Programme qui prend un fichier source et un fichier de sortie en entrée.")
    parser.add_argument("source", type=str, help="Chemin du fichier source")
    parser.add_argument("output", type=str, help="Chemin du fichier de sortie")

    args = parser.parse_args()
    return args.source, args.output

def main(source_file, output_file):
    clean_file(source_file, "cleaned.s")
    parse_file( "cleaned.s", output_file)

if __name__ == "__main__":
    print("Instructions in memory : " + str(len(contants.INSTRUCTION_OPCODE_FUNCTION)))
    source_file, output_file = parse_arguments()
    main(source_file, output_file)