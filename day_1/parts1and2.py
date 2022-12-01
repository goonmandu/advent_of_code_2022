# Part 1 Solution (Unoptimized, First-thought)
def max_calorie_elf_number(infile):
    snacks = [c.strip() for c in infile.readlines()]
    max_calories = 0
    this_calories = 0
    for calorie in snacks:
        if not calorie:
            if this_calories > max_calories:
                max_calories = this_calories
            this_calories = 0
        else:
            this_calories += int(calorie)
    print(f"{max_calories=}")


# Part 2 Solution (Unoptimized, First-thought)
def top_three_elves_total_calories(infile):
    snacks = [c.strip() for c in infile.readlines()]
    top_three_calorie_sum = []
    this_calories = 0
    sum_of_top_three = 0
    for calorie in snacks:
        if not calorie:
            if not len(top_three_calorie_sum):
                top_three_calorie_sum.append(this_calories)
            else:
                for index, c_total in enumerate(top_three_calorie_sum):
                    if this_calories > c_total:
                        top_three_calorie_sum.insert(index, this_calories)
                        top_three_calorie_sum = top_three_calorie_sum[:3]
                        break
            this_calories = 0
        else:
            this_calories += int(calorie)
    for top_calorie in top_three_calorie_sum:
        sum_of_top_three += top_calorie
    print(f"{sum_of_top_three=}")


# Parts 1 and 2 Solution (Better)
def common_solution(infile):
    snacks = [c.strip() for c in infile.readlines()]
    calorie_sums = []
    this_calories = 0
    for calorie in snacks:
        if not calorie:
            calorie_sums.append(this_calories)
            this_calories = 0
        else:
            this_calories += int(calorie)
    calorie_sums.sort(reverse=True)
    max_calories = calorie_sums[0]
    sum_of_top_three = sum(calorie_sums[0:3])
    print(f"{max_calories=}, {sum_of_top_three=}")


def main():
    f = open("input.txt")
    print("Part 1 Unoptimized:")
    max_calorie_elf_number(f)
    f = open("input.txt")
    print("Part 2 Unoptimized:")
    top_three_elves_total_calories(f)
    f = open("input.txt")
    print("Parts 1 and 2 Optimized:")
    common_solution(f)


if __name__ == "__main__":
    main()
