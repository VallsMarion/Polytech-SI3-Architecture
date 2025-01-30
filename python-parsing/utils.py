import re
import contants

# Enum for the type of param
class ParamType:
    REGISTER = 'register'
    IMMEDIATE_NUMBER = 'immediate number'
    LABEL = 'label'

# Check if line is code
def is_code(line):
    # Using regex to cover case where there are spaces before the instruction
    return bool(re.match(r'^\s*\w+', line))

def is_label(line):
    return bool(re.match(r'.*[a-zA-Z0-9]*:', line))

# Get the instruction from a line
def extract_instruction(line):
    # Using regex to extract the instruction
    return re.match(r'^\s*(\w+)', line).group(1)

# Split the parameters from a line
def split_params(line):
    # Using regex to extract the parameters
    return (''.join(line.split()[1:])).replace(' ', '').split(',')

# Get the type of parameter
def get_type_of_param(param):
    # Check if param is a register or an immediate number
    if re.match(r'r\d+', param):
        return ParamType.REGISTER
    elif re.match(r'#-?\d+', param):
        return ParamType.IMMEDIATE_NUMBER
    else:
        return ParamType.LABEL

# Default fill is 3 bits because it is the minimum for an imm (it can also be 5,7 or 8)
def encode_param(param, fill=3):
    type = get_type_of_param(param)
    if type == ParamType.REGISTER:
        # Convert to bin on 3 bits
        return bin(int(param[1:]))[2:].zfill(3)
    elif type == ParamType.IMMEDIATE_NUMBER:
        val = int(param[1:])
        if val < 0:
            return to_twos_complement(val, fill)
        return bin(val)[2:].zfill(fill)
    else:
        raise Exception("Invalid type of param " + param)

def to_twos_complement(value, bit_width):
    return format(value & (2**bit_width - 1), f'0{bit_width}b')

def convert_to_hex(binary):
    return hex(int(binary, 2))

def assert_instruction(instruction):
    if(len(instruction) != 16):
        raise Exception("Instruction should be 16 bits long + " + instruction + " length : " + str(len(instruction)))
    return instruction