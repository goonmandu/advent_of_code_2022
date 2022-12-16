def main():
    with open("input.txt") as f:
        raw_rps = f.readlines()
    rps = [pair.strip() for pair in raw_rps]
    score = 0
    for line in rps:
        if line.endswith("X"):
            score += 1
            if line.startswith("A"):
                score += 3
            elif line.startswith("B"):
                pass
            else:
                score += 6
        elif line.endswith("Y"):
            score += 2
            if line.startswith("A"):
                score += 6
            elif line.startswith("B"):
                score += 3
            else:
                pass
        else:
            score += 3
            if line.startswith("A"):
                pass
            elif line.startswith("B"):
                score += 6
            else:
                score += 3
    print(f"{score=}")


if __name__ == "__main__":
    main()