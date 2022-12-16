def main():
    with open("input.txt") as f:
        raw_rs = f.readlines()
    rucksacks = [rucksack.strip() for rucksack in raw_rs]
    priority = 0
    for rucksack in rucksacks:
        compartment = [rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]]
        for ltr in set(compartment[0]):
            if ltr in set(compartment[1]):
                if 97 <= ord(ltr) <= 122:
                    priority += ord(ltr) - 96
                else:
                    priority += ord(ltr) - 38
    print(f"{priority=}")


if __name__ == "__main__":
    main()