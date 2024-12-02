def main():
    with open("input1.txt", "r") as f:
        list_1, list_2 = [], []
        for line in f.readlines():
            line = line.strip().split()
            list_1.append(int(line[0]))
            list_2.append(int(line[1]))

    zipped_sorted_lists = zip(sorted(list_1), sorted(list_2))
    print(sum([abs(item[0] - item[1]) for item in zipped_sorted_lists]))

if __name__ == "__main__":
    main()