def first_n_unique_letters(file, letters: int) -> int:
    file.seek(0)
    string = file.readlines()[0]
    for idx in range(len(string)):
        unique_letters = []
        for i in range(letters):
            unique_letters.append(string[idx+i])
        if len(set(unique_letters)) == letters:
            return idx + letters


def main():
    with open("input.txt") as f:
        print(first_n_unique_letters(f, 4))
        print(first_n_unique_letters(f, 14))


if __name__ == "__main__":
    main()