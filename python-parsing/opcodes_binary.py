from contants import INSTRUCTION_OPCODE, INSTRUCTION_OPCODE_FUNCTION, CONDITION_CODE, name

from utils import split_params, encode_param, extract_instruction, assert_instruction, get_type_of_param, ParamType

# Get the binary from a line
def get_binary(i, labels, line):
    instruction = extract_instruction(line)
    return assert_instruction(INSTRUCTION_OPCODE_FUNCTION[instruction](i, labels, line)) if instruction in INSTRUCTION_OPCODE_FUNCTION else "0"

@name('lsls')
def lsls_to_binary(i, labels, line):
    params = split_params(line)
    if len(params) == 3:
        opcode = INSTRUCTION_OPCODE["lsls"][0]
        #Rd Rm imm5
        rd = encode_param(params[0])
        rm = encode_param(params[1])
        imm5 = encode_param(params[2], 5)
        return opcode + imm5 + rm + rd
    opcode = INSTRUCTION_OPCODE["lsls"][1]
    rdn = encode_param(params[0])
    rm = encode_param(params[1])
    return opcode + rm + rdn

@name('lsrs')
def lsrs_to_binary(i, labels, line):
    params = split_params(line)
    if len(params) == 3:
        opcode = INSTRUCTION_OPCODE["lsrs"][0]
        # Rd Rm imm5
        rd = encode_param(params[0])
        rm = encode_param(params[1])
        imm5 = encode_param(params[2], 5)
        return opcode + imm5 + rm + rd
    opcode = INSTRUCTION_OPCODE["lsrs"][1]
    rdn = encode_param(params[0])
    rm = encode_param(params[1])
    return opcode + rm + rdn

@name('asrs')
def asrs_to_binary(i, labels, line):
    params = split_params(line)
    if len(params) == 3:
        opcode = INSTRUCTION_OPCODE["asrs"][0]
        # Rd Rm imm5
        rd = encode_param(params[0])
        rm = encode_param(params[1])
        imm5 = encode_param(params[2], 5)
        return opcode + imm5 + rm + rd
    opcode = INSTRUCTION_OPCODE["asrs"][1]
    rdn = encode_param(params[0])
    rm = encode_param(params[1])
    return opcode + rm + rdn

@name('adds')
def adds_to_binary(i, labels, line):
    params = split_params(line)
    if len(params) == 3:
        if get_type_of_param(params[2]) == ParamType.IMMEDIATE_NUMBER:
            opcode = INSTRUCTION_OPCODE["adds"][1]
            # Rd Rn imm3
            rd = encode_param(params[0])
            rn = encode_param(params[1])
            imm3 = encode_param(params[2], 3)
            return opcode + imm3 + rn + rd
        opcode = INSTRUCTION_OPCODE["adds"][0]
        rd = encode_param(params[0])
        rn = encode_param(params[1])
        rm = encode_param(params[2])
        return opcode + rm + rn + rd
    opcode = INSTRUCTION_OPCODE["adds"][2]
    rdn = encode_param(params[0])
    imm8 = encode_param(params[1], 8)
    return opcode + rdn + imm8

@name('subs')
def subs_to_binary(i, labels, line):
    params = split_params(line)
    if len(params) == 3:
        if get_type_of_param(params[2]) == ParamType.IMMEDIATE_NUMBER:
            opcode = INSTRUCTION_OPCODE["subs"][1]
            # Rd Rn imm3
            rd = encode_param(params[0])
            rn = encode_param(params[1])
            imm3 = encode_param(params[2], 3)
            return opcode + imm3 + rn + rd
        opcode = INSTRUCTION_OPCODE["subs"][0]
        rd = encode_param(params[0])
        rn = encode_param(params[1])
        rm = encode_param(params[2])
        return opcode + rm + rn + rd
    opcode = INSTRUCTION_OPCODE["subs"][2]
    rdn = encode_param(params[0])
    imm8 = encode_param(params[1], 8)
    return opcode + rdn + imm8

@name('movs')
def movs_to_binary(i, labels, line):
    params = split_params(line)
    opcode = INSTRUCTION_OPCODE["movs"]
    rd = encode_param(params[0])
    imm8 = encode_param(params[1], 8)
    return opcode + rd + imm8

@name('cmp')
def cmp_to_binary(i, labels, line):
    params = split_params(line)
    if(get_type_of_param(params[1]) == ParamType.IMMEDIATE_NUMBER):
        opcode = INSTRUCTION_OPCODE["cmp"][0]
        rd = encode_param(params[0])
        imm8 = encode_param(params[1], 8)
        return opcode + rd + imm8
    opcode = INSTRUCTION_OPCODE["cmp"][1]
    rn = encode_param(params[0])
    rm = encode_param(params[1])
    return opcode + rm + rn

@name('ands')
def ands_to_binary(i, labels, line):
    params = split_params(line)
    opcode = INSTRUCTION_OPCODE["ands"]
    rdn = encode_param(params[0])
    rm = encode_param(params[1])
    return opcode + rm + rdn

@name('eors')
def eors_to_binary(i, labels, line):
    params = split_params(line)
    opcode = INSTRUCTION_OPCODE["eors"]
    rdn = encode_param(params[0])
    rm = encode_param(params[1])
    return opcode + rm + rdn

@name('adcs')
def adcs_to_binary(i, labels, line):
    params = split_params(line)
    opcode = INSTRUCTION_OPCODE["adcs"]
    rdn = encode_param(params[0])
    rm = encode_param(params[1])
    return opcode + rm + rdn

@name('sbcs')
def sbcs_to_binary(i, labels, line):
    params = split_params(line)
    opcode = INSTRUCTION_OPCODE["sbcs"]
    rdn = encode_param(params[0])
    rm = encode_param(params[1])
    return opcode + rm + rdn

@name('rors')
def rors_to_binary(i, labels, line):
    params = split_params(line)
    opcode = INSTRUCTION_OPCODE["rors"]
    rdn = encode_param(params[0])
    rm = encode_param(params[1])
    return opcode + rm + rdn

@name('tst')
def tst_to_binary(i, labels, line):
    params = split_params(line)
    opcode = INSTRUCTION_OPCODE["tst"]
    rn = encode_param(params[0])
    rm = encode_param(params[1])
    return opcode + rm + rn

@name('rsbs')
def rsbs_to_binary(i, labels, line):
    params = split_params(line)
    opcode = INSTRUCTION_OPCODE["rsbs"]
    rd = encode_param(params[0])
    rn = encode_param(params[1])
    return opcode + rn + rd

@name('cmn')
def cmn_to_binary(i, labels, line):
    params = split_params(line)
    opcode = INSTRUCTION_OPCODE["cmn"]
    rn = encode_param(params[0])
    rm = encode_param(params[1])
    return opcode + rm + rn

@name('orrs')
def orrs_to_binary(i, labels, line):
    params = split_params(line)
    opcode = INSTRUCTION_OPCODE["orrs"]
    rdn = encode_param(params[0])
    rm = encode_param(params[1])
    return opcode + rm + rdn

@name('muls')
def muls_to_binary(i, labels, line):
    params = split_params(line)
    opcode = INSTRUCTION_OPCODE["muls"]
    rdm = encode_param(params[0])
    rn = encode_param(params[1])
    return opcode + rn + rdm

@name('bics')
def bics_to_binary(i, labels, line):
    params = split_params(line)
    opcode = INSTRUCTION_OPCODE["bics"]
    rdn = encode_param(params[0])
    rm = encode_param(params[1])
    return opcode + rm + rdn

@name('mvns')
def mvns_to_binary(i, labels, line):
    params = split_params(line)
    opcode = INSTRUCTION_OPCODE["mvns"]
    rd = encode_param(params[0])
    rm = encode_param(params[1])
    return opcode + rm + rd

@name('str')
def str_to_binary(i, labels, line):
    line = line.replace("[", "").replace("]", "")
    params = split_params(line)
    opcode = INSTRUCTION_OPCODE["str"]
    rt = encode_param(params[0])
    if len(params) == 2:
        imm8 = encode_param("#" + str(0), 8)
        return opcode + rt + imm8
    imm8 = encode_param("#" + str(int(params[2][1:]) // 4), 8)
    return opcode + rt + imm8

@name('ldr')
def ldr_to_binary(i, labels, line):
    line = line.replace("[", "").replace("]", "")
    params = split_params(line)
    opcode = INSTRUCTION_OPCODE["ldr"]
    rt = encode_param(params[0])
    if len(params) == 2:
        imm8 = encode_param("#" + str(0), 8)
        return opcode + rt + imm8
    imm8 = encode_param("#" + str(int(params[2][1:]) // 4), 8)
    return opcode + rt + imm8

@name('add')
def add_to_binary(i, labels, line):
    params = split_params(line)
    opcode = INSTRUCTION_OPCODE["add"]
    imm7 = encode_param("#" + str(int(params[1][1:]) // 4), 7)
    return opcode + imm7

@name('sub')
def sub_to_binary(i, labels, line):
    params = split_params(line)
    opcode = INSTRUCTION_OPCODE["sub"]
    imm7 = encode_param("#" + str(int(params[1][1:]) // 4), 7)
    return opcode + imm7

@name('b')
def b_to_binary(i, labels, line):
    params = split_params(line)
    opcode = INSTRUCTION_OPCODE["b"]
    if params[0] in [label[1] for label in labels]:
        return opcode + encode_param("#" + str([label[0] for label in labels if label[1] == params[0]][0] - i - 3), 11)
    raise Exception("Label not found")

@name('bEQ')
def bEQ_to_binary(i, labels, line):
    params = split_params(line)
    opcode = CONDITION_CODE["eq"]
    if params[0] in [label[1] for label in labels]:
        return opcode + encode_param("#" + str([label[0] for label in labels if label[1] == params[0]][0] - i - 3), 8)
    raise Exception("Label not found")

@name('bNE')
def bNE_to_binary(i, labels, line):
    params = split_params(line)
    opcode = CONDITION_CODE["ne"]
    if params[0] in [label[1] for label in labels]:
        return opcode + encode_param("#" + str([label[0] for label in labels if label[1] == params[0]][0] - i - 3), 8)
    raise Exception("Label not found")

@name('bCS')
def bCS_to_binary(i, labels, line):
    params = split_params(line)
    opcode = CONDITION_CODE["cs"]
    if params[0] in [label[1] for label in labels]:
        return opcode + encode_param("#" + str([label[0] for label in labels if label[1] == params[0]][0] - i - 3), 8)
    raise Exception("Label not found")

@name('bHS')
def bHS_to_binary(i, labels, line):
    params = split_params(line)
    opcode = CONDITION_CODE["hs"]
    if params[0] in [label[1] for label in labels]:
        return opcode + encode_param("#" + str([label[0] for label in labels if label[1] == params[0]][0] - i - 3), 8)
    raise Exception("Label not found")

@name('bCC')
def bCC_to_binary(i, labels, line):
    params = split_params(line)
    opcode = CONDITION_CODE["cc"]
    if params[0] in [label[1] for label in labels]:
        return opcode + encode_param("#" + str([label[0] for label in labels if label[1] == params[0]][0] - i - 3), 8)
    raise Exception("Label not found")

@name('bLO')
def bLO_to_binary(i, labels, line):
    params = split_params(line)
    opcode = CONDITION_CODE["lo"]
    if params[0] in [label[1] for label in labels]:
        return opcode + encode_param("#" + str([label[0] for label in labels if label[1] == params[0]][0] - i - 3), 8)
    raise Exception("Label not found")

@name('bMI')
def bMI_to_binary(i, labels, line):
    params = split_params(line)
    opcode = CONDITION_CODE["mi"]
    if params[0] in [label[1] for label in labels]:
        return opcode + encode_param("#" + str([label[0] for label in labels if label[1] == params[0]][0] - i - 3), 8)
    raise Exception("Label not found")

@name('bPL')
def bPL_to_binary(i, labels, line):
    params = split_params(line)
    opcode = CONDITION_CODE["pl"]
    if params[0] in [label[1] for label in labels]:
        return opcode + encode_param("#" + str([label[0] for label in labels if label[1] == params[0]][0] - i - 3), 8)
    raise Exception("Label not found")

@name('bVS')
def bVS_to_binary(i, labels, line):
    params = split_params(line)
    opcode = CONDITION_CODE["vs"]
    if params[0] in [label[1] for label in labels]:
        return opcode + encode_param("#" + str([label[0] for label in labels if label[1] == params[0]][0] - i - 3), 8)
    raise Exception("Label not found")

@name('bVC')
def bVC_to_binary(i, labels, line):
    params = split_params(line)
    opcode = CONDITION_CODE["vc"]
    if params[0] in [label[1] for label in labels]:
        return opcode + encode_param("#" + str([label[0] for label in labels if label[1] == params[0]][0] - i - 3), 8)
    raise Exception("Label not found")

@name('bHI')
def bHI_to_binary(i, labels, line):
    params = split_params(line)
    opcode = CONDITION_CODE["hi"]
    if params[0] in [label[1] for label in labels]:
        return opcode + encode_param("#" + str([label[0] for label in labels if label[1] == params[0]][0] - i - 3), 8)
    raise Exception("Label not found")

@name('bLE')
def bLE_to_binary(i, labels, line):
    params = split_params(line)
    opcode = CONDITION_CODE["le"]
    if params[0] in [label[1] for label in labels]:
        return opcode + encode_param("#" + str([label[0] for label in labels if label[1] == params[0]][0] - i - 3), 8)
    raise Exception("Label not found")

@name('bLS')
def bLS_to_binary(i, labels, line):
    params = split_params(line)
    opcode = CONDITION_CODE["ls"]
    if params[0] in [label[1] for label in labels]:
        return opcode + encode_param("#" + str([label[0] for label in labels if label[1] == params[0]][0] - i - 3), 8)
    raise Exception("Label not found")

@name('bAL')
def bAL_to_binary(i, labels, line):
    params = split_params(line)
    opcode = CONDITION_CODE["al"]
    if params[0] in [label[1] for label in labels]:
        return opcode + encode_param("#" + str([label[0] for label in labels if label[1] == params[0]][0] - i - 3), 8)
    raise Exception("Label not found")

@name('bGE')
def bGE_to_binary(i, labels, line):
    params = split_params(line)
    opcode = CONDITION_CODE["ge"]
    if params[0] in [label[1] for label in labels]:
        return opcode + encode_param("#" + str([label[0] for label in labels if label[1] == params[0]][0] - i - 3), 8)
    raise Exception("Label not found")

@name('bge')
def bge_to_binary(i, labels, line):
    params = split_params(line)
    opcode = CONDITION_CODE["ge"]
    if params[0] in [label[1] for label in labels]:
        return opcode + encode_param("#" + str([label[0] for label in labels if label[1] == params[0]][0] - i - 3), 8)
    raise Exception("Label not found")

@name('bLT')
def bLT_to_binary(i, labels, line):
    params = split_params(line)
    opcode = CONDITION_CODE["lt"]
    if params[0] in [label[1] for label in labels]:
        return opcode + encode_param("#" + str([label[0] for label in labels if label[1] == params[0]][0] - i - 3), 8)
    raise Exception("Label not found")

@name('bGT')
def bGT_to_binary(i, labels, line):
    params = split_params(line)
    opcode = CONDITION_CODE["gt"]
    if params[0] in [label[1] for label in labels]:
        return opcode + encode_param("#" + str([label[0] for label in labels if label[1] == params[0]][0] - i - 3), 8)
    raise Exception("Label not found")