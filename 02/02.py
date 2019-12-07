# Part 1
# We can be a little lazy and just paste in the whole list instead of reading the file.
original_program = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,6,19,23,2,23,6,27,2,6,27,31,2,13,31,35,1,10,35,39,2,39,13,43,1,43,13,47,1,6,47,51,1,10,51,55,2,55,6,59,1,5,59,63,2,9,63,67,1,6,67,71,2,9,71,75,1,6,75,79,2,79,13,83,1,83,10,87,1,13,87,91,1,91,10,95,2,9,95,99,1,5,99,103,2,10,103,107,1,107,2,111,1,111,5,0,99,2,14,0,0]

# Direction to replace pos 1 with 12 and pos 2 with 2
adj_original_program = list.copy(original_program)
adj_original_program[1] = 12
adj_original_program[2] = 2


def apply_int_code(program, group_of_four):
    code = group_of_four[0]
    if code == 99:
        print("Exit code!")
        return [99]
    if code == 1:
        new_val = program[group_of_four[1]] + program[group_of_four[2]]
    elif code == 2:
        new_val = program[group_of_four[1]] * program[group_of_four[2]]
    else:
        print("Code must be 1, 2, or 99.")
        return None
    program[group_of_four[3]] = new_val
    return program


# Count by 4s (note that this will fail if we get to the end of the list and it doesn't have four elements)
def get_output(program):
    group = 0
    intcode = 1
    valid = True
    new_program = program
    while intcode is not None:
        group_of_four = new_program[(group*4):(group*4+4)]
        intcode = group_of_four[0]
        if intcode is None:
            valid = False
            break
        if intcode == 99:
            break
        else:
            new_program = apply_int_code(new_program, group_of_four)
            group += 1

    return new_program[0], valid

print(f'Solution to part one: {get_output(adj_original_program)}')
print("=============================================================")

# Part 2
for pos1 in range(50):
    for pos2 in range(61):
        print(pos1, pos2)
        copy_program = list.copy(original_program)
        copy_program[1] = pos1
        copy_program[2] = pos2
        output, valid = get_output(copy_program)
        print(output)
        if output == 19690720 and valid:
            print(f'Noun: {pos1}, Verb: {pos2}')
            print(f'Solution: {100 * pos1 + pos2}')
            break
    else:
        continue
    break
