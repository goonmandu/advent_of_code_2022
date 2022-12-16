def main():
    with open("input.txt") as f:
        raw_rs = f.readlines()
    rucksacks = [rucksack.strip() for rucksack in raw_rs]
    badge_priority = 0
    for index in range(0, len(rucksacks), 3):
        for ltr in set(rucksacks[index]):
            if ltr in set(rucksacks[index+1]) and ltr in set(rucksacks[index+2]):
                if 97 <= ord(ltr) <= 122:
                    badge_priority += ord(ltr) - 96
                else:
                    badge_priority += ord(ltr) - 38
    print(f"{badge_priority=}")


if __name__ == "__main__":
    main()