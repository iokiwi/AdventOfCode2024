def main():
    with open("input1.txt", "r") as f:
        l_ids = list()
        r_ids = {}
        for line in f.readlines():
            line = line.strip().split()
            l_ids.append(int(line[0]))
            r_ids[int(line[1])] = r_ids.get(int(line[1]), 0) + 1

    total = 0
    for i in l_ids:
        sub_total = r_ids.get(i, 0) * i
        total += sub_total

    print(total)

if __name__ == "__main__":
    main()