import RandomGenerate
set_code = RandomGenerate.sample

def code_compution(input_code):
    white = []
    black = []
    copy_set_code = [x for x in set_code]
    copy_input_code = [x for x in input_code]
    for i in range(4):
        if input_code[i] == copy_set_code[i]:
            for j in range(4):
                if input_code[i] == input_code[j] and input_code[j].isalpha:
                    input_code[j] =-1
            black.append('black')
    input_code = [x for x in copy_input_code]
    copy_set_code = [x for x in set_code]
    for i in range(4):
        if input_code[i] == copy_set_code[i]:
            copy_set_code[i] = -1
    
    for i in range(4):
        if input_code[i] in copy_set_code:
            for j in range(4):
                if input_code[i] == input_code[j] and input_code[j].isalpha:
                    input_code[j] =-1
            white.append('white')
    output_code = black + white
    return output_code


