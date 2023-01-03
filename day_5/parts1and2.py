import copy


def remove_from_iterable(iterable: list, element) -> list:
    return [e for e in iterable if e != element]


def parse_input(file) -> dict:
    result = {
        "stacks": [],
        "instr": []
    }

    # Parse stacks
    rows = []
    raw_input_by_lines = [line for line in file.readlines()]
    for idx, line in enumerate(raw_input_by_lines):
        rows.append([])
        for i in range(1, len(line), 4):
            rows[idx].append(line[i])
        if idx > 6:
            break

    stacks = []
    for i in range(len(rows[1])):
        stacks.append([])
    for row in rows:
        for idx, char in enumerate(row):
            stacks[idx].append(char)
    for stack in stacks:
        stack.reverse()
        result["stacks"].append(remove_from_iterable(stack, " "))

    # Parse move instructions
    file.seek(0)
    for line_num, contents in enumerate(file.readlines()):
        if line_num > 9:
            extracted_ints = contents.replace("move ", "").replace(" from ", ",").replace(" to ", ",").split(",")
            result["instr"].append(
                {
                    "count": int(extracted_ints[0]),
                    "origin": int(extracted_ints[1]),
                    "dest": int(extracted_ints[2])
                }
            )

    # Done, return dict
    return result


def move_elements_reverse_order(stacks: list[list[str]], count: int, origin: int, dest: int):
    for i in range(count):
        stacks[dest-1].append(stacks[origin-1].pop())


def move_elements_same_order(stacks: list[list[str]], count: int, origin: int, dest: int):
    stacks[dest-1] += stacks[origin-1][-count:]
    stacks[origin-1] = stacks[origin-1][:len(stacks[origin-1]) - count]


def main():
    with open("input.txt") as f:
        parsed = parse_input(f)
    part1_stacks = copy.deepcopy(parsed["stacks"])
    part2_stacks = copy.deepcopy(parsed["stacks"])
    instructions = parsed["instr"]
    for instr_num, instruction in enumerate(instructions):
        move_elements_reverse_order(part1_stacks, instruction["count"], instruction["origin"], instruction["dest"])
        move_elements_same_order(part2_stacks, instruction["count"], instruction["origin"], instruction["dest"])
    print("Part 1: ", end="")
    for stack in part1_stacks:
        print(stack[-1], end="")
    print("\nPart 2: ", end="")
    for stack in part2_stacks:
        print(stack[-1], end="")
    print()


if __name__ == "__main__":
    main()
    