def main():
    with open("input.txt") as f:
        raw_rps = f.readlines()
    rps = [pair.strip() for pair in raw_rps]
    score = 0
    for line in rps:
        if line.endswith("X"):  # LOSE
            if line.startswith("A"):  # ROCK
                score += 3
            elif line.startswith("B"):  # PAPER
                score += 1
            else:  # SCISSORS
                score += 2
        elif line.endswith("Y"):  # DRAW
            score += 3
            if line.startswith("A"):
                score += 1
            elif line.startswith("B"):
                score += 2
            else:
                score += 3
        else:  # WIN
            score += 6
            if line.startswith("A"):
                score += 2
            elif line.startswith("B"):
                score += 3
            else:
                score += 1
    print(f"{score=}")


if __name__ == "__main__":
    main()